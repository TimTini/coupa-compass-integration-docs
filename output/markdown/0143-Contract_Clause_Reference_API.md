---
title: "Contract Clause Reference API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-clause-reference-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-clause-reference-api"
status_code: 200
fetched_at: "2026-04-09T11:59:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Clause Reference API"
---

# Contract Clause Reference API

This API supports future functionality.

## Elements

The following elements are available for the Contract Clause Reference API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contract-document-id | | no | no | any | yes | yes | integer |
| contract-clause-id | | no | no | any | yes | yes | integer |
| clause-key | | yes | no | any | yes | yes | integer |
| clause-referrer-location | | no | no | any | yes | yes | string(255) |
| clause-system-used | | no | no | any | yes | yes | string(255) |
| clause-is-modified | | no | no | any | yes | yes | integer |
| clause-content-checksum | | yes | no | any | yes | yes | string(255) |
| current-content-checksum | Current content checksum | no | no | any | yes | yes | string(255) |
| clause-name | | yes | no | any | yes | yes | string(255) |
| clause-description | | yes | no | any | yes | yes | string(255) |
| clause-classification | | yes | no | any | yes | yes | integer |
| clause-risk-score | | no | no | any | yes | yes | integer |
| id | Coupa unique identifier | no | no | any | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| clause_status | Cause Status | No | No | published, inactive | yes | yes | string(255) |
| clause_effective_from | Clause effective from | No | No | any | yes | yes | datetime |
| clause_effective_to | Clause effective to | No | No | any | yes | yes | datetime |
