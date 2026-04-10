---
title: "Delegates API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/delegates-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/delegates-api"
status_code: 200
fetched_at: "2026-04-09T11:59:38+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Delegates API"
---

# Delegates API

Get delegates data from Coupa to use in your third-party systems. 

## Introduction

The URLs to access delegates is: `https:///api/delegations`.

## Actions

The Delegates API allows you to perform the following actions:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/delegations` | show | Get all delegates in the /delegations table |

## Elements

The following elements are available for the Delegates API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api-In Field?** | **Api-Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| approval-delegate | approval delegate | | | | | yes | boolean |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| delegate | Delegate | yes | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| delegate-id | Delegate | | | | | yes | integer |
| delegator | Delegator | yes | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| delegator-id | Delegator | | | | | yes | |
| end-date | End date | yes | | | | yes | datetime |
| id | Coupa unique identifier | | | | | yes | integer |
| invoice-requester-delegate | Invoice requester delegate | | | | | yes | boolean |
| reason | Reason | yes | | | | yes | string(255) |
| receiving-delegate | Receiving delegate | | | | | yes | boolean |
| review-delegate | Review delegate | | | | | yes | boolean |
| start-date | Start date | yes | | | | yes | datetime |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

## Example cURL request

This cURL request sends a GET call to `/api/delegations`.

```text
curl --location 'https://<instance>.com/api/delegations' \
--header 'Accept: application/xml' \
--header 'Accept: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: _mkra_ctxt=64de41633cd3b523e50fa612a74fcae49aee07a8b4e3c4b71ae59419ce9f4804--200'
```

## Example response

```text
{
"id": 1,
"created-at": "2021-03-18T11:20:50-07:00",
"updated-at": "2021-03-18T11:20:50-07:00",
"delegator-id": 272,
"delegate-id": 273,
"start-date": "2021-03-17T00:00:00-07:00",
"end-date": "2021-03-21T00:00:00-07:00",
"reason": "Testing",
"approval-delegate": true,
"receiving-delegate": false,
"invoice-requester-delegate": false,
"review-delegate": false,
"delegator": {
"id": 272,
"created-at": "2021-03-18T11:16:09-07:00",
"updated-at": "2024-09-03T02:08:51-07:00",
"login": "pradeep_1616091337",
"email": "test@mailosaur.io",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"contracts-user": false,
"analytics-user": false,
"spend-guard-user": false,
"ccw-user": false,
"clm-advanced-user": false,
"supply-chain-user": false,
"risk-assess-user": false,
"travel-user": false,
"treasury-user": false,
"invoicing-user": true,
"employee-number": null,
"firstname": "pradeep_1616091337",
"lastname": "pradeep_1616091337",
"fullname": "pradeep_1616091337 pradeep_1616091337",
"api-user": false,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": null,
"default-locale": null,
"business-group-security-type": 1,
"avatar-thumb-url": null,
"mention-name": "pradeep_1616091337",
"aic-user": false,
"seniority-level": null,
"business-function": null,
"employee-payment-channel": "ERP",
"allow-employee-payment-account-creation": false,
"middlename": null,
"supplier-id": null,
"category-planner-user": false,
"intake-user": false,
"supplier-user": false,
"support-user": false,
"active": true,
"eligible-for-virtual-cards": false,
"allowed-invoice-inboxes": [
{
"name": "Default",
"email-address": "invoices@bizplatform-r41-qe4.coupadev.com"
},
{
"name": "Default",
"email-address": "invoices@bizplatform-r41-qe4.coupadev.com"
}
],
"allow-user-to-upload-invoice-from-mobile": true,
"gpo-entity": null,
"phone-work": null,
"phone-mobile": null,
"country-of-residence": null,
"roles": [
{
"id": 2,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "Admin",
"description": "Full system access to setup and maintain the application",
"omnipotent": true,
"system-role": true
},
{
"id": 3,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true
},
{
"id": 4,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "Buyer",
"description": "Adds ability to manage requisitions, orders, RFQs, suppliers and items, plus access to purchase order reports",
"omnipotent": false,
"system-role": true
},
{
"id": 10103,
"created-at": "2011-11-01T14:11:29-07:00",
"updated-at": "2011-11-01T14:11:29-07:00",
"name": "Split Accounting",
"description": "",
"omnipotent": false,
"system-role": false,
"created-by": {
"id": 1,
"login": "coupasupport",
"employee-number": "",
"firstname": "Coupa",
"lastname": "Support",
"fullname": "Coupa Support",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"employee-number": "",
"firstname": "Coupa",
"lastname": "Support",
"fullname": "Coupa Support",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
}
}
],
"manager": null,
"default-address": null,
"default-account": null,
"default-account-type": null,
"default-currency": {
"id": 1,
"code": "USD",
"decimals": 2
},
"pcard": null,
"department": null,
"legal-entity": null,
"requisition-approval-limit": null,
"expense-approval-limit": null,
"invoice-approval-limit": null,
"contract-approval-limit": null,
"requisition-self-approval-limit": null,
"expense-self-approval-limit": null,
"invoice-self-approval-limit": null,
"contract-self-approval-limit": null,
"work-confirmation-approval-limit": null,
"escalation-threshold": null,
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"user-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"created-by": {
"id": 270,
"login": "e2e",
"employee-number": null,
"firstname": "testname",
"lastname": "testlast",
"fullname": "testname testlast",
"email": "test@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
},
"updated-by": {
"id": 270,
"login": "e2e",
"employee-number": null,
"firstname": "testname",
"lastname": "testlast",
"fullname": "testname testlast",
"email": "test@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
},
"custom-fields": {
"app-platform-e2e-money1718091754": null
}
},
"delegate": {
"id": 273,
"created-at": "2021-03-18T11:16:25-07:00",
"updated-at": "2024-09-03T02:08:51-07:00",
"login": "dhana_1616091337",
"email": "test@mailosaur.io",
"purchasing-user": true,
"expense-user": false,
"sourcing-user": false,
"inventory-user": false,
"contracts-user": false,
"analytics-user": false,
"spend-guard-user": false,
"ccw-user": false,
"clm-advanced-user": false,
"supply-chain-user": false,
"risk-assess-user": false,
"travel-user": false,
"treasury-user": false,
"invoicing-user": true,
"employee-number": null,
"firstname": "dhana_1616091337",
"lastname": "dhana_1616091337",
"fullname": "dhana_1616091337 dhana_1616091337",
"api-user": false,
"salesforce-id": null,
"account-security-type": 0,
"authentication-method": "coupa_credentials",
"sso-identifier": null,
"default-locale": null,
"business-group-security-type": 1,
"avatar-thumb-url": null,
"mention-name": "dhana_1616091337",
"aic-user": false,
"seniority-level": null,
"business-function": null,
"employee-payment-channel": "ERP",
"allow-employee-payment-account-creation": false,
"middlename": null,
"supplier-id": null,
"category-planner-user": false,
"intake-user": false,
"supplier-user": false,
"support-user": false,
"active": true,
"eligible-for-virtual-cards": false,
"allowed-invoice-inboxes": [
{
"name": "Default",
"email-address": "test.com"
},
{
"name": "Default",
"email-address": "test.coupadev.com"
}
],
"allow-user-to-upload-invoice-from-mobile": true,
"gpo-entity": null,
"phone-work": null,
"phone-mobile": null,
"country-of-residence": null,
"roles": [
{
"id": 3,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "User",
"description": "Standard role for all users who need to create and/or approve requisitions",
"omnipotent": false,
"system-role": true
},
{
"id": 4,
"created-at": "2011-08-05T09:46:31-07:00",
"updated-at": "2011-08-05T09:46:31-07:00",
"name": "Buyer",
"description": "Adds ability to manage requisitions, orders, RFQs, suppliers and items, plus access to purchase order reports",
"omnipotent": false,
"system-role": true
}
],
"manager": null,
"default-address": null,
"default-account": null,
"default-account-type": null,
"default-currency": {
"id": 1,
"code": "USD",
"decimals": 2
},
"pcard": null,
"department": null,
"legal-entity": null,
"requisition-approval-limit": null,
"expense-approval-limit": null,
"invoice-approval-limit": null,
"contract-approval-limit": null,
"requisition-self-approval-limit": null,
"expense-self-approval-limit": null,
"invoice-self-approval-limit": null,
"contract-self-approval-limit": null,
"work-confirmation-approval-limit": null,
"escalation-threshold": null,
"expenses-delegated-to": [],
"can-expense-for": [],
"content-groups": [],
"account-groups": [],
"approval-groups": [],
"user-groups": [],
"working-warehouses": [],
"inventory-organizations": [],
"created-by": {
"id": 270,
"login": "e2e",
"employee-number": null,
"firstname": "testname",
"lastname": "testlast",
"fullname": "testname testlast",
"email": "email@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
},
"updated-by": {
"id": 270,
"login": "e2e",
"employee-number": null,
"firstname": "testname",
"lastname": "testlast",
"fullname": "testname testlast",
"email": "email@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
},
"custom-fields": {
"app-platform-e2e-money1718091754": null
}
},
"created-by": {
"id": 1,
"login": "coupasupport",
"employee-number": "",
"firstname": "Coupa",
"lastname": "Support",
"fullname": "Coupa Support",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
},
"updated-by": {
"id": 1,
"login": "coupasupport",
"employee-number": "",
"firstname": "Coupa",
"lastname": "Support",
"fullname": "Coupa Support",
"email": "upgrade+coupasupport@coupa.com",
"salesforce-id": null,
"avatar-thumb-url": null,
"gpo-entity": null,
"custom-fields": null
}
}
```
