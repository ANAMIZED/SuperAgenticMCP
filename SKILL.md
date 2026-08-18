---
name: superagenticmcp
description: >
  SuperAgenticMCP — the switchboard for your agent swarm. MCP-native router and
  multi-agent control plane that plans tasks, routes tool calls to racked MCP
  servers by capability and latency, streams execution, and files results into
  a memory-scope graph. Use when the user needs multi-agent orchestration over
  MCP, a local agent switchboard, capability-based tool routing, or a live
  patch-board view of agent↔server traffic.
license: Apache-2.0
metadata:
  author: ANAMIZED
  repository: https://github.com/ANAMIZED/SuperAgenticMCP
  version: "0.1.0"
  mcp: true
---

# SuperAgenticMCP

**Patch every agent into every tool.**

## When to use this skill

- Orchestrate multiple agents (planner / workers / critic) against a set of MCP servers
- Route tool calls by capability with latency as a tie-breaker
- Run a local switchboard that racks/unracks servers and regenerates config
- Observe live agent→server traffic (patch board + JSONL log + run receipt)
- Persist run artifacts into a linked memory-scope constellation
- Generate or consume a `superagentic.json` router config

## How to run the MCP server

```bash
pip install superagenticmcp
# or from source:
pip install -e .

superagenticmcp
```

MCP client config:

```json
{
  "mcpServers": {
    "superagenticmcp": {
      "command": "superagenticmcp",
      "args": []
    }
  }
}
```

Board mode (when implemented):

```bash
superagenticmcp up --board
# board on http://localhost:7420
```

## Core ideas

1. **Rack** — toggle MCP servers online; they appear on the board and become routable
2. **Plan** — planner decomposes the task order into steps across servers
3. **Route** — capability match first, latency second, fallback when a server is offline
4. **Observe** — every call is a JSONL line; the same stream feeds the log and the board
5. **Remember** — completed runs file artifacts into a linked memory graph

## Principles

1. **Observable by default** — routing and failures must be visible (log + board + receipt)
2. **Config as truth** — rack state and `superagentic.json` stay in sync
3. **Fail closed on budgets** — a run that hits its call budget stops and says so
4. **Demo is not runtime** — the HTML hero is for design feel; production path is the Python MCP server
5. **Additive surface** — keep the public MCP tool surface stable and clear

## Interactive shell

No install required:

https://htmlpreview.github.io/?https://github.com/ANAMIZED/SuperAgenticMCP/blob/main/superagenticmcp.html
