---
title: "Invoice Charge API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-charge-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-charge-api"
status_code: 200
fetched_at: "2026-04-09T11:59:49+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Invoices API (/invoices)"
  - "Invoice Charge API"
---

# Invoice Charge API

## Associations

This API resource is available through [Invoices API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)-da-5926-da-5926).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account | account | yes | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| account-allocations | Account allocations | | | | yes | yes | [Invoice Charge Allocation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-charge-allocation-api) |
| accounting-total | Accounting total | | | | | yes | decimal(30,4) |
| accounting-total-currency | Accounting total currency | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| billing-note | Billing note | | | | yes | yes | text |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| description | Description | | | | yes | yes | string(1550) |
| distributed | Distributed | | | | yes | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| line-num | Line num | | | | yes | yes | integer |
| pct | Pct | | | | yes | yes | decimal(16,10) |
| period | period | | | | yes | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api) |
| tax-lines | Tax lines | | | | yes | yes | [Tax Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/tax-line-api) |
| total | Total | | | | yes | yes | decimal |
| type | Type | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
