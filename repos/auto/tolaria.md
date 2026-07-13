# refactoringhq/tolaria

> "💧 Tolaria is a desktop app for macOS, Windows, and Linux for managing markdown knowledge bases." Files-first, git-first, offline by default — Luca Rossi's personal second-brain shipped as an app.

- **URL**: https://github.com/refactoringhq/tolaria
- **Tags**: `frontend` `infra` `data`
- **Maturity**: 13,498 stars · #8 GitHub Trending 2026-06-08 · created 2026-02-14 · very active (last push 2026-06-08)
- **License**: AGPL-3.0 ⚠

## What it actually is

A desktop markdown knowledge-base manager (TypeScript / Electron-shaped, judging by the stack) targeting people who run their working life out of plain markdown. Built by Luca Rossi (author of the Refactoring newsletter) for his own use — 10,000+ notes, mixed second-brain and personal journaling. Three positioned use cases: personal second brain, company doc workspace as AI context, OpenClaw/assistants memory store. The strong opinion is that your notes are plain `.md` files in a git repo you own — no app-specific format, no cloud lock-in, no server you depend on.

## What's reusable

- **The files-first + git-first architecture.** This is the canonical reference for "knowledge app where the data outlives the app." Worth reading even if you don't use it.
- **Pattern: workspace = git repo.** Every vault is a git remote of your choice; version history is free and the app has no proprietary backend. Generalizes to any "user data should be portable" product.
- **"Use this as AI memory" framing.** Tolaria is positioned as the place agents read/write long-term context. If you're building any persistent-memory agent, the markdown-files-in-git substrate is a strong choice.
- **Loom walkthrough format** as docs — short, opinionated, user-driven. Better onboarding than a wall of text. Pattern worth copying for any app docs.
- **Refactoring.fm community as a launchpad.** Not code, but a model: build a thing for your existing audience, charge for the high-leverage half, OSS the rest.

## Project ideas (forward-looking)

- **AI-assisted second brain on top of Tolaria.** Use Tolaria as the storage substrate, add a Claude/Goose agent that knows your vault. Why this repo: the files-on-disk-in-git model is exactly what an agent wants — no API to call, just read the markdown.
- **Company knowledge base with agent integration.** Tolaria for the human UI, an MCP server over the vault for the agent. Why this repo: doubles the value of every doc.
- **Personal radar built on Tolaria.** Use it as the UI for *this* repo-radar — render `repos/*.md` and `digests/*.md` inside Tolaria, get a real reading app for free. Why this repo: zero impedance mismatch; Tolaria is just markdown + git, which is what we already have.
- **Journaling-as-memory for an agent.** Daily journal in Tolaria → agent reads the past week as context → produces a weekly review. Why this repo: substrate is already there.
- **Vertical Tolaria forks** — for researchers (PDF + notes), VCs (deal notes + companies), consultants (per-client folders). Why this repo: AGPL means you fork and contribute back; ok for internal use.

## What to skip

- Don't pay for "Refactoring" subscription just for Tolaria — the app is fully OSS.
- The Loom walkthroughs are great for vibes, not for code patterns.

## Watch-outs

- **AGPL-3.0.** This is a hard one. If you build a SaaS on top of Tolaria's code, you must open-source your service. Fine for personal use, internal tools, or genuinely open products; **avoid for closed-source commercial products.** This is the most important fact in this writeup.
- **Solo-maintainer project.** Luca is the primary author. Refactoring is his main thing. Bus-factor of 1; budget for "maintainer takes a sabbatical."
- **Electron app.** Heavy, slow to start, RAM-hungry. Trade-off you accept for cross-platform.
- **Created 2026-02-14, currently 13k stars** — very young. Expect breaking changes in the vault format and plugin API.
- **"Files-first" is a strong opinion** — if you want collaborative real-time editing, this is not the app (and probably never will be).
