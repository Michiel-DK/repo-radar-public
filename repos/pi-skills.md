# badlogic/pi-skills

> A small, well-curated set of skills for the pi-coding-agent — wraps Google Workspace, Brave Search, browser automation, transcription, YouTube transcripts, and VS Code.

- **URL**: https://github.com/badlogic/pi-skills
- **Tags**: `skill` `agent` `infra`
- **Maturity**: ~1.9k stars · active
- **License**: MIT

## What it actually is

A 9-skill collection from Mario Zechner (badlogic) built primarily for his own pi-coding-agent but compatible with Claude Code, Codex CLI, Amp, and Droid via symlink/clone installs. Skills are pragmatic, single-responsibility wrappers over CLIs the author also maintains (`@mariozechner/gccli`, `gdcli`, `gmcli`). Each skill is `SKILL.md` + a runtime `{baseDir}` placeholder that gets resolved at execution time. No fancy frameworks — just clean, working integrations to tools an engineer actually uses daily.

## What's reusable

- **`gmcli` / `gccli` / `gdcli` skill pattern** — Gmail, Google Calendar, Google Drive each as a small CLI wrapped by a skill. Reusable architecture: separate the CLI (Node package, tested, versioned) from the skill (markdown wrapper that teaches the agent when/how to use the CLI).
- **`brave-search` skill** — clean reference for "web search but not Google." Pairs Brave Search API with content extraction. Worth borrowing for any agent that needs cheap web search without Google's API surface.
- **`browser-tools` skill** — interactive browser automation via Chrome DevTools Protocol. Skill body teaches the agent the protocol; CLI does the work. Reusable for any "agent needs to click around in a real browser" use case.
- **`transcribe` skill** — Groq Whisper API wrapped in a skill. Cheapest viable transcription option in 2026 (Groq Whisper is ~$0.04/hour).
- **`youtube-transcript` skill** — fetches YouTube transcripts without spinning up the YouTube Data API. Reusable for any media-monitoring or research workflow.
- **`vscode` skill** — file diff/comparison via the `code` CLI. Trivial but useful pattern: skills that wrap **the tool the user is already running** rather than introducing new ones.
- **Multi-harness install instructions in README** — one-liner per harness (pi, Codex CLI, Amp, Droid, Claude Code). Reference template for how to ship a skill bundle to multiple harnesses without per-harness directories like ECC's approach.
- **`{baseDir}` placeholder pattern** — runtime-resolved helper paths inside skill bodies. Worth borrowing for any skill that ships scripts alongside instructions.

## Project ideas (forward-looking)

- **Personal AI ops assistant.** Combine `gmcli` + `gccli` + `gdcli` + `transcribe` into one agent that triages mail, schedules events, files attachments, transcribes voicemails. Why this repo: 4 of the 5 building blocks are already done; only orchestration is new.
- **"Research from a YouTube playlist" pipeline.** `youtube-transcript` extracts → LLM summarizes per video → cross-video synthesis → output to `gdcli`. Why this repo: skills compose cleanly; pi-skills is already a working DAG of these.
- **Customer-call intel agent.** `transcribe` ingests call recordings → LLM extracts action items + sentiment → `gmcli` sends a follow-up email + `gccli` schedules the next touch. Why this repo: pre-built Workspace + transcription wiring saves weeks.
- **`browser-tools` for niche web-app tests.** When Playwright is overkill but you need an agent to actually click around (e.g. testing an internal tool with weird auth), this is lighter weight. Why this repo: skill encodes the CDP protocol so the agent doesn't fumble.
- **A "minimum viable" skill bundle for solo developers.** Fork pi-skills, prune to the 3 skills you use, ship as `dev-essentials`. Why this repo: the curation work is already done; you're just opinionating further.

## What to skip

- The Brave Search API requires its own key — fine for personal use, watch quota for production.
- The `subagent` skill is mentioned in requirements but not in the table — likely WIP, don't depend on it.
- Pi-coding-agent ties some skill ergonomics to its harness; nothing fatal in Claude Code but expect minor friction.

## Watch-outs

- Skills depend on globally-installed npm packages (`@mariozechner/gccli`, etc.) — versioning is on you.
- Google CLIs require OAuth flows; first-run is interactive and won't work in CI without service-account substitution.
- Brave Search and Groq are both paid (free tier exists for both); budget accordingly.
- Browser-tools needs a real Chrome install — won't work in barebones containers.
- Repo is small (1.9k stars) — community support is the maintainer; no SLA, but the author is reachable.
- MIT-licensed code, but the underlying CLI packages are also MIT — verify before redistribution.
