# Andyyyy64/whichllm

> Find the local LLM that actually runs and performs best on your hardware. Ranked by real, recency-aware benchmarks, not parameter count. One command.

- **URL**: https://github.com/Andyyyy64/whichllm
- **Tags**: `llm-ops` `infra` `research`
- **Maturity**: 4,276 stars · 633 today (new to top 10, 2026-06-10) · created 2026-03-04 · active (last push 2026-06-10)
- **License**: MIT

## What it actually is

A CLI that answers "which local model should I run on *this* machine?" It profiles your hardware (VRAM, Apple Silicon, GPU) and ranks GGUF/Ollama/HuggingFace models by **real, recency-aware benchmarks** rather than parameter count — then tells you what will actually fit and perform. One command, `pip install whichllm`. Python 3.11+.

## What's reusable

- **Hardware-aware model selection** — the consumer/local complement to the `cost-aware-llm-pipeline` skill: same question ("which model for this job") on a different axis (local hardware fit + recency-aware quality vs. API $/token).
- **Recency-aware benchmarking** — don't rank on stale leaderboards; weight recent benchmark data. Reusable idea for any "pick the best model" logic.
- **VRAM/Apple-Silicon capability detection** — useful snippet if you ever need to gate features on local hardware.
- The "one command, instant answer" UX — good model for low-friction dev tools.

## Project ideas (forward-looking)

- **Local-model router** — combine whichllm (which model fits) with cost-aware routing (which model is worth it) to auto-pick a local model per task. Why this repo: supplies the hardware-fit half.
- **Offline-first agent setup wizard** — run whichllm during onboarding to choose the embedding/inference model for a local-first memory layer (pairs with MemPalace). Why this repo: removes the "which model?" guesswork.
- **CI matrix for local inference** — use its benchmark harness to validate that a project runs acceptably across consumer hardware tiers. Why this repo: the benchmarking is already built.

## What to skip

- Local inference only — irrelevant if you're API-first (Claude/OpenAI/Gemini hosted). It answers a question you don't have if you never run models locally.

## Watch-outs

- **Benchmark freshness depends on upstream data** — "recency-aware" is only as good as the benchmark sources it pulls.
- Young (created 2026-03); model coverage and ranking methodology may shift.
- GGUF/Ollama-centric — assumes that local-inference stack.
