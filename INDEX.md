# Index

Curated GitHub repo write-ups, sorted by usefulness (highest first). Each row links to a per-repo doc covering what it is, what's reusable, and concrete project ideas.

| Type | Source | Slug | Tags | One-liner | Why it's interesting |
|---|---|---|---|---|---|
| repo | anthropics/skills | [anthropic-skills](repos/anthropic-skills.md) | `skill` `mcp` `agent` | Anthropic's canonical Agent Skills reference repo (creative, technical, doc skills). | The spec + skill-creator + mcp-builder are the canonical starting points for any skill work. |
| repo | anthropics/knowledge-work-plugins | [knowledge-work-plugins](repos/knowledge-work-plugins.md) | `skill` `mcp` `agent` | 11 role-specific Claude plugins (sales, finance, data, legal, PM, etc.). | Reference plugin manifest + connector-graceful skills — clone, swap to your vertical, ship. |
| repo | affaan-m/ECC | [ecc](repos/ecc.md) | `agent` `skill` `mcp` `infra` | Cross-harness operator system: 249 skills, 63 agents, hooks, multi-harness install. | Best reference for "ship same config to N coding harnesses" + continuous-learning pattern. |
| repo | Lum1104/Understand-Anything | [understand-anything](repos/understand-anything.md) | `agent` `rag` `frontend` | Codebase to interactive knowledge graph with multi-agent pipeline + dashboard. | Living architecture docs + onboarding-in-a-box product ideas land directly on this stack. |
| repo | Imbad0202/academic-research-skills | [academic-research-skills](repos/academic-research-skills.md) | `skill` `agent` `research` | 10-stage academic pipeline with mandatory integrity gates and claim-level audit. | Mandatory integrity-gate architecture generalizes to any high-stakes generation pipeline. |
| repo | Leonxlnx/taste-skill | [taste-skill](repos/taste-skill.md) | `skill` `frontend` | Anti-slop frontend skill bundle — dials + design-system map + GSAP skeletons. | Dial-based skill controls and brief-inference pattern; instant polish for any AI-built UI. |
| repo | mukul975/Anthropic-Cybersecurity-Skills | [anthropic-cybersecurity-skills](repos/anthropic-cybersecurity-skills.md) | `skill` `agent` `research` | 754 cybersec skills across 26 domains, mapped to 5 standards frameworks. | Architecture for shipping 100s of vertical skills at scale; framework-mapping pattern reusable. |
| repo | vitali87/code-graph-rag | [code-graph-rag](repos/code-graph-rag.md) | `rag` `agent` `mcp` `data` | Tree-sitter + Memgraph + LLM-as-Cypher: graph-RAG for any polyglot codebase. | Graph-RAG beats embedding-RAG for "what calls X?" — strong for code intel + refactor safety. |
| repo | harry0703/MoneyPrinterTurbo | [moneyprinter-turbo](repos/moneyprinter-turbo.md) | `media` `llm-ops` `agent` | Prompt to short-form video: script + footage + voiceover + subtitles + music. | End-to-end media pipeline with 14+ LLM providers — months of build saved for any video product. |
| repo | badlogic/pi-skills | [pi-skills](repos/pi-skills.md) | `skill` `agent` `infra` | Curated 9-skill bundle: Workspace, Brave, browser, transcribe, YouTube, VS Code. | Quickest path to a personal AI ops assistant; pragmatic skills you'll actually use weekly. |
| repo | obsidianmd/obsidian-clipper | [obsidian-clipper](repos/obsidian-clipper.md) | `scraping` `rag` `llm-ops` `data` | Official web→Markdown clipper with BYO-LLM "Interpreter" (`{{"prompt"}}` template vars; Ollama/Anthropic/etc.). | `defuddle` deterministic extract + template-as-extraction-contract; basis for a clip→`repos/auto/` dogfood feeder. |

## Notes

- `taste-skill` task brief listed it as a subdir of `anthropics/skills`, but no such subdir exists. Canonical repo is `Leonxlnx/taste-skill` and that's what's documented.
- `vitali87/code-graph-rag` returned a transient 404 via `gh repo view` but the repo is live and active — confirmed via search results and the SourceForge backup mirror.
- All other 8 repos were resolved cleanly with the slugs as given.
