# MerchantMiles — System Context (C4)

```mermaid
flowchart TD
    BankUser[Private Banking Client] -->|uses| Web[Web Application]
    Merchant[Merchant] -->|manages offers via| Web
    Admin[Platform Administrator] -->|manages campaigns & benefits| AdminApp[Admin Application]

    Web --> MM[MerchantMiles Platform]
    AdminApp --> MM

    MM -->|payments / commerce| External[External Systems]
    MM -->|reporting / data processing| Reporting[Reporting & Data Processing]

    subgraph Banks
        Clubmiles[Clubmiles - Ecuador]
        Promerica[Promerica - Central America]
    end

    MM --> Clubmiles
    MM --> Promerica
```

## Overview

MerchantMiles is a multi-country loyalty platform in production with the private banking divisions of **Clubmiles** and **Promerica** across **Ecuador and Central America**.

Actors:

- **Private banking clients** — discover and redeem benefits and campaigns.
- **Merchants** — launch and manage offers, campaigns and benefits.
- **Platform administrators** — manage merchants, branches, users, benefits, campaigns, catalogues, data processing and reporting.

External systems: financial/commerce integrations. Confidential details are intentionally excluded.