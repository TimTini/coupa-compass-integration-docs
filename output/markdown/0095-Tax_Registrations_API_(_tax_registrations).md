---
title: "Tax Registrations API (/tax_registrations)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Tax Registrations API (/tax_registrations)"
---

# Tax Registrations API (/tax_registrations)

## Actions

Tax Registration allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/tax_registrations` | create | Create tax registration |
| GET | `/api/tax_registrations` | index | Query tax registrations |
| GET | `/api/tax_registrations/:id` | show | Show tax registration |
| PUT | `/api/tax_registrations/:id` | update | Update tax registration |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Tax code is enabled or disabled | | | true, false | yes | yes | boolean |
| country | Country where the tax code is applied | yes | | | yes | yes | Country |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| fiscal-representative | Fiscal representative who is locally established and who is in general held jointly and severally liable with the tax payer for the payment of the VAT to the tax authorities | | yes | RemitToAddress TaxRegistration | | | |
| id | Coupa unique identifier | | | | | yes | integer |
| local | True if tax registration cannot be used for cross-border invoices | | | true, false | yes | yes | boolean |
| number | Tax Registration number | yes | | | yes | yes | string(47) |
| owner-id | Coupa unique identifier of the object associated with this tax registration | | | | yes | yes | integer |
| owner-type | Type of the owning object | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
