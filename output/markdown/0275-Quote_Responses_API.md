---
title: "Quote Responses API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-responses-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-responses-api"
status_code: 200
fetched_at: "2026-04-09T12:00:02+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Responses API"
---

# Quote Responses API

Use the quote responses API endpoint to view the supplier responses to your sourcing event
and award lines and lots.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/quote_responses/:id/award` | award | Award the quote response. |
| GET | `/api/quote_requests/:quote_request_id/quote_responses` | index | Get the latest submitted response per supplier. To see all responses, use the `/api/quote_requests/:quote_request_id/quote_responses/all` endpoint. |
| GET | `/api/quote_requests/:quote_request_id/quote_responses/all` | all | Get all responses for a Sourcing event, including all submitted and draft responses. |
| GET | `/api/quote_responses` | index | Get all responses of specific Sourcing event. |
| DELETE | `/api/quote_responses/:id/award` | remove_award | Remove award from the quote response. |
| GET | `/api/quote_responses/:id` | show | Get information about the particular response. |
| GET | `/api/quote_responses/all` | all | Get all responses, including all submitted and draft responses. |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| awarded | Awarded | | | | | yes | boolean |
| comments | Comments | | | | | yes | text |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| lines | Lines | | | | | yes | [QuoteResponseLine](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-response-lines-api) |
| position | position | | | | | yes | integer |
| promoted | promoted | | | | | yes | boolean |
| quote-request-id | quote_request_id | | | | | yes | integer |
| quote-request-original-id | Coupa unique identifier for original Sourcing Event | | | | | yes | string |
| quote-request-revision | Sourcing Event Revision | | | | | yes | string |
| quote-supplier | quote_supplier | yes | | | | yes | [QuoteSupplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-suppliers-api) |
| state | state | | | | | yes | string(255) |
| submitted-at | submitted_at | yes | | | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| quote-request-attachment-response | Details about supplier attachments at the event level. | | | | | yes | [Quote Request Attachment Response](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-response-api) |

## Quote Response attachments

To access a Quote Response attachment, you can use the
`/api/quote_requests/:quote_request_id/quote_responses` endpoint to get the
latest submitted response per supplier, or use the
`/api/quote_requests/:quote_request_id/quote_responses/all` endpoint to get
all responses, including historical and draft responses. Under the [Lines](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-response-lines-api) object in the response body, locate the
`id` field in the attachments array. Once you have the attachment ID, you
can use the [Attachments API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) to access the
attachment.

For example, this sample response from a GET request to the
`/api/quote_requests/:quote_request_id/quote_responses/all` endpoint
includes a sample attachment ID:

```text
[
{
"id": 1,
"created-at": "2023-05-03T08:14:37-07:00",
"updated-at": "2023-05-03T08:14:48-07:00",
"quote-request-id": 1,
"submitted-at": "2023-05-03T08:14:48-07:00",
"state": "submitted",
"promoted": false,
"position": null,
"comments": null,
"exported": false,
"quote-request-original-id": null,
"quote-request-revision": null,
"awarded": false,
"lines": [
{
"id": 1,
"created-at": "2023-05-03T08:14:37-07:00",
"updated-at": "2023-05-24T04:26:55-07:00",
"price-amount": "1.0",
"quantity": "1.0",
"reporting-price-amount": "1.0",
"price-currency": {
"id": 1,
"code": "USD",
"decimals": 2
},
"quote-request-line-id": 1,
"lot-id": 1,
"lead-time": null,
"cost-element-values": {},
"supplier-item-name": null,
"item-description": null,
"item-part-number": null,
"awarded": false,
"easy-form-response": null,
"shipping-term": null,
"attachments": [
{
"file": "path_to_attachment.xlsx",
"file-content-type": "application/octet-stream",
"file-file-name": "attachment_name.xlsx",
"file-file-size": "11565",
"file-url": "http://my-website.com/attachment/attachment_file/file/246/attachment_name.xlsx",
"id": 246, # <--- Attachment ID is here
"intent": "Internal",
"linked-to": "quote_request_attachment",
"text": null,
"type": "AttachmentFile",
"url": "http://my-website.com/attachments/246/view/attachment_name.xlsx"
}
],
```
