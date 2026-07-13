# ogulcancelik/herdr

> Agent multiplexer that lives in your terminal — run all your coding agents in one place, see who's blocked, working, or done at a glance.

- **URL**: https://github.com/ogulcancelik/herdr
- **Tags**: `agent` `infra` `frontend`
- **Maturity**: 9,180 stars (486 today — persister 7d, 2026-07-01) · created 2026-03 · active (last push 2026-06-30)
- **License**: NOASSERTION (check before use)

## What it actually is

A Rust terminal multiplexer purpose-built for running fleets of coding agents (Claude Code, Codex, etc.) side by side. Each agent gets a *real* terminal (full-screen TUIs render correctly), you split/drag panes into workspaces and tabs, and each pane surfaces a status — blocked / working / done — so you can supervise many agents at once. Runs wherever you can ssh. It's "tmux for agents," and it exposes a socket API for programmatic control.

## What's reusable

- pattern: **fleet status model (blocked/working/done)** — a clean abstraction for supervising N agents; directly relevant to any multi-agent dashboard.
- `socket-api` — programmatic pane/agent control; useful if you want to script an agent fleet rather than babysit it.
- pattern: **real-terminal-per-agent** — avoids the "app's imitation of a terminal" problem when agents run TUIs.

## Project ideas (forward-looking)

- **Supervisor UI for repo-radar agent runs**: use herdr (or its status model) to watch parallel digest-writer / writeup-drafter agents. Why this repo: the blocked/working/done supervision is already solved.
- **Scripted agent orchestration via the socket API**: drive a fixed workflow across panes programmatically. Why: socket API turns the multiplexer into an automatable substrate.

## What to skip

- If you only ever run one agent at a time, this is overkill — its value is fleet supervision.

## Watch-outs

- **License is NOASSERTION** — resolve licensing before depending on it commercially.
- Rust binary that manages terminals/ssh sessions — audit before granting it access to real servers.
