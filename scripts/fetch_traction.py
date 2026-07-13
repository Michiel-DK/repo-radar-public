#!/usr/bin/env python3
"""Fetch traction / revenue signal for repo-radar.

The radar's other sources are *supply* (GitHub trending — buildable tech) and
*demand* (HN / Reddit — unmet pain). This one is *traction*: what's actually
making money right now, and in which categories. Source is TrustMRR, which
verifies revenue straight from Stripe / RevenueCat.

Sources
-------
- **TrustMRR public snapshot** (`/api/ai`) — 25 recently-listed + 25 best-deal
  startups with verified MRR. No auth, no key. ALWAYS ON.
- **TrustMRR full API** (`/api/v1/startups`) — top movers by revenue + MRR
  growth across the marketplace, with category filtering. Needs a
  TRUSTMRR_API_KEY env var (free key from the TrustMRR dashboard). Skipped if
  unset. Their docs ask you to use the API, not scrape the site.

Output
------
data/traction/<UTC-date>.jsonl — one JSON row per startup signal, `source`- and
`kind`-tagged. Stdlib only (urllib) so it runs in CI with no extra deps.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "data" / "traction"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
UA = "repo-radar-traction/0.1 (personal idea radar)"

BASE = "https://trustmrr.com"

# Categories worth tracking for a builder radar. Used only in the keyed path.
CATEGORIES = ["ai", "saas", "developer-tools", "fintech", "marketing"]

# Fields we keep off each startup object (both endpoints share this shape).
KEEP = [
    "name", "slug", "url", "website", "description", "country",
    "foundedDate", "category", "paymentProvider", "targetAudience",
    "customers", "activeSubscriptions", "askingPrice",
    "profitMarginLast30Days", "growth30d", "growthMRR30d", "multiple",
    "rank", "onSale", "firstListedForSaleAt", "xHandle",
]


def _get(url, headers=None, timeout=20):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def _row(item, kind):
    """Normalise a TrustMRR startup object into a flat radar row."""
    rev = item.get("revenue") or {}
    row = {"source": "trustmrr", "kind": kind}
    for k in KEEP:
        if k in item:
            row[k] = item[k]
    # Monetary fields are already in whole USD (despite the docs saying "cents":
    # verified against the live leaderboard — Stan reads mrr=3569654.22 = $3.57M).
    row["mrr_usd"] = round(rev.get("mrr") or 0, 2)
    row["revenue_30d_usd"] = round(rev.get("last30Days") or 0, 2)
    if item.get("askingPrice") is not None:
        row["asking_price_usd"] = round(item["askingPrice"], 2)
    return row


# ------------------------------------------------------------- public snapshot

def fetch_public():
    """The keyless /api/ai snapshot: recently-listed + best-deal startups."""
    try:
        data = _get(f"{BASE}/api/ai")
    except Exception as e:  # noqa: BLE001
        print(f"[trustmrr] public snapshot failed: {e}", file=sys.stderr)
        return []
    rows = []
    for item in data.get("recentlyListedStartups", []):
        rows.append(_row(item, "recently_listed"))
    for item in data.get("bestDeals", []):
        rows.append(_row(item, "best_deal"))
    print(f"[trustmrr] {len(rows)} public rows "
          f"({sum(r['kind']=='recently_listed' for r in rows)} recent, "
          f"{sum(r['kind']=='best_deal' for r in rows)} best-deal)")
    return rows


# ----------------------------------------------------------------- keyed feed

def fetch_keyed(top=20):
    """Top movers by revenue + MRR growth via the authenticated API."""
    key = os.environ.get("TRUSTMRR_API_KEY")
    if not key:
        print("[trustmrr] TRUSTMRR_API_KEY not set — skipping full-API pull "
              "(public snapshot still ran)")
        return []

    hdr = {"Authorization": f"Bearer {key}", "User-Agent": UA}
    rows, seen = [], set()

    def pull(kind, params):
        # limit is capped at 10 server-side; page up to `top`.
        got, page = 0, 1
        while got < top:
            q = urllib.parse.urlencode({**params, "limit": 10, "page": page})
            try:
                data = _get(f"{BASE}/api/v1/startups?{q}", headers=hdr)
            except urllib.error.HTTPError as e:
                print(f"[trustmrr] {kind} page {page} HTTP {e.code}",
                      file=sys.stderr)
                return
            except Exception as e:  # noqa: BLE001
                print(f"[trustmrr] {kind} page {page} failed: {e}",
                      file=sys.stderr)
                return
            batch = data.get("data", [])
            if not batch:
                return
            for item in batch:
                slug = item.get("slug")
                if slug and (kind, slug) not in seen:
                    seen.add((kind, slug))
                    rows.append(_row(item, kind))
                    got += 1
                    if got >= top:
                        break
            if not data.get("meta", {}).get("hasMore"):
                return
            page += 1
            time.sleep(0.3)  # be polite

    pull("top_revenue", {"sort": "revenue-desc"})
    # Floor out near-zero MRR so growth % isn't dominated by $1 → $5 jumps.
    pull("top_growth", {"sort": "growth-desc", "minMrr": 100})
    print(f"[trustmrr] {len(rows)} keyed rows "
          f"({sum(r['kind']=='top_revenue' for r in rows)} revenue, "
          f"{sum(r['kind']=='top_growth' for r in rows)} growth)")
    return rows


# ------------------------------------------------------------------------- main

def main():
    print(f"[traction] fetch for {TODAY}")
    rows = fetch_public()
    rows += fetch_keyed()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{TODAY}.jsonl"
    with open(out, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"[traction] wrote {len(rows)} rows -> {out.relative_to(REPO)}")


if __name__ == "__main__":
    main()
