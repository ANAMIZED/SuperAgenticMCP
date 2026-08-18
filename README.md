# SuperAgenticMCP

**The switchboard for your agent swarm.**

SuperAgenticMCP is a production-oriented, MCP-native router and multi-agent control plane. It sits between your agents and the MCP servers they need — planning the task, routing each tool call to the right server, streaming every step, and filing results into memory.

> Patch every agent into every tool.

[![CI](https://github.com/ANAMIZED/SuperAgenticMCP/actions/workflows/ci.yml/badge.svg)](https://github.com/ANAMIZED/SuperAgenticMCP/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Server-green)](https://modelcontextprotocol.io/)

---

## Surfaces

| Surface | Entry |
|---------|--------|
| **MCP Server** | `superagenticmcp` |
| **CLI** | `superagenticmcp-cli status` / `up` |
| **SDK** | `from superagenticmcp.sdk import SuperAgenticClient` |
| **Board (live)** | `superagenticmcp up --board` → http://localhost:7420 |
| **Hero demo** | [`superagenticmcp.html`](superagenticmcp.html) (no install) |
| **Multi-agent** | Planner → Workers → Critic (`skills/`) |
| **CI** | `.github/workflows/ci.yml` |

---

## Why SuperAgenticMCP?

| Problem | Approach |
|---------|----------|
| Agents need many MCP servers | One process racks servers and routes by capability |
| Tool calls are opaque | Live patch board + JSONL log + run receipt |
| Multi-agent coordination is ad-hoc | Built-in planner / worker / critic loop |
| Memory evaporates between runs | Memory scope constellation of artifacts |
| Config drifts from reality | Rack toggles generate `superagentic.json` |

---

## Features

| Capability | Status |
|------------|--------|
| MCP over stdio + streamable HTTP | ✅ |
| Capability-first routing + latency tie-break | ✅ (demo) |
| Planner → parallel workers → critic | ✅ (demo) |
| Hot-swap server rack | ✅ (demo) |
| Live patch board + phosphor log | ✅ |
| Memory scope (3D constellation) | ✅ |
| Call budgets + offline skip | ✅ |
| Dynamic `superagentic.json` | ✅ |
| Self-learning model routing (bandit / NeuralUCB) | 🚧 |
| Agentic commerce (x402) | 🚧 |
| Dynamic SKILL.md loader | 🚧 |

---

## Quick start

```bash
# From source (recommended while alpha)
git clone https://github.com/ANAMIZED/SuperAgenticMCP
cd SuperAgenticMCP
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

superagenticmcp            # MCP server (stdio)
superagenticmcp-cli status
superagenticmcp up --board # router + live board on :7420
```

Or open the zero-install hero demo:

https://htmlpreview.github.io/?https://github.com/ANAMIZED/SuperAgenticMCP/blob/main/superagenticmcp.html

### MCP client config

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

---

## How routing works

1. **Protocol** — Model Context Protocol over stdio and streamable HTTP; one session per racked server.
2. **Agent loop** — Planner decomposes the order; workers execute in parallel where steps allow; critic checks before shipping.
3. **Routing** — Capability match first, latency as tie-break, automatic fallback when a server drops.
4. **Guardrails** — Per-server tool allow-lists and per-run call budgets.
5. **Telemetry** — Every call is one JSONL line (same stream the console prints), replayable on the board.
6. **Footprint** — Single process, no database required for the core path.

---

## Repository layout

```
src/superagenticmcp/
  server.py          # MCP entry (FastMCP)
  router.py          # Capability + latency routing
  agents/            # Planner / workers / critic
  board/             # Live board + telemetry
  memory/            # Scope graph
  config.py          # superagentic.json handling

skills/              # Agent-discoverable skills
superagenticmcp.html # Interactive hero demo (no install)
AGENTS.md            # Orientation for coding agents
SKILL.md             # Skill metadata
server.json          # MCP registry metadata
glama.json           # Glama registry metadata
```

---

## Related projects

- [OpenGOS](https://github.com/ANAMIZED/OpenGOS) — grants + public-goods funding MCP
- [server-os](https://github.com/ANAMIZED/server-os) — agents as processes
- [LRSI](https://github.com/ANAMIZED/LRSI) — local recursive self-improvement kernel
- [x402-cloudflare-starter](https://github.com/ANAMIZED/x402-cloudflare-starter) — USDC micropayments

---

## License

Apache-2.0

Built for the Model Context Protocol · Unit 001 · SA-MCP MK.4
