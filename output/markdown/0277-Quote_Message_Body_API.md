---
title: "Quote Message Body API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-message-body-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-message-body-api"
status_code: 200
fetched_at: "2026-04-09T12:00:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Message Body API"
---

# Quote Message Body API

Use the Quote Message Body API to view message details and attachments sent or recieved by
the buyer in relation to your sourcing event.

## Associations

This resource is associated with the [Quote Request API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| body | Message body. | No | No | Any | No | Yes | string |
| status | Messge status. | No | No | Any | No | Yes | string |
| attachments | Message attachments. | No | No | Any | No | Yes | array |
