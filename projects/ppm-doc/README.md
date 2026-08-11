# ppm-doc — MCP Server Case Study

## Executive Summary

`ppm-doc` is an MCP (Model Context Protocol) server published as an npm package. It connects an AI assistant to Jira and the current Git repository, and generates structured development documents (Markdown) for user stories. It reduces the manual overhead of documentation in development workflows.

## Business Problem

Development teams spend significant time producing consistent development documentation for each user story, gathering context across Jira, the current Git branch, changed files and open pull requests. This work is repetitive, error-prone and does not scale as the number of stories grows.

## Solution

An MCP server that gives an AI assistant direct, governed access to Jira and Git context, so the assistant can generate consistent `.md` development documents automatically.

Workflow:

```text
AI Assistant
        │  consumes MCP tools
        ▼
ppm-doc (MCP server, npm package)
        │
        ├──────────────► Git branch / changed files / open PRs
        │
        └──────────────► Jira (user story context)
                │
                ▼
        Development document (.md) written to docs/
```

## My Role

- **Leadership** — defined the automation boundary: what the assistant may do and what stays human.
- **Architecture** — designed the MCP server structure, tool contracts and Jira/Git integration.
- **Engineering** — implemented and published the npm package with the MCP tools.

## Architecture

### Components

- **MCP server** — exposes capabilities as MCP tools; run as a local/remote server consumed by AI assistants (see [AI / MCP reference →](../../diagrams/README.md#available-diagram-files)).
- **Git integration** — detects the current branch, changed files and open pull requests.
- **Jira integration** — fetches user story context.

### Design intent

- Business rules are deterministic and kept outside prompts.
- The assistant only consumes validated context (Jira stories + Git state), not unverified claims.
- Output is written as Markdown documents to a known location (`docs/`).

## Technology

- MCP (Model Context Protocol), TypeScript / Node.js, npm
- Jira API integration
- Git CLI integration
- Markdown (`.md`) document generation

## Integrations

- Jira (user story context)
- Git (branch, diffs, pull requests)
- Local filesystem (document output)

## Key Decisions

| Decision | Context | Rationale |
|---|---|---|
| MCP server published as npm package | Assistants (Claude, opencode, etc.) consume tools via MCP | Reusable, versioned, standard tool contract without bespoke integration |
| Deterministic rules outside prompts | Prompt-only behavior is unpredictable | Business logic stays reviewable and testable |
| Git context + Jira context combined at the tool level | Documentation needs both sources | The tool returns a complete, consistent document, not fragments |

## Trade-offs

- **Standardized document output over free-form writing** — consistency wins for reviewability; creative writing remains human.
- **Fixed tool set over open-ended agent autonomy** — the assistant can do only what the tools allow; high-impact actions still require human approval.

## Security

- Credentials for Jira are configuration/secrets managed outside the repository.
- The server operates on the local repository and confirmed Jira context — no broad access is granted.
- Least-privilege scope: the assistant can read story context and write documents, nothing more.

## Scalability

- The MCP server is a thin integration layer; scaling is horizontal by adding the package to more environments.
- Document generation scales with assistant usage, not with manual effort.

## Reliability

**Implemented**:

- Validation tool (`validate_jira`) checks connectivity and credentials before any job runs.
- Tool results are structured and verifiable.

**Recommended**:

- Retry/backoff on transient Jira or Git failures `[Metric to validate]`.
- Observability for generation runs (success/failure) `[Metric to validate]`.

## Results

### Implementation

- `ppm-doc` published as an npm MCP server that generates development documents for Jira user stories using Git context.

### Outcome

- Development documentation is produced by the AI assistant through MCP tools instead of manual copy/paste across Jira, Git and local context.

### Result

> Quantitative impact (documents generated, time saved) is `[Metric to validate]` — see [metrics inventory →](../../docs/metrics-inventory.md).

## Lessons Learned

- A narrow, well-scoped MCP toolset is more reliable than open-ended agent autonomy.
- Validating the source (Jira connectivity, credentials) before generating avoids garbage documents.
- Publishing MCP servers as npm packages makes the automation portable across environments.

---

## Related

- [AI Process Automation →](../ai-automation/README.md)
- [MCP architecture →](../../ai/mcp.md)
- [AI / MCP reference diagram →](../../diagrams/README.md#available-diagram-files)
- [Metrics inventory →](../../docs/metrics-inventory.md)