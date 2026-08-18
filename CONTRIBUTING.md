# Contributing to SuperAgenticMCP

Thank you for helping build the switchboard for agent swarms.

## Development setup

```bash
git clone https://github.com/ANAMIZED/SuperAgenticMCP
cd SuperAgenticMCP
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
```

## Conventions

- Python 3.11+
- Format and lint with `ruff`
- Keep the MCP tool surface additive and documented
- Prefer observable failures (clear log lines, skip offline servers) over silent drops
- The hero demo (`superagenticmcp.html`) is a design surface; production logic lives under `src/superagenticmcp/`

## Running checks

```bash
ruff check src
ruff format --check src
pytest          # when tests are present
```

## Pull requests

1. Fork and create a branch from `main`
2. Keep changes focused (one concern per PR when possible)
3. Update `README.md`, `AGENTS.md`, or `SKILL.md` if you change public surfaces
4. Ensure CI (`.github/workflows/ci.yml`) would pass
5. Describe the change and any intentional deviations from existing routing/guardrail behavior

## Boundaries

See `AGENTS.md` for the project’s “do not” list. In particular:

- Do not hardcode secrets
- Do not invent tool results on the real server path
- Do not remove call budgets or allow-lists without explicit design discussion

## License

By contributing you agree that your contributions are licensed under the Apache-2.0 license of this repository.
