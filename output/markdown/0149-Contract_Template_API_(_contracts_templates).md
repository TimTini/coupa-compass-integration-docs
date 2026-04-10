---
title: "Contract Template API (/contracts/templates)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-template-api-(contractstemplates)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-template-api-(contractstemplates)"
status_code: 200
fetched_at: "2026-04-09T11:59:36+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Template API (/contracts/templates)"
---

# Contract Template API (/contracts/templates)

In support of [Contract Template Management](https://compass.coupa.com/x297495.xml) you can now restrict access to contract templates by
assigning a contract template to a content group. The Contract
Template API allows your system to get them.

The URL to access contract templates
is: `https:///api/contracts/templates`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Contract Template API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/contracts/templates` | index | Query contract templates |
| GET | `/api/contracts/templates/:id` | show | Show contract template |

## Elements

The following elements are available for the Contract
Template API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Is Template Active | no | no | any | yes | yes | boolean |
| authoring-method | Authoring Method | | | msword,<br>msword_and_online | yes | yes | string(255) |
| content-groups | Business Groups | | | yes | yes | [Content Groups](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) | |
| contract-classification | Contract classification | | | | yes | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | yes | datetime | | | | |
| created-by | User who created | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) | |
| description | Description | | | yes | yes | string(255) | |
| fill-with-counterparty | Fill with Counterparty | | | | yes | yes | boolean |
| hierarchy-type | Hierarchy Type | | | | yes | string(255) | |
| id | Coupa unique identifier | | | yes | integer | | |
| name | Name | yes | | | yes | yes | string(255) |
| template-generator-id | Template Generator ID | yes | | | | yes | string(1024) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | yes | datetime | | | | |
| updated-by | User who updated | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) | |
| template_generator_type | Template Generator Typetemplate_generator_type | | | | yes | integer | |
| supporting_document | Supporting Documentsupporting_document | | | | yes | boolean | |
| source | Identifier for Contract Template Source | | | | yes | | string(255) |
| contract_types | Contract Types | | | | yes | yes | [Contract Types](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-types-api) |
| contract_hierarchy_types | Contract Hierarchy Types | | | | yes | yes | ContractHierarchyType |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
