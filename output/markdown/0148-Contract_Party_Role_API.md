---
title: "Contract Party Role API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-party-role-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-party-role-api"
status_code: 200
fetched_at: "2026-04-09T11:59:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Party Role API"
---

# Contract Party Role API

## Elements

The following elements are available for the Contract Party Role API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | | yes | yes | boolean |
| contract-classification-ids | Contract classification ids | | | | yes | | [] |
| contract-classifications | Contract classifications | yes | | | | yes | ContractClassification |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Description | | | | yes | yes | string(500) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | Name | yes | yes | | yes | yes | string(50) |
| role-directionality | Role directionality | yes | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
