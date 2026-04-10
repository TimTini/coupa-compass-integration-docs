---
title: "Users Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/users-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/users-import"
status_code: 200
fetched_at: "2026-04-09T12:00:49+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Users Import"
---

# Users Import

## Overview

The User Import process read files from the `./Incoming/Users/` in the SFTP.
These files will be moved to the archive folder located at
`./Incoming/Archive/Users/` before being processed in alphanumeric
order.

- Associated fields like `Content Groups`, `Account Group Names`, etc. must already exist. They will not be created through the users
integration (CSV or API).

- Integrations (CSV or API) currently supports only a full default account code. If only a
portion of the default account code is used as a source field, the integration can query
Coupa for any account that matches the partial account with a limit of 1.

## Keys

- Id

- Employee Number

- Login

## Validations

You can update any field if you include `Id`. You can update
`Login` using `Employee Number`. However, you cannot update
`Employee Number` using `Login`. Coupa tries to create a new
record with the login, and the integration will fail.

## User Authentication

Methods that don't use standard Coupa credentials need to be configured in the customer
instance before they are available as choices on a user record. These are case some sample
values and their associated reference field:

- LDAP - "ldap" - The `Login` field is mapped to the LDAP
`sAMAccountName` field

- SAML - "saml" - The `Sso Identifier` field is mapped to the SAML
`NameID`

## User

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Id | No | No | integer | Unique identifier Coupa assigns when a new record is created. It can’t be modified, but can be used to update the record. | |
| Login | Yes | Yes | string(255) | Must be at least 2 characters | |
| Status | No | No | | Possible values are active or inactive. Inactive users cannot login. | |
| Purchasing User | No | No | boolean | Purchasing User License? | |
| Coupa Navi Ai Agent User | No | No | boolean | Navi Ai Agent User License? | |
| Expense User | No | No | boolean | Expense User License? | |
| Sourcing User | No | No | boolean | Sourcing User License? | |
| Inventory User | No | No | boolean | Inventory User License? | |
| Contracts User | No | No | boolean | Contracts User License? | |
| Analytics User | No | No | boolean | Analytics User License? | |
| AI Classification User | No | No | boolean | AI Classification User License? | |
| Spend Guard User | No | No | boolean | Spend Guard User License? | |
| Navi Chatbot User | No | No | boolean | Navi User License? | |
| Contingent Workforce User | No | No | boolean | Contingent Workforce User License? | |
| Risk Assess User | No | No | boolean | Risk Assess User License? | |
| Does the user have a Contract Lifecycle Management Advanced License? | No | No | boolean | Contract Lifecycle Management Advanced License? | |
| Supply Chain User | No | No | boolean | Supply Chain User License? | |
| Travel User | No | No | boolean | Travel User License? | |
| Treasury User | No | No | boolean | Treasury User License? | |
| Authentication Method | No | No | string(255) | Optional field to specify LDAP or SAML authentication if you have either of those enabled | |
| Sso Identifier | No | No | string(255) | Identifier for SSO/SAML | |
| Generate Password And Notify User | No | No | | Set to Yes if you want the system to invite the user to the system and have them set up their password | |
| Email | Yes | Yes | string(255) | User's email address | |
| First Name | Yes | No | string(40) | User's first name | |
| Last Name | Yes | No | string(40) | User's last name | |
| Employee Number | No | Yes | string(255) | User's employee number, often used for cross-referencing with the HR system | |
| Department | No | No | | Must match department name exactly. | |
| Phone Work | No | No | string(255) | Your user's work phone number in the format xxx-yyy-zzzz. Intl numbers must be prefaced by a + sign and the country code. +aa xxx-yyy-zzzz | |
| Phone Mobile | No | No | string(255) | Your user contact's mobile number | |
| Approval Limit | No | No | | The amount and currency code of the approval limit in the form 1000.00 USD. May also be the name of an already created approval limit or position. Setting this field will set Requisition Approval Limit, Expense Approval Limit and Invoice Approval Limit. | |
| Requisition Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. | |
| Expense Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. | |
| Invoice Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. | |
| Contract Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. | |
| Service/Time Sheets Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. | |
| Receipt Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Receipt Approval Limit. | |
| Sourcing Launch Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. This field will set Sourcing Launch Approval Limit | |
| Sourcing Award Approval Limit | No | No | | The amount and currency code of the approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. This field will set Sourcing Award Approval Limit | |
| Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Requisition Self Approval Limit, and Expense Self Approval Limit. | |
| Requisition Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Requisition Self Approval Limit, and Expense Self Approval Limit. | |
| Expense Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Requisition Self Approval Limit, and Expense Self Approval Limit. | |
| Invoice Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Requisition Self Approval Limit, and Expense Self Approval Limit. | |
| Contract Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Requisition Self Approval Limit, and Expense Self Approval Limit. | |
| Receipt Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Receipt Self Approval Limit | |
| Sourcing Launch Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. This field will set Sourcing Launch Self Approval Limit | |
| Sourcing Award Self Approval Limit | No | No | | The amount and currency code of the self approval limit in the form '1000.00 USD'. May also be the name of an already created approval limit or position. This field will set Sourcing Award Self Approval Limit | |
| Escalation Threshold Limit | No | No | | The amount and currency code of the escalation threshold in the form '1000.00 USD'. May also be the name of an already created approval limit or position. Setting this field will set Escalation Threshold. | |
| Approver Login | No | No | | Your user's next approver | |
| Default Chart of Accounts Name | No | No | | Default chart of accounts for this user. | |
| Default Account Code | No | No | | If the user has a particular account that he or she charges most purchases to, you can enter in a default account | |
| Default Account Code Segment-1 | No | No | | Default Account Code Segment-1 | |
| Default Account Code Segment-2 | No | No | | Default Account Code Segment-2 | |
| Default Account Code Segment-3 | No | No | | Default Account Code Segment-3 | |
| Default Account Code Segment-4 | No | No | | Default Account Code Segment-4 | |
| Default Account Code Segment-5 | No | No | | Default Account Code Segment-5 | |
| Default Account Code Segment-6 | No | No | | Default Account Code Segment-6 | |
| Default Account Code Segment-7 | No | No | | Default Account Code Segment-7 | |
| Default Account Code Segment-8 | No | No | | Default Account Code Segment-8 | |
| Default Account Code Segment-9 | No | No | | Default Account Code Segment-9 | |
| Default Account Code Segment-10 | No | No | | Default Account Code Segment-10 | |
| Default Account Code Segment-11 | No | No | | Default Account Code Segment-11 | |
| Default Account Code Segment-12 | No | No | | Default Account Code Segment-12 | |
| Default Account Code Segment-13 | No | No | | Default Account Code Segment-13 | |
| Default Account Code Segment-14 | No | No | | Default Account Code Segment-14 | |
| Default Account Code Segment-15 | No | No | | Default Account Code Segment-15 | |
| Default Account Code Segment-16 | No | No | | Default Account Code Segment-16 | |
| Default Account Code Segment-17 | No | No | | Default Account Code Segment-17 | |
| Default Account Code Segment-18 | No | No | | Default Account Code Segment-18 | |
| Default Account Code Segment-19 | No | No | | Default Account Code Segment-19 | |
| Default Account Code Segment-20 | No | No | | Default Account Code Segment-20 | |
| User Role Names | No | No | | Possible values are User, Buyer, Accounts Payable, Central Receiving, Accounting Supervisor, Edit as Approver, Inventory Manager, and/or Admin. If entering more than one, use a comma to separate. You can also pass custom role names in this element. | |
| Default Currency | No | No | | Enter in the 3-digit currency code. If a value is not provided and the user record doesn't have a default currency already set, then the default currency is set to the instance's reporting currency. | |
| Default Locale | No | No | string(10) | Enter in the 2 or 5 letters locale code. For example: en or en-US. | |
| Content Groups | No | No | | Enter in content groups (for security) | |
| Default Address Location Code | No | No | | For shipping address, enter in location code | |
| Default Address Street 1 | No | No | | For shipping address, enter in street address line 1 | |
| Default Address Street 2 | No | No | | For shipping address, enter in street address line 2 | |
| Default Address Street 3 | No | No | | For shipping address, enter in street address line 3 | |
| Default Address Street 4 | No | No | | For shipping address, enter in street address line 4 | |
| Default Address City | No | No | | For shipping address, enter in city | |
| Default Address State | No | No | | For shipping address, enter in state | |
| Default Address Postal Code | No | No | | For shipping address, enter in postal code | |
| Default Address Country Code | No | No | | For shipping address, enter in country code | |
| Default Address Attention | No | No | | For shipping address, enter in Attention line | |
| Default Address Name | No | No | | For shipping address, enter in address nickname | |
| Remove Default Address | No | No | | Remove the default address for this user | |
| Receive Coupa Emails | No | No | | Possible values are Yes or No. If yes, the person will receive updates from Coupa Service Delivery and Operations on any announcements | |
| Limit Showing of DataTable Views | No | No | | Do now allow user to create datatable views | |
| Account Security Type | No | No | integer | Possible values are '0' (or blank; No account-based restrictions), '1' (Restrict to the user's default Chart of Accounts) or '2' (Restrict based on account groups). | |
| Business Group Security Type | No | No | integer | Sets the content groups for the user. Options include: 0 = No content group restrictions, 1 = Basic content plus selected content groups if content groups are specified, basic content only if no content groups are specified. | 0, 1 |
| Account Group Names | No | No | | Account groups that the user should have access to (for account-based document security) | |
| Approval Group Names | No | No | | Approval groups that the user should belong to | |
| Warehouses | No | No | | Warehouses | |
| Inventory Organizations | No | No | InventoryOrganization | Inventory Organizations | |
| Allow user to upload Invoice images from Coupa Mobile to Invoice Inbox | No | No | boolean | Allow user to upload Invoice images from Coupa Mobile to Invoice Inbox | |
| Mention Name | No | Yes | string(255) | Mention Name | |
| Country Of Residence Code | No | No | | User's country of residence code | |
| Legal Entity Name | No | No | | Legal Entity Name | |
| Seniority Level | No | No | string(255) | Seniority Level | |
| Business Function | No | No | string(255) | Business Function | |
| Employee Payment Channel | No | No | string(255) | Determine how expenses will be paid to the employee. 'ERP' per default and can be switched to 'CoupaPay' if instance allows it. | |
| Allow Employee Payment Account Creation | No | No | boolean | Allow the user to create an Employee Payment Account, regardless of the Employee Payment Channel. | |
| Groups | No | No | UserGroup | Groups | |
| Middle Name | No | No | string(255) | User's middle name | |
| Pcard Name | No | No | | If the user has a purchasing credit card, you can enter in the person's name on the card | |
| Pcard Number | No | No | | Enter in the purchasing credit card's number | |
| Pcard Expiration | No | No | | Enter in the purchasing credit card's expiration date | |
| Pcard Cvv | No | No | | DEPRECATED NO LONGER SUPPORTED | |
| Projects | No | No | | Projects | |
| Invoicing User | No | No | boolean | Invoicing User License? | |

## List of Valid Locales

en, tr, ja, cs, es, da, de-AT, de-CH, de, en-AU, de-BE, de-LU, en-CA, en-GB, en-HK, en-IE,
en-IN, en-ME, en-MT, en-MY, en-NZ, en-PH, en-ZA, es-CO, es-MX, es-PR, es-IC, fi, fr-BE,
fr-CA, fr-CH, fr, hu, fr-LU, it-CH, it, ko, nl-BE, nl, no, pl, pt-BR, pt, ru, ro, sr, sv,
zh-CN, zh-TW, zh-HK, en, tr, ja, cs, es, da, de-AT, de-CH, de, en-AU, en-CA, en-GB, en-IE,
en-ZA, es-CO, es-MX, es-PR, fi, fr-BE, fr-CA, fr-CH, fr, hu, it-CH, it, ko, nl-BE, nl, no,
pl, pt-BR, pt, ru, sv, zh-CN, zh-TW, zh-HK,
