---
title: "Shipping Terms API (/shipping_terms)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/shipping-terms-api-(shipping_terms)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/shipping-terms-api-(shipping_terms)"
status_code: 200
fetched_at: "2026-04-09T11:59:17+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Shipping Terms API (/shipping_terms)"
---

# Shipping Terms API (/shipping_terms)

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET\|POST | `/api/shipping_terms(/:action(/:id))` | {:index=>"Query shipping terms", :create=>"Create shipping term", :show=>"Show shipping term", :update=>"Update shipping term", :destroy=>"Delete shipping term"} | |
| POST | `/api/shipping_terms` | create | Create shipping term |
| GET | `/api/shipping_terms` | index | Query shipping terms |
| GET | `/api/shipping_terms/:id` | show | Show shipping term |
| PUT | `/api/shipping_terms/:id` | update | Update shipping term |

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | true | yes | yes | boolean | | |
| code | code | yes | yes | | yes | yes | string(255) |
| content-groups | Content groups | | | | yes | yes | [BusinessGroup](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| description | description | | | | yes | yes | text |
| id | Coupa unique identifier | | | | | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
