# ADR-004 — Embeddings for Semantic Retrieval

## Status

Accepted

## Context

Keyword search is insufficient for some semantic recommendation and retrieval use cases.

## Decision

Represent relevant content as embeddings and perform vector similarity search.

## Consequences

### Positive

- Semantic similarity
- Better contextual retrieval
- Useful for recommendation and RAG

### Risks

- Embedding model changes can affect results
- Vector indexes require maintenance
- Quality requires evaluation
- Embeddings may contain sensitive semantic information

## Mitigation

Version embedding models and datasets, evaluate retrieval quality and apply appropriate access controls.
