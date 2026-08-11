# MCP Case Study

## Overview

Model Context Protocol (MCP) servers expose capabilities to AI assistants as a set of clearly defined tools. I build and publish MCP servers as **npm packages** so assistants can consume real systems (Jira, Git) in a safe and structured way.

## Flow

```text
Jira
  ↓
MCP Server (npm package)
  ↓
AI Model
  ↓
Requirements / User Story
  ↓
Technical Documentation (.md)
  ↓
Input to Development Workflow
```

## `ppm-doc` — MCP server published on npm

`ppm-doc` is an MCP server (npm package) that connects to Jira and generates development documents (`.md`) for user stories.

Capabilities (as documented for the package):

- Detects the current Git branch, changed files and open pull requests.
- Fetches the user story context from Jira.
- Generates structured development documentation automatically.

Tools exposed:

- `validate_jira` — verifies Jira connectivity and credentials.
- `jira_info` — fetches a user story as structured info.
- `ppm_doc` — fetches a user story and writes a development document to `docs/`.
- `greet` — registers a user story key for doc generation.

Value: reduces the documentation overhead of development workflows — an AI assistant consumes the MCP tools and produces consistent `.md` docs without manual copy/paste across Jira, Git and local context.

> Referenced behavior matches the package's public documentation (npm `ppm-doc` v1.3.1). No additional functionality is claimed.

## Design principles

- Expose capabilities as discrete, validated tools.
- Keep credentials configurable via environment variables.
- Deterministic steps stay in code; the model orchestrates, not decides business logic.
- Provide fallbacks when external systems are unavailable.
- Observed runs are logged for auditability.