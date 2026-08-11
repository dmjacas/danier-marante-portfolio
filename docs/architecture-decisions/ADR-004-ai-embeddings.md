# ADR-004 — Embeddings for Semantic Retrieval

## Status

Accepted

## Context

Keyword search is insufficient for some semantic recommendation and retrieval use cases. AI features need the ability to find content by meaning rather than by exact terms.

## Problem

How to enable semantic retrieval and recommendations in a way that is maintainable and evaluable.

## Options Considered

### Option 1 — Keyword/full-text search only

- Pros: simple, deterministic, no new infrastructure.
- Cons: poor at synonyms, intent and cross-language meaning.

### Option 2 — Embeddings + vector search

- Pros: semantic similarity, better contextual retrieval, useful for recommendation and RAG.
- Cons: embedding model changes can affect results; vector indexes require maintenance; quality requires evaluation; embeddings may contain sensitive semantic information.

### Option 3 — Hybrid (keyword + vector)

- Pros: combines deterministic matching with semantic retrieval.
- Cons: more components to operate and tune.

## Decision

Represent relevant content as embeddings and perform vector similarity search, optionally combined with structured filters or hybrid retrieval.

## Rationale

Semantic capture cannot be achieved with keyword search alone; embeddings enable retrieval by meaning and power RAG and recommendations.

## Trade-offs

### Advantages

- Semantic similarity
- Better contextual retrieval
- Useful for recommendation and RAG

### Disadvantages / Risks

- Embedding model changes can affect results
- Vector indexes require maintenance
- Quality requires evaluation
- Embeddings may contain sensitive semantic information

## Consequences

- Versioning of embedding models and datasets is required.
- Retrieval quality is evaluated against a defined set of queries.
- Access controls apply to source content and vector data.

## Mitigation

Version embedding models and datasets, evaluate retrieval quality and apply appropriate access controls.

## Related Projects

- AI solutions / AI architecture
- Enterprise AI capabilities in this portfolio

## Related ADRs

- [ADR-002 — PostgreSQL](./ADR-002-postgresql.md)