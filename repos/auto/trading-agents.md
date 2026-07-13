# TauricResearch/TradingAgents

> "Multi-Agents LLM Financial Trading Framework." Open-source replication of a hedge-fund-style multi-agent setup — analyst, researcher, trader, risk manager — each an LLM agent collaborating on trades.

- **URL**: https://github.com/TauricResearch/TradingAgents
- **Tags**: `agent` `research` `llm-ops` `data`
- **Maturity**: 84,632 stars · 546 today on trending 2026-06-09 · created 2024-12-28 · active (last push 2026-06-01)
- **License**: Apache 2.0
- **Paper**: arXiv 2412.20138

## What it actually is

A Python framework that decomposes "should we buy/sell this stock" into a multi-agent pipeline mirroring a real trading desk: fundamental analyst, sentiment analyst, technical analyst, news researcher, bull/bear debate, trader, risk manager. Each role is an LLM agent with a specific prompt and access to specific tools (price feeds, news APIs, etc.). The agents pass structured outputs to each other; final trade decision aggregates the chain. Published as an arXiv paper with the code — academic-research-style release. 84k stars in ~18 months puts it in the top tier of agent-research repos.

## What's reusable

- **The multi-agent role decomposition itself.** "Split a complex decision into specialist roles, have them debate, aggregate" generalizes way beyond trading. Same pattern works for medical diagnosis, legal review, code review, product decisions.
- **The bull/bear debate step.** Before trading, two adversarial agents argue opposite positions. This is the most copy-able idea — useful for any high-stakes decision where you want adversarial verification.
- **Per-role prompt templates.** Even if you don't trade, the analyst/researcher/risk-manager prompts are reference material for "how to write an LLM prompt for a specialist role."
- **Tool/data-access decomposition.** Different agents have different tools — analyst sees prices, news researcher sees news. Pattern for any system where you don't want every agent reading every source.
- **The paper.** arXiv 2412.20138 walks through the architecture; useful to read even if you never run the code.
- **Hidden value: the data-pipeline plumbing.** Even if the trading logic is academic, the price + news + sentiment fetchers are reusable in any finance-adjacent project.

## Project ideas (forward-looking)

- **Multi-agent code reviewer.** Replace "fundamental / sentiment / technical" with "correctness / security / performance" and have the agents debate before approving a PR. Why this repo: the bull/bear adversarial pattern is exactly what code review wants.
- **Multi-agent due diligence for VC deals.** Analyst (financials) + market researcher (TAM) + tech reviewer (defensibility) + risk manager (red flags). Why this repo: framework already handles role coordination.
- **Adversarial fact-checking pipeline.** Bull agent argues a claim is true, bear agent argues false, judge synthesizes. Why this repo: the debate substrate is the load-bearing part.
- **"Should I take this job offer" agent.** Same decomposition: financial analyst, growth analyst, risk manager. Outputs structured decision memo. Why this repo: structure transfers as-is.
- **Demonstrably bad project idea: actually trade with this.** Don't. See watch-outs.

## What to skip

- The actual back-test results in the paper are promising on backtests, but back-tests routinely overfit; don't take the P&L claims as a green light.
- The "Discord / WeChat / Trendshift" badges are decoration.
- The i18n READMEs are just translations.

## Watch-outs

- ⚠ **Do not trade real money with this.** Academic prototype. No order management, no slippage modeling, no compliance, no risk circuit breakers. People will deploy it anyway, and lose money. Be wiser.
- **LLM-decision-making in finance is heavily regulated** in most jurisdictions. Even a personal-use bot can violate exchange TOS or local financial-services law.
- **84k stars in 18 months is hype-heavy.** Real production usage of this framework as a trading system is approximately zero; the stars come from people interested in the multi-agent pattern, not from traders.
- **Costs add up.** A full pipeline run is many LLM calls per trade signal. At GPT-4 / Claude-Opus prices, a daily-bar strategy on 50 stocks gets expensive fast. Use cheaper models (Haiku/Flash) for prototyping.
- **No model abstraction shown clearly in README** — check `config.py` or similar to see how to swap models; default may assume OpenAI.
