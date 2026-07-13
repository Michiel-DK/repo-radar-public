# Panniantong/Agent-Reach

> "Give your AI agent eyes to see the entire internet." One CLI to read & search Twitter, Reddit, YouTube, GitHub, Bilibili, Xiaohongshu — zero API fees, install via one line pasted to your agent.

- **URL**: https://github.com/Panniantong/Agent-Reach
- **Tags**: `agent` `mcp` `scraping` `infra`
- **Maturity**: 23,995 stars · #6 GitHub Trending 2026-06-08 · created 2026-02-24 · active (last push 2026-05-18)
- **License**: MIT

## What it actually is

A Python toolkit (CLI + MCP server) that bundles working scrapers/readers for the platforms AI agents typically can't access: YouTube (yt-dlp transcripts), Twitter/X (twitter-cli), Reddit, Bilibili, Xiaohongshu (Rednote), GitHub, generic web pages, and RSS. Install model: paste one URL into your agent ("帮我安装 Agent Reach: https://…/install.md") and it sets itself up. Targets Chinese + global platforms equally — Bilibili and Xiaohongshu are first-class, which is rare. The thesis: every platform has its own auth/scraping/IP-block gotcha, and you shouldn't redo the work yourself.

## What's reusable

- **The per-platform readers themselves.** Working yt-dlp transcript fetch, twitter-cli wrapper, reddit reader that bypasses the 403 ban on AWS IPs, Bilibili connector, Xiaohongshu cookie-based reader. Each is a self-contained capability you can lift.
- **The "paste-this-link to your agent" install pattern.** The README content at `/install.md` is written as instructions FOR the agent to execute, not for the human. This is a clean trick — install is fully agent-driven, no human ops needed.
- **MCP server packaging.** Exposes each platform reader as an MCP tool, usable from Claude / Cursor / any MCP host. Reference if you're shipping any "give the agent tool X" capability.
- **Bilibili + Xiaohongshu first-class support.** If you're building anything for the Chinese market or anything Chinese-content-aware, this is the only OSS reference I've seen with both wired up.
- **Pattern: "free, self-hosted alternative to paid platform APIs."** Twitter API is $100/mo+, Reddit API is increasingly paywalled, YouTube Data API has quotas — this routes around all of them with cookies/scrapers.

## Project ideas (forward-looking)

- **Drop-in "internet eyes" for any Claude/Goose/Cursor agent project.** When you build any agent that "should be able to read X," wire this MCP server first. Why this repo: the readers all exist; you save weeks of per-platform plumbing.
- **Chinese-market competitive intel agent.** Bilibili + Xiaohongshu + Weibo readers feeding a per-brand or per-product daily brief. Why this repo: the China-platform support is rare and expensive to build from scratch.
- **Repo-radar trend explainer.** Feed today's trending repo list into Agent-Reach, pull Reddit/HN/X discussion of each, synthesize "why it's trending." Why this repo: closes the loop between *what's trending* (this radar) and *why people are talking about it*.
- **Brand sentiment monitor with cookies-not-APIs.** Useful for hobby/personal use where API costs would kill the project. Why this repo: zero ongoing API fees.
- **Auto-transcribe-and-summarize YouTube learning queue.** Watch-later list → batch transcribe → daily digest. Why this repo: transcript fetcher is the hard part and it's solved here.

## What to skip

- The Chinese-first README is fine; the [English version](docs/README_en.md) and Japanese/Korean translations are linked but the project is genuinely Chinese-dev-led — don't assume parity.
- Don't run the cookie-based readers (Xiaohongshu especially) on a logged-in account you care about; risk of account flag.

## Watch-outs

- **TOS risk.** Reddit, X, YouTube all explicitly disallow this. Fine for personal use; risky to build a B2B product on.
- **Cookies-on-your-local-box auth model** means anything you ship to other people needs them to provide their own cookies. Friction.
- **Platforms break the readers.** Twitter changes its endpoints constantly; expect ongoing breakage. The README explicitly says "平台封了我们修" (when platforms ban it, we fix it) — depends on the maintainer's velocity.
- **No English-language community.** Issues and discussions are largely in Chinese. Fine for code use, hard for debugging via the community.
- **23k stars in ~4 months is hot.** Could be the new defacto agent-internet-access layer, or could be a launch-spike repo — revisit in 90 days.
