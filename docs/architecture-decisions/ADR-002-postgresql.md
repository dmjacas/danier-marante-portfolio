# ADR-002 — PostgreSQL

## Status

Accepted

## Context

Core business workloads require transactional consistency, relational modeling and mature SQL capabilities.

## Problem

Which primary data platform to use for transactional business data — including the loyalty, e-commerce and banking platforms in this portfolio.

## Options Considered

### Option 1 — NoSQL document store

- Pros: flexible schemas, horizontal scaling.
- Cons: weak multi-record transactional guarantees; relational reporting and joins become application responsibility.

### Option 2 — MySQL/other relational

- Pros: mature relational model.
- Cons: acceptable; PostgreSQL chosen where advanced extensions (e.g. vector search) or richer features provide advantage.

### Option 3 — PostgreSQL

- Pros: strong transactional guarantees, mature indexing and SQL, rich extension ecosystem (e.g. vector search).
- Cons: operational concerns include backups, migrations, connection management and query performance.

## Decision

Use PostgreSQL as the primary relational data platform where transactional relational workloads are required.

## Rationale

PostgreSQL provides a balance of transactional integrity, mature SQL, operational ecosystem and extensibility (including vector-search workloads relevant to AI features).

## Trade-offs

### Advantages

- Strong transactional guarantees
- Mature indexing and SQL
- Good ecosystem
- Extensions available for advanced workloads such as vector search

### Disadvantages

- Requires disciplined migrations and connection management
- Horizontal scalability requires additional patterns (replicas, sharding, partitioning)

## Consequences

- Backups, migrations, connection management and query performance are documented operational concerns.
- Where semantic retrieval is needed, PostgreSQL/vector extensions can serve before a dedicated vector store is justified (see ADR-004).

## Related Projects

- MerchantMiles
- Chaide (e-commerce)
- GreenCloud, NeutralBank, Neutralfy

## Related ADRs

- [ADR-004 — Embeddings](./ADR-004-ai-embeddings.md)