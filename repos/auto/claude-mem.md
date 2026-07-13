# thedotmack/claude-mem

> Persistent context across sessions for every agent — captures what your agent does, compresses it with AI, injects relevant context into future sessions.

- **URL**: https://github.com/thedotmack/claude-mem
- **Tags**: `agent` `rag` `skill` `data`
- **Maturity**: 81,523 stars · 218 today (newcomer 2026-06-10) · created 2025-08-31 · active (last push 2026-06-10)
- **License**: Apache-2.0

## What it actually is

A cross-session memory engine for coding agents. It hooks the session lifecycle: captures everything the agent does, **compresses it with an LLM**, stores it (SQLite + ChromaDB embeddings), and **injects relevant context back** at the start of future sessions. Multi-host by design — Claude Code, Codex, Gemini, Copilot, OpenCode, etc. Ships as a Claude Code plugin/skill. JavaScript.

## What's reusable

- **The capture → compress → inject loop** — this is the exact shape of a vertical agent's "learning loop": accumulate raw events, compress, surface relevant slice later. A working reference implementation.
- **Compression-before-store** — instead of dumping raw logs, LLM-summarize then embed. Keeps the store small and recall sharp; a good pattern for any long-running agent.
- **Session-lifecycle hooks** as the integration point — clean way to make memory passive (no user action required) — ideal when the design goal is to never require proactive data entry.
- Multi-host adapter layer — one memory engine, many agent front-ends.

## Project ideas (forward-looking)

- **Persistent context for the repo-radar digest agent** — remember prior digests/themes so each day builds on the last instead of starting cold.
- **Memory substrate comparison** — benchmark claude-mem (compress-then-store) vs. MemPalace (verbatim, no-API) for the per-tenant brain; they sit at opposite ends of the cost/fidelity axis.
- **Cross-session memory for any vertical agent** — many vertical agent ideas want an agent that remembers the customer; this is the engine.

## What to skip

- 81k stars on a repo this size is suspiciously high — treat the metric skeptically and judge on the code, not the badge.
- It's opinionated about the Claude Code lifecycle; the "works with everything" list may be aspirational for some hosts.

## Watch-outs

- **LLM compression cost** — capture+compress runs a model per session; not free at scale (contrast MemPalace's zero-API approach).
- ChromaDB + SQLite local deps; embedding model dependency for recall.
- Huge topic-tag surface (mem0, supermemory, openmemory…) suggests a crowded, fast-moving category — expect churn and consolidation.
