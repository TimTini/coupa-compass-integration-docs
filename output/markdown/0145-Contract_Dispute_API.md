---
title: "Contract Dispute API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-dispute-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-dispute-api"
status_code: 200
fetched_at: "2026-04-09T11:59:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Dispute API"
---

# Contract Dispute API

## Elements

The following elements are available for the Contract Dispute API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alternative-dispute-resolution | | no | no | mediation, arbitration, mediation_arbitration | yes | yes | integer |
| jurisdiction-exclusivity | | no | no | not_specified, exclusive, non_exclusive | yes | yes | integer |
| jurisdiction-country | | no | no | any | yes | yes | |
| governing-law-country | | no | no | any | yes | yes | |
| governing-law-subdivision | | no | no | any | yes | yes | |
| jurisdiction-subdivision | | no | no | any | yes | yes | |
| id | Coupa unique identifier | no | no | any | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| contract_type_custom_field_1 | Contract type custom field 1 | no | no | any | yes | yes | string(255) |
| contract_type_custom_field_2 | Contract type custom field 2 | no | no | any | yes | yes | string(255) |
| contract_type_custom_field_3 | Contract type custom field 3 | no | no | any | yes | yes | string(255) |
| contract_type_custom_field_4 | Contract type custom field 4 | no | no | any | yes | yes | string(255) |
| contract_type_custom_field_5 | Contract type custom field 5 | no | no | any | yes | yes | string(255) |
| contract_type_custom_field_6 | | no | no | any | yes | | string(255) |
| contract_type_custom_field_7 | | no | no | any | yes | | string(255) |
| contract_type_custom_field_8 | | no | no | any | yes | | string(255) |
| contract_type_custom_field_9 | | no | no | any | yes | | string(255) |
| contract_type_custom_field_10 | | no | no | any | yes | | string(255) |
