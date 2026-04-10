---
title: "Punchout Site API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/punchout-site-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/punchout-site-api"
status_code: 200
fetched_at: "2026-04-09T11:59:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Punchout Site API"
---

# Punchout Site API

## Associations

This API is associated with the [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

## Elements

The following elements are available for the Punchout Site
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contract-id | Contract | yes | | | yes | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | User |
| description | Description | | | | | yes | string(255) |
| disable-cert-verify | Disable cert verify | | | | yes | yes | boolean |
| domain | domain | yes | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| identity | identity | yes | | | yes | yes | string(255) |
| is-from-coupa-checkout | is_from_coupa_checkout | | | | yes | | boolean |
| name | name | yes | yes | | yes | yes | string(255) |
| protocol | protocol | yes | | | yes | yes | string(255) |
| secret | secret | yes | | | yes | yes | string(255) |
| sender-domain | sender_domain | yes | | | yes | yes | string(255) |
| sender-identity | sender_identity | yes | | | yes | yes | string(255) |
| ssl-version | Ssl version | | | | yes | yes | string(255) |
| supplier-id | supplier_id | | | | yes | yes | integer |
| supports-edit | supports_edit | | | | yes | yes | boolean |
| supports-inspect | supports_inspect | | | | yes | yes | boolean |
| title | Title | | | | | yes | string |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | User |
| url | url | yes | | | yes | yes | string(255) |
