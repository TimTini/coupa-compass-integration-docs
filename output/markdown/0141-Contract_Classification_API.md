---
title: "Contract Classification API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-classification-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-classification-api"
status_code: 200
fetched_at: "2026-04-09T11:59:34+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Classification API"
---

# Contract Classification API

## Elements

The following elements are available for the Contract Classification API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | | | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| name | Name | | | | | yes | string(255) |
| contract-classification | Contract classification | | | | yes | yes | any |
