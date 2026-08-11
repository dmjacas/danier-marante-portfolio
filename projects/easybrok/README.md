# EasyBrok — Insurance Sales Management (in production)

## Overview

**EasyBrok** is a tool for the management of insurance sales, used in production to streamline the sales process and related operations. It is part of an insurance-sector family of solutions that includes **EasyRoute** and **SegurosYa**.

> This product is live in production. Proprietary source code, credentials, private endpoints and confidential customer information are intentionally excluded.

## Technologies

- AngularJS (frontend)
- Laravel (backend)
- REST APIs
- MySQL / relational database
- Insurance sales workflows

## Engineering concerns

### Performance

Fast responses for sales and quote processes.

### Security

Access control and protection of client and policy data.

### Reliability

Robust handling of sales states and external integrations.

### Observability

Logging and monitoring to diagnose production issues.

## Architectural lessons

- Keep sales rules clear and deterministic.
- Isolate integrations with insurers and external systems behind contracts.
- Track sales states explicitly.
- Document important decisions with ADRs.