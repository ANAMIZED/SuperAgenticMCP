"""Smoke tests — import and version surface."""

from __future__ import annotations


def test_version():
    import superagenticmcp

    assert superagenticmcp.__version__


def test_server_import():
    from superagenticmcp.server import main

    assert callable(main)


def test_sdk_status():
    from superagenticmcp.sdk import SuperAgenticClient

    client = SuperAgenticClient()
    st = client.status()
    assert st["name"] == "superagenticmcp"
    assert client.health()["status"] == "ok"
