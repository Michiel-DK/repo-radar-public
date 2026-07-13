# CopilotKit/CopilotKit

> "The Frontend Stack for Agents & Generative UI." React/Angular/Vue/Mobile/Slack adapters for shipping agent-native UIs, plus the AG-UI Protocol the project is pushing as a standard.

- **URL**: https://github.com/CopilotKit/CopilotKit
- **Tags**: `agent` `frontend`
- **Maturity**: 34,334 stars · 378 today on trending 2026-06-09 · created 2023-06-19 (3+ years) · very active (last push 2026-06-09)
- **License**: MIT

## What it actually is

The "frontend half" of the agent stack — when you have a working agent (Claude/Goose/LangGraph/your own LangChain thing), CopilotKit gives you the React/Angular/Vue/React-Native/Slack/etc. components to put it in front of users. Generative UI (agent renders cards/forms/charts, not just text), shared state between agent and app, human-in-the-loop approval flows, hooks for streaming, all batteries included. The team also maintains **AG-UI Protocol** — their proposed standard for how agent backends talk to frontends. Pre-dates the current agent wave (created 2023), 34k stars, very mature compared to most repos on today's trending list.

## What's reusable

- **The whole component library** for any "agent inside an existing web app" use case. React is most polished; other framework adapters exist but vary.
- **Generative UI primitives** — the right abstraction for "agent renders UI, not just text." If you've ever hand-rolled `if (response.type === 'chart') { ... }` switches, this replaces that.
- **Shared-state model** — agent and React app see the same state. Reference for any "co-driving" UX (agent + user editing the same doc, both adjusting the same form).
- **Human-in-the-loop approval components** — pre-built modals for "agent wants to run X, approve?" patterns. Saves a week of UI work.
- **AG-UI Protocol spec** — read this whether you use CopilotKit or not. It's the most worked-out attempt at standardizing the agent↔frontend boundary. Even if you write your own protocol, this is the strawman to beat.
- **Slack adapter** — non-obvious surface that turns out to be high-leverage for B2B internal tools.

## Project ideas (forward-looking)

- **Internal agent dashboard for any business workflow.** CopilotKit + your existing data + Claude/Goose backend → an in-app assistant that can read/act on the data. Why this repo: the chat-with-state-and-actions pattern is the whole point.
- **Generative-UI configurator product.** Sell agent-assisted form/dashboard/report building. Why this repo: generative-UI primitives are the hardest UX piece and they're solved.
- **Drop a copilot into an existing SaaS.** Most B2B SaaS will ship "copilot" surfaces in 2026. CopilotKit is the path of least resistance for React-based ones. Why this repo: standardized, batteries-included.
- **AG-UI-protocol adapter for `claude-agent-sdk` or `goose`.** Make any CopilotKit-shaped frontend talk to those backends. Why this repo: spec is documented; adapter is small.
- **"Copilot for Slack" for any internal data store.** Internal tools rarely justify a custom UI but very much justify a Slack bot. Why this repo: Slack adapter is real and works.

## What to skip

- Don't pull the React Native package if you only ship web; npm graph is heavy.
- The "Enterprise Intelligence Platform" link is the team's commercial offering — fine, but the OSS library is the part you need.
- Some examples in the README are Next.js-specific; not a constraint, just a default.

## Watch-outs

- **Vendor (CopilotKit, Inc.) owns the library.** Same risk profile as Roboflow/Supervision — pure OSS but vendor-steered. They have an "Enterprise Intelligence Platform" that monetizes; features that compete may get less love.
- **AG-UI Protocol is *their* proposed standard.** Worth supporting, but it's not yet a multi-vendor consortium standard — adoption could stall.
- **React-first.** Other framework adapters exist but are less polished. If your stack is non-React, eval depth carefully before committing.
- **3+ years of API churn.** Pin to a release; old tutorials may use a removed API.
- **34k stars + 3 years = real production usage**, but also means there's a stable "right way" to use it — fighting the framework is painful.
