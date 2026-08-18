---
name: routing-capability
description: >-
  Capability-first routing with latency tie-break for racked MCP servers.
  Use when selecting which server handles a tool call.
version: 0.1.0
license: Apache-2.0
tags: [superagenticmcp, routing, mcp, server-os]
---

# Routing / Capability Skill

## Workflow

1. Match required capability tags against the rack.
2. Prefer lowest observed latency among matches.
3. Fall back or skip offline servers with an explicit log line.

## Rules

- Never invent tool results on the production path.
- Keep rack state and `superagentic.json` in sync.
- Document latency class (Core / Research / Dev / Data / Comms).
