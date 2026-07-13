# RyanCodrai/turbovec

> "A 10M-document corpus takes 31 GB of RAM as float32. turbovec fits it in 4 GB — and searches it faster than FAISS." Rust vector index with Python bindings, built on Google Research's TurboQuant quantizer.

- **URL**: https://github.com/RyanCodrai/turbovec
- **Tags**: `rag` `data` `infra`
- **Maturity**: 8,666 stars · #2 GitHub Trending 2026-06-08 · created 2026-03-26 · active (last push 2026-05-30)
- **License**: MIT (PyPI and crates.io published)

## What it actually is

A vector ANN index implementing Google Research's [TurboQuant](https://arxiv.org/abs/2504.19874) — a data-oblivious quantizer that matches the Shannon lower bound on distortion with no codebook training and no separate train phase. Written in Rust with hand-rolled NEON (ARM) and AVX-512BW (x86) kernels; exposed via Python bindings (`pip install turbovec`) and a Rust crate. Targets the "online ingest, no train step, no rebuild" workflow — add vectors and they're searchable. Claims ~8× memory compression (31 GB → 4 GB for 10M docs at fp32) and 12–20% faster than FAISS IndexPQFastScan on ARM, match-or-beat on x86.

## What's reusable

- **The whole index** as a drop-in FAISS replacement when you need lower RAM and/or simpler ops (no `train()` step is a real operational win).
- **Filter-at-search-time API** — pass an ID allowlist or slot bitmask to `search()`; the kernel honours it directly so you always get up to `k` results from the allowed set without over-fetching. Most ANN libs make you over-fetch and post-filter, hurting recall on selective filters. This is the right API.
- **The TurboQuant algorithm itself** is the real reusable insight — it's data-oblivious (no training data needed), which means the same quantizer works across domains and you can ingest live. Worth reading the paper even if you don't use this library.
- **Reference for shipping a Rust core with Python bindings** to both PyPI and crates.io with proper SIMD feature detection. Solid template for any "fast core + Python wrapper" project.

## Project ideas (forward-looking)

- **Local-first RAG appliance.** Pair with a local embedding model (e.g., `all-MiniLM-L6-v2` or Nomic Embed) for a fully air-gapped RAG stack with no managed service. Why this repo: the memory footprint makes this realistic on a laptop.
- **Per-user vector index inside a multi-tenant SaaS.** Filter-by-bitmask lets you store all users in one index and scope at query time. Why this repo: most ANN libs force you into N indexes; this gives you one with strict isolation.
- **Embedded vector search in a desktop AI app.** Bundle the Rust binary, store vectors as a small file, query without a server. Why this repo: 4 GB for 10M docs fits in a desktop process.
- **Replacement for the FAISS step in `code-graph-rag` or similar pipelines.** Drop-in swap if you're already using FAISS IndexPQFastScan. Why this repo: same API surface, lower RAM, faster on ARM (which matters on Apple Silicon dev machines).
- **Online vector index for streaming data.** No train step means you can ingest live event embeddings and search them immediately. Why this repo: most ANN libs need batch retraining.

## What to skip

- Don't bother reading any of the README badge soup. The README is heavily marketed; skip to the API examples and the paper link.
- The TurboQuant paper itself is what matters; the library is one implementation of it.

## Watch-outs

- **Brand-new (created 2026-03-26).** Two months old at trending time — no production track record, expect API churn.
- **SIMD path matters a lot for the claimed numbers.** If you're on an x86 chip without AVX-512BW (e.g., most consumer Intel pre-Sapphire Rapids, all AMD pre-Zen 4) you fall back to a scalar path and the FAISS-beating numbers disappear.
- **MIT-licensed implementation of a Google-research algorithm.** Algorithm itself is in the paper; check for any patent disclaimers in the TurboQuant publication before commercial use.
- **No managed-service story.** This is a library, not a vector DB. You handle persistence, sharding, replication yourself.
- **Bench numbers come from the project author.** Take "12–20% faster than FAISS" with the usual caveats; reproduce on your hardware before committing.
