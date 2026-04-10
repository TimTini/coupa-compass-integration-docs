---
title: "Supplier Information Sites API (/supplier_information_sites)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-sites-api-(supplier_information_sites)-da-5815-da-5815"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-sites-api-(supplier_information_sites)-da-5815-da-5815"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Supplier Information Sites API (/supplier_information_sites)"
---

# Supplier Information Sites API (/supplier_information_sites)

The URL to access supplier information is: `https:///api/supplier_information_sites`

SIM API permissions must be included with your API key to enable proper usage. Existing API keys without SIM API permissions won't be able to access the `/api/supplier_information_sites` resource. See [API Key Security](https://compass.coupa.com/x294382.xml) and [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

SIM API GET calls include SIM Sites in response payloads. For more information, see [Postman Collection for Coupa APIs](https://compass.coupa.com/x285429.xml).

## Actions

The Supplier Information Sites API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/supplier_information` | create | Create |
| GET | `/api/supplier_information` | index | Index |
| GET | `/api/supplier_information/:id` | show | Show |
| PUT | `/api/supplier_information/:id` | update | Update |
| POST | `/api/supplier_information/:supplier_information_id/supplier_information_sites` | create | Create supplier information site |
| POST | `/api/supplier_information_sites` | create | Create supplier information site |
| DELETE | `/api/supplier_information/:supplier_information_id/supplier_information_sites/:id` | destroy | Delete supplier information sites |
| DELETE | `/api/supplier_information_sites/:id` | destroy | Delete supplier information sites |
| GET | `/api/supplier_information/:supplier_information_id/supplier_information_sites` | index | Query supplier information sites |
| GET | `/api/supplier_information_sites` | index | Query supplier information sites |
| GET | `/api/supplier_information/:supplier_information_id/supplier_information_sites/:id` | show | Show supplier information site |
| GET | `/api/supplier_information_sites/:id` | show | Show supplier information site |
| PATCH | `/api/supplier_information/:supplier_information_id/supplier_information_sites/:id` | update | Update supplier information site |
| PUT | `/api/supplier_information/:supplier_information_id/supplier_information_sites/:id` | update | Update supplier information site |
| PATCH | `/api/supplier_information_sites/:id` | update | Update supplier information site |
| PUT | `/api/supplier_information_sites/:id` | update | Update supplier information site |
| PUT | `/api/supplier_information_sites/:id?exported=true` | update | Updates `last-exported-at` with timestamp. (`exported=false` sets value to null) |

## Elements

The following elements are available for the Supplier Information Sites API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code | supplier_code | yes | yes | any | yes | yes | string(20) |
| name | Supplier Information name | yes | no | any | yes | yes | string(255) |
| po_method | Purchase order transmission method | no | no | any | yes | yes | string(255) |
| po_change_method | Purchase order change transmission method | no | no | any | yes | yes | string(255) |
| default_locale | Default Locale for sending emails to this supplier site | no | no | any | yes | yes | string(255) |
| cxml_url | URL where POs are sent if PO transmission is "cxml" | no | no | any | yes | yes | string(255) |
| cxml_domain | "From" , our domain | no | no | any | yes | yes | string(255) |
| cxml_identity | "From", our identity | no | no | any | yes | yes | string(255) |
| cxml_supplier_domain | "To", supplier domain | no | no | any | yes | yes | string(255) |
| cxml_supplier_identity | "To", supplier identity | no | no | any | yes | yes | string(255) |
| cxml_secret | Shared secret | no | no | any | yes | yes | string(255) |
| cxml_protocol | Transmission protocol | no | no | any | yes | yes | string(255) |
| cxml_http_username | User name required to access the Supplier's online store | no | no | any | yes | yes | string(255) |
| cxml_ssl_version | Specify the SSL version used for cXML communication with the supplier | no | no | any | yes | yes | string(255) |
| buyer_hold | Hold all POs for buyer review | no | no | any | yes | yes | boolean |
| disable_cert_verify | Specify whether to ignore SSL certificate mismatch errors | no | no | any | yes | yes | boolean |
| po_email | Email where POs are sent if PO transmission is "email" | no | no | any | yes | yes | string(255) |
| active | true if the site is active | no | no | any | yes | yes | boolean |
| allow_change_requests | Allows suppliers to create change requests from CSP | no | no | any | yes | yes | integer |
| supplier_information_id | Supplier Information id | no | no | any | yes | yes | integer |
| payment_term | Default payment term, selectable from drop down | no | no | any | yes | yes | |
| shipping_term | Supplier shipping term, selectable from drop down | no | no | any | yes | yes | |
| content_groups | | no | no | any | yes | yes | [] |
| addresses | Supplier Information Site addresses | no | no | any | yes | yes | [] |
| contacts | Supplier Information Site contacts | no | no | any | yes | yes | [] |
| id | Coupa Internal ID | no | no | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | yes | yes | datetime |
| last_exported_at | Last exported flag | no | no | any | yes | yes | datetime |
| created_by | User who created | no | no | any | yes | yes | |
| updated_by | User who updated | no | no | any | yes | yes | |
