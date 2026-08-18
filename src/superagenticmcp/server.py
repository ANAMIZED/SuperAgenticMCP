"""MCP entry point for SuperAgenticMCP (FastMCP).

This is the primary agent-facing surface. The browser demo
(superagenticmcp.html) is a design prototype; production traffic
flows through this server.
"""

from __future__ import annotations

try:
    from fastmcp import FastMCP
except ImportError:  # pragma: no cover
    FastMCP = None  # type: ignore

mcp = FastMCP("SuperAgenticMCP") if FastMCP is not None else None


if mcp is not None:

    @mcp.tool()
    def status() -> dict:
        """Return router status: version, racked servers (stub), and health."""
        return {
            "name": "superagenticmcp",
            "version": "0.1.0",
            "status": "ok",
            "note": "Alpha scaffold — routing and rack will land in subsequent commits.",
            "board": "http://localhost:7420 (when running with --board)",
        }

    @mcp.tool()
    def list_rack() -> dict:
        """List currently racked MCP servers (stub)."""
        return {
            "servers": [],
            "note": "Rack population is not yet wired. See superagenticmcp.html for the design target.",
        }


def main() -> None:
    """Entry point for the `superagenticmcp` console script."""
    if mcp is None:
        raise SystemExit(
            "fastmcp is required. Install with: pip install -e '.[dev]'"
        )
    mcp.run()


if __name__ == "__main__":
    main()
