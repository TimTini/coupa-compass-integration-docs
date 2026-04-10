---
title: "Financial Counterparties API (/financial_counterparties)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/financial-counterparties-api-(financial_counterparties)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/financial-counterparties-api-(financial_counterparties)"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Financial Counterparties API (/financial_counterparties)"
---

# Financial Counterparties API (/financial_counterparties)

Use the financial counterparties API to create and update
financial counterparties.

The URL to access budget lines
is: `https:///api/financial_counterparties`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Financial Counterparties API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/financial_counterparties` | create | Create financial counterparty |
| GET | `/api/financial_counterparties` | index | Query financial counterparty |
| GET | `/api/financial_counterparties/:id` | show | Show financial counterparty |
| PATCH | `/api/financial_counterparties/:id` | update | Update financial counterparty |
| PUT | `/api/financial_counterparties/:id` | update | Update financial counterparty |

## Elements

The following elements are available for the Financial
Counterparties API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| abbreviation | Abbreviation, this field is now required, and this type is now string(50) | yes | yes | | yes | yes | string(50) |
| active | Active | | | | yes | yes | boolean |
| counterparty-address | Counterparty Address | | | | yes | yes | Counterparty Address |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa Internal ID | | | | | yes | integer |
| name | Name | yes | | | yes | yes | string(255) |
| payment-usage | Payment Usage | | | | yes | yes | string(255) |
| swift-code | Swift Code | | | | yes | yes | string(255) |
| treasury-usage | Treasury Usage | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| bank_code | Bank code | | | | yes | yes | string(16) |
| branch_code | Branch code | | | | yes | yes | string(10) |
| description | Description | | | | yes | yes | string(500) |
| external_identification_lei | Legal Entity Identifier (LEI) | | | | yes | yes | string(20) |
| external_identification_name | Deviating Name | | | | yes | yes | string(100) |
