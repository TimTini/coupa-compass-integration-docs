---
title: "RA Risk Request API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-risk-request-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-risk-request-api"
status_code: 200
fetched_at: "2026-04-09T11:59:29+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "RA Risk Request API"
---

# RA Risk Request API

Use the RA Risk Request API to view and update risk assessment requests between Risk Assess
and Coupa Core.

## Elements

The following elements are available for the RA Risk Request
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | no | no | any | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| state | | no | no | any | | yes | integer |
| cra-risk-type | | no | no | any | | yes | integer |
| cra-risk-id | | no | no | any | | yes | string(255) |
| active | | no | no | any | | yes | boolean |
| created-by | User who created | no | no | any | | yes | |
| updated-by | User who updated | no | no | any | | yes | |
| ra_risk_request_scores | | no | no | any | | yes | |
