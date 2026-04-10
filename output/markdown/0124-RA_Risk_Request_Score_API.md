---
title: "RA Risk Request Score API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-risk-request-score-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-risk-request-score-api"
status_code: 200
fetched_at: "2026-04-09T11:59:30+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "RA Risk Request Score API"
---

# RA Risk Request Score API

Use the RA Risk Request Score API to view and update risk assessment score requests between
Risk Assess and Coupa Core.

## Elements

The following elements are available for the RA Risk Request
Score API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | no | no | any | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| cra-score-risk-type | | yes | no | any | | yes | integer |
| risk-score | | no | no | any | | yes | decimal(5,2) |
| risk-value | | no | no | any | | yes | string(255) |
| ra-risk-request-id | | no | no | any | | yes | integer |
| created-by | User who created | no | no | any | | yes | |
| updated-by | User who updated | no | no | any | | yes | |
