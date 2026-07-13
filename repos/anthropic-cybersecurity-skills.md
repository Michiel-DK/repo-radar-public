# mukul975/Anthropic-Cybersecurity-Skills

> 754 structured cybersecurity skills for AI agents, each mapped to 5 frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF) across 26 security domains.

- **URL**: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- **Tags**: `skill` `agent` `research`
- **Maturity**: ~13k stars · active · community project (NOT affiliated with Anthropic despite the name)
- **License**: Apache 2.0

## What it actually is

The largest open-source library of structured agentic skills targeting one vertical (cybersecurity). Each skill is a directory with `SKILL.md` (YAML frontmatter — keyword-rich description + framework mappings + tags — and Markdown body — `When to Use` / `Prerequisites` / `Workflow` / `Verification`), plus `references/`, `scripts/`, `assets/`. Conforms to the [agentskills.io](https://agentskills.io) standard. Domains: cloud sec, threat hunting, threat intel, web app sec, network sec, malware analysis, DFIR, SOC ops, IAM, container sec, OT/ICS, API sec, vuln mgmt, IR, red team, pentest, endpoint, DevSecOps, phishing, crypto, zero trust, mobile, ransomware, compliance, deception. Every skill costs ~30 tokens to discover, 500-2000 to fully load — designed for progressive disclosure at 754x scale.

## What's reusable

- **Pattern**: **frontmatter as discovery layer, body as execution layer** — agents scan all 754 frontmatters in one pass (~22k tokens), then load only matching skills. Cleanest reference for "thousands of skills without blowing context."
- **The 4-section body structure (`When to Use` / `Prerequisites` / `Workflow` / `Verification`)** — generalizes to any domain. Worth copying as a skill template.
- **Framework-mapping as multi-tag classification** — every skill carries a `mitre_attack`, `nist_csf`, `d3fend_techniques`, etc. list. Pattern reusable for any domain with standard frameworks (legal: CFR refs; finance: GAAP/IFRS; medical: ICD-10).
- **Skill dir layout** (`SKILL.md` + `references/standards.md` + `references/workflows.md` + `scripts/` + `assets/`) — separates the "always loaded" body from "loaded only when needed" deep refs. Excellent pattern for any complex skill that has both procedural and reference content.
- **Cross-platform compatibility statement** — works with Claude Code, Copilot, Codex CLI, Cursor, Gemini CLI, 20+ harnesses. Pattern: don't hardcode harness assumptions in skill content.
- **MITRE ATT&CK Navigator layer export** — reusable trick for any domain with a public taxonomy: ship a navigator/visualizer artifact alongside the skills.

## Project ideas (forward-looking)

- **Vertical skill library for VC/private-equity workflows.** Apply the same architecture (frontmatter + 4-section body + framework mappings) to the VC research workflow (due diligence, market mapping, term sheets, fund reporting). Why this repo: blueprint for organizing 100s of vertical skills without the discovery cost.
- **Legal-ops skill library mapped to CFR/UCC.** Skills like "review-a-master-services-agreement", "audit-data-processing-addendum-for-gdpr", each tagged with the regulations it addresses. Why this repo: framework-mapping is the load-bearing pattern that makes such a library queryable.
- **AI agent for SOC tier-1 triage.** Drop this skill library into a SOC agent, give it read-access to SIEM, let it triage alerts using the playbooks. Why this repo: the playbooks ARE the skills; no extra prompt engineering required.
- **Compliance-evidence generator.** Pick a control framework (SOC 2, ISO 27001), get the skills mapped to its categories, run each, produce audit evidence. Why this repo: NIST CSF mappings already exist; SOC 2 mapping would be a one-time add.
- **"Cybersecurity intern in a box" educational product.** Skills double as a structured curriculum (when to use which tool, in what order). Sell to bootcamps. Why this repo: 754 procedures already follow practitioner playbooks.

## What to skip

- The Casky.ai playground + GARS-2026 survey CTAs are marketing for the maintainer's hosted product; skip unless you want their hosted version.
- The "Hermes Agent" compatibility badge points at a specific third-party harness — irrelevant if you're not using it.
- Domain coverage is uneven — 60 cloud-security skills vs 2 deception-tech skills. Don't assume completeness in the long tail.

## Watch-outs

- **NOT an Anthropic project** despite the name. Single-maintainer community project. Apache-2.0, so usable, but no Anthropic SLA.
- Skills are quality-variable — some are deep playbooks, some are sparse stubs. Spot-check before relying.
- MITRE framework versions matter — this maps to ATT&CK v19.1. Update path for future ATT&CK versions is a manual relabeling exercise.
- The 30-tokens-per-frontmatter math assumes you actually load all 754 — in practice most harnesses don't, so test discovery latency before relying on the architecture claim.
- Some skills include offensive techniques (red team, pentest). Deploy with appropriate authorization scoping or you're shipping a footgun.
