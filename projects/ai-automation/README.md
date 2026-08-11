# AI Process Automation — Case Study

## Objective

Automate repetitive engineering and business processes using AI assistants, MCP servers, workflow orchestration and local models — reducing manual steps while keeping sensitive data under control.

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

## Technologies

- MCP (Model Context Protocol) servers published as npm packages
- TypeScript / Node.js for MCP tooling
- n8n for workflow orchestration and integrations
- Ollama for local/self-hosted LLMs
- Cloud LLM providers when capacity or quality is required
- Jira / Git integrations as automation sources

## Example: `ppm-doc` MCP server

An MCP server published as an npm package that connects to Jira and generates development documents (`.md`) for user stories.

- Detects the current Git branch, changed files and open pull requests
- Fetches the user story context from Jira
- Generates structured development documentation automatically

Tools exposed:

- `validate_jira` — verifies Jira connectivity and credentials
- `jira_info` — fetches a user story as structured info
- `ppm_doc` — fetches a user story and writes a development document to `docs/`
- `greet` — registers a user story key for doc generation

This reduces the documentation overhead of development workflows: an AI assistant consumes the MCP tools and produces consistent `.md` docs without manual copy/paste across Jira, Git and local context.

## Design goals

- Automate repetitive work reliably and with clear boundaries
- Keep business rules deterministic and outside prompts
- Run models locally (Ollama) when data must stay private or offline
- Use cloud LLMs only when local models are insufficient
- Expose capabilities as reusable MCP tools / npm packages
- Human approval for high-impact automated actions
- Observability: log every automation run and its outcome