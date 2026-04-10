---
title: "RA Risk Request Relationship API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-risk-request-relationship-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-risk-request-relationship-api"
status_code: 200
fetched_at: "2026-04-09T11:59:29+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "RA Risk Request Relationship API"
---

# RA Risk Request Relationship API

Use the RA Risk Request Relationship API to view and update risk assessment relationship
requests between Risk Assess and Coupa Core.

## Elements

The following elements are available for the RA Risk Request
Relationship API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | no | no | any | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| riskable-id | | yes | no | any | | yes | integer |
| riskable-type | | yes | no | any | | yes | integer |
| external-riskable-id | | yes | no | any | | yes | integer |
| external-riskable-type | | yes | no | any | | yes | integer |
| active | | no | no | any | | yes | boolean |
| created-by | User who created | no | no | any | | yes | |
| updated-by | User who updated | no | no | any | | yes | |
