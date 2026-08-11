# MerchantMiles Data Architecture

## Database Strategy

**Database per service.** Each microservice owns its PostgreSQL database. No shared database across services.

```text
Users Service      → PostgreSQL (users DB)
Benefits Service   → PostgreSQL (benefits DB)
Campaigns Service  → PostgreSQL (campaigns DB)
```

> Validated with the project owner (V4). If additional services exist (e.g. merchants, reporting), each follows the same ownership model.

## Service Ownership

Each service is the only writer of its database. Other services access data only through the owning service's API.

## Schema Strategy

Databases are isolated per service. Cross-service data access happens via API contracts, not via shared tables.

## Data Isolation

Isolation is enforced at the **service boundary** (each service owns its data) rather than by database-level tenant constructs.

## Transactions

Transactions are scoped within a service's own database. Cross-service consistency relies on API orchestration and, where needed, asynchronous processing rather than distributed transactions.

## Consistency

- Strong consistency within a service's local transaction.
- Cross-service consistency is eventual or orchestrated at the application layer.

## Reporting

Reporting and data-processing workloads do not read directly across service databases; they use the owning services' APIs (or a dedicated reporting path) to avoid coupling.

## Data Processing

Data processing and reporting are capabilities of the platform; they consume service APIs to build catalogues, reports and processed datasets.

## Trade-offs

- **Database per service** gives clear ownership and independent evolution, at the cost of cross-service queries and the need for API-based access.
- Avoiding shared databases reduces coupling but increases orchestration complexity for cross-service flows.
- Strong local consistency with orchestrated/eventual cross-service consistency is simpler to operate than distributed transactions.

## Lessons Learned

- Define business boundaries before defining database ownership.
- A service must own its data to remain independently deployable.
- Reporting is a consumer of service APIs, not a free reader of every table.
- Avoid sharing databases indiscriminately (see [ADR-001](../../docs/architecture-decisions/ADR-001-microservices.md)).

## Related

- [MerchantMiles case study →](README.md)
- [ADR-001 — Microservices →](../../docs/architecture-decisions/ADR-001-microservices.md)
- [ADR-002 — PostgreSQL →](../../docs/architecture-decisions/ADR-002-postgresql.md)