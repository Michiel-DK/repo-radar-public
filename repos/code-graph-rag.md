# vitali87/code-graph-rag

> A graph-based RAG system for any codebase: Tree-sitter parses → Memgraph stores → natural-language queries via Cypher.

- **URL**: https://github.com/vitali87/code-graph-rag (live; gh API returned 404 transiently — confirmed via SourceForge mirror `spashx/code-graph-rag` and the live web page redirect)
- **Tags**: `rag` `agent` `mcp` `data`
- **Maturity**: stars unknown (gh metadata refused; README badges suggest active codecov + OpenSSF scorecard) · active (recent C-language PR landed)
- **License**: not surfaced in metadata; check repo before commercial use

## What it actually is

A Python (3.12+) CLI + MCP server that ingests a multi-language codebase (Python, TS, JS, Rust, Java, C, C++, Lua + several "in development"), parses it with Tree-sitter into a unified node/edge schema, and stores the result in Memgraph. You then query the graph in natural language — an "orchestrator" LLM routes intent, a "cypher" LLM translates English → Cypher, and the system returns code snippets and graph results. Also ships as an MCP server so Claude Code can drive the same query/edit loop interactively. Supports OpenAI, Gemini, and local Ollama models, mix-and-match per role.

## What's reusable

- **Pattern**: deterministic Tree-sitter parse → graph store → LLM-as-query-translator. Way more accurate than embedding-RAG for "what calls X?" / "what depends on Y?" questions. Worth borrowing whenever you can express a relationship explicitly.
- **Two-model split**: orchestrator (intent routing) on a smart model + cypher generator on a cheap model. Mirrors the cost-aware-pipeline pattern.
- **Unified schema across languages** — single graph shape, language-specific parsers feed into it. Reusable design choice for any polyglot data pipeline.
- **Docker-compose for Memgraph** — clean local-dev recipe for a graph DB that's normally a pain to stand up.
- **MCP integration** — exposes the query/edit surface to any MCP client. Reference implementation for "wrap your own graph as a tool for an agent harness."

## Project ideas (forward-looking)

- **Polyglot codebase concierge for legacy/M&A audits.** Point at a recently-acquired codebase, generate the graph, then let acquirers ask "what does this module depend on?" and "who owns the payment flow?" in natural language. Why this repo: legacy codebases are almost always polyglot — Tree-sitter handles that without per-language work.
- **Refactor-safety bot.** Before a large refactor, generate the graph and have the agent enumerate every caller/dependent of the symbol being changed. Wraps `arbor`-style deterministic call-graph reasoning around an LLM planner. Why this repo: deterministic graph rules out the hallucination class that breaks refactor agents.
- **MCP server for a private codebase, exposed to claude.ai.** Stand up the MCP server inside your VPN, give claude.ai read-only access — now the assistant can answer architecture questions over the actual code without leaking source. Why this repo: MCP path is documented, Memgraph stays local.
- **Code-graph + news fusion for VC due diligence.** Combine `pgv_news_articles`-style entity graph with this code-graph for OSS-heavy startups ("does the founder's GitHub actually back the technical claim in the deck?"). Why this repo: gives you the deterministic OSS half of the picture.
- **`/understand-anything` competitor with a real graph DB backend.** Where Understand-Anything ships a JSON file + browser dashboard, this ships Memgraph + Cypher — easier to query programmatically, harder to ship as a plugin. Why this repo: better choice when the graph is consumed by another service, not a human.

## What to skip

- The "interactive code optimization" feature looks demo-heavy; the parsing + query layer is the load-bearing part.
- The shipped Cypher prompts are fine starting points but specific to Memgraph's flavor; if you swap to Neo4j you'll need rework.
- The "edit code" capabilities turn this into a coding agent — out of scope if you only want a knowledge layer.

## Watch-outs

- License not in gh API metadata; verify before any redistribution.
- Heavy deps: Memgraph (Docker), Tree-sitter grammars, `pymgclient` needs cmake, ripgrep, Python 3.12+. Not a 5-minute install.
- Languages marked "In Development" (C#, Go, PHP, Scala) are partial — verify coverage before committing to a stack.
- Provider-explicit config (separate provider for orchestrator vs cypher) is great for cost control but adds setup surface area.
