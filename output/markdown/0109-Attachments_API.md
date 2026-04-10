---
title: "Attachments API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/attachments-api"
status_code: 200
fetched_at: "2026-04-09T11:59:27+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Attachments API"
---

# Attachments API

Use the Attachments API to manage attachments on Coupa Reference and Transactional objects.

## Actions

Most Coupa resources allow you to add attachments to both the core resources along with comments on the resource. See the [Comments API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/comments-api) for details.

The Attachments API allows you to perform the following actions.

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | /api/contracts/:contract_id/attachments | create | Create attachment |
| POST | /api/invoices/:invoice_id/attachments | create | Create attachment |
| POST | /api/expense_reports/:expense_report_id/attachments | create | Create attachment |
| POST | /api/purchase_orders/:purchase_order_id/attachments | create | Create attachment |
| POST | /api/users/:user_id/attachments | create | Create attachment |
| POST | /api/requisitions/:requisition_id/attachments | create | Create attachment |
| GET | /api/contracts/:contract_id/attachments | index | Query attachments |
| GET | /api/inventory_transactions/:id/attachments/:id | show | Show attachment |
| GET | /api/invoices/:invoice_id/attachments | index | Query attachments |
| GET | /api/expense_reports/:expense_report_id/attachments | index | Query attachments |
| GET | /api/purchase_orders/:purchase_order_id/attachments | index | Query attachments |
| GET | /api/users/:user_id/attachments | index | Query attachments |
| GET | /api/requisitions/:requisition_id/attachments | index | Query attachments |
| GET | /api/contracts/:contract_id/attachments/:id | show | Show attachment |
| GET | /api/invoices/:invoice_id/attachments/:id | show | Show attachment |
| GET | /api/expense_reports/:expense_report_id/attachments/:id | show | Show attachment |
| GET | /api/purchase_orders/:purchase_order_id/attachments/:id | show | Show attachment |
| GET | /api/users/:user_id/attachments/:id | show | Show attachment |
| GET | /api/requisitions/:requisition_id/attachments/:id | show | Show attachment |
| GET | /api/attachments/:attachment_id | show | Show attachment based on an attachment ID.<br>![](https://compass.coupa.com/DITARoot/icons/important.png) Note:<br>To explicitly define the object the attachment is associated with, you can include the `attachable_type` parameter. For example, at GET call to `/api/attachments/:id?attachable_type=Contract` returns the attachment associated with a contract. |
| PATCH | /api/contracts/:contract_id/attachments/:id | update | You cannot update attachments via the API |
| PUT | /api/contracts/:contract_id/attachments/:id | update | You cannot update attachments via the API |
| PATCH | /api/invoices/:invoice_id/attachments/:id | update | You cannot update attachments via the API |
| PUT | /api/invoices/:invoice_id/attachments/:id | update | You cannot update attachments via the API |
| PATCH | /api/expense_reports/:expense_report_id/attachments/:id | update | You cannot update attachments via the API |
| PUT | /api/expense_reports/:expense_report_id/attachments/:id | update | You cannot update attachments via the API |
| PATCH | /api/purchase_orders/:purchase_order_id/attachments/:id | update | You cannot update attachments via the API |
| PUT | /api/purchase_orders/:purchase_order_id/attachments/:id | update | You cannot update attachments via the API |
| PATCH | /api/users/:user_id/attachments/:id | update | You cannot update attachments via the API |
| PUT | /api/users/:user_id/attachments/:id | update | You cannot update attachments via the API |
| PATCH | /api/requisitions/:requisition_id/attachments/:id | update | You cannot update attachments via the API |
| PUT | /api/requisitions/:requisition_id/attachments/:id | update | You cannot update attachments via the API |
| DELETE | /api/requisitions/:requisition_id/attachments/:id | delete | Delete an attachment from the Requisition Header (works for other document types too, like Orders) |
| DELETE | /api/requisition_lines/:requisition_line_id/attachments/:id | delete | Delete an attachment from the Requisition Line (works for other document types too, like Orders) |
| DELETE | /api/attachments/:attachment_id | delete | Delete an attachment |
| POST | /api/quote_requests/:quote_request_id/attachments | create | Add an attachment to an event. |
| DELETE | /api/quote_requests/:quote_request_id/attachments/:id | destroy | Delete an attachment associated with an event. |
| GET | /api/quote_requests/:quote_request_id/attachments | index | Get attachments associated with an event. |
| POST | /api/quote_request_lines/:quote_request_line_id/attachments | create | Add an attachment to an event line. |
| DELETE | /api/quote_request_lines/:quote_request_line_id/attachments/:id | destroy | Delete an attachment associated with an event line. |
| GET | /api/quote_request_lines/:quote_request_line_id/attachments | index | Get attachments associated with an event line. |
| POST | /api/quote_request_attachments/:quote_request_attachment_id/attachments | create | Add an attachment under the **Details** section of an event. |
| DELETE | /api/quote_request_attachments/:quote_request_attachment_id/attachments/:id | destroy | Delete an attachment under the **Details** section of an event. |
| GET | /api/quote_request_attachments/:quote_request_attachment_id/attachments | index | Get attachments under the **Details** section of an event. |

## Elements

The following elements are available for the Attachments API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| file-url | URL to attached file | | | | yes | yes | string |
| id | Coupa unique identifier | | yes | | | yes | integer |
| intent | intent | | | | yes | yes | string(40) |
| linked-to | link to specific feature | | | | yes | | string(255) |
| text | text | | | | yes | | text |
| type | type | yes | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| url | url | | | | yes | | string(255) |

## Create a Contract attachment

Method

POST `/api/requisitions/:id/attachments`

Example cURL request

```text
curl -X POST \
https://<INSTANCE>/api/requisitions/12345/attachments \
-H "Accept: application/xml" \
-H "content-type: multipart/form-data" \
-H "x-coupa-api-key: <API KEY>" \
-F "attachment[file]=@/Users/IntegrationAdmin/Contracts/Standard_Terms_Conditions.pdf" \
-F "attachment[type]=file"
-F "attachment[intent]=Supplier"
```

## Add an attachment under the **Details** section of a Sourcing event

Method
POST `/api/quote_request_attachments/10058/attachments`

Request parameters
Set request parameters to these values:

- `attachment[file]`: upload your attachment

- `attachment[type]`: file

- `attachment[intent]`: Supplier

- `attachment[linked_to]`: quote_request_attachment

Example cURL request

```text
curl --location 'https://<your-instance>.com/api/quote_request_attachments/10058/attachments ' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--form 'attachment[file]=@"/file-path.png"' \
--form 'attachment[type]="file"' \
--form 'attachment[intent]="Supplier"' \
--form 'attachment[linked_to]="quote_request_attachment"'
```

## Get an attachment associated with a Sourcing event

Method
GET `/api/quote_requests/10153/attachments/4712295`

Example cURL request

```text
curl --location 'https://<your-instance>.com/api/quote_requests/10153/attachments/4712295' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: _mkra_ctxt=c7e24ee9dd42c97a2bbfd26a2215079d12490dcfb828c19c332fdef146268332--200'
```

## Create an attachment associated with a Sourcing event

Method
POST `/api/quote_requests/10153/attachments/4712295`

Request parameters
For For attachments under event terms and conditions section, set `linked_to` to `attachment_to_suppliers`. For attachments under event terms and conditions section, set `linked_to` to `event_terms`.

```text
{
"type": "text",
"text": "Event info attachment text",
"linked_to": "attachment_to_suppliers", // For attachments under event info
"intent" : "Supplier"
}
```

Example cURL request

```text
curl --location 'https://<your-instance>.com/api/quote_requests/10153/attachments/4712295' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: _mkra_ctxt=c7e24ee9dd42c97a2bbfd26a2215079d12490dcfb828c19c332fdef146268332--200'
```
