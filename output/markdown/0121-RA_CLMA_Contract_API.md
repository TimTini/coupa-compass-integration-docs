---
title: "RA CLMA Contract API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-clma-contract-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/ra-clma-contract-api"
status_code: 200
fetched_at: "2026-04-09T11:59:29+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "RA CLMA Contract API"
---

# RA CLMA Contract API

Use the RA CLMA Contract API to view and update contracts between Risk Assess and CLMA.

## Elements

The following elements are available for the RA CLMA
Contract API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| non-disclosure-copying-restriction | | no | no | any | yes | yes | integer |
| permitted-disclosees-directors-officers | | no | no | any | yes | yes | boolean |
| permitted-disclosees-employees | | no | no | any | yes | yes | boolean |
| permitted-disclosees-advisers | | no | no | any | yes | yes | boolean |
| permitted-disclosees-contractors | | no | no | any | yes | yes | boolean |
| id | Coupa unique identifier | no | no | any | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
