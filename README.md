# repo-radar

Personal catalogue of GitHub repos worth borrowing from, with a per-repo write-up of:

- what the repo actually is
- what's reusable
- concrete project ideas where it would unlock leverage

Used as a feeder pool for future project decisions — not a code library.

**Status (2026-09-04).** The automated half runs daily (GitHub Actions, 06:00 UTC: trending
snapshots under `data/daily/`, terse auto write-ups under `repos/auto/`). The hand-written
entries at the top level of `repos/` and the digests under `digests/` paused after 2026-07-06
while the same reading time went into building; the snapshots kept accumulating, so the raw
signal is current even where the commentary is not.

## Layout

```
repos/
  <repo-slug>.md           # hand-curated, authoritative
  auto/<repo-slug>.md      # auto-generated from daily trending; promote to repos/ when keep-worthy
INDEX.md                   # one-line summary + tags per hand-curated repo
TEMPLATE.md                # the shape both manual and auto writeups follow

data/
  daily/YYYY-MM-DD.jsonl   # one snapshot per day of github.com/trending (overall + Python/TS/Rust/Go)
  rolling/top-30d.json     # newcomers / climbers / persisters over the trailing window
  seen.json                # first_seen / last_seen / days_seen per slug, all-time

digests/
  YYYY-MM-DD.md            # daily human-readable digest: top-N, trends, links to auto writeups

scripts/
  fetch_trending.py        # scrape trending + enrich each repo via the GitHub API
  compute_trends.py        # diff today against history, write rolling/seen artifacts
  fetch_problems.py        # demand signals (HN always; Reddit if secrets set)
  fetch_traction.py        # experimental TrustMRR revenue signal; not wired into the daily cron
```

## Conventions

- One markdown file per repo under `repos/`, named `<owner-or-slug>.md`.
- Each repo doc follows the template in [`TEMPLATE.md`](TEMPLATE.md).
- Tag every repo with at least one of: `agent`, `skill`, `mcp`, `rag`, `scraping`, `llm-ops`, `frontend`, `data`, `research`, `infra`, `media`.
- When a repo no longer looks useful, move it to `repos/archived/` rather than delete.
- `repos/auto/` is a **feeder pool** — auto-generated drafts. Promote to `repos/` when you've read and want to keep one; otherwise it stays as a low-cost reference.

## How this gets used

When starting a new project, skim `INDEX.md` for matches against the project's shape (agent harness, RAG, scraping, etc.), then read the matching repo docs for concrete file paths and patterns to copy. Use the latest `digests/*.md` to spot what's emerging *right now* that the curated list hasn't caught up with.

## Daily pipeline

**Split into two halves**: data fetch runs autonomously on a GitHub Actions cron; interpretation (digest + auto-summaries) is human-paced — open `claude` in this repo whenever you want a fresh report.

### Autonomous half — GitHub Actions cron at 06:00 UTC

`.github/workflows/daily.yml` runs every day at `06:00 UTC` (≈08:00 Brussels in summer) on GitHub's infra — so it fires even when your laptop is asleep. It also has a manual "Run workflow" button (`workflow_dispatch`). Each run:

1. Checks out `master` fresh in a clean runner.
2. `python3 scripts/fetch_trending.py` — scrapes `github.com/trending` (overall + Python/TS/Rust/Go), enriches every unique repo via the GitHub API (stars, description, license, README excerpt, topics). Writes `data/daily/YYYY-MM-DD.jsonl`.
3. `python3 scripts/compute_trends.py` — diffs against history: newcomers, climbers, persisters, rolling top-N. Writes `data/rolling/top-30d.json` and updates `data/seen.json`.
4. `python3 scripts/fetch_problems.py` (best-effort) — HN demand signals → `data/problems/YYYY-MM-DD.jsonl`.
5. Commits to `master`, pushes via the built-in `GITHUB_TOKEN`.

No paid API keys needed — uses `GITHUB_TOKEN` for the API. Optional repo secrets: `REDDIT_CLIENT_ID`/`REDDIT_CLIENT_SECRET` (Reddit demand source).

### Human-paced half — `claude` in the repo when you want a digest

Open a Claude Code session in this repo and ask for today's digest. Claude will read `data/daily/<today>.jsonl` + `data/rolling/top-30d.json`, write `digests/YYYY-MM-DD.md`, and write 5-8 `repos/auto/<slug>.md` writeups for new trending repos that don't yet have one.

### Run manually

Just want raw data without waiting for the cron?
```bash
python3 scripts/fetch_trending.py      # ~1-2 min
python3 scripts/compute_trends.py      # <1s
python3 scripts/fetch_problems.py      # HN (+ Reddit if secrets set)
```

Uses `gh auth token` for the GitHub API (5000 req/hr; a run uses ~170 — two calls per repo across ~80 trending repos — well under the limit).

### Cron controls

```bash
gh workflow run daily.yml --ref master     # fire now
gh run list --workflow=daily.yml -L 5      # recent runs
```

### What's intentionally NOT in the pipeline

- **No UI.** Markdown + git.
- **No LLM API calls in the cron.** Summaries happen inside a Claude session when you want to read.
- **No autonomous digest.** Read-loop is on your terms, not the cron's.

## Setup

```bash
python3 -m pip install -r requirements.txt
gh auth login   # if not already
```
