# anthropics/skills

> Official Anthropic public repo for Agent Skills — reference implementations across creative, technical, enterprise, and document-generation use cases.

- **URL**: https://github.com/anthropics/skills
- **Tags**: `skill` `mcp` `agent` `frontend` `data`
- **Maturity**: ~146k stars · active · Anthropic-maintained
- **License**: Apache 2.0 (most skills) — `docx`, `pdf`, `pptx`, `xlsx` are source-available, not open source

## What it actually is

Anthropic's canonical demonstration repo for the Agent Skills standard. Three pieces: (1) `./skills/` with example skills across creative (algorithmic-art, canvas-design, theme-factory), technical (mcp-builder, webapp-testing, web-artifacts-builder, claude-api), enterprise (brand-guidelines, internal-comms, slack-gif-creator), and the four production document skills (`docx`, `pdf`, `pptx`, `xlsx`) that power Claude's create-files capability under the hood. (2) `./spec/` with the Agent Skills specification. (3) `./template/` for new skills. Designed as the **reference for what good skills look like**, not as a sprawling library to install whole.

## What's reusable

- **`./spec/`** — THE Agent Skills specification. Read this before writing any skill. Defines the YAML frontmatter contract, progressive-disclosure model, file layout conventions.
- **`./template/`** — minimal SKILL.md starting point. Use as the empty-state when bootstrapping new skills.
- **`skills/skill-creator/`** — meta-skill for creating new skills. Has agents subdir, eval-viewer, references, scripts. Reference for the full anatomy of a "create and iterate skills" workflow including evals. **Important**: includes guidance on writing skill descriptions that are slightly "pushy" to combat undertrigger — useful prompt-engineering note.
- **`skills/mcp-builder/`** — scaffolds new MCP servers. Reusable for anyone shipping their own MCP server (which is most agentic projects in 2026).
- **`skills/claude-api/`** — building Claude API apps with prompt caching, model migration, thinking, batch. Already referenced in my CLAUDE.md.
- **`skills/webapp-testing/`** — pattern for testing web apps end-to-end with an agent. Reusable for any "verify the change actually works" workflow.
- **`skills/web-artifacts-builder/`** — pattern for skills that produce HTML/JS artifacts (dashboards, mini-apps).
- **`skills/docx`, `pptx`, `xlsx`, `pdf`** (source-available, not OSS) — production-quality document generation. Heavy reference for any "Claude makes me a slide deck/spreadsheet" use case.
- **`skills/brand-guidelines/` + `theme-factory/`** — reference for skills that enforce house style (color, typography, voice).
- **Pattern**: progressive disclosure (`metadata` always loaded → `SKILL.md` loaded on trigger → bundled resources loaded as needed). Documented explicitly in `skill-creator`.
- **Pattern**: "domain organization" — when a skill spans multiple variants (frameworks, languages), organize by variant rather than by section. Documented in `skill-creator/SKILL.md`.

## Project ideas (forward-looking)

- **Skill-quality dashboard.** Use `skill-creator/eval-viewer/generate_review.py` as the basis for a CI tool that runs evals on every skill in a project repo and surfaces drift. Why this repo: eval-viewer is already wired to the skill-creator workflow.
- **Custom MCP server for any internal tool, generated via `mcp-builder`.** Standard pattern for "expose internal API X to an agent without writing FastAPI by hand." Why this repo: `mcp-builder` knows the MCP spec; you just describe the tool.
- **Branded artifact generator for a startup.** Combine `brand-guidelines` + `theme-factory` + `web-artifacts-builder` to spin up branded mini-apps (calculators, configurators, lead-gen widgets) from prompts. Why this repo: three composable skills already exist.
- **Spec-driven skill library for any domain.** Use `./spec/` as the standard, then organize hundreds of skills following the official structure. Better than inventing your own format. Why this repo: spec is canonical; following it means future tooling will Just Work.
- **Slide-deck generator from internal data.** Use `pptx` (source-available) + a data-fetch step + theme-factory styling. Why this repo: `pptx` skill is the production code Anthropic uses; quality is high.

## What to skip

- The "Partner Skills" Notion link is marketing — useful as inspiration, not as code.
- The four document skills (`docx`, `pdf`, `pptx`, `xlsx`) are **source-available, not open source** — fine to study, NOT fine to redistribute or use commercially without checking terms.
- `slack-gif-creator` and similar one-trick skills are demos — useful as shape references, not as production skills.
- Don't install the whole plugin (`document-skills@anthropic-agent-skills`) unless you actually need every doc type — they're heavy.

## Watch-outs

- **License is mixed**: Apache 2.0 on most skills, source-available on the 4 document skills. Read the disclaimer in the README before commercial use.
- The disclaimer is also clear that "behaviors you receive from Claude may differ from what is shown in these skills" — these are illustrative, not the literal production behavior.
- Repo is owned by Anthropic — long-term stability is good, but they may rename/restructure (e.g. spec versioning) and you'll need to migrate.
- "146k stars" is partly halo effect from being an official Anthropic repo; not every skill in here is best-in-class for its domain (`Anthropic-Cybersecurity-Skills` is bigger for security, `taste-skill` for design, etc.).
- Agent Skills spec is still maturing — pin to a version of the spec if your project depends on the exact shape.
