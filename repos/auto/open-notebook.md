# lfnovo/open-notebook

> "An open source, privacy-focused alternative to Google's NotebookLM." Multi-model, 100% local, full-featured notebook with research / podcast / chat / search workflows.

- **URL**: https://github.com/lfnovo/open-notebook
- **Tags**: `rag` `agent` `frontend` `research`
- **Maturity**: 27,933 stars · #4 GitHub Trending 2026-06-08 · created 2024-10-21 · active (last push 2026-06-04)
- **License**: MIT

## What it actually is

A NotebookLM-shaped app you can self-host: upload sources (PDFs, URLs, YouTube transcripts, audio, raw text), then chat with them, generate audio podcasts, run multi-step research, and produce structured notes. Stack appears to be TypeScript frontend + Python backend. The pitch is privacy + provider-choice: pick any LLM (OpenAI, Anthropic, Gemini, local via Ollama), run it on your machine or VPS, your sources never leave your control. Heavily documented (start-here / user guide / core concepts / installation) and i18n'd for 8 languages — clearly aimed at non-dev end users, not just hackers.

## What's reusable

- **The product shape itself.** This is the canonical reference for "what does a privacy-first NotebookLM look like" — even if you don't use the code, the feature set is the spec.
- **Multi-provider abstraction.** Switching between OpenAI / Anthropic / Gemini / Ollama in a single app is non-trivial — they've solved it.
- **Source ingestion pipeline.** PDF + URL + YouTube + audio → embeddings → chat. If you're building any "talk to your docs" app, this is a working reference.
- **Podcast generation** (NotebookLM's killer feature) — multi-voice TTS over a generated script. Wiring this end-to-end is fiddly; they have a working example.
- **Docker deploy** is documented and used in the wild — usable as the "self-hosting NotebookLM" reference for a vibe-coded internal version.
- **i18n done from day one** — useful pattern if you're shipping to a non-English audience.

## Project ideas (forward-looking)

- **Internal company knowledge notebook.** Self-host inside the firewall; ingest internal docs, Slack exports, Notion dumps. Why this repo: the privacy story is already the thesis, just point it at your data.
- **Vertical NotebookLM** — e.g., for lawyers (case law sources), VCs (deal docs), researchers (papers). Fork the UI, lock down the source types. Why this repo: shaving features is easier than building the whole notebook UX.
- **Podcast generator product.** Strip everything but the source-ingest + podcast-gen path. Sell as a "turn your docs into a daily briefing podcast." Why this repo: the multi-voice script gen is the hard part and already exists.
- **Local-first research assistant for your own writing.** Ingest your past blog posts / notes / drafts, chat with them while writing the next piece. Why this repo: works on a laptop, no cloud, your prose stays yours.
- **NotebookLM-quality assessment substrate.** Use it as the eval rig for "is my source-grounded chat better than NotebookLM" — feed both the same sources, compare outputs.

## What to skip

- Don't read the i18n directories unless you need that language; they multiply the apparent code size.
- The hosted "open-notebook.ai" site is the SaaS version — fine to demo, but the value here is self-hosting.

## Watch-outs

- **"100% local" is conditional on choosing local providers.** Default config is OpenAI/Anthropic; you have to explicitly wire Ollama.
- **Heavy app** — TypeScript frontend + Python backend + audio pipeline + embeddings store + Docker. Not a lightweight thing to embed; this is "host the whole app."
- **27k stars in ~20 months is fast, but app maturity != API stability.** Expect breaking changes; pin to a release tag.
- **Audio podcast quality depends on the TTS provider you wire up.** Default may not match NotebookLM-quality voices; budget for ElevenLabs or similar if you want parity.
- **AGPL-style usage expectations are NOT here (it's MIT)** — good for forking, but check Discord/community for any "please don't compete with us" social contract.
