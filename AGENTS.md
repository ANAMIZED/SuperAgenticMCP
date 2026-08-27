# AGENTS.md — SuperAgenticMCP

This file is the contract for any AI coding agent working on this repository.

**Layout standard:** [Server OS](https://github.com/ANAMIZED/server-os)  
See `docs/LAYOUT.md`.

## What this project is

SuperAgenticMCP is the **switchboard for agent swarms**: an MCP-native router and
multi-agent control plane that racks MCP servers, plans tasks (planner → workers →
critic), routes by capability then latency, streams steps to a live board + JSONL
log, and files runs into a memory-scope constellation.

A senior engineer with only the source code and `README.md` must be able to install,
exercise public surfaces, and verify via `scripts/verify.sh`.

## How to run & verify

```bash
pip install -e ".[dev]"
make test
bash scripts/verify.sh
```

MCP: `superagenticmcp`  
CLI: `superagenticmcp-cli status`  
Hero: `superagenticmcp.html`  
WebMCP board: `web/board.html`

## Hard rules for agents

1. Never break the verify contract (`scripts/verify.sh`).
2. Fail closed — no silent drops of tool calls or servers.
3. Capabilities and allow-lists only — no ambient authority.
4. Keep secrets out of source and the hero HTML.
5. Simulation belongs only in the browser demo; the real server path must not invent tool results.
6. Prefer small, focused changes. Update README.md and AGENTS.md when public surfaces change.
7. Do not invent a parallel layout — Server OS is the permanent standard.
8. WebMCP is a page front door. Do not replace stdio MCP with it.

## Surfaces that must stay working

MCP Server, CLI, SDK import, skills frontmatter, AGENTS.md, `scripts/verify.sh`, CI, `web/board.html`.

See `docs/WEBMCP.md`.
