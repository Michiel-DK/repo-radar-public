# QuantumNous/new-api

> Next-generation LLM gateway and AI asset-management system — cross-convert any LLM into OpenAI / Claude / Gemini-compatible formats behind one endpoint.

- **URL**: https://github.com/QuantumNous/new-api
- **Tags**: `llm-ops` `infra` `agent`
- **Maturity**: 38,072 stars · 239 today (newcomer 2026-06-10) · created 2023-11-10 · active (last push 2026-06-10)
- **License**: AGPL-3.0

## What it actually is

A self-hostable **LLM gateway**: put many model providers behind one endpoint and expose them in OpenAI-, Claude-, or Gemini-compatible formats, with centralized key/quota/usage management ("AI asset management"). Mature for its category (created 2023, 38k stars, 8.6k forks). Go. The "one endpoint, many providers, format-translated" pattern — the infra layer under multi-model apps.

## What's reusable

- **Format cross-conversion** — call any provider through an OpenAI/Claude/Gemini-shaped API so app code stays provider-agnostic. The boring-but-essential layer under cost-aware routing and the model-gateway theme the radar keeps surfacing (pair with `Wei-Shaw/sub2api`).
- **Centralized key + quota + usage management** — reusable if you run multiple agents/tenants and need per-tenant rate limits and spend tracking (directly relevant to any per-tenant LLM-cost concern in vertical SaaS).
- **Self-hostable gateway** — keeps keys and traffic in your infra rather than a SaaS middleman.

## Project ideas (forward-looking)

- **Per-tenant LLM cost control for vertical SaaS** — front per-tenant vertical agents with new-api to meter and cap each tenant's model spend. Why this repo: quota + usage tracking is already built.
- **Provider-failover layer** — route to a fallback provider on outage/ratelimit without app changes. Why this repo: the format-translation + routing is the hard part, done.
- **Single gateway for repo-radar's own agents** — centralize the keys used by the digest writer + scrapers behind one metered endpoint. Why this repo: simpler ops, one place to watch spend.

## What to skip

- Overkill for a single-provider, single-app setup — only earns its keep with multiple providers/tenants or real spend-management needs.

## Watch-outs

- **AGPL-3.0** — copyleft. Fine for self-host/internal use, but network-use triggers source-disclosure obligations; check before bundling into a commercial product.
- Operationally heavy (a service to run, secure, and update) vs. a library.
- Repo history spans owners (`Calcium-Ion`/`QuantumNous`) — confirm the canonical upstream before depending on it.
