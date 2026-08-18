"""CLI entry for SuperAgenticMCP."""

from __future__ import annotations

import typer
from rich.console import Console

app = typer.Typer(
    name="superagenticmcp-cli",
    help="SuperAgenticMCP CLI — status, board, and rack helpers.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def status() -> None:
    """Print router status."""
    console.print("[bold]SuperAgenticMCP[/bold] v0.1.0 — alpha scaffold")
    console.print("MCP entry: [cyan]superagenticmcp[/cyan]")
    console.print("Hero demo: [cyan]superagenticmcp.html[/cyan]")
    console.print("Board:     not yet wired (target :7420)")


@app.command()
def version() -> None:
    """Print package version."""
    from superagenticmcp import __version__

    console.print(__version__)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
