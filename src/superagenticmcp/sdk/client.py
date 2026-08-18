"""Minimal client stub — expands as router HTTP/board lands."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SuperAgenticClient:
    """SDK client for SuperAgenticMCP.

    Alpha: local status helpers only. Remote board/router API will attach here.
    """

    base_url: str = "http://127.0.0.1:7420"

    def status(self) -> dict:
        """Return local package status (no network in alpha)."""
        from superagenticmcp import __version__

        return {
            "name": "superagenticmcp",
            "version": __version__,
            "base_url": self.base_url,
            "note": "Alpha scaffold — remote API not yet wired.",
        }

    def health(self) -> dict:
        """Alias for status during scaffold phase."""
        return {"status": "ok", **self.status()}
