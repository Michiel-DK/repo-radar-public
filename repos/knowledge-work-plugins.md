# anthropics/knowledge-work-plugins

> 11 role-specific Claude plugins (sales, marketing, finance, legal, data, product, support, etc.) — skills + commands + MCP connectors bundled per job function.

- **URL**: https://github.com/anthropics/knowledge-work-plugins
- **Tags**: `skill` `mcp` `agent`
- **Maturity**: ~19k stars · active · Anthropic-maintained
- **License**: Apache 2.0

## What it actually is

The official Anthropic plugin marketplace for Claude Cowork (also installable in Claude Code). Each plugin is a folder containing `.claude-plugin/plugin.json`, `.mcp.json` (connector config), `commands/` (slash commands), and `skills/` (auto-firing domain expertise). 11 plugins span: productivity, sales, customer-support, product-management, marketing, legal, finance, data, enterprise-search, bio-research, and a meta-plugin for managing plugins (`cowork-plugin-management`). All file-based — markdown + JSON, no code, no build step. Designed to be forked and customized per company.

## What's reusable

- **The plugin manifest schema** (`.claude-plugin/plugin.json` + `.mcp.json` + `skills/` + `commands/`) — the cleanest reference for building your own plugins, by definition.
- **`sales/skills/account-research`** — the closest off-the-shelf scaffold for any "research a company before X" workflow. Already structures output with quick-take + company-profile + key-people sections, gracefully degrades when CRM/enrichment connectors are absent.
- **`sales/skills/call-prep`, `call-summary`, `competitive-intelligence`, `pipeline-review`** — full set of sales-cycle skills with consistent output formats.
- **`product-management/`** — specs, roadmaps, user-research synthesis. Pattern reusable for any "structured artifact + stakeholder loop" role.
- **`data/`** — write SQL + run statistical analysis + build dashboards + validate before sharing. Reusable for any analyst workflow.
- **`enterprise-search/`** — cross-tool search pattern (Slack + Notion + Guru + Jira + Asana + MS365). Same approach reusable for any "one query, many sources" UX.
- **`legal/`** — contract review + NDA triage + compliance check. Reusable framework even if specific clauses differ per jurisdiction.
- **`.mcp.json` patterns** — concrete examples of wiring MCP connectors to skills (Slack, HubSpot, Snowflake, Linear, Figma, etc.). Best reference for "what MCP servers exist that I might use."
- **Connector-graceful skills** — every skill works without its connector, gets better with it. Pattern: never hard-require a connector inside a skill.

## Project ideas (forward-looking)

- **Vertical-specific plugin pack** (e.g. for VC investing, for legal-ops, for academic deans). Fork the structure, swap the skills, ship under your own marketplace. Why this repo: the plugin spec + 11 reference implementations remove every structural decision.
- **"Sales plugin for technical founders"** — take `sales/account-research` + `call-prep`, replace HubSpot connector with a lighter Folk/Attio/Notion stack, ship as a paid plugin to bootstrappers. Why this repo: 80% of the prompts already work for B2B SaaS sales.
- **Cross-functional onboarding plugin.** When someone changes roles internally, install the destination plugin and they're immediately productive in the new function. Why this repo: each role's vocabulary + workflow is already encoded.
- **Internal-tools chat plugin for any company.** Fork `enterprise-search`, point the MCP config at the actual internal stack, distribute via Cowork. Why this repo: the multi-connector skill pattern is well-trodden here.
- **Plugin-as-a-knowledge-asset for SMB consultants.** A management consultant's playbook codified as a plugin per engagement type. Why this repo: file-based + no-build means a non-engineer consultant can maintain it.

## What to skip

- The `bio-research` plugin is highly domain-specific (PubMed, ChEMBL, Open Targets); only useful if you're actually in life sciences.
- Many MCP connectors listed in the table assume hosted/enterprise tools (Snowflake, Databricks, ZoomInfo, Klaviyo) — for indie/early-stage use you'll swap most of them out.
- Don't deploy raw — every plugin has placeholders like "your terminology, your processes" that need company-specific filling before they're better than vanilla Claude.

## Watch-outs

- Apache 2.0 — friendly for commercial use, attribution required.
- Designed for Claude Cowork; in Claude Code you lose the "skills auto-fire" UX subtlety. Still useful via slash commands.
- MCP connectors require the corresponding MCP server to exist and be reachable — not auto-provisioned.
- Anthropic-maintained, so quality is high, but the choice of which roles to ship (and which to skip) reflects Anthropic's product priorities, not yours.
