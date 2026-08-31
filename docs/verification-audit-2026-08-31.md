# Verification audit — 2026-08-31

Part of a portfolio-wide audit: each repo checked against the five conditions
needed to honestly claim "we check, show the honest result, act on it."
Cross-repo comparison lives in roger3000-dev
`docs/verification-audit-portfolio-2026-08-31.md`. Code-level audit via an
Explore agent.

The five conditions: (1) **oracle** — a defined "correct" to check against;
(2) **chokepoint** — the check runs on every output, enforced; (3) **failure
surface** — a designed state for "no / I don't know"; (4) **consequence** — a
failed check changes behavior automatically; (5) **receipt** — evidence
persists and is inspectable.

## Verdicts

| # | Condition | Verdict | Evidence |
|---|---|---|---|
| 1 | Oracle | **absent** | Nothing is ever compared against a defined "correct." Near-misses: `fetch_trending.py:131-144` *overwrites* scraped fields with API values instead of diffing them; `seen.json` holds later-observed outcomes but nothing scores a prior call against them; `fetch_traction.py` pulls Stripe-verified MRR — a genuine external oracle — and is orphaned (not in `daily.yml`, not in README, ran once on 2026-07-13, never joined against anything). |
| 2 | Chokepoint | **absent** | No tests exist, no schema validation, no CI beyond the fetch cron. |
| 3 | Failure surface | **partial** | Honest but voluntary: `enrich_error`/`readme_error` persisted per-row; digests carry candid gap notes ("06-18 through 06-22 are missing and unrecoverable"). See finding below for where this slipped. |
| 4 | Consequence | **absent** | Deliberately so: `daily.yml:68` `fetch_problems.py \|\| echo "[warn] ...continuing"`. Rows with `enrich_error` flow unfiltered into `stars_gained` rankings. |
| 5 | Receipt | **present** | The one solid condition: immutable dated JSONL in git, `seen.json`, error fields in-row, digests cite inputs by path. Git history is a real audit log. |

Fairness note: the absences are *chosen*, not overlooked — the README states
"no LLM API calls in the cron / no autonomous digest" as deliberate design.
This is a personal radar, not a product making claims. The audit matters
anyway because of one finding:

## Finding: an unbacked ✅

`digests/2026-07-06.md` claimed **"✅ Full-week continuity … (verified: daily
snapshots + HN problems both present for all 7 days)"** — and no code computes
that. `compute_trends.py:151` writes `snapshot_count` and never checks date
contiguity. The claim happens to be true (all 14 files re-checked by hand,
2026-08-31, present and non-empty), but "verified" implied a verifier that
does not exist. The same hand that writes the honest ⚠ notes emitted an
unbacked ✅. Fixed in this PR: the digest line now says how the check was
actually done.

Lesson for the whole portfolio: the word "verified" is only allowed when it
names its verifier.

## If this repo should ever join the "checked" banner

Both halves of an oracle already sit in the data, unused:

1. **Score the radar's own calls.** `seen.json` records which repos persisted.
   A tiny script can grade each digest's newcomer/climber tags against what
   the following weeks actually showed — turning the digest from commentary
   into a scored prediction log.
2. **Un-orphan `fetch_traction.py`.** Stripe-verified MRR is the one external
   ground truth here; join it against past radar picks ("did the radar surface
   things that turned out to be real businesses?").
3. Cheap floor regardless: a continuity check in `compute_trends.py` (assert
   the 7 dates exist before a digest claims a full week), and stop letting
   `enrich_error` rows into rankings unfiltered.

Otherwise: leave it as a personal tool and keep it off any claim-making
surface — which is a legitimate outcome of this audit, not a failure.
