# mvanhorn/last30days-skill

> "An AI agent-led search engine scored by upvotes, likes, and real money — not editors." Searches Reddit, X, YouTube, HN, TikTok, Polymarket, and the web in parallel and synthesizes one grounded brief.

- **URL**: https://github.com/mvanhorn/last30days-skill
- **Tags**: `skill` `agent` `research` `rag`
- **Maturity**: 34,232 stars · #1 GitHub Trending 2026-06-08 · created 2026-01-23 · active (last push 2026-06-06)
- **License**: MIT

## What it actually is

An Anthropic-style Agent Skill (`/last30days`) that runs a multi-source search over what real people are voting/engaging on right now, then has an agent judge synthesize the answer. Substrate: Python skill bundle distributed via the Claude Code plugin marketplace and the cross-host `skills` package (works in Codex, Cursor, Copilot, Gemini CLI, OpenClaw, etc.). The pitch: Google aggregates editors, this aggregates people — Reddit upvotes, X likes, YouTube transcripts, TikTok engagement, Polymarket odds. Zero-config for Reddit/HN/Polymarket/GitHub; a 30-second setup wizard unlocks X/YouTube/TikTok.

## What's reusable

- **The cross-host distribution model** — same skill bundle installs into Claude Code (marketplace), Codex/Cursor/Copilot/Gemini (`npx skills add ...`), and 50+ Agent Skills hosts. Reference for how to ship one skill once and have it usable everywhere.
- **`skills/last30days/SKILL.md`** is declared the source-of-truth for runtime behavior — pattern for "README describes the project, SKILL.md is the contract." Good separation.
- **Multi-source agent judge pattern** — fan out to N social/data sources in parallel, weight by engagement signal, agent synthesizes. Generalizes to any "real-people scoring" use case.
- **Polymarket as a signal source** is a fresh idea — money-weighted opinions are a different kind of ground truth from likes/upvotes.
- **Setup-wizard skill** — first-run interactive auth flow for paid/auth'd platforms (X/YouTube/TikTok) without burdening zero-config users. Pattern worth copying for any skill that has both free and authenticated modes.

## Project ideas (forward-looking)

- **VC-deal-flow signal aggregator.** Replace Reddit/X with Crunchbase/PitchBook/HN/X-fintwit feeds; same agent-judge synthesis. Why this repo: the parallel-fanout + engagement-weighted synthesis is exactly the shape.
- **Personal "what's hot in my stack" digest.** Subscribe to a list of topics (your frameworks, your competitors); daily brief from the last 30 days of social signal. Why this repo: the skill is the brief generator already.
- **Repo-radar trend explainer.** Pipe today's GitHub trending list *into* `/last30days` to get "why is this repo blowing up across social right now." Why this repo: completes the loop between trending detection (this radar) and trend explanation (social-signal synthesis).
- **Polymarket-driven research assistant.** Strip everything but Polymarket + web search; turn into a forecasting-research skill. Why this repo: the Polymarket integration is already wired.
- **Customer-voice-of-the-market skill.** Aim it at a product or brand, score Reddit/X/TikTok/YouTube mentions, generate a quarterly brief. Why this repo: the scoring + judge is plug-and-play.

## What to skip

- The trending badge / Trendshift links in the README are marketing decoration.
- Don't reuse the Polymarket scraper verbatim if you're not also using their odds-weighting logic — values are meaningless without it.

## Watch-outs

- **TOS risk on X/TikTok/Reddit scraping.** The "no API fees" model means cookie-based or unofficial endpoints — fine for personal use, risky to ship in a B2B product.
- **Skill spec lock-in.** Built against Anthropic's Agent Skills format; cross-host claims rely on the `skills` npm package translating. If that package goes stale you lose the cross-host story.
- **Quality is judge-dependent.** The "agent judge synthesizes" step is where slop can creep in if you swap models — pin the judge model or eval it.
- **Stars-per-day is very high (3.5k/day).** Early-stage hype; revisit in 30 days to see if usage sticks or this was a launch spike.
