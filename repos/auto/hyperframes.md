# heygen-com/hyperframes

> "Write HTML. Render video. Built for agents." TypeScript framework that turns HTML/CSS/media + seekable animations into deterministic MP4s — the unit an agent can author and a pipeline can render reliably.

- **URL**: https://github.com/heygen-com/hyperframes
- **Tags**: `agent` `media` `frontend` `infra`
- **Maturity**: 25,875 stars · 407 today on trending 2026-06-09 · created 2026-03-10 · very active (last push 2026-06-09)
- **License**: Apache 2.0

## What it actually is

An open-source framework from HeyGen (the avatar-video company) for turning HTML + CSS + media + GSAP-style animations into deterministic MP4 videos. Substrate: Node ≥22, Puppeteer for rendering, FFmpeg for encoding. The thesis is in the README tagline: *agents are good at writing HTML, so make video output a function of HTML.* You hand the agent a templating model it already knows (HTML/CSS) instead of a video-editing DSL it doesn't, and HyperFrames handles the deterministic frame-by-frame render. MCP-compatible (listed in topics) — usable as an MCP tool from any agent.

## What's reusable

- **The "HTML as video DSL" insight.** Don't invent a custom video format for agents; lean on what LLMs are already trained on. Generalizes: any agent-authored output format should map to a substrate LLMs know well.
- **Deterministic Puppeteer-based renderer.** Most "HTML to video" pipelines drift between runs because of timing/JS execution. HyperFrames pins this. Look at how, even if you build your own.
- **GSAP + FFmpeg integration patterns.** GSAP for the animation timeline, FFmpeg for encoding. Working reference for both.
- **The block catalog** (e.g., `data-chart` shown in the link) — reusable HTML/CSS components designed to render cleanly to video. Useful as a starting design system for any "agent-makes-charts-or-cards" project.
- **MCP server exposure.** The framework can run as an MCP tool, so Claude/Goose can produce videos with a single tool call.
- **TypeScript-first.** Cleaner DX than the Python `moviepy`/`manim` ecosystems for the LLM-output-then-render workflow.

## Project ideas (forward-looking)

- **Daily auto-video digest of repo-radar.** Pipe today's trending → HTML cards → MP4 via HyperFrames → publish to YouTube Shorts. Why this repo: HTML templating + MP4 render is the entire missing piece between this radar and a video format.
- **"Explain this PR" video generator.** Diff → HTML walkthrough with code blocks and annotations → MP4. Why this repo: complex layout is easy in HTML, hard in moviepy.
- **Per-customer onboarding videos at scale.** Personalized HTML template, render N times with N data inputs. Why this repo: deterministic render means same HTML always produces same frames — caching and reproducibility win.
- **Newsletter-to-podcast-clip pipeline.** Newsletter HTML → 30-second teaser video. Why this repo: drop-in replacement for After Effects in agent-driven pipelines.
- **Stock chart explainer videos.** Pair with the data layer from TradingAgents or similar — produce a daily "what moved" video per ticker. Why this repo: chart blocks already exist in the catalog.

## What to skip

- HeyGen's commercial avatar product is what the company sells — HyperFrames is open source but the polished avatar pieces are gated. Don't expect avatar features here.
- Don't try to do real-time / live video with this — it's render-to-file, not streaming.
- The badge-heavy README scrolls forever; jump to Quickstart and the Catalog link.

## Watch-outs

- **Puppeteer + Chrome dep is heavy.** RAM-hungry, Docker images get big.
- **Apache 2.0 on the library**, but the *blocks catalog* and any HeyGen-published templates may have separate terms — check before bundling them in a commercial product.
- **Node ≥22 requirement** — newer than many CI images. Update your runners.
- **Vendor (HeyGen) owns the project.** Same caveat: features that compete with the paid avatar product may get less love.
- **Created 2026-03-10** — three months old. API will move; pin versions.
- **Deterministic-render is harder than it looks.** Pin Chrome version too; browser updates can shift sub-pixel rendering and break determinism.
