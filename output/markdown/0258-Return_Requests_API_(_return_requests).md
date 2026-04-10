---
title: "Return Requests API (/return_requests)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/return-requests-api-(return_requests)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/return-requests-api-(return_requests)"
status_code: 200
fetched_at: "2026-04-09T11:59:59+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Receipts API"
  - "Return Requests API (/return_requests)"
---

# Return Requests API (/return_requests)

The URL to access return requests is:
`https:///api/return_requests`

## Associations

This resource is associated with [Receipts API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api).

## Actions

The Return Requests API includes these methods:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/return_requests` | index | Query return requests |
| GET | `/api/return_requests/:id` | show | Query a return request by ID |
| POST | `/api/return_requests` | create | Create a return request in draft status |
| POST | `/api/return_requests/:id/submit` | submit | Submit a return request for approval |
| PUT/PATCH | `/api/return_requests/:id` | update | Update a return request that is in draft status |
| DELETE | `/api/return_requests/:id` | destroy | Delete a return request in draft status only |

For more information about the Return Requests API payload, see [Receipts API Example Calls](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/receipts-api/receipts-api-example-calls).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| address | Address | yes | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| created-at | Created Date | | | | | yes | datetime |
| created-by | Created By | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | ID | | | | | yes | integer |
| lines | Return Lines | yes | | | yes | yes | [ReturnRequestLine](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/return-request-line-api) |
| number | Return # | | | | yes | yes | string(255) |
| rma | RMA | | | | yes | yes | string(255) |
| status | Status | | | | yes | yes | string(255) |
| updated-at | Updated Date | | | | | yes | datetime |
| updated-by | Updated By | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
