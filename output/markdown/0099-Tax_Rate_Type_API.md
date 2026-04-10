---
title: "Tax Rate Type API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-type-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-type-api"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Tax Registrations API (/tax_registrations)"
  - "Tax Rate Type API"
---

# Tax Rate Type API

## Associations

This resource is associated `/api/invoices` via the [Tax Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/tax-line-api) resource.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Values** | **In** | **Out** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | no | no | yes/no<br>true/false | | yes | boolean |
| country | Country where the tax rate type is applied | | | | yes | yes | Country |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | Description of the tax rate type | | yes | | yes | yes | string(255) |
| effective-date | Effective date | no | no | datetime | | yes | datetime |
| expiration-date | Expiration date | no | no | datetime | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
