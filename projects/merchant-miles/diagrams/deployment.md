# MerchantMiles — Deployment

Only infrastructure that can be published is shown. Specific account, region and configuration details are intentionally excluded.

```mermaid
flowchart LR
    subgraph Public
        CDN[CDN / Edge]
    end
    subgraph AWS[Cloud Platform - AWS]
        Web[Web Application - containers]
        GW[API Gateway]
        Srv[Services]
        DB[(Managed Database - PostgreSQL)]
        Storage[Object Storage]
        IAM[IAM / Auth]
    end

    CDN --> Web
    Web --> GW
    GW --> Srv
    Srv --> DB
    Srv --> Storage
    IAM -. auth .-> Web
    IAM -. auth .-> GW
```

## Principles

- Managed services where they reduce operational burden.
- Infrastructure as Code for reproducibility and reviewable change.
- Least-privilege IAM.
- CI/CD with rollback path.
- Backups and monitoring are operational requirements (see [Reliability](../reliability.md)).