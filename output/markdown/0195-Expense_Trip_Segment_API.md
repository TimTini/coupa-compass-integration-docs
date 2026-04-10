---
title: "Expense Trip Segment API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-trip-segment-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-trip-segment-api"
status_code: 200
fetched_at: "2026-04-09T11:59:46+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Trip Segment API"
---

# Expense Trip Segment API

## Associations

This resource is associated with [Expenses API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api).

The following elements are available for the Expense
Trip Segment API:

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| end-at | End at | | | | | yes | |
| end-location | End location | yes | | | | yes | string(255) |
| end-location-id | End location | yes | | | | yes | string(255) |
| errors | Errors | | | | | yes | |
| id | Coupa unique identifier | | | | yes | yes | integer |
| is-travel-segment | Is travel segment | | | | | yes | boolean |
| start-at | Start at | | | | | yes | |
| start-location | Start location | yes | | | yes | yes | string(255) |
| start-location-id | Start location | yes | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| segment_num | | | | | yes | | integer |
| segment_type | | | | | yes | yes | string(255) |
| expense_trip_segment_mileage | | | | | yes | yes | |
| end_location | | yes | | | yes | | string(255) |
| is_travel_segment | | | | | yes | | boolean |
