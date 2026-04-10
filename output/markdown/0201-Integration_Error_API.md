---
title: "Integration Error API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-error-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-error-api"
status_code: 200
fetched_at: "2026-04-09T11:59:48+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Integrations API (/integrations)"
  - "Integration Error API"
---

# Integration Error API

The URL to access Integration Error
is `https://{your_instance}/api/integration_errors`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

Integration History Record API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/integration_errors` | query | Query integration errors |
| POST | `/api/integration_errors` | create | Create integration error |
| GET | `/api/integration_errors/{id}` | show | Show integration error |
| PATCH | `/api/integration_errors/{id}` | update | Update integration error |
| PUT | `/api/integration_errors/{id}` | update | Update integration error |
| PUT | `/api/integration_errors/{id}/resolve` | resolve | Resolve integration error |
| PUT | `/api/integration_errors/{id}/unresolve` | unresolve | Unresolve resolved integration error |
| POST | `/api/integration_errors/create_alert` | create_alert | /integration_errors/create_alert |

## Elements

These are the elements available for the Integration
Error API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contact-alert-type | contact_alert_type | yes | | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | yes | yes | datetime |
| created-by | User who created | | | | | yes | [Users](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| creation-method | creation_method | | | | yes | yes | string(255) |
| document-id | document_id | | | | yes | yes | integer |
| document-revision | document_revision | | | | yes | yes | integer |
| document-status | document_status | | | | yes | yes | string(255) |
| document-type | document_type | | | ContingentWorkOrderHeader, ExternalOrderHeader, OrderHeader, InventoryTransaction, InvoiceHeader, ExpenseReport, RequisitionHeader, Account, Supplier, User, Address, RemitToAddress, Contract, ExchangeRate, Invoice, Requisition, Payment, ApprovalChain, LookupValue, Item, SupplierInformation, Asn::Header, AccountValidationRule, Payables::External::Payable, Charge, Payables::Invoice, Payables::Expense, CoupaPay::Payment, CoupaPay::Statement, ReceiptRequest, InventoryRequestHeader | yes | yes | string(255) |
| external-id | external-id | | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| integration | integration | | | | yes | yes | [Integration](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)) |
| integration-filename | filename that is associated with integration error | | | | yes | yes | string(255) |
| integration-run | integration-run | yes | | | yes | | |
| integration-run-id | Integration Run ID | | | | yes | yes | integer |
| resolved | True if this error is resolved | | | | | yes | boolean |
| responses | Response from external system | | | | yes | yes | [IntegrationRecordResponse](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-record-response-api) |
| status | transaction status | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | yes | yes | datetime |
| updated-by | User who updated | | | | | yes | [Users](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
