# Leonxlnx/taste-skill

> Anti-slop Agent Skills for premium frontends — stops the AI from generating boring, generic UIs.

- **URL**: https://github.com/Leonxlnx/taste-skill
- **Tags**: `skill` `frontend`
- **Maturity**: ~31k stars · active (v2 experimental rewrite, frequent releases)
- **License**: MIT

> **Discrepancy note**: the task brief mapped `taste-skill` to a subdir of `anthropics/skills`, but no such subdir exists there. The canonical taste-skill is `Leonxlnx/taste-skill` — used here.

## What it actually is

A bundle of portable Agent Skills (works with Claude Code, Codex, Cursor, and any `npx skills add` compatible harness) that upgrades AI-built frontends — stronger layout, typography, motion, spacing — instead of the default boilerplate React+Tailwind aesthetic every coding agent produces. Each skill is one `SKILL.md` file with opinionated design rules (em-dash bans, GSAP code skeletons, design-system maps, brief-inference protocols). Also ships **image-generation skills** for design reference boards (web, mobile, brand kits) that pair with ChatGPT Images / Codex image mode.

## What's reusable

- **`taste-skill` (v2)** — the default design skill. Reads the brief, infers the design language, exposes three dials (`DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY` each 1-10). Reusable pattern: **dials at the top of a skill file** to let users tune without rewriting the skill.
- **`redesign-skill`** — different shape: audit existing UI first, then surgically fix. Reusable pattern for any "improve existing thing" skill (not just UI — same shape works for code reviews, doc revisions).
- **`output-skill`** — prevents the agent from shipping half-finished work / placeholder comments. Generally useful guardrail prompt.
- **Image-gen skills (`imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`)** — image-only outputs to be passed back to a coding agent. Pattern: **separate the "what should this look like" step from the "how to build it" step**.
- **Pre-flight checklists in skill bodies** — pattern that catches issues before the agent commits to a direction.
- **`stitch-skill`** — exports a `DESIGN.md` from the skill output so other agents can read the design decisions back later.

## Project ideas (forward-looking)

- **Auto-redesign service for indie SaaS sites.** User points the agent at their live URL, `redesign-skill` audits it, agent ships a PR with the new design. Why this repo: redesign skill already encodes "audit then fix" without the agent immediately rewriting everything.
- **Brand-consistent landing-page generator for an agency.** Drop in `brandkit` output, then `taste-skill` enforces the brand variables across pages. Why this repo: the dials + DESIGN.md export turns "design taste" into a controllable parameter.
- **A/B-test design variants in one prompt.** Generate three sites at `DESIGN_VARIANCE = 3 / 6 / 9`, ship all three, measure which converts. Why this repo: dial-based control is exactly the right abstraction for variant generation.
- **"Make my AI app not look like an AI app" plugin.** Anyone shipping a v0/Bolt-generated app can layer this skill on top to remove the tell-tale generic aesthetic. Why this repo: that's literally the stated purpose, and the skill is already battle-tested with 31k stars.
- **Internal style-enforcer for a design system.** Fork taste-skill, swap the design rules for the company's tokens + components, ship as a private skill. Why this repo: structure (dials + brief inference + design-system map) generalizes; rules can be replaced.

## What to skip

- Several visual-direction variants (`brutalist-skill`, `soft-skill`, `minimalist-skill`) are aesthetic templates — useful as references but skip if you have your own design language.
- The image-generation skills require ChatGPT Images or similar; not free, not portable to local models.
- v1 of `taste-skill` is preserved as `taste-skill-v1` for backward compat — don't start there; v2 is the active surface.

## Watch-outs

- Output quality depends heavily on the coding agent's frontend skills underneath; this skill biases the direction but can't fix a weak coder model.
- GSAP code skeletons assume you're OK with GSAP as a runtime dep — drop-in fix is to rewrite skill rules around your motion library of choice (Framer Motion, Motion One).
- MIT-licensed but the maintainer explicitly disclaims any associated token/crypto project — community has some scam-attempt history.
- The "anti-slop" framing is marketing — the actual skill is a high-quality prompt; manage expectations vs the hype.
