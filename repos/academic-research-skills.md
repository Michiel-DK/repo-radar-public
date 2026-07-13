# Imbad0202/academic-research-skills

> Claude Code skills for the full academic-paper pipeline: research → write → review → revise → finalize, with integrity gates against AI failure modes.

- **URL**: https://github.com/Imbad0202/academic-research-skills
- **Tags**: `skill` `agent` `research`
- **Maturity**: ~26k stars · v3.10.0 · active
- **License**: CC BY-NC 4.0 (non-commercial)

## What it actually is

A 10-stage academic pipeline shipped as Claude Code skills (also has a Codex CLI sibling repo). Skills: Deep Research (13-agent team with Socratic / PRISMA / fact-check modes), Academic Paper (12-agent writing pipeline with style calibration, LaTeX hardening, revision coaching), Academic Paper Reviewer (7-agent multi-perspective peer review with 0-100 rubrics), Academic Pipeline (orchestrator). Hard gates at Stage 2.5 and 4.5 explicitly block known AI failure modes (citation hallucination, claim-not-supported, fabricated references, methodology fabrication). Built on top of published research on AI-research failure rates (Lu et al. *Nature* 2026, Zhao et al. arXiv 2026-05 — 146k hallucinated citations in 2025 alone).

## What's reusable

- **Pattern**: **mandatory integrity gates that cannot be skipped** — Stage 2.5 (pre-review integrity check) + Stage 4.5 (post-revision integrity check). Reusable for any high-stakes generation pipeline.
- **Pattern**: **claim-level locator anchors** (v3.7.3+) — every citation carries a structured anchor that points back to the source claim, enabling claim-level audit. Generalizes to any domain where sourcing matters.
- **`ARS_CLAIM_AUDIT=1` opt-in audit pass** — fetches each cited source, verifies the claim, classifies failures into 5 HIGH-WARN classes. Reusable as a "fact-check pass" pattern for any RAG output.
- **Calibration framework** — ships a 20-tuple gold set with FNR<0.15 + FPR<0.10 acceptance thresholds. Worth borrowing for any LLM evaluator skill.
- **Style Calibration skill** — learns user's voice from past work, then enforces it. Pattern reusable for any "match the company tone" application.
- **R&R Traceability Matrix (Schema 11)** — independent verification of revision claims. Generalizes to any "did you actually address the feedback?" loop.
- **Data Access Level metadata** (`data_access_level: raw | redacted | verified_only`) — pattern for ground-truth isolation, adapted from Anthropic's automated-w2s-researcher. Useful any time skills touch sensitive data.
- **Collaboration Depth Observer** — advisory-only agent that runs alongside the integrity gates but doesn't dilute them. Pattern: keep advisory + blocking checks structurally separate.
- **Benchmark Report JSON Schema** — enforces honest benchmark comparisons (apples-to-apples, no cherry-picking). Reusable schema for any evals output.

## Project ideas (forward-looking)

- **VC due-diligence pipeline with mandatory integrity gates.** Replace "academic paper" with "investment memo" — same shape: research → draft → integrity check → review → revise → integrity recheck → publish. Why this repo: integrity-gate architecture is generic; just need to swap rubric content.
- **Internal-research pipeline for a corporate strategy team.** Long-form internal reports with the same hallucination-resistance properties. Why this repo: claim-level anchoring + automated audit is gold for high-stakes business writing.
- **Legal-brief writer with citation verification.** Briefs hallucinate case law (literally — see the Mata v. Avianca case). This pipeline's `ARS_CLAIM_AUDIT` translates directly: fetch the cited case, verify the holding. Why this repo: existing audit infrastructure + 5-failure-mode taxonomy.
- **Grant-application pipeline.** Same multi-agent structure (PI + statistician + ethics reviewer + budget reviewer) with hard integrity gates before submission. Why this repo: academic context is the closest existing analog.
- **Open-source thesis-writing assistant for grad students.** Repackage with simpler UX, distribute via a university partnership. Why this repo: it IS that already — just needs a friendlier wrapper.

## What to skip

- The Chinese-localization machinery is excellent but irrelevant unless writing Chinese papers.
- Stage 6 (Process Summary with Collaboration Quality Evaluation) is advisory and a bit precious for non-academic use.
- The PRISMA systematic-review mode is highly domain-specific (medical/social science meta-analysis); skip unless that's the use case.

## Watch-outs

- **CC BY-NC 4.0 — non-commercial**. Cannot be used in a commercial product without permission. Major constraint vs MIT/Apache repos.
- Requires Pandoc + tectonic + Source Han Serif TC fonts for full LaTeX/PDF output; Markdown output works without them.
- Cost estimate: ~$4-6 for a 15k-word paper through the full pipeline — fine for academic use, may be too much for a SaaS unless model-routed.
- Skill body assumes the user is an academic researcher; vocabulary and tone won't fit naive corporate writers without rework.
- Heavy reliance on Semantic Scholar API for citation verification — that API is rate-limited and occasionally unreliable.
- Author actively iterating (v3.10 on a recent release); pin a version or expect churn.
