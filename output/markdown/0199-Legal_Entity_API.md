---
title: "Legal Entity API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/legal-entity-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/legal-entity-api"
status_code: 200
fetched_at: "2026-04-09T11:59:46+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Legal Entity API"
---

# Legal Entity API

## Associations

The API resource is associated with the [Expenses API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bill-to-address | Bill to address | | | | | yes | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | User |
| id | Coupa unique identifier | | | | | yes | integer |
| name | Name | true | true | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | User |
| abbreviation | Abbreviation | true | true | | yes | yes | string(50) |
| active | Active | | | | yes | yes | boolean |
| parent | Parent | | | | yes | yes | Legal Entity |
| currency | Currency | true | | | yes | yes | Currency |
| bill-to-addresses | Bill to Address | | | | yes | | Address |
| swift_code | SWIFT Code | | | | yes | yes | string(11) |
| accounting_method | Accounting Method | | | ifrs, ifrs_9, us_gaap | yes | yes | string(7) |
| corporate_sector | Corporate Sector | | | | yes | yes | string(16) |
| use_fx_rates_reciprocal | Use FX rates reciprocal | | | | yes | yes | boolean |
| description | Description | | | | yes | yes | string(500) |
| external_identification_lei | Legal Entity Identifier | | | | yes | yes | string(20) |
| external_identification_name_matching | Deviating Name Matching | | | | yes | yes | string(100) |
| external_identification_name_trading | Deviating Name Trading | | | | yes | yes | string(100) |
| external_identification_swift | Deviating SWIFT Code | | | | yes | yes | string(11) |
| external_identification_company_code | Company Code | | | | yes | yes | string(11) |
| external_identification_creditor_id | SEPA Creditor ID | | | | yes | yes | string(35) |
| external_identification_ic_identifier_gl | IC Identifier for GL Exports | | | | yes | yes | string(50) |
