"""Fetch GitHub trending (overall + selected languages) and enrich each repo via the GitHub API.

Output: data/daily/YYYY-MM-DD.jsonl, one JSON object per repo with:
  slug, owner, name, url, description, language, stars, stars_today,
  forks, license, pushed_at, created_at, topics, readme_excerpt,
  source ("overall" | "lang:python" | ...), fetched_at.

Reads GITHUB_TOKEN from env or `gh auth token` for authenticated API calls.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DAILY_DIR = ROOT / "data" / "daily"
LANGUAGES = ["", "python", "typescript", "rust", "go"]  # "" = overall
TRENDING_URL = "https://github.com/trending/{lang}?since=daily"
USER_AGENT = "repo-radar/0.1 (+https://github.com/Michiel-DK/repo-radar)"
README_MAX_CHARS = 2000


def github_token() -> str | None:
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        return tok
    try:
        out = subprocess.check_output(["gh", "auth", "token"], stderr=subprocess.DEVNULL, text=True)
        return out.strip() or None
    except Exception:
        return None


def session(token: str | None) -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"})
    if token:
        s.headers["Authorization"] = f"Bearer {token}"
    return s


def parse_trending(html: str, source: str) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    out: list[dict] = []
    for rank, art in enumerate(soup.select("article.Box-row"), start=1):
        h2 = art.select_one("h2 a")
        if not h2 or not h2.get("href"):
            continue
        slug = h2["href"].strip("/")
        if "/" not in slug:
            continue
        owner, name = slug.split("/", 1)

        desc_el = art.select_one("p")
        description = desc_el.get_text(strip=True) if desc_el else ""

        # Footer line: language span, total stars, forks, "N stars today"
        lang_el = art.select_one("span[itemprop='programmingLanguage']")
        language = lang_el.get_text(strip=True) if lang_el else None

        stars_today = None
        for span in art.select("span.d-inline-block"):
            txt = span.get_text(" ", strip=True)
            m = re.match(r"([\d,]+)\s+stars\s+today", txt)
            if m:
                stars_today = int(m.group(1).replace(",", ""))
                break

        out.append({
            "slug": slug,
            "owner": owner,
            "name": name,
            "url": f"https://github.com/{slug}",
            "description": description,
            "language_hint": language,
            "stars_today": stars_today,
            "rank_in_source": rank,
            "source": source,
        })
    return out


def fetch_trending_all() -> dict[str, dict]:
    """Fetch trending for every configured language; dedupe by slug, keep best rank/source."""
    by_slug: dict[str, dict] = {}
    s = requests.Session()
    s.headers["User-Agent"] = USER_AGENT
    for lang in LANGUAGES:
        url = TRENDING_URL.format(lang=lang)
        src = "overall" if not lang else f"lang:{lang}"
        try:
            r = s.get(url, timeout=20)
            r.raise_for_status()
        except Exception as e:
            print(f"  [warn] failed to fetch {src}: {e}", file=sys.stderr)
            continue
        repos = parse_trending(r.text, src)
        print(f"  {src}: {len(repos)} repos")
        for repo in repos:
            existing = by_slug.get(repo["slug"])
            if existing is None:
                repo["sources"] = [repo.pop("source")]
                by_slug[repo["slug"]] = repo
            else:
                existing["sources"].append(repo["source"])
                # keep the best (lowest) rank
                existing["rank_in_source"] = min(existing["rank_in_source"], repo["rank_in_source"])
        time.sleep(0.3)  # be polite to github.com
    return by_slug


def enrich(repo: dict, api: requests.Session) -> dict:
    slug = repo["slug"]
    try:
        r = api.get(f"https://api.github.com/repos/{slug}", timeout=20)
        if r.status_code == 404:
            repo["enrich_error"] = "404"
            return repo
        r.raise_for_status()
        d = r.json()
        repo["stars"] = d.get("stargazers_count")
        repo["forks"] = d.get("forks_count")
        repo["watchers"] = d.get("subscribers_count")
        repo["language"] = d.get("language") or repo.get("language_hint")
        repo["license"] = (d.get("license") or {}).get("spdx_id")
        repo["pushed_at"] = d.get("pushed_at")
        repo["created_at"] = d.get("created_at")
        repo["topics"] = d.get("topics") or []
        repo["default_branch"] = d.get("default_branch")
        repo["open_issues"] = d.get("open_issues_count")
        repo["archived"] = d.get("archived", False)
        repo["api_description"] = d.get("description")
    except Exception as e:
        repo["enrich_error"] = str(e)
        return repo

    # README excerpt (markdown, decoded)
    try:
        rr = api.get(
            f"https://api.github.com/repos/{slug}/readme",
            headers={"Accept": "application/vnd.github.raw"},
            timeout=20,
        )
        if rr.status_code == 200:
            text = rr.text
            # strip HTML comments + collapse blank runs to keep excerpt readable
            text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
            text = re.sub(r"\n{3,}", "\n\n", text).strip()
            repo["readme_excerpt"] = text[:README_MAX_CHARS]
        elif rr.status_code != 404:
            repo["readme_error"] = f"status {rr.status_code}"
    except Exception as e:
        repo["readme_error"] = str(e)

    return repo


def main() -> int:
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DAILY_DIR / f"{today}.jsonl"

    print(f"[fetch] scraping github.com/trending for {LANGUAGES}…")
    by_slug = fetch_trending_all()
    print(f"[fetch] {len(by_slug)} unique repos after dedup")

    token = github_token()
    if not token:
        print("[warn] no GITHUB_TOKEN found (or `gh auth token`); enrichment will be unauthenticated and may hit rate limits", file=sys.stderr)
    api = session(token)

    fetched_at = dt.datetime.now(dt.timezone.utc).isoformat()
    enriched: list[dict] = []
    for i, (slug, repo) in enumerate(by_slug.items(), start=1):
        print(f"  [{i}/{len(by_slug)}] {slug}")
        repo["fetched_at"] = fetched_at
        enriched.append(enrich(repo, api))

    # Sort by stars_today desc (None last), then stars desc
    enriched.sort(key=lambda r: (-(r.get("stars_today") or 0), -(r.get("stars") or 0)))

    with out_path.open("w") as f:
        for repo in enriched:
            f.write(json.dumps(repo, ensure_ascii=False) + "\n")
    print(f"[fetch] wrote {out_path} ({len(enriched)} repos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
