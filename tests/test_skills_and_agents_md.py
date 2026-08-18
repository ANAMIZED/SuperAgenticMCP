"""Contract tests for Server OS layout: AGENTS.md + skills frontmatter."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_agents_md_has_verify_contract():
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    assert "verify.sh" in text
    assert "Server OS" in text or "server-os" in text.lower()


def test_layout_md_declares_server_os():
    text = (ROOT / "docs" / "LAYOUT.md").read_text(encoding="utf-8")
    assert "Server OS" in text


def test_skill_packages_have_frontmatter():
    required = ["multi-agent-workflow", "routing-capability", "memory-scope"]
    for name in required:
        path = ROOT / "skills" / name / "SKILL.md"
        assert path.is_file(), f"missing {path}"
        first = path.read_text(encoding="utf-8").splitlines()[0]
        assert first.strip() == "---", f"{name} missing YAML frontmatter"
