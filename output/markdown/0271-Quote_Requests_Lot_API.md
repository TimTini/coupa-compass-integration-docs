---
title: "Quote Requests Lot API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-lot-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-lot-api"
status_code: 200
fetched_at: "2026-04-09T12:00:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Requests Lot API"
---

# Quote Requests Lot API

The quote request line resource lets you work with the lots on a sourcing event.

## Associations

This resource is associated with [Quote Request API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| expected-quantity | Quantity of lots we want | | | | yes | yes | integer |
| id | Coupa unique identifier | | | | | yes | integer |
| lines | Lines which belongs to lot | | | | yes | yes | [Quote Request Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-line-api) |
| name | Name of the lot | | | | yes | yes | string(255) |
