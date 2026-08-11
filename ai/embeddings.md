# Embeddings & Retrieval

## Problem

Keyword search is insufficient for semantic recommendation and retrieval use cases (finding content by meaning rather than by exact term).

## Approach

Represent relevant content as embeddings and perform vector similarity search, optionally combined with structured filters.

```text
Content
  ↓
Embedding Service
  ↓
Vector Store
  ↓
Similarity Search / RAG
  ↓
Context for LLM
```

## Experience

- Embedding models with managed LLM platforms such as Amazon Bedrock.
- Vector stores: managed options and PostgreSQL/vector extensions (see ADR-002 and ADR-004).
- Retrieval-Augmented Generation (RAG) to give the model bounded, relevant context.
- Versioning and evaluation of embedding models and datasets.

## Risks

- Embedding model changes can alter retrieval results without obvious code changes.
- Vector indexes require maintenance.
- Retrieval quality requires evaluation.
- Embeddings may encode sensitive semantic information.

## Mitigations

- Version embedding models and datasets.
- Evaluate retrieval quality on a defined set of questions.
- Apply appropriate access controls to source content and vector data.
- Provide deterministic fallbacks for critical operations.