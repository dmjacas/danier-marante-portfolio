# ADR-002 — PostgreSQL

## Status

Accepted

## Context

Core business workloads require transactional consistency, relational modeling and mature SQL capabilities.

## Decision

Use PostgreSQL as a primary relational data platform where transactional relational workloads are required.

## Consequences

- Strong transactional guarantees
- Mature indexing and SQL
- Good ecosystem
- Extensions available for advanced workloads such as vector search

Operational concerns include backups, migrations, connection management and query performance.
