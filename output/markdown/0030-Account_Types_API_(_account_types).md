---
title: "Account Types API (/account_types)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)"
status_code: 200
fetched_at: "2026-04-09T11:59:07+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Account Types API (/account_types)"
---

# Account Types API (/account_types)

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/account_types/:id/copy` | copy | Copy/Clone existing chart of accounts |
| POST | `/api/account_types` | create | Create chart of accounts |
| GET | `/api/account_types` | index | Query chart of accounts |
| GET | `/api/account_types/:id` | show | Show chart of accounts |

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A false value will inactivate the chart of account making it no longer available to users. A true value will make it active and available to users. | yes | yes | boolean | | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| id | Coupa unique identifier | | | | | yes | integer |
| legal-entity-name | Legal entity or entities that are associated with this chart of accounts | | | | | yes | string |
| name | name | yes | yes | | yes | yes | string(50) |
| primary-address | Primary Address | | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| primary-contact | Primary Contact | | | | yes | yes | Contact |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-groups-api) |
| dynamic_flag | Boolean value for determing if account type is dynamic | | | | | yes | boolean |
