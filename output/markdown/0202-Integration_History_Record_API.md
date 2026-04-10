---
title: "Integration History Record API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-history-record-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-history-record-api"
status_code: 200
fetched_at: "2026-04-09T11:59:48+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Integrations API (/integrations)"
  - "Integration History Record API"
---

# Integration History Record API

The URL to access Integration History
Record is `https://{your_instance}/api/integration_history_records`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

Integration History Record API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/integration_history_records/acknowledge` | acknowledge | |
| POST | `/api/integration_history_records` | create | Create integration history record |
| POST | `/api/integration_history_records/create_alert` | create_alert | |
| POST | `/api/integration_history_records/`<br>`create_alert_and_mark_exported` | create_alert_and_mark_exported | |
| GET | `/api/integration_history_records` | index | Query integration history records |
| POST | `/api/integration_history_records/mark_exported` | mark_exported | |
| GET | `/api/integration_history_records/:id` | show | Show integration history record |
| PATCH | `/api/integration_history_records/:id` | update | Update integration history record |
| PUT | `/api/integration_history_records/:id` | update | Update integration history record |

## Elements

These are the elements available for the Integration
History Record API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contact-alert-type | contact_alert_type | yes | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | yes | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| creation-method | creation_method | | | | yes | yes | string(255) |
| document-id | document_id | yes | | | yes | yes | integer |
| document-revision | document_revision | | | | yes | yes | integer |
| document-status | document_status | | | | yes | yes | string(255) |
| document-type | document_type | yes | ExternalOrderHeader, OrderHeader, InventoryTransaction, InvoiceHeader, ExpenseReport, RequisitionHeader, Account, Supplier, User, Address, RemitToAddress, Contract, ExchangeRate, Invoice, Requisition, Payment, ApprovalChain, LookupValue, Item, SupplierInformation, Asn::Header, AccountValidationRule, ContingentWorkOrderHeader, Payables::External::Payable, Charge, Payables::Invoice, Payables::Expense, CoupaPay::Payment, CoupaPay::Statement, ReceiptRequest, InventoryRequestHeader | yes | yes | string(255) | |
| external-id | external_id | | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| integration | integration | | | | yes | yes | [Integration](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)) |
| integration-run | integration_run | | | | yes | | [Integration Run](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-runs-api) |
| integration-run-id | Unique identifier for integration run | | | | yes | yes | integer |
| integration_filename | Filename for bulk import/export | | | | | yes | string(255) |
| resolved | True if this record is resolved | | | | | yes | boolean |
| responses | Response from external system | | | | yes | yes | [Integration Record Response](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-record-response-api) |
| status | transaction status | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
