---
title: "Expense Reports API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-reports-api"
status_code: 200
fetched_at: "2026-04-09T11:59:45+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
  - "Expense Reports API"
---

# Expense Reports API

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| PUT | `/api/expense_reports/:id/add_approver` | add_approver | Manually add an approver for an expense report |
| POST | `/api/expense_reports` | create | Create an expense report in draft status |
| GET | `/api/expense_reports` | index | Query expense reports |
| PUT | `/api/expense_reports/:id/remove_approval` | remove_approval | Remove an approver who was manually added |
| GET | `/api/expense_reports/:id` | show | Show expense report |
| GET | `/api/expense_reports/:id/download` | download | Download all receipts associated with an expense report in .zip file format |
| PUT | `/api/expense_reports/:id/submit` | submit | Create an expense report and attempt to submit it for approval |
| PUT | `/api/expense_reports/:id` | update | Update expense report |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| approvals | Approvals | | | | | yes | [Approval](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/approvals-api-(approvals)) |
| audit-score | Coupa's Audit Score | | | | | yes | integer |
| auditor-note | Auditor Comments on Expense Report | | | | yes | yes | text |
| comments | Comments | | | | | yes | [Comment](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/comments-api) |
| created-at | Time of Record Creation | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| currency | Currency Code | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| end-date | Return date | | | | yes | yes | date |
| erp-document-id | Expense document id on ERP side | | | | yes | yes | string(255) |
| erp-document-status | Expense document status on ERP side | | | | yes | yes | string(255) |
| events | Events | | | | | yes | ExpenseReportEventHistory |
| expense-lines | Expense lines | | | | yes | yes | [ExpenseLine](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api) |
| expense-policy-violations | Expense policy violations | | | | | yes | ExpensePolicyViolation |
| expense-violations | Expense violations | | | | | yes | [ExpenseViolation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-violation-api) |
| expensed-by | Expensed by user | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| exported | Indicates if transaction has been exported | | | | | yes | boolean |
| external-src-name | External source name | | | | yes | yes | string(255) |
| external-src-ref | External source reference | | | | yes | yes | string(255) |
| id | Coupa's Expense Report ID | | | | | yes | integer |
| is-trip | Trip Report | | | | yes | yes | boolean |
| last-exported-at | Date and time transaction was last exported in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| paid | Has expense report been paid? | | | | yes | yes | boolean |
| past-due | Report has passed the due date in the format True or false | | | true, false | | yes | boolean |
| payment | Payment | | | | yes | yes | Payment |
| payment-channel | Channel used to pay the Reimbursable Total. | | | | | yes | string(255) |
| reconciliation-lines | Payments | | | | | yes | [] |
| reimbursable-total-amount | Amount reimbursable to the End User. | | | | | yes | decimal(32,4) |
| reimbursable-total-currency | Currency of Reimbursable Total. | | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| reject-reason | Reason why report was rejected | | | | yes | yes | text |
| report-due-date | Due date before which report needs to be submitted in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| start-date | Departure date | | | | yes | yes | boolean |
| status | Current Expense Report Status | | | | | yes | string(255) |
| submitted-at | Date Expense Report was Submitted for Approval | | | | yes | yes | datetime |
| submitted-by | Submitted by user | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| title | Expense Report Title | | | | yes | yes | string(255) |
| total | Expense Report Total in Transactional Currency | | | | | yes | decimal(32,4) |
| travel-trip | Travel trip | | | | | yes | |
| updated-at | Time of Record Creation | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| report_warnings | Report level warning messages | | | | | yes | string(255) |
