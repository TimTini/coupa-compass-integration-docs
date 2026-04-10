---
title: "Integration Runs API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-runs-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-runs-api"
status_code: 200
fetched_at: "2026-04-09T11:59:48+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Integrations API (/integrations)"
  - "Integration Runs API"
---

# Integration Runs API

The URL to access Integration Runs
is `https://.coupahost.com/api/integration_runs`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

Integration Runs API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | /api/integration_runs | create | Create integration run with status of pending |
| PUT | /api/integration_runs/:id/fail | fail | Set integration run status as failed |
| GET | /api/integration_runs | index | Query integration runs |
| PUT | /api/integration_runs/:id/pause | pause | Set integration run status as paused |
| PUT | /api/integration_runs/:id/pending | pending | Set integration run status as pending |
| PUT | /api/integration_runs/:id/run | run | Set integration run status as running |
| GET | /api/integration_runs/:id | show | Show integration run |
| PUT | /api/integration_runs/:id/success | success | Set integration run status as successful |
| PATCH | /api/integration_runs/:id | update | Update integration run |
| PUT | /api/integration_runs/:id | update | Update integration run |

## Elements

These are the elements available for
the Integration Run API:

| **Element** | **Description** | **Type** | **API In** | **API Out** | **Required** | **Length** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| end-time | end_time | | | | yes | yes | datetime |
| flow | flow | | | | yes | yes | Flow |
| id | Coupa unique identifier | | | | | yes | integer |
| integration | integration | yes | | | yes | yes | Integration |
| integration | Standard | boolean | | | No | | any |
| integrationError | document_type | string(255) | | | No | | OrderHeader, InventoryTransaction, InvoiceHeader, ExpenseReport, RequisitionHeader, Account, Supplier, User, Address, RemitToAddress, Contract, ExchangeRate, Invoice, Requisition, Payment, ApprovalChain, LookupValue, Item, SupplierInformation |
| integrationError | document_id | integer | | | No | | any |
| integrationError | document_status | string | | | No | | any |
| integrationError | document_revision | integer | | | No | | any |
| integration-errors | integration_errors | string | | | | yes | [IntegrationError](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/integrations-api-(integrations)/integration-error-api) |
| integrationError | document_type | string(255) | | | false | | OrderHeader, InventoryTransaction, InvoiceHeader, ExpenseReport, RequisitionHeader, Account, Supplier, User, Address, RemitToAddress, Contract, ExchangeRate, Invoice, Requisition, Payment, ApprovalChain, LookupValue, Item, SupplierInformation |
| integrationError | document_id | integer | | | false | | any |
| integrationError | document_status | string | | | false | | any |
| integrationError | document_revision | integer | | | false | | any |
| records-processed | records_processed | | | | yes | yes | integer |
| start-time | start_time | | | | yes | yes | datetime |
| status | transaction status | | | | | yes | string |
| total-records | total_records | | | | yes | yes | integer |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
