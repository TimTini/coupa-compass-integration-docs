---
title: "Budget Lines API (/budget lines)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/budget-lines-api-(budget-lines)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/budget-lines-api-(budget-lines)"
status_code: 200
fetched_at: "2026-04-09T11:59:09+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Budget Lines API (/budget lines)"
---

# Budget Lines API (/budget lines)

Use the budget line API to create and update budget lines that you have associated with your
accounts.

The URL to access budget lines is: `https:///api/budget lines`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- If submitting this API using a static Chart of Accounts-based budget period, any
segment values included must be from an existing account.

- If submitting this API using a dynamic Chart of Accounts, any segment values included
must match existing account segments or lookup values. This API does not directly create
the account.

## Actions

The Budget Lines API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/budget_lines/:id/adjust` | adjust | Create budget line adjustment for budget line |
| POST | `/api/budget_lines` | create | Create budget line |
| GET | `/api/budget_lines` | index | Query budget lines |
| GET | `/api/budget_lines/:id` | show | Show budget line |
| PUT | `/api/budget_lines/:id` | update | Update budget line |

## Elements

The following elements are available for the Budget Lines API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | amount | | | | | yes | decimal |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency of transaction | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| description | description | | | | yes | yes | string |
| error-on-overrun | Prevent submission of requisitions that would exceed the budget | | | | yes | yes | boolean |
| id | Coupa unique identifier | | | | | yes | integer |
| notes | notes | | | | yes | yes | text |
| overrun-calculation | overrun_calculation | | | | yes | yes | integer |
| owner | budget owner | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| owner-is-approver | Owner is approver? | | | | yes | yes | integer |
| pending_requisitions_amount | Amount consumed by pending requisitions | | | | | yes | decimal |
| period | This is the nickname for the budget line. Users can view and search against this field through the user interface. | yes | | | yes | yes | Period |
| remaining | remaining | | | | | yes | decimal |
| remaining-budget | Remaining Budget | | | | yes | | decimal |
| segment-1 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-10 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-11 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-12 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-13 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-14 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-15 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-16 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-17 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-18 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-19 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-2 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-20 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-3 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-4 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-5 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-6 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-7 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-8 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| segment-9 | Optionally provide each segment individually.This is required if any of segments contains the dash "-" character, which prevents the Budgeting Segment code from being split automatically | | | | yes | yes | string |
| set-amount-from-xml | set_amount_from_xml | | | | yes | | |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- For large data set and performance optimization, always limit your result with some
GET criteria.

- You can use POST to create new budget lines for existing budget periods and existing
account segments (that is, segment-1, segment-2, and so on). This means that you
cannot create new budget periods using the API.

- Once the budget line is created and associated with an account type (that is, a
chart of accounts) and specific account, you cannot change this information.
