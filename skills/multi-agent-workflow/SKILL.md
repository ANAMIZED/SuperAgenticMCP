---
name: multi-agent-workflow
description: >-
  Planner → workers → critic loop for SuperAgenticMCP missions.
  Use when coordinating multi-step agent work across racked MCP servers.
version: 0.1.0
license: Apache-2.0
tags: [superagenticmcp, multi-agent, orchestration, server-os]
---

# Multi-Agent Workflow Skill

## Workflow

1. Planner decomposes the order into steps with capability requirements.
2. Workers execute in parallel where the DAG allows.
3. Critic validates before shipping the receipt.

## Rules

- Respect per-run call budgets and per-server allow-lists.
- Emit JSONL for every step (board + memory scope).
- Fail closed if a required capability is offline.
