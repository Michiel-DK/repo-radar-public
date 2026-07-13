# diegosouzapw/OmniRoute

> The free AI gateway — one endpoint, 231+ providers (50+ free); connect Claude Code, Codex, Cursor, Cline & Copilot to free Claude/GPT/Gemini with stacked token compression and auto-fallback.

- **URL**: https://github.com/diegosouzapw/OmniRoute
- **Tags**: `llm-ops` `infra`
- **Maturity**: 8,874 stars (387 today — just off top-15, 2026-07-01) · created 2026-02 · active (last push 2026-07-01)
- **License**: MIT

## What it actually is

A self-hostable AI gateway that fronts 231+ providers (50+ with free tiers) behind one OpenAI/Anthropic-compatible endpoint. It does smart auto-fallback across providers, aggregates free tiers (claims ~1.6B free tokens/month), and adds stacked "RTK + Caveman" prompt compression claiming 15–95% token savings. Supports MCP/A2A and multimodal, ships Desktop/PWA. Substrate is TypeScript. This is the most built-out expression yet of the cost/routing pattern the radar keeps surfacing — 06-23's freellmapi, matured.

## What's reusable

- pattern: **provider-abstraction + auto-fallback** — one endpoint, many backends, degrade gracefully. This is the reference implementation of the `cost-aware-llm-pipeline` skill's routing half.
- pattern: **prompt/token compression as a gateway concern** — compress before the model, transparently. Worth studying (verify the 15–95% claim on real prompts before trusting).
- The provider registry itself — a maintained map of 231+ providers + free tiers is useful data even if you don't adopt the gateway.

## Project ideas (forward-looking)

- **Cost floor for LLM pipelines**: route non-critical LLM calls (auto-writeups, enrichment) through a free-tier-first gateway. Why this repo: the free-tier aggregation + fallback is already built.
- **Compression A/B harness**: measure real token savings of its compression on your actual prompts before committing. Why: pairs with the `bounded-experiment-loop` skill.

## What to skip

- The eye-popping "free tokens/month" and "15–95% savings" numbers are marketing — treat as hypotheses to test, not facts.

## Watch-outs

- **Routing to free tiers means routing your prompts through many third parties** — data-handling / privacy risk; don't send sensitive or private data through it (rules it out for any local-only / privacy-sensitive pipeline).
- Compression can degrade output quality — validate per task.
- Young project (created 2026-02); provider list churns.
