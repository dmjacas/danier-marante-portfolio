# AI Architecture

## Goal

Design enterprise AI capabilities that can be integrated into existing applications without coupling business logic to a single LLM provider.

## Reference architecture

```text
Application
    │
    ▼
AI Orchestrator
    │
    ├──────────────► Prompt / Policy Layer
    │
    ├──────────────► Embedding Service
    │                     │
    │                     ▼
    │                Vector Store
    │
    ├──────────────► LLM Provider
    │
    └──────────────► Tools / MCP / APIs
```

## Production experience

This section covers architecture patterns used in working software.

- Provider abstraction so business logic is not pinned to one LLM provider.
- Embeddings and vector search for semantic retrieval on application content.
- MCP servers exposed to AI assistants as reusable tools.
- Workflow orchestration (n8n) that connects triggers, integrations and AI steps.
- Local models (Ollama) where data privacy or cost requires self-hosting, and cloud LLMs when capacity or quality wins.
- Deterministic business rules kept outside prompts and enforced in application code.
- Human approval for high-impact automated actions.

## Experiments / Proof of Concept

This section covers experimentation work that is not necessarily in production.

- Prompt engineering and evaluation techniques across models.
- Prototype agents and tool-calling flows.

Classification: production vs PoC was verified against documented project material. Anything not confirmed is marked `[TBD]`.

## Design goals

- Provider abstraction
- Secure data handling
- Evaluation and monitoring
- Cost control
- Deterministic business rules
- Human approval for high-impact actions