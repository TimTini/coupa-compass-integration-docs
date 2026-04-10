---
title: "Supplier User API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-user-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/supplier-user-api"
status_code: 200
fetched_at: "2026-04-09T11:59:21+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Supplier User API"
---

# Supplier User API

## Associations

This API is associated with the [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

## Elements

The following elements are available for the Supplier User API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-groups | account_groups | | | | yes | yes | Account Group |
| account-security-type | account_security_type | | | | yes | yes | integer |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | | | | yes | yes | true |
| aic-user | Does the user have an AI Classification License? | | | | yes | yes | boolean |
| allow-employee-payment-account-creation | Allow the user to create an Employee Payment Account, regardless of the Employee Payment Channel. | | | | yes | yes | boolean |
| allow-user-to-upload-invoice-from-mobile | Allow user to upload Invoice images from Coupa Mobile to Invoice Inbox | | | | yes | yes | boolean |
| analytics-user | Does the user have an Analytics License? | | | | yes | yes | boolean |
| api-user | Is an API User? | | | | | yes | boolean |
| approval-groups | approval_groups | | | | yes | yes | [User Group](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-groups-api) |
| approval-limit | Maximum amount allowed to approve. | | | | yes | | Approval Limit |
| authentication-method | What Authentication Method will be used (Coupa_Credentials, LDAP, SAML)? | | | | yes | yes | string(255) |
| avatar-thumb-url | Avatar url | | | | | yes | string |
| business-function | The employee's main job role in your company, e.g. Sales, Executive, Administrative, Managerial, etc. | | | | yes | yes | string(255) |
| business-group-security-type | business_group_security_type | | | 0, 1 | yes | yes | integer |
| can-expense-for | can_expense_for | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| category_planner_user | Does the user have a Category Planner License? | | | | yes | yes | boolean |
| category_strategy_user | Does the user have a Category Strategy License? | no | | | | yes | boolean |
| ccw-user | Does the user have a Contingent Workforce License? | | | | yes | yes | boolean |
| clm-advanced-user | Does the user have a Contract Lifecycle Management Advanced License? | | | | yes | yes | boolean |
| content-groups | Content groups | | | | yes | yes | [Business Group](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) |
| contract-approval-limit | Contract approval limit | | | | yes | yes | Approval Limit |
| contract-self-approval-limit | Contract self approval limit | | | | yes | yes | Approval Limit |
| contracts-user | Does the user have a Contracts License? | | | | yes | yes | boolean |
| country-of-residence | Country of residence | | | | yes | yes | Country |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| default-account | default_account | | | | yes | yes | [Account](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)) |
| default-account-type | default_account_type | | | | yes | yes | [Account Type](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| default-address | default_address | | | | yes | yes | [Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)-da-5757-da-5757) |
| default-currency | default_currency | | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| default-locale | Default locale | | | | yes | yes | string(10) |
| department | department | | | | yes | yes | [Department](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)) |
| email | email | yes | yes | | yes | yes | string(255) |
| employee-number | employee number | | yes | | yes | yes | string(255) |
| employee-payment-channel | Determine how expenses will be paid to the employee. 'ERP' per default and can be switched to 'CoupaPay' if instance allows it. | | | | yes | yes | string(255) |
| escalation-threshold | Escalation threshold | | | | yes | yes | Approval Limit |
| expense-approval-limit | expense_approval_limit | | | | yes | yes | Approval Limit |
| expense-self-approval-limit | expense_self_approval_limit | | | | yes | yes | Approval Limit |
| expense-user | Does the user have an Expense License? | | | | yes | yes | boolean |
| expenses-delegated-to | Expenses delegated to | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| firstname | first name | yes | | | yes | yes | string(40) |
| fullname | full name | | | | | yes | string(255) |
| generate-password-and-notify | Set to Yes if you want the system to invite the user to the system and have them set up their password | | | Yes, No | yes | | string |
| id | Coupa unique identifier | | | | | yes | integer |
| inventory-organizations | inventory_organizations | | | | yes | yes | Inventory Organization |
| inventory-user | Inventory user | | | | yes | yes | boolean |
| invoice-approval-limit | invoice_approval_limit | | | | yes | yes | Approval Limit |
| invoice-self-approval-limit | Maximum amount allowed for Invoice self approvals | | | | yes | yes | Approval Limit |
| lastname | last name | yes | | | yes | yes | string(40) |
| legal-entity | Legal Entity | | | | yes | yes | [Legal Entity](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/expenses-api-(expense_reports)/legal-entity-api) |
| login | login | yes | yes | | yes | yes | string(255) |
| manager | Manager | | | | yes | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| mention-name | Mention Name | | yes | | yes | yes | string(255) |
| middlename | middle name | | | | yes | yes | string(255) |
| password | Changed password | | | | yes | | string |
| phone-mobile | phone mobile | | | | yes | yes | Phone Number |
| phone-work | phone work | | | | yes | yes | Phone Number |
| purchasing-user | Does the user have a Purchasing License? | | | | yes | yes | boolean |
| requisition-approval-limit | requisition_approval_limit | | | | yes | yes | Approval Limit |
| requisition-self-approval-limit | requisition_self_approval_limit | | | | yes | yes | Approval Limit |
| risk-assess-user | Does the user have a Risk Assess License? | | | | yes | yes | boolean |
| roles | roles | | | | yes | yes | Role |
| salesforce-enabled | salesforce_enabled | | | | yes | | boolean |
| salesforce-id | salesforce_id | yes | | | yes | yes | string(255) |
| self-approval-limit | Maximum amount allowed for self approvals | | | | yes | | Approval Limit |
| seniority-level | The employee's job grade or band in your company's hierarchy. | | | | yes | yes | string(255) |
| sourcing-user | Sourcing user | | | | yes | yes | boolean |
| spend-guard-user | Does the user have a Spend Guard License? | | | | yes | yes | boolean |
| sso-identifier | User's Single Sign-on ID (SSO ID) | | | | yes | yes | string(255) |
| supply-chain-user | Does the user have a Supply Chain License? | | | | yes | yes | boolean |
| travel-user | Does the user have a Travel License? | | | | yes | yes | boolean |
| treasury_user | Does the user have a Treasury License? | | | | yes | yes | boolean |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| user-groups | User groups | | | | yes | yes | [User Group](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)/user-groups-api) |
| work-confirmation-approval-limit | work_confirmation_approval_limit | | | | yes | yes | Approval Limit |
| working-warehouses | working_warehouses | | | | yes | yes | [Warehouse](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api) |
| msp_user | Boolean flag to tell if the user is of MSP type | | | any | | yes | boolean |
| invoicing_user | Does the user have a Invoicing License? | | | any | yes | | boolean |
