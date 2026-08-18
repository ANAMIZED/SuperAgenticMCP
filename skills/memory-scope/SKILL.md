---
name: memory-scope
description: >-
  Memory-scope constellation: persist run artifacts as a linked graph for
  later retrieval and board visualization.
version: 0.1.0
license: Apache-2.0
tags: [superagenticmcp, memory, observability, server-os]
---

# Memory Scope Skill

## Workflow

1. On run complete, file receipt + key artifacts into the scope graph.
2. Link nodes by mission, server, and capability.
3. Surface on the board memory constellation.

## Rules

- Preserve provenance and timestamps on every node.
- Do not drop failed runs — file them with status=failed.
