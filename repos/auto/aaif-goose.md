# aaif-goose/goose

> "Your native open source AI agent — desktop app, CLI, and API — for code, workflows, and everything in between." Just moved from Block to the Linux Foundation's Agentic AI Foundation (AAIF).

- **URL**: https://github.com/aaif-goose/goose
- **Tags**: `agent` `mcp` `infra` `frontend`
- **Maturity**: 48,043 stars · #7 GitHub Trending 2026-06-08 · created 2024-08-23 · very active (last push 2026-06-08)
- **License**: Apache 2.0

## What it actually is

A general-purpose desktop / CLI / API AI agent written in Rust. Three surfaces share one core: native macOS/Linux/Windows desktop app, full-featured CLI for terminal workflows, and an embeddable API. Supports 15+ LLM providers (Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, …) including using your existing Claude/ChatGPT/Gemini *subscriptions* via ACP. Connects to 70+ extensions via MCP. Recently moved from `block/goose` (originally Block, Inc.) to the Linux Foundation's Agentic AI Foundation — meaningful governance signal, this is now a foundation project rather than a vendor project.

## What's reusable

- **The desktop-app + CLI + API trifecta on one Rust core.** This is the architecture you'd want for any "agent that the user can drive from chat, terminal, or programmatically." Hard to build, fully working here.
- **ACP (Agent Client Protocol) integration** — use your existing Claude/ChatGPT/Gemini *subscriptions* instead of API keys. Reference for any agent that wants to be friendly to the "I'm already paying for Pro" user.
- **15+ provider abstraction layer.** If you need to write a provider adapter, the existing 15 are the reference set.
- **70+ MCP extension catalog wired through one host.** Living reference for what's actually useful as MCP tooling.
- **Foundation-governance project structure.** If your project is heading toward neutrality (multi-vendor, multi-org), this is a current example of the move from "company OSS" to "foundation OSS."

## Project ideas (forward-looking)

- **Skill / extension for goose targeted at your workflow.** Same effort as a Claude skill, larger install base (Goose desktop ships everywhere). Why this repo: MCP-compatible, so any MCP server you write works in both Claude and goose.
- **Goose as the "Cursor for non-code work."** Wire your team's daily research / writing / data tasks via MCP extensions; replace 5 SaaS subscriptions. Why this repo: the desktop UX is already there.
- **Embedded agent inside your own product.** Use the goose API to ship an AI assistant in your app without writing the agent loop. Why this repo: Rust, embeddable, Apache 2.0.
- **Provider-neutral evals.** Run the same prompt across 15 providers via goose's adapter layer — easy A/B for "which model is best at task X for cost Y."
- **ACP-based product where users bring subscriptions.** No "configure your API key" friction. Why this repo: ACP integration is non-trivial and already done.

## What to skip

- The migration disclaimer at the top of the README will be stale in a few weeks — don't take "still being updated" as a permanent state.
- Don't bother with the slim "code suggestions" framing in older docs — goose is a general agent now.

## Watch-outs

- **Governance just moved.** "Aaif-goose" namespace is new; expect references to `block/goose` for a while and some link rot during transition.
- **Linux Foundation projects can stall** if no company funds them post-donation. Watch funding/maintainer signals over the next 6 months.
- **15-provider matrix is a lot of surface to keep working.** Some providers will lag releases; pin to a known-good provider for production use.
- **Desktop + CLI + API in one repo = big repo.** Build times are real if you fork.
- **Direct competitor to Claude Code, Cursor, etc.** As of today the Anthropic ecosystem feels stickier; goose's edge is the provider neutrality + LF governance.
