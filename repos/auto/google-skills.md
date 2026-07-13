# google/skills

> Agent Skills for Google products and technologies — Gemini API, Cloud Run, BigQuery, AlloyDB, GKE, Firebase, plus Well-Architected Framework skills.

- **URL**: https://github.com/google/skills
- **Tags**: `skill` `agent` `infra`
- **Maturity**: 12,716 stars · ranked #14 GitHub Trending 2026-06-09 (461 stars today) · created 2026-03-31 · active (last push 2026-06-05)
- **License**: Apache 2.0

## What it actually is

Google's official Agent Skills repo, following the same spec as `anthropics/skills` and `openai/plugins`. Two clusters: (1) **Skills for Google Cloud products** — AlloyDB Basics, BigQuery Basics, Cloud Run Basics, Cloud SQL Basics, Firebase Basics, GKE Basics, plus "Recipe" skills for onboarding/auth/network-observability and the Google Cloud Well-Architected Framework broken down by Security / Reliability / Cost / Operational Excellence. (2) **Skills for Google's agent platform itself** — Gemini API on Agent Platform, Gemini Interactions API, Managed Agents API, Skill Registry API. Install via `npx skills add google/skills` (same install path as Anthropic / others — cross-vendor).

## What's reusable

- **The fact that this exists**. Google adopting the same `agentskills.io` spec as Anthropic is the most important signal of the past month: the Skills format is becoming a multi-vendor standard, not a single-vendor format. Any skill you write today is portable across Anthropic + Google + OpenAI hosts.
- **WAF (Well-Architected Framework) as skills** — Security / Reliability / Cost / OpExc as four separate skills. Pattern is reusable: take any opinionated framework / playbook (your team's playbook, OWASP, NIST, a brand guideline) and ship it as a skill bundle so agents follow it by default.
- **"Recipe" skills** (`google-cloud-recipe-onboarding`, `google-cloud-recipe-auth`, `google-cloud-recipe-networking-observability`) — pattern for "common multi-step task as a single skill." Good shape if you have repeated playbook-style operations.
- **Skill Registry API skill** — a meta-skill for discovering/managing other skills. Useful reference if you're building any agent platform.
- **Per-cloud-product skill structure** under `./skills/cloud/<product>-basics` — clean naming, scannable. Use as the template for "one skill per product/feature" libraries.

## Project ideas (forward-looking)

- **Cross-vendor skill verification harness.** Now that Google, Anthropic, and OpenAI all use the same format, you can build a CI that runs the same skill against three hosts and checks the result. Why this repo: completes the third corner of the triangle.
- **GCP-flavored vertical assistant.** Combine `google/skills` (Cloud) with a vertical layer (e.g., compliance, data, ML ops). Why this repo: the bottom layer is already done.
- **"Best of three" skill picker.** Aggregate the official skills from Anthropic + Google + OpenAI for any task, let the agent pick whichever ranks best. Why this repo: provides the Google contribution.
- **Internal Cloud onboarding skill, modeled on `google-cloud-recipe-onboarding`.** For any team that wants "agent walks new hires through our cloud setup," fork this skill, swap GCP for your stack. Why this repo: the structure is a working reference.
- **Cross-cloud Well-Architected eval.** Same WAF skills repointed at AWS / Azure / Cloudflare. Why this repo: the four-pillar split (Security / Reliability / Cost / OpExc) is industry-standard, so the structure copies cleanly.

## What to skip

- Don't install all the skills if you only use 2-3 of GCP — `npx skills add google/skills` lets you pick.
- The Gemini-specific skills are only useful if you're targeting Gemini's agent platform — skip for Claude/OpenAI-only deployments.
- "Under active development" disclaimer is real; expect skill APIs to churn over the next quarter.

## Watch-outs

- **Google-product lock-in by design** — all these skills assume you're using GCP. They're not provider-neutral the way Anthropic's general skills are.
- **Apache 2.0 is permissive**, but the skills themselves often imply commercial Google Cloud usage (you'll pay GCP bills to actually run what they enable).
- **Created 2026-03-31** — very young. Names and structure may rename.
- **No `claude-api` or `mcp-builder` equivalents here yet** — this is a *product* skill catalog, not a *platform* skill catalog like Anthropic's. Different shape, different use.
- **Watch for divergence in the spec.** Each vendor is the spec authority for their own repo; if Google and Anthropic interpret a spec edge case differently, your "portable" skill stops being portable.
