# obsidian-clipper

> Highlight and capture the web in your favorite browser — saved as durable Markdown into an Obsidian vault.

- **URL**: https://github.com/obsidianmd/obsidian-clipper
- **Tags**: `scraping` `rag` `llm-ops` `data`
- **Maturity**: 4.7k★ · last release v1.7.0 (2026-06) · **active** (1,015 commits, official Obsidian project)
- **License**: MIT (trademarks/marketing assets excluded)

## What it actually is

The official cross-browser (Chrome/Firefox/Safari, incl. iOS) web clipper for Obsidian. Input = any web page; output = a clean Markdown note written into a local vault, populated from a **template** (variables + filters). The substrate is TypeScript; content extraction is handled by [`defuddle`](https://github.com/kepano/defuddle) (deterministic readability/DOM cleanup), with `DOMPurify`, `lz-string`, `dayjs`.

The interesting half is **Interpreter**: a bring-your-own-LLM layer. You configure a provider — **Anthropic, OpenAI, Gemini, Azure, DeepSeek/xAI/Perplexity/HF, or Ollama for fully-local** — and write natural-language prompt variables `{{"summarise the thesis in 3 bullets"}}` directly in the template. At clip time it sends the page context + all template prompts in **one request** and substitutes the answers, with chainable filters for post-processing (`{{"summary"|blockquote}}`). Selector variables scope the model to a page region.

## What's reusable

- **The clean embodiment of repo-radar's favourite pattern**: deterministic extract (`defuddle`) split from the LLM semantic step (Interpreter). Same split as `academic-research-skills`' gated pipeline — here it's a shipped, maintained reference.
- **`defuddle`** — standalone, MIT, importable: web page → clean Markdown/structured content without an LLM. Useful anywhere you scrape-then-summarise (cheaper, deterministic first pass before any model call).
- **Template-as-extraction-contract**: `{{"prompt"|filter}}` variables turn a Markdown template into a typed extraction spec. The pattern maps directly onto `TEMPLATE.md`'s fields — a template *is* the schema.
- **One-request batching**: all prompts in a template go to the model in a single call, not N calls per field. Cost pattern worth copying (see the `cost-aware-llm-pipeline` skill).
- **BYO-LLM provider abstraction** with **Ollama/local** as a first-class option — squarely aimed at the "run AI on my own terms" data-control demand.

## Project ideas (forward-looking)

- **Dogfood: clip→vault feeder for repo-radar itself** *(front-runner — lowest friction pilot we have).* repo-radar already *is* a Markdown vault (`repos/`, `products/`, `[[wikilinks]]`, `TEMPLATE.md`). Build a clipper template whose `{{"..."}}` prompts mirror TEMPLATE.md's headings (what-it-is / reusable / project-ideas / watch-outs), pointed at a vault folder = `repos/auto/`. Clip any product page or GitHub repo → Interpreter drafts the write-up in our own house format → review and promote. The vault exists, the value is immediate, and it stress-tests the BYO-LLM extraction stack with zero new infra.
- **"Ask my documents" cited-answers copilot.** The clip→vault→cited-query stack is the skeleton of a local-first document Q&A tool. Building the dogfood loop teaches the BYO-LLM structured-extraction + local-first-vault retrieval mechanics such a tool needs, before committing to a full build.
- **Local-first research vault** with Ollama Interpreter — clip + auto-summarise + auto-tag with no data leaving the machine. A direct answer to the independence / data-control demand cluster.
- **Template marketplace angle**: opinionated, vertical clipper templates (legal, finance, competitive-intel) are a thin, shippable artefact on top of someone else's maintained extension.

## What to skip

- The browser-extension shell (manifest, popup UI, i18n) is not reusable for a headless pipeline — what you want is `defuddle` + the Interpreter prompt/template/batching pattern, not the extension.
- Clipping is a human-in-the-loop surface (someone must sit and clip). If your use case needs unattended ingestion, take the extraction *pattern* but not the extension.

## Watch-outs

- Interpreter sends **page content to your chosen provider** — for anything sensitive or regulated, default to Ollama (local) or be explicit about data egress.
- Vault writes need the Obsidian app (Local REST / file access); the extension assumes a human-in-the-loop Obsidian install, not a server. For an automated feeder you'd reimplement the write path against the file system, keeping only the extraction logic.
- "One request with all prompts" means a big template = a big context window per clip; watch token cost on long pages.
