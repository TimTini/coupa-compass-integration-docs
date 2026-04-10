---
title: "Currencies API (/currencies)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)"
status_code: 200
fetched_at: "2026-04-09T11:59:12+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Currencies API (/currencies)"
---

# Currencies API (/currencies)

Use the currencies API to query the different currencies your
account has set up within Coupa.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The PUT, POST, and PATCH actions are not supported and will be removed. Coupa will
automatically create new currencies as new ISO currencies are added. For any new currencies
needed that are not in Coupa, please contact Support or post as a request on the Coupa
Community.

The URL to access
currencies is: `https:///api/currencies`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Currencies API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/currencies` | index | Query currencies |
| GET | `/api/currencies/:id` | show | Show currency |

## Elements

The following elements are available for the Currencies API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| code | code | yes | yes | | yes | yes | string |
| created-by | created_by | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| decimals | decimals | | | | | yes | integer |
| enabled-flag | enabled_flag | | | | yes | | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | yes | | yes | | string |
| symbol | symbol | | | | yes | | string |
| updated-by | updated_by | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
