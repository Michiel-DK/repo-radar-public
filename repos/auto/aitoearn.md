# yikart/AiToEarn

> "Let's use AI to Earn!" One-person-company AI content marketing agent — auto-publish, monetize, engage across TikTok, YouTube, Instagram, X, Douyin, Xiaohongshu, Kuaishou, Bilibili, and more.

- **URL**: https://github.com/yikart/AiToEarn
- **Tags**: `agent` `media` `frontend` `llm-ops`
- **Maturity**: 19,410 stars · #5 GitHub Trending 2026-06-08 · created 2025-02-24 · active (last push 2026-05-21)
- **License**: MIT

## What it actually is

An Electron desktop app + supporting infrastructure for solo content creators: pick a topic, AI generates the draft (video or image-text), AiToEarn auto-publishes to 13+ social platforms (Douyin, Xiaohongshu, Kuaishou, Bilibili, WeChat Video, TikTok, YouTube, Facebook, Instagram, Threads, X, Pinterest, LinkedIn), tracks engagement, and routes monetization back to you. Recent version 2.4 added HappyHorse 1.0 + Seedance 2.0 (Chinese video models) for batch draft generation, multi-model selection, and reference-image/video support. Five distinct ways to use it: web app, OpenClaw embedded, Claude/Cursor MCP, Docker self-host, source-build for developers. Chinese-led (Aitoearn.ai) but multilingual.

## What's reusable

- **The cross-platform publisher.** 13+ platform auto-publish is the unsexy-but-load-bearing part of any content business. Wiring even three of these from scratch takes weeks.
- **MCP integration.** Exposed as MCP tools so any agent (Claude / Cursor) can drive it. Reference for "wrap an existing product as an MCP server."
- **Multi-model draft generation.** Switches between HappyHorse, Seedance, and others — pattern for any "select-the-best-model-for-this-content" app.
- **Reference-image + reference-video constraints.** Useful technique for keeping brand-consistent outputs across many platforms.
- **"OpenClaw" integration** — the lobster-themed AI tool ecosystem out of China; useful if you're targeting that market.
- **Pattern: "OPC (one-person-company) productivity stack."** The framing is sharper than "creator tools" — single creator, fully automated, target = monetization.

## Project ideas (forward-looking)

- **Niche vertical creator agent.** Strip AiToEarn down to one vertical (e.g., real estate listings, recipe shorts, language learning) — opinionated content gen + auto-publish. Why this repo: publisher is solved; you just write the prompt + style guide.
- **B2B social ops dashboard for SMBs.** Repackage as "we run your TikTok/Instagram." Why this repo: it's already a full pipeline, just add the agency layer.
- **Cross-platform analytics + repurposing for an existing creator.** Pull your YouTube videos, auto-cut to shorts, push to TikTok/Reels/Shorts/Bilibili. Why this repo: distribution is done.
- **"Content commodity exchange" feature inspired by their v2.1 trading market.** Match creators with brands paying for promotional posts; AiToEarn handles the publishing. Why this repo: the marketplace mechanic is already there.
- **Brand-safety guardrails layer.** Most auto-publish tools skip moderation; build the "AI-generated content review" service that sits in front of AiToEarn. Why this repo: clean integration point.

## What to skip

- The English README (`README_EN.md`) is thinner than the Chinese original; read the Chinese one through a translator if you really want to evaluate.
- The "5 ways to use it" matrix is marketing — for real eval pick one (Docker self-host).
- The image-heavy README content takes forever to load; skim, don't read.

## Watch-outs

- **TOS landmine across 13 platforms.** Auto-publishing without each platform's blessing is borderline-or-worse for most of them. Personal use is fine; building a SaaS on this would be a legal/relationship minefield.
- **API key model.** Requires obtaining an AiToEarn API key for the embedded / Docker / MCP paths — vendor dependency for the "free" tier.
- **Chinese-first ecosystem.** Bilibili / Xiaohongshu / Douyin / Kuaishou / WeChat are first-class; Western platforms feel slightly less invested-in. Fine if your audience overlaps, less fine otherwise.
- **Electron app.** Heavy, OS-permissions-hungry (it has to drive auth flows for 13 platforms).
- **19k stars in 16 months is hot, but content-auto-publish tools have a 12-month half-life as platforms change their auth.** Expect ongoing breakage.
