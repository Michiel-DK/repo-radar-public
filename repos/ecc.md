# affaan-m/ECC

> The harness-native operator system for agentic work — 249 skills, 63 agents, hooks, rules, MCP configs, and a Rust control-plane prototype, all evolved from 10+ months of daily multi-harness use.

- **URL**: https://github.com/affaan-m/ECC
- **Tags**: `agent` `skill` `mcp` `infra` `llm-ops`
- **Maturity**: ~200k stars (per repo description) · last commit 2026-06 · active (weekly releases)
- **License**: MIT

## What it actually is

A massive, opinionated cross-harness skill+agent bundle. Ships across Claude Code, Cursor, OpenCode, Codex (app + CLI), Gemini, Zed, Copilot, and ~7 more harnesses from a single repo. Each harness gets its own dotfile dir (`.claude/`, `.codex/`, `.cursor/`, etc.). Includes a continuous-learning system that extracts patterns from sessions into reusable skills ("instincts"), hooks for memory persistence, runtime gating (`ECC_HOOK_PROFILE=minimal|standard|strict`), AgentShield security scanning, harness-audit scoring, parallel multi-agent orchestration (PM2-managed), and an experimental Rust control plane (`ecc2/`) for sessions/status/daemon. Self-described as the "harness performance optimization system."

## What's reusable

- **Pattern**: one repo → N harness installs via per-harness dotfile dirs. Cleanest answer I've seen to "ship the same agentic config to every coding tool."
- **`skills/cost-aware-llm-pipeline`** — model routing by task complexity + budget tracking + retry logic + caching. Already adopted in my CLAUDE.md as a referenced skill.
- **`skills/continuous-learning-v2`** — pattern for distilling session transcripts into reusable skills automatically. Generalizes well beyond coding.
- **`skills/skill-stocktake`** — meta-skill for auditing your own skill collection.
- **Selective install architecture** (`install-plan.js` / `install-apply.js` + manifest + SQLite state store) — reference for how to ship a large config bundle without forcing all-or-nothing.
- **`hooks/`**: session-start, stop-phase, runtime-gating — high-quality examples of every hook surface area Claude Code exposes.
- **`/harness-audit` + `/quality-gate` + `/model-route` commands** — patterns for self-improving agent setups.
- **Multi-agent orchestration via PM2** (`/multi-plan`, `/multi-execute`, `/multi-backend`, `/multi-frontend`) — reference for "run N agents in parallel and coordinate via PM2 process supervision."
- **`ecc status --markdown`** — turns local state-store into a handoff document. Useful pattern for end-of-session summaries.

## Project ideas (forward-looking)

- **Personal "harness pack" for a tech stack.** Fork ECC, strip everything outside the 10 skills + 5 commands you actually use, keep the multi-harness install machinery. Solves the "I want the same setup in Claude Code, Cursor, and Codex CLI without copy-pasting" problem. Why this repo: install-plan / install-apply pair handles selective install already; you just curate.
- **Session-replay-to-skill pipeline as a SaaS.** Watch a user's Claude Code sessions, extract recurring patterns, propose new skills, let them accept/reject. Sell to engineering teams. Why this repo: continuous-learning-v2 is the working core algorithm.
- **Internal harness-audit / quality-gate dashboards for ops teams.** Run the audit command nightly across all engineers, surface skill-adoption gaps. Why this repo: audit scoring is deterministic + already implemented.
- **Cross-harness skill marketplace.** A registry where skills come with `compatibility` manifests (claude/codex/cursor/opencode) and the installer figures out routing. Why this repo: their install-plan format is a fine starting protocol.
- **Skill-conflict linter.** When two skills both want to trigger on the same prompt, surface it before runtime. Why this repo: 249 skills in one repo means they had to solve this — read how.

## What to skip

- The whole `ecc2/` Rust control-plane is alpha and not yet a general release. Don't depend on its CLI for anything serious.
- The "Itô prediction-market skill pack" and several operator-product skills (`ecc-tools-cost-audit`, `customer-billing-ops`) are commercial-tier and tied to their hosted product. Skip unless you're literally running their hosted service.
- The hook system is powerful but easy to misconfigure — start with `ECC_HOOK_PROFILE=minimal` and add only what you can debug.
- The dashboard GUI (Tkinter) is a 2026 add-on; nice idea, but Tkinter limits portability.

## Watch-outs

- The repo's surface is **huge** — 63 agents, 249 skills, 79 legacy command shims. Just cloning and installing the full profile will saturate any harness's discovery cost.
- Their own README warns: "Do not stack install methods" — easy to end up with duplicated skills if you mix plugin install + manual install.
- MIT-licensed OSS, but the project's commercial tier (ECC Pro, GitHub App) shapes which features get polished first. Some skills exist primarily to drive the upsell.
- The "instinct" learning system writes to `.claude/` automatically — review hooks before enabling on sensitive repos.
- The repo description claims 200k+ stars; treat that as a marketing number and trust your own engineering judgment per skill.
