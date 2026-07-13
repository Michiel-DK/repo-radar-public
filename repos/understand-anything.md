# Lum1104/Understand-Anything

> Turn any codebase, knowledge base, or docs into an interactive knowledge graph you can explore, search, and ask questions about.

- **URL**: https://github.com/Lum1104/Understand-Anything
- **Tags**: `agent` `rag` `frontend` `research`
- **Maturity**: ~50k stars · last commit 2026-06 · active
- **License**: MIT

## What it actually is

A Claude Code plugin (also installable via one-line script for Codex, Cursor, Gemini CLI, Copilot, OpenCode, etc.) that runs a multi-agent pipeline over a directory, extracts every file/function/class/dependency, and renders an interactive force-directed graph dashboard. Inputs: a repo or a Karpathy-pattern LLM wiki. Outputs: `.understand-anything/knowledge-graph.json` plus a browser-served dashboard with semantic search, guided tours, persona-adaptive UI, layer visualization, and diff-impact analysis. Substrate: TypeScript + multi-agent prompts; deterministic extractor for structure, LLM agents for semantic enrichment.

## What's reusable

- **Pattern**: split-stage pipeline — deterministic parser → LLM enrichment → graph store → dashboard. Same shape as a quality scraping/extraction pipeline; the LLM only does the parts a parser can't.
- **Pattern**: incremental re-analysis only on changed files. Persists the previous graph, diffs, re-runs LLM only on deltas. Cheap to keep fresh.
- **`/understand-knowledge` flow** — points at a wiki/markdown corpus (`index.md` + wikilinks), extracts entities + claims, builds a community-clustered graph. Reusable pattern for any link-rich markdown corpus (notes, internal docs).
- **Dashboard UX**: force-directed graph + fuzzy/semantic search + click-to-context node panels + guided tour generator. Worth stealing the layout pattern even if not the code.
- **Persona-adaptive UI** — toggle detail level by audience (PM/junior/power-user). Same data, different framing.
- **Multi-language install script** (`install.sh`/`install.ps1` with per-platform branches) — clean reference for a skill bundle that ships to ~10 harnesses.

## Project ideas (forward-looking)

- **Onboarding-in-a-box product for engineering teams.** Drop the plugin into a new hire's repo on day 1, generate a guided tour ordered by dependency, plus a persona-adaptive dashboard. Sell as a SaaS layer that hosts the graph + tracks completion. Why this repo: the guided-tour generator and graph-as-UI are 80% of the product; commercial value is in hosting + analytics.
- **Living architecture docs for a fast-moving startup.** Plugin runs on every merge to master via a post-commit hook (`--auto-update`), publishes the graph to an internal docs site. Solves the "ARCHITECTURE.md is always stale" problem. Why this repo: the incremental re-analysis pattern means it stays cheap as the codebase grows.
- **Knowledge-base navigator for a personal/team second brain.** Run `/understand-knowledge` over a Karpathy-style wiki or an Obsidian vault, get an explorable concept graph with semantic search. Why this repo: the wiki-mode extractor is already built and produces force-directed clusters out of the box.
- **PR-impact bot.** Wrap `/understand-diff` in a GitHub Action that comments on PRs with a graph-impact diff ("this PR touches the auth domain and downstream payments"). Why this repo: `/understand-diff` already does this for one shot; CI wrapper is the only new code.
- **Code-graph-as-context for a coding agent.** Use the generated `knowledge-graph.json` as a structured retrieval layer for any RAG agent — instead of embedding chunks, query the graph by entity/relationship. Why this repo: produces the graph for free; agent only needs a query layer on top.

## What to skip

- The multilingual READMEs are noise unless you ship a non-English UI.
- The "Persona-Adaptive UI" is more demo than substance — useful as a pattern, not as code to copy verbatim.
- Don't try to use the dashboard standalone for non-code corpora without going through `/understand-knowledge` — the structural-graph view assumes file/function/class nodes.

## Watch-outs

- TypeScript + Node toolchain for the dashboard; not pure-Python like most of this list.
- LLM calls are required for the semantic step — budget accordingly on large repos (200k LOC is the headline use case).
- MIT-licensed so commercial use is fine, but the dashboard and install scripts are quite opinionated about the directory layout (`.understand-anything/`).
- Plugin marketplace install path assumes Claude Code; for other harnesses the install.sh route is more brittle.
