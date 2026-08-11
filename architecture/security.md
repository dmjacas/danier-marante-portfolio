# Security Architecture

## Authentication

Typical enterprise architecture:

```text
Client
  │
  ▼
Identity Provider
  │
  │ Access Token
  ▼
API Gateway
  │
  ▼
Backend Services
```

## Controls

- OAuth 2.0 / OpenID Connect
- JWT validation
- Role-based authorization
- Least-privilege IAM
- HTTPS/TLS
- Secure HTTP headers
- CORS configuration
- Input validation
- Rate limiting
- Secret management
- Audit logging

## Security principle

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to do?

Both should be explicitly enforced at the appropriate architectural boundaries.
