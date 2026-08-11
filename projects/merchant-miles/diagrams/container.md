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

    subgraph Data[Data Store]
        PG[(PostgreSQL)]
    end

    Next --> GW
    GW --> Users
    GW --> Benefits
    GW --> Campaigns
    Users --> PG
    Benefits --> PG
    Campaigns --> PG
    DataProc -.-> PG

    subgraph Cloud[Cloud Platform]
        AWS[AWS managed services]
    end
```

## Notes

- Frontend: React, Next.js, TypeScript.
- Backend: .NET Core 8, REST APIs, microservices behind an **API Gateway**.
- Data: PostgreSQL (transactional).
- Deployment: AWS, Docker, CI/CD, Infrastructure as Code.
- Details are architectural; proprietary implementation is excluded.