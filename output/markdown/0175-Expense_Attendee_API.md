---
title: "Expense Attendee API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-attendee-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-attendee-api"
status_code: 200
fetched_at: "2026-04-09T11:59:41+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Attendee API"
---

# Expense Attendee API

## Association

This resource is associated with [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api).

## Elements

| **Field Name** | **Field Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api-In Field?** | **Api-Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | | | yes | boolean |
| company | Company | | | | yes | yes | string(308) |
| company-active | Company field in use | | | | | yes | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| expense-attendee-type-custom-field-1 | Expense attendee type custom field 1 | | | | yes | yes | text |
| expense-attendee-type-custom-field-10 | Expense attendee type custom field 10 | | | | yes | yes | text |
| expense-attendee-type-custom-field-2 | Expense attendee type custom field 2 | | | | yes | yes | text |
| expense-attendee-type-custom-field-3 | Expense attendee type custom field 3 | | | | yes | yes | text |
| expense-attendee-type-custom-field-4 | Expense attendee type custom field 4 | | | | yes | yes | text |
| expense-attendee-type-custom-field-5 | Expense attendee type custom field 5 | | | | yes | yes | text |
| expense-attendee-type-custom-field-6 | Expense attendee type custom field 6 | | | | yes | yes | text |
| expense-attendee-type-custom-field-7 | Expense attendee type custom field 7 | | | | yes | yes | text |
| expense-attendee-type-custom-field-8 | Expense attendee type custom field 8 | | | | yes | yes | text |
| expense-attendee-type-custom-field-9 | Expense attendee type custom field 9 | | | | yes | yes | text |
| expense-attendee-type-id | Expense attendee type | | | | yes | yes | integer(11) |
| expense-attendee-type-name | Expense attendee type name | | | | | yes | [Expense Attendee Type](https://compass.coupa.com/x286047.xml) |
| first-name | First name | yes | | | yes | yes | string(308) |
| id | Coupa unique identifier | | | | | yes | integer |
| last-name | Last name | yes | | | yes | yes | string(308) |
| title | Title | | | | yes | yes | string(308) |
| title-active | Title field in use | | | | | yes | |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| user-id | Coupa's unique ID for the user | | | | yes | yes | integer(11) |
