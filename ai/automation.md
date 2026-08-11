# Process Automation

## Goal

Automate repetitive engineering and business processes with AI while keeping sensitive data under control and business rules deterministic.

## Approach

```text
Trigger (Jira / webhook / schedule)
        │
        ▼
Workflow Orchestration (n8n)
        │
        ├──────────────► AI Assistant / Agent
        │                     │
        │                     ├──────────────► MCP Tools / npm packages
        │                     │
        │                     └──────────────► LLM Provider
        │
        └──────────────► Local Models (Ollama)   [privacy / offline]
                              │
                              ▼
                          Output / Document / Action
```

## Components

### n8n — orchestration

n8n coordinates workflows, triggers and integrations across tools: Jira, Git, CRMs, webhooks, schedules. It routes the flow, connects to sources and executes the automation.

### MCP servers / npm packages — reusable tooling

MCP servers packaged as npm packages expose reusable capabilities to AI assistants. `ppm-doc` connects to Jira and generates development documents from user stories. See the [MCP case study](mcp.md).

### Ollama — local models

Ollama serves models locally when data must stay private, offline or cost-sensitive. Cloud LLMs (e.g. Amazon Bedrock) handle workloads that exceed local capacity.

## Design goals

- Automate repetitive work reliably and with clear boundaries.
- Keep business rules deterministic and outside prompts.
- Run models locally when data must stay private; use cloud only when needed.
- Expose capabilities as reusable MCP tools / npm packages.
- Human approval for high-impact automated actions.
- Observability: log every automation run and its outcome.