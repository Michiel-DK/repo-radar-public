# browser-use/video-use

> Edit videos with Claude Code — drop raw footage in a folder, chat with the agent, get `final.mp4` back. 100% open source.

- **URL**: https://github.com/browser-use/video-use
- **Tags**: `agent` `media` `llm-ops`
- **Maturity**: 12,850 stars (721 today — persister 4d, 2026-07-01) · created 2026-04 · active (last push 2026-07-01)
- **License**: MIT

## What it actually is

An agent-driven video editor from the browser-use team: point Claude Code at a folder of raw footage and describe what you want; it cuts filler words and dead space, auto-color-grades segments, adds audio fades at cuts, burns styled subtitles, and generates animation overlays (via HyperFrames). No presets/menus — the agent drives ffmpeg. It's the "agent drives a full media pipeline" pattern (headline of 06-23) applied to editing rather than generation. Python.

## What's reusable

- pattern: **agent-over-ffmpeg** — natural-language intent → deterministic ffmpeg chains. The clean split between the LLM (what to do) and ffmpeg (how) is the reusable architecture, echoing our "deterministic extract + LLM semantic step" motif.
- pattern: **folder-in / artifact-out UX** — no menus, just drop files and chat. Low-friction agent-tool design worth copying.
- The specific transforms (filler-word cut, 30ms fades, 2-word subtitle chunks) as a recipe library.

## Project ideas (forward-looking)

- **Automated content repurposing**: turn recorded sessions/demos into shippable clips via an agent. Why this repo: the edit pipeline is already agent-driven and open source.
- **Pattern donor for other agent-over-tool builds**: mirror the LLM-intent → deterministic-toolchain split for non-video domains (docs, data viz). Why: it's a crisp reference for that architecture.

## What to skip

- Ties into HyperFrames for overlays and browser-use Cloud upsell — the core local editing works without them; skip the cloud path unless you want it.

## Watch-outs

- ffmpeg-heavy; assumes a working ffmpeg install and the compute for transcodes.
- Model-dependent quality (the cut/grade decisions are LLM-driven) — review output before publishing.
