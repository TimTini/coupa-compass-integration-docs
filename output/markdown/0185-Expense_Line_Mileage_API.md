---
title: "Expense Line Mileage API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-mileage-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-line-mileage-api"
status_code: 200
fetched_at: "2026-04-09T11:59:44+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Line Mileage API"
---

# Expense Line Mileage API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| distance | Distance | yes | | | | yes | decimal(32,4) |
| distance-unit | Distance unit | yes | | | | yes | string(255) |
| end-address | End address | yes | | | | yes | string(255) |
| expense-line-mileage-allocations | Expense line mileage allocations | | | | | yes | Expense Line Mileage Allocation |
| expense-mileage-region | Expense mileage region | | | | | yes | Expense::Mileage::Region |
| expense-mileage-vehicle-type | Expense mileage vehicle type | | | | | yes | Expense::Mileage::VehicleType |
| id | Coupa unique identifier | | | | | yes | integer |
| passenger-count | Passenger count | | | | | yes | integer |
| round-trip | Round trip | | | | | yes | boolean |
| start-address | Start address | yes | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
