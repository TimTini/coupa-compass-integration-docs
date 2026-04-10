---
title: "Quote Request Attachment Response API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-response-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-response-api"
status_code: 200
fetched_at: "2026-04-09T12:00:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Request Attachment Response API"
---

# Quote Request Attachment Response API

Use the Quote Request Attachment Response API to view event-level attachments.

## Associations

This resource is associated with the [Quote Responses API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-responses-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| quote-request-attachment | Event-level attachment submitted by the Buyer. | No | No | Any | No | Yes | [Quote Request Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-api) |
| attachments | Event-level attachment submitted by the Supplier. | No | No | Any | No | Yes | array |
