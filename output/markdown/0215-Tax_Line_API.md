---
title: "Tax Line API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/tax-line-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/tax-line-api"
status_code: 200
fetched_at: "2026-04-09T11:59:50+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Invoices API (/invoices)"
  - "Tax Line API"
---

# Tax Line API

## Associations

This API resource is available through [Invoices API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)-da-5926-da-5926) and
[Invoice Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | amount | | | | yes | yes | decimal(32,4) |
| amount-engine | Amount calculated by either Coupa Native or External Tax Engine based on configuration | | | | | yes | decimal(32,4) |
| base | Base to Calculate Withholding | | | | yes | yes | decimal(30,4) |
| basis | Supplier Withholding Base Suggestion | | | | yes | yes | decimal(30,6) |
| code | code | | | | | yes | string(255) |
| code-engine | Code returned by External Tax Engine based on configuration | | | | | yes | string(255) |
| code-id | code_id | | | | yes | | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Tax Reference | | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | yes | yes | integer |
| kind-of-factor | Kind of Factor | | | | | yes | string(255) |
| nature-of-tax | Kind of Tax | | | | | yes | string(255) |
| product-tax-classification | Product Tax Classification | | | | yes | yes | string(3) |
| rate | rate | | | | yes | yes | float |
| rate-engine | Rate returned by External Tax Engine based on configuration | | | | | yes | decimal(30,6) |
| supplier-rate | Supplier Withholding Rate Suggestion | | | | yes | yes | decimal(32,4) |
| tax-code | tax_code | | | | yes | yes | Tax Code |
| tax-rate | Rate of Tax | | | | yes | yes | [Tax Rate](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-api) |
| tax-rate-type | Type of Tax | | | | yes | yes | [Tax Rate Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-type-api) |
| taxable-amount | Amount | | | | yes | yes | decimal(32,4) |
| type | WithholdingTaxLine or TaxLine | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| withholding-amount | Withholding Amount | | | | yes | yes | decimal(30,4 |
