---
title: "Tax Code Rules API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-code-rules-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-code-rules-api"
status_code: 200
fetched_at: "2026-04-09T11:59:24+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Tax Registrations API (/tax_registrations)"
  - "Tax Code Rules API"
---

# Tax Code Rules API

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-segment-1 | Account segment 1 | | | | yes | yes | string(255) |
| account-segment-2 | Account segment 2 | | | | yes | yes | string(255) |
| account-segment-3 | Account segment 3 | | | | yes | yes | string(255) |
| account-segment-4 | Account segment 4 | | | | yes | yes | string(255) |
| account-segment-5 | Account segment 5 | | | | yes | yes | string(255) |
| account-type | chart of accounts | yes | | | yes | yes | [Account Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| active | Active | | | | yes | yes | boolean |
| buyer-fiscal-rep-country | Buyer fiscal rep country | | | | yes | yes | Country |
| buyer-tax-registration | Buyer tax registration | | | | yes | yes | [Tax Registration](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)) |
| cash-accounting-scheme-reference | Cash accounting scheme reference | | | | yes | yes | Cash Accounting Scheme Reference |
| category | Category | | | goods, services, monetary, others | yes | yes | string(255) |
| commodity | Commodity | | | | yes | yes | [Commodity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/commodities-api-(commodities)) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| deductibility | Deductibility | | | fully_deductible, partially_deductible, not_deductible | yes | yes | string(255) |
| document-type | Document type | | | | yes | yes | string(255) |
| effective-date | Effective date | yes | | | yes | yes | datetime |
| end-date | End date | | | | yes | yes | datetime |
| expense-category | expense category | | | | yes | yes | [ExpenseCategory](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-category-api) |
| id | Coupa unique identifier | | | | yes | yes | integer |
| jurisdiction | Jurisdiction | | | intra_eu, domestic, cross_border | yes | yes | string(255) |
| name | Name | | | | yes | yes | string(255) |
| priority | Priority | yes | | | yes | yes | integer |
| subcategory | Subcategory | | | raw_materials, investment_goods, services_exceptions | yes | yes | string(255) |
| supplier | supplier | | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| supplier-fiscal-rep-country | Supplier fiscal rep country | | | | yes | yes | Country |
| tax-code | tax code | yes | | | yes | yes | [Tax Code](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-code-api) |
| tax-rate | Tax rate | | | | yes | yes | string(255) |
| tax-rate-customer-accounting | Tax rate customer accounting | | | | yes | yes | boolean |
| tax-rate-type | Tax rate type | | | | yes | yes | [Tax Rate Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/tax-registrations-api-(tax_registrations)/tax-rate-type-api) |
| tax-reference | Tax reference | | | | yes | yes | Tax Reference |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | yes | datetime | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
