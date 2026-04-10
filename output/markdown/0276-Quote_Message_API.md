---
title: "Quote Message API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-message-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-message-api"
status_code: 200
fetched_at: "2026-04-09T12:00:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Message API"
---

# Quote Message API

Use the Quote Message API to view messages sent or recieved by the buyer in relation to your
sourcing event.

## Associations

This resource is associated with the [Quote Request API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| quote-supplier-id | Quote Supplier ID | No | No | Any | No | Yes | string |
| quote-requests-user-id | Quote Request User ID | No | No | Any | No | Yes | string |
| quote-message-body | Message Body | No | No | Quote Message Body object | No | Yes | [QuoteMessageBody](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-message-body-api) |
