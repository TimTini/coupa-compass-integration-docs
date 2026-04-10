---
title: "Contract Party API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-party-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-party-api"
status_code: 200
fetched_at: "2026-04-09T11:59:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Party API"
---

# Contract Party API

## Elements

The following elements are available for the Contract Party API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bill-to-address | Bill to Address | | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| business-entity | Business entity | yes | | | yes | yes | [BusinessEntity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/business-entities-api-(business_entities)) |
| business-name | Business Name | | | | yes | yes | string(255) |
| clma-id | CLM Advanced Counterparty Identifier | | | | yes | yes | integer |
| contact-name | Contact Name | | | | yes | yes | string(255) |
| contact-title | Contact Title | | | | yes | yes | string(255) |
| contract-party-contacts | Contract party contacts | | | | yes | yes | [ContractPartyContact](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-party-contact-api) |
| contract-party-role | Contract party role | | | | yes | yes | ContractPartyRole |
| counterparty-role | Counterparty Role | | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| email | Email | | | | yes | yes | string(255) |
| entity-name | Entity Name | yes | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| legal_entity | Legal entity in your corporate group | | | | yes | yes | string(255) |
| mail-to-address | Mail to Address | | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| party-alias | Party alias | | | | yes | yes | string(255) |
| party-directionality | Party directionality | | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
