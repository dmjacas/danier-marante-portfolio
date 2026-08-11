# Cloud Architecture

## Reference AWS Architecture

```text
                         Internet
                            │
                            ▼
                     ┌─────────────┐
                     │ CloudFront  │
                     └──────┬──────┘
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ▼                           ▼
          S3 / Frontend              API Gateway
                                          │
                                          ▼
                                   Application Layer
                                          │
                           ┌──────────────┼──────────────┐
                           ▼              ▼              ▼
                        Lambda       Containers      Services
                           │              │              │
                           └──────────────┼──────────────┘
                                          ▼
                                     PostgreSQL
```

## Principles

- Managed services where they reduce operational burden
- Least-privilege IAM
- Secrets stored outside source code
- Infrastructure as Code
- Automated deployments
- Centralized monitoring and logging
- Encryption in transit and at rest
- Backups and disaster recovery
- Cost visibility

## Infrastructure as Code

Terraform can be used to define:

- Networking
- IAM
- Compute
- Storage
- Databases
- CDN
- Serverless infrastructure
- Monitoring
