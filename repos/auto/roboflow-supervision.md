# roboflow/supervision

> "We write your reusable computer vision tools." From data loading to real-time zone counting, a Python toolkit for the CV-plumbing nobody wants to write twice.

- **URL**: https://github.com/roboflow/supervision
- **Tags**: `data` `infra` `media`
- **Maturity**: 42,292 stars · #3 GitHub Trending 2026-06-08 · created 2022-11-28 · very active (last push 2026-06-08, multi-year)
- **License**: MIT

## What it actually is

Roboflow's production-grade utility belt for computer vision in Python: dataset loading (COCO, Pascal VOC, YOLO formats), model-agnostic detection/segmentation/tracking primitives, annotator widgets, real-time zone counting / line crossing, metrics (mAP, confusion matrices), and video processing helpers. Plays nice with any detector (Ultralytics YOLO, Roboflow Inference, Detectron2, Hugging Face) — you bring the model, supervision handles the boilerplate. Battle-tested: 42k stars over 3+ years, weekly pushes, real Roboflow customers in the dependency chain.

## What's reusable

- **Detection / segmentation annotators** — the kind of "draw boxes with labels and confidence" code you'd otherwise write 5× and never quite right.
- **`Detections` data class** — a standard interchange object across models. If you switch detectors (YOLO → DETR → something custom), your downstream code stays put.
- **Real-time zone counting + line-crossing** — drop-in for any "count things crossing this line" or "alert if N people in zone X" use case (retail analytics, traffic, security).
- **Tracker integrations** — ByteTrack and other trackers wrapped with a uniform API.
- **Dataset format converters** — COCO ↔ Pascal VOC ↔ YOLO without rewriting the parser each time.
- **Metrics module** — production-quality mAP and confusion-matrix code; usable even if you don't use the rest of the library.
- **Pattern: "model-agnostic primitives over a common data class."** This is how you write a utility library that survives the model-zoo churn — same pattern works for any rapidly evolving ML domain.

## Project ideas (forward-looking)

- **In-store retail analytics tool.** YOLO + supervision zone counting → "how many people are at the checkout right now / dwell time per aisle." Why this repo: zone counting and crossing logic is already production-quality.
- **Real-time agentic security camera.** Detect → tag → describe with VLM → alert if anomaly. Why this repo: supervision handles the perception loop, you just add the VLM step.
- **CV pipeline for any agent skill that needs "look at this video."** When you build a Claude/Goose skill that ingests video, this is the layer between raw frames and structured detections.
- **Sports / traffic data extractor.** Bird's-eye-view homography + tracking + zone counting for any "count balls / cars / players" use case.
- **Auto-annotation feeder pool for training data.** Use a big VLM to label, supervision to manage the dataset, autodistill (roboflow's other repo) to compress to a small model.

## What to skip

- The huge README badge soup is decorative.
- The `notebooks` and `inference` cross-links in the README are Roboflow's other repos — useful, but separate decisions.
- Don't pull in the Hugging Face Hub integration if you only need local files; it adds a heavy dep.

## Watch-outs

- **Owned by Roboflow (a vendor).** Library itself is permissively licensed and not lock-in, but Roboflow steers the roadmap — features that overlap with their paid SaaS may get less love.
- **Heavy install** if you pull all extras (`supervision[desktop]` etc.). Pin to the slim install for production.
- **API has churned in 3+ years.** Pin versions; old tutorial code may not work.
- **It's a toolkit, not a framework.** Not opinionated about pipeline shape — fine, but means more glue code than a framework like Ultralytics.
