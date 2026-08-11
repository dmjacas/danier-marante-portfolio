# Architecture Decision Records

Architecture decisions recorded to make reasoning visible: each ADR documents Context, Problem, Options Considered, Decision, Rationale, Trade-offs, Consequences and Related Projects.

## Records

| ADR | Decision | Used in |
|---|---|---|
| [ADR-001 — Microservices](ADR-001-microservices.md) | Service boundaries around business capabilities | MerchantMiles |
| [ADR-002 — PostgreSQL](ADR-002-postgresql.md) | PostgreSQL as primary relational platform | MerchantMiles, Chaide, GreenCloud, NeutralBank, Neutralfy |
| [ADR-003 — AWS](ADR-003-aws.md) | AWS as the cloud platform | MerchantMiles, Chaide, GreenCloud |
| [ADR-004 — Embeddings](ADR-004-ai-embeddings.md) | Embeddings + vector search for semantic retrieval | AI Engineering / AI solutions |

## Knowledge network

```text
MerchantMiles
 ├── ADR-001 Microservices
 ├── ADR-002 PostgreSQL
 └── ADR-003 AWS

AI Engineering
 └── ADR-004 AI / Embeddings

Chaide · GreenCloud · NeutralBank · Neutralfy
 └── ADR-002 PostgreSQL (+ ADR-003 where AWS applies)
```

## Related

- [Architecture knowledge base →](../../architecture/README.md)
- [MerchantMiles case study →](../../projects/merchant-miles/README.md)
- [AI Engineering →](../../ai/README.md)