# usestrix/strix

> The open-source AI pentesting tool — autonomous AI hackers that find and fix your app's vulnerabilities.

- **URL**: https://github.com/usestrix/strix
- **Tags**: `agent` `security` `llm-ops`
- **Maturity**: 28,406 stars (515 today, 2026-07-01) · created 2025-08 · active (last push 2026-06-30)
- **License**: Apache-2.0

## What it actually is

An autonomous offensive-security agent: point it at an app and it runs a full pentest loop — recon, exploit attempts, and remediation suggestions — rather than a single static scan. Positioned for bug-bounty / red-teaming / CTF workflows. Python; heavily tagged (ai-pentesting, red-teaming, CTF-tools, LLM-security). This is the "security expertise as a *running agent*" step beyond last snapshot's *packaged* cyber skills (Anthropic-Cybersecurity-Skills).

## What's reusable

- pattern: **autonomous find→exploit→fix loop** — a concrete template for domain agents that don't just report but act and verify. Relevant to any "agent that does real work safely" build.
- pattern: **tool-gated offensive actions** — how it bounds what the agent may do is worth studying for any agent given dangerous capabilities.
- The MITRE/framework-tagged skill taxonomy (shared lineage with the cyber-skills thread) as a way to structure domain knowledge.

## Project ideas (forward-looking)

- **CI security gate**: run strix as an adversarial check in your CI/deploy pipelines before release. Why this repo: the autonomous loop is already built; you supply the target + scope.
- **Reference for "safe autonomous action"**: mine its guardrails when designing any agent that mutates real systems. Why: pentesting forces the hardest version of that problem.

## What to skip

- Only relevant if you have authorized targets — this is dual-use; don't point it at anything you don't own or aren't engaged to test.

## Watch-outs

- **Authorization is mandatory** — offensive tooling; running it against third-party systems without permission is illegal.
- Model-dependent (LLM-driven exploitation) — quality and cost scale with the backing model.
