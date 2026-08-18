#!/usr/bin/env bash
# SuperAgenticMCP verification contract (Server OS layout standard).
# Alpha: layout, imports, CLI, skills, AGENTS — expand as router/API lands.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="${ROOT}/src${PYTHONPATH:+:$PYTHONPATH}"
PASS=0
FAIL=0

green() { printf "\033[32m✓ %s\033[0m\n" "$*"; PASS=$((PASS+1)); }
red()   { printf "\033[31m✗ %s\033[0m\n" "$*"; FAIL=$((FAIL+1)); }
info()  { printf "\033[36m→ %s\033[0m\n" "$*"; }

info "Server OS layout contract..."
if [[ -f "$ROOT/docs/LAYOUT.md" ]] && grep -qi "Server OS" "$ROOT/docs/LAYOUT.md"; then
  green "docs/LAYOUT.md declares Server OS standard"
else
  red "docs/LAYOUT.md missing or does not declare Server OS"
fi

info "Checking AGENTS.md..."
if [[ -f "$ROOT/AGENTS.md" ]] && grep -q "verify.sh" "$ROOT/AGENTS.md"; then
  green "AGENTS.md present with verify contract"
else
  red "AGENTS.md missing or incomplete"
fi

info "Checking skills frontmatter..."
SKILL_COUNT=0
for d in multi-agent-workflow routing-capability memory-scope; do
  f="$ROOT/skills/$d/SKILL.md"
  if [[ -f "$f" ]] && head -1 "$f" | grep -q '^---'; then
    SKILL_COUNT=$((SKILL_COUNT+1))
  else
    red "Skill missing or invalid frontmatter: $d"
  fi
done
if [[ "$SKILL_COUNT" -eq 3 ]]; then
  green "All 3 SKILL.md packages present with frontmatter"
fi

info "Root SKILL.md + registry metadata..."
for f in SKILL.md server.json glama.json; do
  if [[ -f "$ROOT/$f" ]]; then green "$f present"; else red "$f missing"; fi
done

info "Import smoke..."
if python -c "import superagenticmcp; assert superagenticmcp.__version__; from superagenticmcp.server import main; from superagenticmcp.sdk import SuperAgenticClient" 2>/dev/null; then
  green "Package + server + SDK import OK"
else
  red "Import smoke failed"
fi

info "CLI status..."
if python -m superagenticmcp.cli status >/dev/null 2>&1 || superagenticmcp-cli status >/dev/null 2>&1; then
  green "CLI status OK"
else
  # typer module path
  if PYTHONPATH="$ROOT/src" python -c "from superagenticmcp.cli import main; main()" status >/dev/null 2>&1; then
    green "CLI status OK (module)"
  else
    red "CLI status failed"
  fi
fi

info "Pytest..."
if (cd "$ROOT" && python -m pytest -q tests/ 2>/dev/null); then
  green "Pytest suite passed"
else
  red "Pytest failures"
fi

info "Ruff (if installed)..."
if command -v ruff >/dev/null 2>&1; then
  if (cd "$ROOT" && ruff check src && ruff format --check src); then
    green "Ruff check + format OK"
  else
    red "Ruff failed"
  fi
else
  info "ruff not on PATH — skip (CI installs it)"
fi

echo ""
echo "===================================="
echo " SuperAgenticMCP verification result"
echo "===================================="
echo "  PASSED: $PASS"
echo "  FAILED: $FAIL"
echo "===================================="

if [[ "$FAIL" -eq 0 ]]; then
  echo "ALL CHECKS PASSED — layout, AGENTS, skills, imports, CLI, tests."
  exit 0
else
  echo "SOME CHECKS FAILED — inspect output above."
  exit 1
fi
