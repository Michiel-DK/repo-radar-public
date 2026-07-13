# NVIDIA/SkillSpector

> Security scanner for AI agent skills — detect vulnerabilities, malicious patterns, and security risks before installing.

- **URL**: https://github.com/NVIDIA/SkillSpector
- **Tags**: `skill` `agent` `infra` `research`
- **Maturity**: 1,897 stars · 280 today (newcomer 2026-06-10) · created 2026-03-21 · active (last push 2026-06-10)
- **License**: Apache-2.0

## What it actually is

A static security scanner for agent **Skills** — the skill bundles used by Claude Code, Codex CLI, Gemini CLI, etc., which execute with implicit trust and minimal vetting. SkillSpector inspects a skill before you install it and flags vulnerabilities and malicious patterns. The README cites research that **26.1% of skills contain vulnerabilities** and **5.2% show malicious-leaning behavior** — i.e. the Skills ecosystem now has a real supply-chain attack surface. Python.

## What's reusable

- **The defensive layer of the Skills ecosystem.** As the radar has tracked, Skills went multi-vendor (Anthropic → Google → OpenAI) and multi-author; SkillSpector is the inevitable next layer — *vetting before install*. Pair mentally with `anthropics/claude-code-security-review`.
- **Pre-install scanning as a gate** — pattern for any agent that installs third-party extensions: scan → score → block on threshold. Reusable for an internal skill registry.
- **The vulnerability/malicious-rate stats** — concrete numbers to cite when arguing that skill supply-chain security matters.
- Detection rules for skill-specific risks (exfiltration patterns, dangerous shell, prompt-injection vectors) — reference catalog if you build your own scanner.

## Project ideas (forward-looking)

- **Skill-registry gate** — wrap `npx skills add` so anything from `repos/auto/` candidates gets SkillSpector-scanned before it touches your machine. Why this repo: the scanner already exists; you just wire the gate.
- **CI for your own skills** — run SkillSpector on every skill you author/publish so you don't ship a vulnerable one. Why this repo: turnkey static analysis.
- **"Skill trust score" in repo-radar** — when a trending repo is a skill bundle, auto-run SkillSpector and record the score in its writeup. Why this repo: makes the radar security-aware.

## What to skip

- Static analysis only — it won't catch runtime/dynamic exfiltration. Treat a clean scan as necessary, not sufficient.

## Watch-outs

- **NVIDIA-backed but young** (created 2026-03) — detection rules will evolve; false-positive/negative rates unknown.
- Apache-2.0, fine for commercial use.
- The cited 26.1%/5.2% figures are from research the repo points to — verify the methodology before quoting them as fact.
