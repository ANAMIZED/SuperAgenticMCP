# SuperAgenticMCP — Universal Agentic MCP Server

**The production operating system for Agentic AI.**

100% open source • Model Context Protocol (MCP) compliant • Self-optimizing multi-arm bandit + Contextual NeuralUCB routing • Meta Agent + A2A Swarm Agents • Native Agentic Commerce (x402 / AP2 / ACP / UCP / MPP) • Multilingual • Mobile-first PWA dashboard • Local-first or cloud-scale.

Any MCP host (Claude Desktop, Cursor, Windsurf, custom agents, etc.) connects once and instantly gains superpowers.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](docker-compose.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)]()

## ✨ Features

- **Official MCP Server** – Built on Anthropic’s `mcp[cli]` SDK (FastMCP). Supports stdio, HTTP/SSE, WebSocket.
- **Self-Learning Routing Engine** – Multi-arm bandit (cost × quality × latency) + Thompson Sampling over OpenRouter models. Online Bayesian updates after every invocation.
- **Compute Contextual Neural Bandit** – Real-time arbitrage across GPU providers (Groq, Together, Fireworks, local Ollama, Bedrock, etc.) using NeuralUCB.
- **Meta Agent & Swarm Agents** – Hierarchical orchestration + decentralized A2A-compatible swarms with Redis blackboard.
- **Agentic Commerce Stack** – Native x402 Payment Required, AP2, ACP, UCP, MPP. Crypto-first (USDC, stablecoins) with <2s settlement.
- **Dynamic SKILL.MD Loader** – Auto-discovers and registers thousands of Anthropic-style skills from `./skills/`.
- **Multilingual** – NLLB-powered translation layer (any → any language).
- **Mobile-Ready** – Full PWA dashboard at `/dashboard` with live bandit metrics, swarm status, and one-click x402 demo.
- **Local-first & Cloud-scale** – One-command Docker compose or Helm/Kubernetes/Cloudflare ready.
- **Observability** – Redis + PostgreSQL telemetry for bandit feedback loop and audit logs.



