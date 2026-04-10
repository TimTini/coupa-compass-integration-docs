---
title: "Expense Virtual Card API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-virtual-card-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-virtual-card-api"
status_code: 200
fetched_at: "2026-04-09T11:59:46+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Virtual Card API"
---

# Expense Virtual Card API

## Association

This resource is associated with [Expense Reports API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | | | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | | yes | datetime |
| amount | Original preapproved amount | yes | | any | | yes | decimal(32,4) |
| available_amount | Remaining preapproved amount | | | any | | yes | decimal(32,4) |
| reporting_total | The reporting total that was approved | | | any | | yes | decimal(32,4) |
| active_card_url | URL of Active Virtual Card | | | any | | yes | |
| currency | Original preapproved currency | | | any | | yes | |
| available_amount_currency | Remaining preapproved currency | | | any | | yes | |
| created_by | User who created preapproval request | | | any | | yes | |
| updated_by | User who last updated preapproval request | | | any | | yes | |
