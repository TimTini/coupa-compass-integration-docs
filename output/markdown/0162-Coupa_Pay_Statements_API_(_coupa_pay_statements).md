---
title: "Coupa Pay Statements API (/coupa_pay/statements)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/coupa-pay-statements-api-(coupa_paystatements)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/coupa-pay-statements-api-(coupa_paystatements)"
status_code: 200
fetched_at: "2026-04-09T11:59:39+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Coupa Pay Statements API (/coupa_pay/statements)"
---

# Coupa Pay Statements API (/coupa_pay/statements)

## Overview

Corporate card payment partner statements that have a status of
approved for payment may be retrieved from Coupa to the
ERP using a GET request sent to the Statements API
endpoint: `https://{your_instance_name}/api/coupa_pay/statements`

Once a statement is exported for accounting or ERP payment,
that statement should be marked as exported using the PUT
call, so it is not retrieved a second
time.

API Operations supported:

- GET

- PUT(only to mark exported)

The API key used to fetch/update data must have permission to
index, show, and update Api/Coupa_Pay/Statements data.

Statement data can be queried by all fields within the payload.
Typical query parameters are:

- ?exported=false

- ?payment-partner[issuing-bank]=<*Bank_Name*>

- ?status=approved_for_payment (status is not in the
payload response)

These query parameters can be combined into a statement like the
following:

- API GET
`https://{`
*your_instance_name*
`}/api/coupa_pay/statements?status=approved_for_payment&exported=false&payment-partner[issuing-bank]=`
*XYZBank*

- This will return statements for XYZBank Issuer Payment
Partner that are approved but not exported.

- For ERP payments you should only pull approved statements
from Coupa to the ERP.

An exported statement should be marked as exported
once it is fetched successfully. You can do that with a call
like the following:

- API PUT
`https://{`
*your_instance_name*
`}/api/coupa_pay/statements/?exported=true`
OR

- API PUT
`https://{`
*your_instance_name*
`}/api/coupa_pay/statements/` with
a payload like:

- `true`

## Elements

| **Field Name** | **Field Description** | **Required Field?** | **Unique** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Unique identifier (read-only) | | Yes | | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ (read-only) | | | | | yes | string($datetime) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ (read-only) | | | | | yes | string($datetime) |
| external-ref-id | External reference identifier | Yes | | | | yes | string(255) |
| coupa-pay-id | | | | | | yes | integer |
| name | Name | | | | | | string(255) |
| amount | dollar amount for this allocation | | | | | yes | decimal(30,2) |
| statement-date | Receipt timestamp in the format: YYYY-MM-DDTHH:MM:SS+HH:MMZ | Yes | | | | yes | string($datetime) |
| number-of-lines | (read-only) | | | | | Yes | integer |
| total | Sum of all statement lines (read-only) | | | | | Yes | decimal(16,10) |
| last-exported-at | timestamp | | | | | | string($datetime) |
| exported | True / False was the statement sent to an external system of record. (read-only) | | | | | Yes | boolean |
| payment-partner | Coupa Pay - Virtual Card Partner | | | | | | |
| currency | Currency | yes | | | | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
