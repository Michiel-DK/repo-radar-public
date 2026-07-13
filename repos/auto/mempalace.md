# MemPalace/mempalace

> Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 on LongMemEval — zero API calls.

- **URL**: https://github.com/MemPalace/mempalace
- **Tags**: `agent` `rag` `mcp` `data`
- **Maturity**: 55,220 stars · 404 today (new to top 12, 2026-06-10) · created 2026-04-05 · active (last push 2026-06-08)
- **License**: MIT

## What it actually is

An open-source long-term memory layer for AI agents: store interactions, retrieve relevant context later. Pitches itself on *benchmarks* (96.6% Recall@5 on LongMemEval) and *local-first* operation — verbatim storage with a pluggable backend (ChromaDB by default) and **zero API calls**, so the memory layer doesn't add per-query LLM cost. Exposed over MCP, so any MCP-capable agent can use it as a memory tool. Python.

## What's reusable

- **The "no API calls" retrieval design** — verbatim store + local embedding/retrieval. Directly relevant to any per-tenant LLM-unit-economics concern: memory/recall that doesn't bill per query.
- **MCP-exposed memory** — pattern for "memory as a tool any agent can call" rather than bolted into one harness.
- **Benchmark-first positioning** (LongMemEval R@5) — a reusable framing: lead with a recall number, not vibes.
- Pluggable backend abstraction (Chroma now, swappable) — clean seam if you want a different vector store.

## Project ideas (forward-looking)

- **Per-tenant brain for vertical SaaS.** MemPalace is a candidate substrate for a "personal brain per tenant" — local-first, per-tenant memory with cheap recall. Why this repo: solves the cost + isolation concern out of the box.
- **Local memory for a personal agent.** Drop-in long-term memory for any MCP agent without sending data to an API. Why this repo: privacy + zero marginal cost.
- **Memory-backed digest writer.** Give the repo-radar digest agent persistent memory of past digests so it can say "this is the 3rd day X persisted." Why this repo: cheap recall over accumulated daily snapshots.

## What to skip

- The eye-popping star count (55k) + 7k forks for a 2-month-old repo warrants a sniff test — verify the LongMemEval claim before trusting it as production-grade.

## Watch-outs

- **Impostor-site warning in the README** — only trust the GitHub repo + official PyPI; there are spoofs. Signal that the name is being squatted.
- Very young (created 2026-04). API/storage format likely to churn.
- "Best-benchmarked" is self-reported — reproduce the benchmark before betting on it.
