---
title: "Quote Request Attachment API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-api"
status_code: 200
fetched_at: "2026-04-09T12:00:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Request Attachment API"
---

# Quote Request Attachment API

The quote request attachment resource lets you manage the attachments on sourcing events.

## Associations

This resource is associated with the [Quote Request API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| allow-to-respond | Allow to respond | | | | yes | yes | boolean |
| attachments | Attachments | | | | yes | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| id | Coupa unique identifier | | | | yes | yes | integer |
| instruction | Instruction | | | | yes | yes | text |
| name | Name | | | | yes | yes | string(255) |
| response-required | Response required | | | | yes | yes | boolean |
