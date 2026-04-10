---
title: "Supplier Information Tax Registrations API (/supplier_information_tax_registrations)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-tax-registrations-api(supplier_information_tax_registrations)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-tax-registrations-api(supplier_information_tax_registrations)"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Supplier Information Tax Registrations API (/supplier_information_tax_registrations)"
---

# Supplier Information Tax Registrations API (/supplier_information_tax_registrations)

The URL to access supplier information
is: `https:///api/supplier_information_tax_registrations`

SIM API permissions must be included with your API key to
enable proper usage. Existing API keys without SIM API
permissions won't be able to access
the `/api/supplier_information_tax_registrations`
resource. See [API Key Security](https://compass.coupa.com/x294382.xml) and [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Supplier Information Tax Registrations API allows you
to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/supplier_information_tax_registrations` | create | Create supplier information tax registration |
| DELETE | `/api/supplier_information_tax_registrations/:id` | destroy | /api/supplier_information_tax_registrations/:id |
| GET | `/api/supplier_information_tax_registrations/:id` | show | Show supplier information tax registration |
| PATCH | `/api/supplier_information_tax_registrations/:id` | update | Update supplier information tax registration |
| PUT | `/api/supplier_information_tax_registrations/:id` | update | Update supplier information tax registration |

## Elements

The following elements are available for the Supplier
Information Tax Registrations API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| number | Tax Number | yes | no | any | yes | yes | string(940) |
| supplier_information_address_id | Primary Address ID | no | no | any | yes | yes | integer |
| supplier_information_id | Supplier Information ID | no | no | any | yes | yes | integer |
| active | Tax Registration Status | no | no | any | yes | yes | boolean |
| local | Local Tax Number | no | no | any | yes | yes | boolean |
| country | Country Sub Object | yes | no | any | yes | yes | |
| id | Tax Registration ID | no | no | any | yes | yes | integer |
| created_at | Created Date and Time | no | no | any | yes | yes | datetime |
| updated_at | Last Updated Date and Time | no | no | any | yes | yes | datetime |
| created_by | User who created | no | no | any | yes | yes | integer |
| updated_by | User who last updated | no | no | any | yes | yes | integer |
