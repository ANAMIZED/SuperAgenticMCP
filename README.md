# SuperAgenticMCP

**The switchboard for your agent swarm.**

SuperAgenticMCP is a production-oriented, MCP-native router and multi-agent control plane. It sits between your agents and the MCP servers they need — planning the task, routing each tool call to the right server, streaming every step, and filing results into memory.

> Patch every agent into every tool.

[![CI](https://github.com/ANAMIZED/SuperAgenticMCP/actions/workflows/ci.yml/badge.svg)](https://github.com/ANAMIZED/SuperAgenticMCP/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Server-green)](https://modelcontextprotocol.io/)

**Layout standard:** [Server OS](https://github.com/ANAMIZED/server-os) — see [`docs/LAYOUT.md`](docs/LAYOUT.md).

---

## Surfaces

| Surface | Entry |
|---------|--------|
| **Web control plane** | [`superagenticmcp.html`](superagenticmcp.html) / [`web/`](web/) (offline hero) |
| **MCP Server** | `superagenticmcp` |
| **CLI** | `superagenticmcp-cli status` |
| **SDK** | `from superagenticmcp.sdk import SuperAgenticClient` |
| **Board (target)** | `superagenticmcp up --board` → http://localhost:7420 |
| **Skills** | `skills/*/SKILL.md` |
| **AGENTS.md** | Coding-agent contract |
| **Verify** | `bash scripts/verify.sh` |
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
| MCP over stdio (+ streamable HTTP planned) | ✅ scaffold |
| Capability-first routing + latency tie-break | 🚧 / demo in hero |
| Planner → parallel workers → critic | 🚧 / demo in hero |
| Hot-swap server rack | 🚧 / demo in hero |
| Live patch board + phosphor log | ✅ hero |
| Memory scope (3D constellation) | ✅ hero |
| Call budgets + offline skip | 🚧 |
| Dynamic `superagentic.json` | 🚧 |
| Server OS layout + verify contract | ✅ |
| Self-learning model routing (bandit) | 🚧 |
| Agentic commerce (x402) | 🚧 |

---

## Quick start

```bash
git clone https://github.com/ANAMIZED/SuperAgenticMCP
cd SuperAgenticMCP
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"

superagenticmcp                 # MCP server (stdio)
superagenticmcp-cli status
make test
bash scripts/verify.sh
```

Zero-install hero:

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

### Docker (scaffold)

```bash
docker compose up --build
```

---

## How routing works

1. **Protocol** — Model Context Protocol; one session per racked server.
2. **Agent loop** — Planner decomposes; workers run in parallel where allowed; critic checks before ship.
3. **Routing** — Capability match first, latency as tie-break, fallback when a server drops.
4. **Guardrails** — Per-server allow-lists and per-run call budgets.
5. **Telemetry** — JSONL lines + board replay.
6. **Footprint** — Single process for the core path; no DB required.

---

## Repository layout

```
src/superagenticmcp/   # MCP, CLI, SDK
skills/                # Packaged skills (Server OS style)
web/                   # Control-plane path
scripts/verify.sh      # Verify contract
tests/                 # Smoke + contract tests
superagenticmcp.html   # Hero demo
docs/LAYOUT.md         # Permanent layout standard = Server OS
AGENTS.md              # Agent contract
```

---

## Related projects

- [server-os](https://github.com/ANAMIZED/server-os) — **layout standard** · agents as processes
- [OpenGOS](https://github.com/ANAMIZED/OpenGOS) — grants + public-goods funding MCP
- [LRSI](https://github.com/ANAMIZED/LRSI) — local recursive self-improvement kernel
- [x402-cloudflare-starter](https://github.com/ANAMIZED/x402-cloudflare-starter) — USDC micropayments

---

## License

Apache-2.0

Built for the Model Context Protocol · Unit 001 · SA-MCP MK.4 · Server OS layout
