# harry0703/MoneyPrinterTurbo

> Give it a video topic or keyword → fully automatic short-form video: script → stock footage → voiceover → subtitles → music → final MP4.

- **URL**: https://github.com/harry0703/MoneyPrinterTurbo
- **Tags**: `media` `llm-ops` `agent`
- **Maturity**: ~78k stars · last commit 2026-06 · active
- **License**: MIT

## What it actually is

Python MVC app (Streamlit WebUI + FastAPI) that generates short-form videos (9:16 or 16:9) end-to-end from a prompt. Pipeline: LLM writes the script → searches Pexels (or local folder) for stock footage → TTS voiceover (multiple providers, real-time preview) → subtitle generation with style controls → background music mix → ffmpeg/moviepy assembly. Supports OpenAI, Gemini, Moonshot, DeepSeek, Ollama, Azure, qwen, ernie, MiniMax, Pollinations, ModelScope, gpt4free, one-api, AIHubMix — basically every LLM provider. Has batch mode (generate N variants, pick one). Ships Docker + Colab + Windows one-click. Massive community + 75k+ stars.

## What's reusable

- **Pattern**: prompt → multi-tool pipeline → MP4 with intermediate human-pickable variants. The "batch N, pick one" pattern is broadly useful for any creative-LLM workflow.
- **`config.example.toml`** — clean reference for how to expose 10+ LLM providers behind one interface without becoming spaghetti.
- **Subtitle styling code** (font/position/color/stroke per-clip) — surprisingly tricky to do well; this is a working reference.
- **Multi-provider TTS abstraction** with live preview — pattern reusable for any voice-app prototype.
- **MVC + Streamlit UI for an LLM pipeline** — solid template for "internal tool with both API and human-driven UI" without touching React.
- **Pexels stock-footage integration** — reusable for any pipeline that needs royalty-free B-roll.

## Project ideas (forward-looking)

- **Weekly auto-generated company explainer videos.** Feed it the week's product changelog or release notes, get a 60s shareable video. Why this repo: end-to-end pipeline already exists; only the prompt template needs work.
- **Localized social content engine.** Translate one English script into 8 languages, generate 8 voiceovers + subtitle tracks, batch-export. Sell the orchestration as a SaaS. Why this repo: multi-language script + multi-provider TTS already wired up.
- **"News-of-the-day in 60 seconds" feed.** Cron-fetch top headlines from an RSS bundle → script-write each → render a video per item → publish to a YouTube Shorts queue. Why this repo: subtitle/music/footage stack saves 2 months of build.
- **Internal explainer videos for new hires.** Convert any internal doc (e.g. "How our deploy pipeline works") into a 2-minute walkthrough with stock B-roll + voiceover. Why this repo: turnkey for non-technical operators who can't open Premiere.
- **A/B-test video ad generator.** Same script, 10 variants with different voice/footage/music; auto-publish to Meta Ads API and pick the winner. Why this repo: batch-mode is already there; only the analytics loop is new.

## What to skip

- The community Windows one-click installer is a v1.2.6 build — out of date. Use uv-sync or Docker instead.
- gpt4free / Pollinations providers are unreliable in production; treat as demo paths.
- The default LLM prompt for script generation is decent but biased toward Chinese-language motivational shorts ("生命的意义是什么"). Replace with your own.

## Watch-outs

- MIT-licensed code, but every video uses third-party assets (Pexels footage, royalty-free music, TTS voices) — license cascade is your problem, not the repo's.
- Pexels API has a rate limit and Pexels-attribution requirements depending on use.
- Subtitle rendering uses MoviePy + ImageMagick; CPU-bound, slow on long videos.
- TTS providers add cost per minute — Azure/OpenAI voices are good but priced; locally-hosted Coqui needs GPU.
- README is primarily Chinese with English/Arabic translations; navigating issues requires translation if Chinese isn't your strong suit.
