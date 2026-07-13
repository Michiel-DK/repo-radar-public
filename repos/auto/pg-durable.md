# microsoft/pg_durable

> "PostgreSQL in-database durable execution." Long-running, fault-tolerant SQL functions: define a workflow in SQL, let pg_durable checkpoint each step, and resume across crashes/restarts/failed steps — no extra worker/queue/cron infra.

- **URL**: https://github.com/microsoft/pg_durable
- **Tags**: `infra` `data` `llm-ops`
- **Maturity**: 1,721 stars · 339 today on trending 2026-06-09 · created 2026-02-13 · active (last push 2026-06-08)
- **License**: PostgreSQL License (custom, very permissive — like BSD)

## What it actually is

A Postgres extension (written in Rust via pgrx, judging by language and style) that brings Temporal/DBOS/Restate-style durable execution *inside* Postgres. You define a multi-step workflow in SQL functions; pg_durable checkpoints each step's output in the database; if the step / worker / server crashes, it resumes from the last checkpoint when it comes back. No external workflow engine, no message queue, no cron-and-status-tables scaffolding. Targets backend/data engineers who already keep state in Postgres and don't want to add Temporal/Airflow/Step Functions to their stack just to make a background job reliable. Microsoft also pitches it as the engine inside their new Azure HorizonDB service.

## What's reusable

- **The pattern itself: durable execution inside the database.** If you're already on Postgres, every external workflow engine is a step backward in operational simplicity. pg_durable shows what the in-DB version looks like.
- **The SQL-as-workflow-DSL choice.** Workflow steps are SQL functions; the orchestrator runs in the DB. Means you can debug a stuck workflow with `SELECT`s — no new UI to learn.
- **Checkpoint table design.** Read how they store step outputs and resume cursors; this is the kind of thing you'd otherwise hand-roll badly (see: every team that has "we built a poor man's workflow with a Postgres `status` column").
- **AI-pipeline framing.** Topics include `ai-pipelines` and `ai-workflows` — they're explicitly targeting "agent step graphs persisted to a database." If you're building an agent that needs to survive a process restart, this is the storage layer.
- **PG 17 + 18 support.** Production-ready Postgres versions, not just the bleeding-edge tip.

## Project ideas (forward-looking)

- **Agent-step persistence layer.** Instead of an in-memory agent loop, persist each tool call / LLM call / reflection step as a pg_durable step. Resume conversations across server restarts. Why this repo: provides the substrate; you bring the agent.
- **Replace your half-written workflow system.** Almost every backend team has a `status` column on a queue table and a worker that polls it. Replace with pg_durable. Why this repo: drop-in for the most-common pattern.
- **Repo-radar's daily pipeline as a pg_durable workflow.** If this radar grows beyond a daily cron, the per-step (fetch → enrich → trends → digest → commit) shape maps naturally onto a durable workflow. Why this repo: resumability matters if any single step starts taking minutes.
- **DBT-shaped data pipeline with durable retries.** Each SQL transformation as a step; failures retry from the last successful step. Why this repo: removes the need for Airflow.
- **Multi-agent debate logger** (compose with TradingAgents-style patterns) — each agent's turn is a durable step; if the debate crashes mid-way, restart from the last reply. Why this repo: each LLM call is exactly the kind of "expensive, would hate to redo" step that benefits from checkpointing.

## What to skip

- The "Try in Azure HorizonDB" CTA is Microsoft's marketing — the library is the load-bearing part; you don't need their managed service to use it.
- Don't reach for this if you have a multi-DB stack already running Temporal — switching back to a Postgres-only workflow is regression for some teams.

## Watch-outs

- **License is "PostgreSQL License" (BSD-like, very permissive)** but the README badge says `NOASSERTION` from GitHub's detector — confirm by reading `LICENSE.txt` before commercial use.
- **Postgres extension means deployment friction.** Managed Postgres providers (RDS, Cloud SQL, Supabase) often won't let you install arbitrary extensions. Self-managed Postgres or Azure HorizonDB only, until ecosystem catches up.
- **Created 2026-02-13** — four months old; expect API churn. Pin to release tags.
- **Microsoft-led OSS** — solid for Postgres extensions historically (`pg_dirtyread`, `pglogical` derivatives), but governance is single-company. Watch for any signal of foundation donation.
- **Durable execution is a load-bearing primitive.** Hard to remove once you depend on it. Eval carefully before betting an architecture on it.
- **Performance is unknown at scale.** Microsoft's pitch is "compute close to data," which is good for medium workflows; for high-throughput it may not beat dedicated engines. Bench before betting.
