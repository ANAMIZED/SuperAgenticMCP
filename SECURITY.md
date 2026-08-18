# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | Yes       |

## Reporting a vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Report responsibly via a private GitHub security advisory.

Include description, reproduction steps, and impact (capability bypass, budget
bypass, credential leak, arbitrary tool execution).

## Security model

- Racked servers and tools are capability-matched — no ambient authority
- Call budgets and allow-lists are guardrails (must not be removed casually)
- Secrets never belong in source or the hero HTML
- Fail closed on offline or unauthorized tool paths
- Hero demo is simulation only; production path must not invent tool results
