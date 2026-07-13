# obra/superpowers

> An agentic skills framework & software-development methodology that works — composable skills + initial instructions that make sure your agent actually uses them.

- **URL**: https://github.com/obra/superpowers
- **Tags**: `skill` `agent` `llm-ops`
- **Maturity**: 243,302 stars (890 today — persister 5d, 2026-07-01) · 21.5k forks · created 2025-10 · active (last push 2026-07-01)
- **License**: MIT

## What it actually is

A complete SDLC methodology *for coding agents*, built on a set of composable skills plus bootstrap instructions that make the agent reach for the right skill at the right moment (brainstorming → planning → subagent-driven development). The differentiator vs. a plain skills bundle: it ships **host adapters for 10+ agents** (Claude Code, Antigravity, Codex App/CLI, Cursor, Factory Droid, Copilot CLI, Kimi Code, OpenCode, Pi), so the same skill set is portable across harnesses. Substrate is shell + markdown skills.

## What's reusable

- **Cross-harness skill packaging** — the install adapters per host agent are the interesting bit: one skill set, many agent runtimes. Directly relevant to any multi-tenancy / cross-harness packaging problem.
- pattern: **"instructions that guarantee skill invocation"** — the framework's core trick is not the skills but the bootstrap prompt that makes the agent *use* them consistently. Study this if your skills get ignored.
- pattern: **subagent-driven development** as a named methodology — decompose → subagents → integrate, encoded as skills rather than prose.

## Project ideas (forward-looking)

- **Cross-harness skill exporter**: take an existing skill set and generate the per-host adapters superpowers ships. Why this repo: it's already solved the "install into N agents" matrix.
- **Methodology-as-skills for a pipeline**: encode a multi-step digest flow (fetch → compute → interpret → writeups) as a superpowers-style skill chain with enforced invocation. Why: the bootstrap-instruction pattern fixes "agent forgot the process."

## What to skip

- The methodology is opinionated (brainstorm-heavy); if you already have a tight process, take the adapters + invocation trick, not the whole SDLC.

## Watch-outs

- Shell-based install; audit the bootstrap scripts before running against a real project.
- Fast-moving (daily pushes) — pin a commit if you depend on it.
