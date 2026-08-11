# MerchantMiles — Containers (C4)

```mermaid
flowchart TD
    subgraph Web[Web & Admin Applications]
        Next[Next.js / React]
    end

    subgraph Api[Application Layer]
        GW[API Gateway]
        Users[Users Service]
        Benefits[Benefits Service]
        Campaigns[Campaigns Service]
        DataProc[Data Processing]
    end

    subgraph Data[Data Store - PostgreSQL]
        PGU[(users DB)]
        PGB[(benefits DB)]
        PGC[(campaigns DB)]
    end

    Next --> GW
    GW --> Users
    GW --> Benefits
    GW --> Campaigns
    Users --> PGU
    Benefits --> PGB
    Campaigns --> PGC
    DataProc -.->|service APIs| Users
    DataProc -.->|service APIs| Benefits
    DataProc -.->|service APIs| Campaigns

    subgraph Cloud[Cloud Platform]
        AWS[AWS managed services]
    end
```

## Notes

- Frontend: React, Next.js, TypeScript.
- Backend: .NET Core 8, REST APIs, microservices behind an **API Gateway**.
- Data: **database per service** — each service owns its PostgreSQL database (see [Data Architecture](../data-architecture.md)).
- Reporting/data processing consume service APIs, not shared tables.
- Deployment: AWS, Docker, CI/CD, Infrastructure as Code.
- Details are architectural; proprietary implementation is excluded.