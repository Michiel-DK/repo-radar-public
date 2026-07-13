# google/agents-cli

> The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud.

- **URL**: https://github.com/google/agents-cli
- **Tags**: `agent` `skill` `infra`
- **Maturity**: 4,396 stars (445 today, 2026-07-01) · created 2026-04 · active (last push 2026-06-28)
- **License**: Apache-2.0
- **PyPI**: `google-agents-cli`

## What it actually is

Google's official CLI + skill pack for building agents on the Gemini Enterprise Agent Platform (ADK / Agent Development Kit). Install it and it teaches *your existing coding assistant* the create → evaluate → deploy loop for Google Cloud agents. The signal that matters: **a hyperscaler shipping the "skills that upgrade any coding agent" pattern as an official on-ramp** — the strongest validation yet that skill packs are becoming a real distribution channel.

## What's reusable

- pattern: **vendor skill-pack as distribution** — meeting developers inside whatever coding agent they already use, instead of a bespoke IDE. A distribution model worth copying for your own tooling.
- pattern: **create → evaluate → deploy** as the canonical agent lifecycle encoded as skills; a clean structure to mirror.
- Reference for **agent evaluation** — the "evaluate" step (ADK eval harness) is often the missing piece in homegrown agent stacks.

## Project ideas (forward-looking)

- **Skill-pack distribution**: package agent capabilities as an installable skill pack the way Google does here. Why this repo: proves the "skills into any host agent" distribution model at vendor scale.
- **Borrow the eval harness shape**: adopt its create→evaluate→deploy framing for your own agent builds. Why: evaluation is often the weak spot; this is a reference.

## What to skip

- Deployment targets Gemini Enterprise / Google Cloud — the *deploy* half is GCP-locked and irrelevant if you're not on GCP. Take the CLI/skills packaging pattern, not the cloud binding.

## Watch-outs

- Gemini/GCP-centric; assumes that stack for anything beyond authoring.
- Official Google repo — Apache-2.0 but tied to a commercial platform; watch for platform lock-in in the deploy path.
