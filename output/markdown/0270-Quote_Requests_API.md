---
title: "Quote Requests API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-api"
status_code: 200
fetched_at: "2026-04-09T12:00:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Requests API"
---

# Quote Requests API

Use the quote requests API to create, and manage and view your sourcing events.

## Actions

For more endpoints associated with Quote Request attachments and tasks, see the [Attachments API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) and the [Task API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/task-api-(tasks)).

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/quote_requests` | create | Create a Sourcing event |
| POST | `/api/quote_requests/create_from_source` | create_from_source | Create Sourcing event from Requisition, Contract, Catalog, Order pad, Order lines, Invoice lines, and items |
| GET | `/api/quote_requests` | index | Returns all Sourcing events |
| GET | `/api/quote_requests/:id` | show | Get information about the particular event |
| PUT | `/api/quote_requests/:id` | update | Update a Sourcing event. |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| allow-award-individual-line-items | Ability to award individual line items | | | | yes | yes | boolean |
| allow-multiple-response | Allow multiple responses from one supplier | | | | yes | yes | boolean |
| attachments | Attachments - there can be event details, terms and conditions, regular attachments | | | | yes | yes | [Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api) |
| automatic-bid-unsealing | If checked, bids will be unsealed automatically | | | true, false | yes | yes | boolean |
| business-partners | Business partners | | | | yes | yes | [Quote Requests User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-user-api) |
| comments | Comments | | | | yes | yes | text |
| commodity | Commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| content-groups | Content Groups | | | | yes | yes | [Period](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/budget-period-api) |
| currency | Currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| custom-fields | Custom fields | | | | | yes | |
| exported | Indicates if event has been exported | | | | yes | | boolean |
| description | Event name | | | | yes | yes | text |
| easy-forms | Forms | no | no | any | yes | yes | [Form](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| end-time | Time when event should end, format: %m/%d/%y %I:%M %p %z | | | | yes | yes | datetime |
| event-type | Type of event | yes | | | yes | yes | string(255) |
| hidden | Is true if the event is a hidden event | | | | yes | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| forms | Forms (deprecated in R23; replaced by easy-forms) | | | | yes | yes | [Form](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/form-api) |
| lines | Lines | | | | yes | yes | [Quote Request Line](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-line-api) |
| lots | Lots | | | | yes | yes | [Quote Requests Lot](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-requests-lot-api) |
| quote-request-attachments | Quote request attachments | | | | yes | yes | [Quote Request Attachment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-attachment-api) |
| quote-suppliers | Quote suppliers | | | | yes | yes | Quote Supplier |
| revision | Revision | | | | | yes | string(255) |
| sealed-bids | If checked, bids will be sealed | | | | yes | yes | boolean |
| sealing-type | Sealing type ('one_step_unsealing' or 'two_steps_unsealing') should be selected when Unseal Manually option is chosen | | | one_step_unsealing, two_steps_unsealing | yes | yes | integer |
| sealing-stage | Sealing Stage | | | all_envelopes_sealed, envelope1_unsealed, envelope2_unsealed | | yes | integer |
| start-on-submit | Flag that indicates whether to start event on submit or not | | | | yes | yes | boolean |
| start-time | Time when event should start, format: %m/%d/%y %I:%M %p %z | | | | yes | yes | datetime |
| state | State | | | | | yes | string(255) |
| tags | Tags | | | | yes | yes | [Tag](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/tag-api) |
| template-id | Template ID | | | | | yes | integer |
| timezone | Event timezone | | | | yes | yes | string(255) |
| base_price_calculation_method | Base price calculation method ('average_of_supplier_responses', 'lowest_supplier_response_in_prebid' or 'manually_enter_base_prices') allows to understand the method by which the base price will be calculated | | | | yes | yes | integer |
| cost_avoidance | Cost avoidance | | | | yes | yes | decimal(30,4) |
| cost_avoidance_currency | Cost Avoidance Currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| creatable-from-id | Creatable From Object ID | | | | | yes | integer |
| creatable-from-type | Creatable From Object Type | | | | | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| planned_savings | Planned savings | | | | yes | yes | decimal(30,6) |
| planned-savings-currency | Planned Savings Currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| negotiated_savings | Alias of savings to be used as a key in API | | | | yes | yes | decimal(32,4) |
| negotiated-savings-currency | Negotiated Savings Currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| original-id | Coupa unique identifier for original event | | | | | yes | integer |
| allow_supplier_to_send_attachments | If set to true by the buyer, the supplier is allowed to send attachments in the message center | | | | yes | yes | boolean |
| submit-time | Time when event should be submitted, format: %m/%d/%y %I:%M %p %z. Default time: none | | | | yes | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| quote-message | Messages sent or received by the buyer. | | | | | yes | [QuoteMessage](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-message-api) |
| allow-suppliers-to-choose-currency | If set to true, then the supplier is allowed to choose from the list of quote request currencies | | | | yes | yes | boolean |
| quote-request-currencies | Quote Request Currencies - List of currencies for the quote request | | | | yes | yes | [QuoteRequestCurrency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-request-currency-api) |

## Create an event from a template or an existing sourcing event

Method
POST `/api/quote_requests`

Example request payload

```text
{
"source_id": 105, // Id of the template or existing event
"description": "New name for the event",
"commodity": {
"id": 9
},
"currency": {"id": 1},
"lines": [
{
"description": "New item to be added to event",
"type": "QuoteRequestQuantityLine",
"quantity": 10
}
],
"quote_request_attachments":[
{
"name": "Attachmet One",
"instruction": "Some dummy instruction",
"response_required": true,
"allow_to_respond": true
}
]
}
```

Example cURL request

```text
curl --location 'https://<your-instance>.com/api/quote_requests' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Accept: application/octet-stream' \
--header 'Content-Type: text/plain' \
--header 'Authorization: ••••••' \
--data '{
"source_id": 105, // Id of the template or existing event
"description": "New name for the event",
"commodity": {
"id": 9
},
"currency": {"id": 1},
"lines": [
{
"description": "New item to be added to event",
"type": "QuoteRequestQuantityLine",
"quantity": 10
}
],
"quote_request_attachments":[
{
"name": "Attachmet One",
"instruction": "Some dummy instruction",
"response_required": true,
"allow_to_respond": true
}
]
}'
```

## Create an event with multiple currencies

Method
POST `/api/quote_requests`

Example request payload

```text
{
"source_id": 108,
"description": "New name for the event",
"commodity": {
"id": 9
},
"currency": {"id": 1},
"allow_suppliers_to_choose_currency": true,
"quote_request_currencies": [
{
"from_currency": {"code": "INR"},
"rate": 10
}
],
"lines": [
{
"description": "New item to be added to event",
"type": "QuoteRequestQuantityLine",
"quantity": 10
}
]
}
```

Example cURL request

```text
curl --location 'https://<your-instance>/api/quote_requests' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Accept: application/octet-stream' \
--header 'Content-Type: text/plain' \
--header 'Authorization: ••••••' \
--data '{
"source_id": 108,
"description": "New name for the event",
"commodity": {
"id": 9
},
"currency": {"id": 1},
"allow_suppliers_to_choose_currency": true,
"quote_request_currencies": [
{
"from_currency": {"code": "INR"},
"rate": 10
}
],
"lines": [
{
"description": "New item to be added to event",
"type": "QuoteRequestQuantityLine",
"quantity": 10
}
]
}'
```
