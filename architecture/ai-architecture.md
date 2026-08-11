# AI Architecture

## Enterprise AI Reference Architecture

```text
                         User / Application
                                │
                                ▼
                         AI Application
                                │
                     ┌──────────┴──────────┐
                     │                     │
                     ▼                     ▼
                 LLM / Bedrock       Retrieval Layer
                                           │
                              ┌────────────┴────────────┐
                              ▼                         ▼
                         Embeddings                Vector Store
                              │                         │
                              └────────────┬────────────┘
                                           ▼
                                    Context / RAG
                                           │
                                           ▼
                                        LLM
                                           │
                                           ▼
                                      Response
```

## Components

- Amazon Bedrock
- Embedding models
- Vector databases
- Retrieval-Augmented Generation
- Prompt engineering
- AI agents
- MCP
- MCP servers published as npm packages
- n8n workflow orchestration
- Ollama (local / self-hosted LLMs)
- Tool calling
- Guardrails
- Observability

## AI engineering principles

1. Keep business rules outside prompts whenever possible.
2. Validate model output.
3. Treat LLMs as probabilistic components.
4. Protect sensitive information.
5. Measure quality and latency.
6. Control token and infrastructure cost.
7. Provide deterministic fallbacks for critical operations.

## Process automation

AI can automate engineering and business processes when orchestrated correctly:

- n8n coordinates workflows, triggers and integrations across tools (Jira, Git, CRMs, webhooks, schedules).
- MCP servers packaged as npm packages expose reusable capabilities to AI assistants (e.g. `ppm-doc` generates development docs from Jira user stories).
- Ollama serves models locally when data must stay private, offline or cost-sensitive; cloud LLMs handle workloads that exceed local capacity.
- Exposed tools must have clear contracts, validation and observability so automated runs remain safe and auditable.
