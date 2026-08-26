# SuperAgenticMCP

[![CI](https://github.com/ANAMIZED/SuperAgenticMCP/actions/workflows/ci.yml/badge.svg)](https://github.com/ANAMIZED/SuperAgenticMCP/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/MCP-server-purple.svg)](src/superagenticmcp/server.py)
[![SDK](https://img.shields.io/badge/SDK-Python-green.svg)](src/superagenticmcp/sdk/)
[![CLI](https://img.shields.io/badge/CLI-superagenticmcp--cli-orange.svg)](src/superagenticmcp/cli.py)
[![Board](https://img.shields.io/badge/Board-hero%20demo-009688.svg)](superagenticmcp.html)
[![USDC](https://img.shields.io/badge/USDC-Base%20%7C%20ETH%20%7C%20Solana-2775CA.svg)](#usdc-crypto)

**The switchboard for your agent swarm.**

SuperAgenticMCP is a production-oriented, MCP-native router and multi-agent control plane. It sits between your agents and the MCP servers they need — planning the task, routing each tool call to the right server, streaming every step, and filing results into memory.

> Patch every agent into every tool.

**[Support Agentic OS Kernels ($99)](https://buy.stripe.com/bJecN63wObPv6Bf7Zm43S02)** · **[Agentic OS Cycle ($0.75)](https://buy.stripe.com/3cI14o8R8dXD3p3frO43S04)** · **[Public Goods Support](https://donate.stripe.com/00w5kE3wOg5L8Jn2F243S00)** · **[USDC](#usdc-crypto)**

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
| Agentic commerce (x402) | ✅ routes to [x402-cloudflare-starter](https://github.com/ANAMIZED/x402-cloudflare-starter) `GET /v1/cycle` · `/v1/search` · `/v1/draft` |

Commerce is **not** reimplemented here. Rack the x402 Worker; keep Stripe Payment Links for humans. Receipts are not Desk unlocks.

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

## Support

### Fiat (Stripe)

| Offer | Link |
|-------|------|
| **Support Agentic OS Kernels** — $99 | [buy.stripe.com/…](https://buy.stripe.com/bJecN63wObPv6Bf7Zm43S02) |
| **Agentic OS Cycle** — $0.75 | [buy.stripe.com/…](https://buy.stripe.com/3cI14o8R8dXD3p3frO43S04) |
| **Public Goods Support** | [donate.stripe.com/…](https://donate.stripe.com/00w5kE3wOg5L8Jn2F243S00) |

GitHub Sponsors: [ANAMIZED](https://github.com/sponsors/ANAMIZED)

### USDC (crypto)

Non-custodial addresses controlled by ANAMIZED. Pure **x402** micropayments preferred for agents — see [x402-cloudflare-starter](https://github.com/ANAMIZED/x402-cloudflare-starter).

| Network | Address | Explorer |
|---------|---------|----------|
| **Base** | `0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438` | [basescan](https://basescan.org/address/0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438) |
| **Ethereum** | `0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438` | [etherscan](https://etherscan.io/address/0xD3d0E9eDAe3Ac7bb199a8EAA761BdA423b878438) |
| **Solana** | `ETQwWf19axArsY493UfC6bxe2BmEzmzvCb58PPnC38A` | [solscan](https://solscan.io/account/ETQwWf19axArsY493UfC6bxe2BmEzmzvCb58PPnC38A) |

Send only **USDC** on the matching network. Wrong asset or chain can mean permanent loss.

---

## Related projects

- [server-os](https://github.com/ANAMIZED/server-os) — **layout standard** · agents as processes
- [OpenGOS](https://github.com/ANAMIZED/OpenGOS) — grants + public-goods funding MCP
- [LRSI](https://github.com/ANAMIZED/LRSI) — local recursive self-improvement kernel
- [x402-cloudflare-starter](https://github.com/ANAMIZED/x402-cloudflare-starter) — USDC micropayments (Base + Solana)

---

## License

Apache-2.0

Built for the Model Context Protocol · Unit 001 · SA-MCP MK.4 · Server OS layout
