---
title: "Charges API (/charges)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/charges-api-(charges)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/charges-api-(charges)"
status_code: 200
fetched_at: "2026-04-09T11:59:33+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Charges API (/charges)"
---

# Charges API (/charges)

## Overview

The URL to access charges is: `https://{your_instance_name}/api/charges` or you can see the OpenAPI docs here: `https://{your_instance_name}/api_docs/14`.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/charges` | index | Query Charges |
| GET | `/api/charges/:id` | show | Show Charges |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-type-id | Chart of Accounts ID associated with the charge | | | | | yes | integer(11) |
| accounting-currency | Currency Code for Accounting Total | | | | | yes | |
| accounting-total | Amount of charge in Chart Of Accounts Accounting Currency | | | | | yes | decimal |
| card-provider-account | Card Provider Account | | | | yes | yes | string(255) |
| charge-allocations | Account Allocations for charge | | | | | yes | [Charge Allication](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/charges-api-(charges)/charge-allocation-api) |
| charge-date | Date of the charge | yes | | | yes | yes | datetime |
| charge-tax-lines | Tax lines for charge | | | | | yes | [] |
| coupa-pay-id | Unique Coupa Pay ID | | | | yes | yes | integer(11) |
| coupa-pay-statement-id | Unique Coupa Pay Statement ID | | | | yes | yes | integer(11) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Base currency of the card | yes | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| document_id | Transactional document ID associated with the charged card | | | | | yes | integer |
| document-type | Type of transactional document associated with the charged card | | | | | yes | string(255) |
| expense-holding-account | Expense holding account | | | | | | |
| exported | Indicates if transaction has been exported | | | | | yes | boolean |
| external-ref-id | Unique 3rd party system ID | yes | | | yes | yes | string(255) |
| holding-account | Holding account | | | | | yes | |
| id | Unique Coupa ID | | | | | yes | integer(11) |
| issuer-bank | Issuer's Bank | | | | | yes | |
| issuer-reconciliation-id | Issuer Reconciliation ID | | | | | yes | string(255) |
| last-exported-at | Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| legal_entity_name | Legal Entity name | | | | | yes | string |
| mcc | Merchant Category Code | | | | yes | yes | string(255) |
| merchant-currency | Currency the card was charged in | yes | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| merchant-reference | Card provided merchant information | | | | yes | yes | string(255) |
| merchant-total | Total the merchant charged in merchant currency | | | | yes | yes | decimal(30,6) |
| order-header-currency | Currency from the charged card's Purchase Order | | | | | yes | string(6) |
| order-header-id | Purchase Order ID associated with the charged card | | | | | yes | integer(11) |
| order-header-number | Purchase Order Number associated with the charged card | | | | | yes | string(20) |
| order-header-total | Total amount on the charged card's Purchase Order | | | | | yes | string(255) |
| payment_partner | | | | | | yes | |
| posting_date | Date the charge posted | | | | yes | yes | datetime |
| statement | Statement | | | | yes | | CoupaPay::Statement |
| statement-id | Unique Coupa ID | yes | | | | yes | integer(11) |
| statement-name | Name of the Statement that this Charge belongs to | | | | | yes | string(255) |
| supplier | supplier | yes | | | yes | | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-id | Unique Coupa Supplier ID | | | | | yes | integer(11) |
| supplier-name | Supplier in Coupa that made the charge | | | | | yes | string(255) |
| total | Total of the charge in the card base currency | | | | yes | yes | decimal(30,6) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| virtual-card | Virtual card | yes | | | yes | | CoupaPay::VirtualCard |
| virtual-card-id | Coupa ID for associated Virtual Card | | | | | yes | integer(11) |

## Example API Calls

| **Element** | **Details** |
| --- | --- |
| URL | `https://{instancename}/api/charges/{id}` |
| Operation | GET |
| Parameters | Query parameters |
| Request body | None |
| Example requests | @@BLOCK_0@@ |
