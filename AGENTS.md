# AGENTS.md

## What this project is

**SuperAgenticMCP** is the switchboard for agent swarms.

It is an MCP-native router and multi-agent control plane that:

- Racks MCP servers (filesystem, web-search, GitHub, Postgres, memory, browser, code-runner, messenger, …)
- Plans tasks (planner → workers → critic)
- Routes each tool call by capability match, then latency
- Streams every step to a live patch board and JSONL log
- Files completed runs into a memory-scope constellation

It is local-first, single-process for the core path, and designed so the design can be felt before the full runtime lands.

## Repository layout

```
src/superagenticmcp/
  server.py          # MCP entry point (FastMCP) — primary interface
  router.py          # Capability + latency routing, call budgets
  agents/            # Planner, workers, critic orchestration
  board/             # Live board, JSONL telemetry, receipts
  memory/            # Memory-scope graph
  config.py          # superagentic.json load / generate
  sdk/               # Python client
  cli.py             # CLI entry

skills/              # Agent-discoverable skills (SKILL.md style)
docs/                # Human documentation
superagenticmcp.html # Interactive browser shell (no install)
server.json          # MCP registry metadata
glama.json           # Glama registry metadata
```

## Conventions

- Python **3.11+**
- Package name: `superagenticmcp`
- Import path: `superagenticmcp`
- Entry point: `superagenticmcp` → `superagenticmcp.server:main`
- MCP framework: **FastMCP**
- Lint/format: `ruff`
- Config truth: the rack state and `superagentic.json` must stay in sync
- Prefer observable failures (skip offline servers, emit clear log lines) over silent drops

## How to run

```bash
pip install -e ".[dev]"
superagenticmcp                 # MCP server on stdio
python -m superagenticmcp       # same
superagenticmcp up --board      # router + board UI
```

Zero-install demo:

```
open superagenticmcp.html
# or
https://htmlpreview.github.io/?https://github.com/ANAMIZED/SuperAgenticMCP/blob/main/superagenticmcp.html
```

## Boundaries (do not)

- Do not hardcode API keys or secrets into source or the hero HTML
- Do not invent tool results in the real server path — simulation belongs only in the browser demo
- Do not remove call-budget or allow-list guardrails without an explicit design decision
- Keep the MCP tool surface clear and stable; prefer additive changes
- Do not treat the hero HTML as production runtime; it is a design-and-feel surface
- Preserve provenance and timestamps on any telemetry or memory nodes

## Adding a racked server

1. Define the server package / command under the config schema (see `config.py` / `superagentic.json` shape)
2. Expose tools via MCP so the router can capability-match
3. Document latency class and category (Core / Research / Dev / Data / Comms)
4. Wire into the board legend and rack UI when the real board is implemented
5. Update README features / surfaces if the public surface changes

## Related files for agents

- `SKILL.md` — skill description for agent skill discovery
- `server.json` — MCP registry metadata
- `glama.json` — Glama registry metadata
- `superagenticmcp.html` — interactive design prototype of the control surface
