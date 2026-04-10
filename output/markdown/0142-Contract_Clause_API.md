---
title: "Contract Clause API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-clause-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-clause-api"
status_code: 200
fetched_at: "2026-04-09T11:59:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Clause API"
---

# Contract Clause API

This API supports future functionality.

## Elements

The following elements are available for the Contract Clause API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contract-id | | no | no | any | yes | yes | integer |
| clause-type-id | | no | no | any | yes | yes | integer |
| clause-type-name | Clause type name | no | no | any | yes | yes | |
| contract-clause-reference | | no | no | any | yes | yes | |
| id | Coupa unique identifier | no | no | any | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
