---
title: "Expenses API (/expense_reports)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)"
status_code: 200
fetched_at: "2026-04-09T11:59:41+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Expenses API (/expense_reports)"
---

# Expenses API (/expense_reports)

## Overview

When working with the Expenses API, you've got a few resource
endpoints you can work from:

| **Resource** | **Path** | **Description** |
| --- | --- | --- |
| Full expense reports | `/api/expense_reports/` | Full expense reports that contain information on approvals, comments, users, history, and more. See Actions and Elements below for details. |
| Expense lines | `/api/expense_lines/` | Expense lines that contain information on accounts, preapprovals, types, attendees, and more. See [Expense Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/expense-lines-api) for details. |
| Expense artifacts | `/api/expense_reports/{id}/expense_artifacts` | You can pull individual attachments from the expense header or line using this resource. Path varies on parent item being referenced. |
