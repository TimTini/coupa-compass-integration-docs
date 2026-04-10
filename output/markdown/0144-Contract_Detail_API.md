---
title: "Contract Detail API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-detail-api-da-5867-da-5867"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-detail-api-da-5867-da-5867"
status_code: 200
fetched_at: "2026-04-09T11:59:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Detail API"
---

# Contract Detail API

## Elements

The following elements are available for the Contract Detail API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contract_country | Contract Country | no | | | yes | yes | Country |
| contract-type-custom-field-1 | Contract type custom field 1 | | | | yes | yes | string(255) |
| contract-type-custom-field-10 | Contract type custom field 10 | | | | yes | yes | string(255) |
| contract-type-custom-field-2 | Contract type custom field 2 | | | | yes | yes | string(255) |
| contract-type-custom-field-3 | Contract type custom field 3 | | | | yes | yes | string(255) |
| contract-type-custom-field-4 | Contract type custom field 4 | | | | yes | yes | string(255) |
| contract-type-custom-field-5 | Contract type custom field 5 | | | | yes | yes | string(255) |
| contract-type-custom-field-6 | Contract type custom field 6 | | | | yes | yes | string(255) |
| contract-type-custom-field-7 | Contract type custom field 7 | | | | yes | yes | string(255) |
| contract-type-custom-field-8 | Contract type custom field 8 | | | | yes | yes | string(255) |
| contract-type-custom-field-9 | Contract type custom field 9 | | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| external_object_name | External object name | no | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| notice-methods | Notice methods | | | | yes | yes | string(255) |
| skip_archival | | | | | yes | yes | boolean |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| commodity | Commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
