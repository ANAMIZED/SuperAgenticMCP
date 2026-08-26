"""MCP entry point for SuperAgenticMCP (FastMCP).

This is the primary agent-facing surface. The browser demo
(superagenticmcp.html) is a design prototype; production traffic
flows through this server.
"""

from __future__ import annotations

from typing import Annotated, Any

from pydantic import Field

try:
    from fastmcp import FastMCP
except ImportError:  # pragma: no cover
    FastMCP = None  # type: ignore

from superagenticmcp.tools.hints import tool_hints

mcp = FastMCP("SuperAgenticMCP") if FastMCP is not None else None

_RACK: list[dict[str, Any]] = []

_RO = {"read_only": True, "destructive": False, "idempotent": True, "open_world": False}
_RW = {"read_only": False, "destructive": False, "idempotent": True, "open_world": False}
_DEL = {"read_only": False, "destructive": True, "idempotent": True, "open_world": False}


if mcp is not None:

    @mcp.tool(
        name="status",
        title="Get router status",
        description=(
            "Return SuperAgenticMCP router health: version, process status, and how many MCP "
            "servers are currently racked. Use this as a connectivity probe before list_rack or "
            "route_task. Read-only local state. Does not call downstream MCP servers (not "
            "open-world). Pair with list_rack for the actual catalog."
        ),
        annotations=tool_hints("Get router status", **_RO),
    )
    def status() -> dict:
        return {
            "name": "superagenticmcp",
            "version": "0.2.0",
            "status": "ok",
            "rack_count": len(_RACK),
            "board": "http://localhost:7420 (when running with --board)",
        }

    @mcp.tool(
        name="list_rack",
        title="List racked MCP servers",
        description=(
            "List MCP servers currently mounted on the SuperAgentic rack (name, command or URL, "
            "notes). Use after rack_add to confirm membership. Empty list means no servers have "
            "been registered in this process. Read-only; use rack_add / rack_remove to mutate. "
            "Does not probe remote health."
        ),
        annotations=tool_hints("List racked MCP servers", **_RO),
    )
    def list_rack() -> dict:
        return {"servers": list(_RACK), "count": len(_RACK)}

    @mcp.tool(
        name="rack_add",
        title="Add a server to the rack",
        description=(
            "Register an MCP server on the in-memory rack so later route_task calls can target "
            "it by name. Overwrites an existing entry with the same name (idempotent upsert). "
            "Does not start the child process and does not validate the command. Use list_rack "
            "to inspect and rack_remove to delete. Local write only."
        ),
        annotations=tool_hints("Add a server to the rack", **_RW),
    )
    def rack_add(
        name: Annotated[str, Field(description="Short rack key used by route_task and rack_remove.")],
        command: Annotated[str, Field(description="stdio command or streamable HTTP URL for the child MCP server.")],
        notes: Annotated[str, Field(description="Optional human note describing capabilities.")] = "",
    ) -> dict:
        entry = {"name": name.strip(), "command": command.strip(), "notes": notes}
        _RACK[:] = [s for s in _RACK if s.get("name") != entry["name"]]
        _RACK.append(entry)
        return {"status": "ok", "server": entry, "count": len(_RACK)}

    @mcp.tool(
        name="rack_remove",
        title="Remove a server from the rack",
        description=(
            "Remove one MCP server from the in-memory rack by name. Destructive. Missing names "
            "return an error object rather than raising. Does not stop a running child — only "
            "drops the catalog entry. Use list_rack first to confirm the name."
        ),
        annotations=tool_hints("Remove a server from the rack", **_DEL),
    )
    def rack_remove(
        name: Annotated[str, Field(description="Rack key previously passed to rack_add.")],
    ) -> dict:
        before = len(_RACK)
        _RACK[:] = [s for s in _RACK if s.get("name") != name]
        if len(_RACK) == before:
            return {"error": f"server not on rack: {name}"}
        return {"status": "removed", "name": name, "count": len(_RACK)}

    @mcp.tool(
        name="route_task",
        title="Plan a task against the rack",
        description=(
            "Produce a routing plan for a natural-language task against the current rack. In "
            "this release the planner is a deterministic stub: it lists candidate servers and "
            "does not execute downstream tools. Use after rack_add. Not a substitute for status. "
            "Read-only with respect to the rack; no network calls yet."
        ),
        annotations=tool_hints("Plan a task against the rack", **_RO),
    )
    def route_task(
        task: Annotated[str, Field(description="Natural-language goal to route across racked MCP servers.")],
        preferred_server: Annotated[str, Field(description="Optional rack name to prefer. Empty means first match / all.")] = "",
    ) -> dict:
        names = [s.get("name") for s in _RACK]
        chosen = preferred_server if preferred_server in names else (names[0] if names else None)
        return {
            "task": task,
            "candidates": names,
            "chosen": chosen,
            "executed": False,
            "note": "Planner stub — no downstream MCP calls are issued in this version.",
        }


def main() -> None:
    """Entry point for the `superagenticmcp` console script."""
    if mcp is None:
        raise SystemExit("fastmcp is required. Install with: pip install -e '.[dev]'")
    mcp.run()


if __name__ == "__main__":
    main()
