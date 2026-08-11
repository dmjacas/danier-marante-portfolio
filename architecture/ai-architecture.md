# AI Architecture

> The full AI engineering material lives in the dedicated section [AI Engineering →](../ai/README.md). This page keeps the architecture-level reference and links to the detailed documents.

## Reference architecture

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
- MCP (servers published as npm packages, e.g. `ppm-doc`)
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

## Related documents

- [AI Engineering overview →](../ai/README.md)
- [AI Architecture deep dive →](../ai/architecture.md)
- [MCP case study →](../ai/mcp.md)
- [Process automation →](../ai/automation.md)
- [Embeddings & retrieval →](../ai/embeddings.md)
- [AI agents →](../ai/agents.md)