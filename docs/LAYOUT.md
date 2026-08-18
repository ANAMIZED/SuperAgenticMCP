# Repository Layout Standard

**Server OS is the permanent layout standard for all ANAMIZED repos.**

Reference implementation: [ANAMIZED/server-os](https://github.com/ANAMIZED/server-os)

This repository (SuperAgenticMCP) follows that standard. Product identity stays
switchboard / MCP router; packaging, contracts, and surfaces match Server OS.

## Required surfaces

| Surface | Path / entry |
|---------|----------------|
| AGENTS.md | Coding-agent contract (must mention `scripts/verify.sh`) |
| SKILL.md | Root skill discovery metadata |
| skills/*/SKILL.md | Packaged skills with YAML frontmatter |
| MCP | `superagenticmcp` → `superagenticmcp.server:main` |
| CLI | `superagenticmcp-cli` |
| SDK | `superagenticmcp.sdk` |
| Web control plane | `web/` + hero `superagenticmcp.html` |
| Verify | `scripts/verify.sh` |
| CI | `.github/workflows/ci.yml` |
| Packaging | `pyproject.toml` (Hatch, src layout) |
| Registry | `server.json`, `glama.json` |
| Ops | `Dockerfile`, `docker-compose.yml`, `Makefile` |

## Principles (from Server OS)

1. Fail closed — prefer explicit skip/error over silent success.
2. No ambient authority — capabilities and allow-lists only.
3. Observable by default — JSONL / receipts / board telemetry.
4. Zero tribal knowledge — a senior engineer ships from README + source alone.
5. Mock/offline path stays deterministic when added.

## Do not

- Invent a parallel layout for this repo family.
- Remove `scripts/verify.sh` or the AGENTS.md verify contract.
- Treat the hero HTML as production runtime.
