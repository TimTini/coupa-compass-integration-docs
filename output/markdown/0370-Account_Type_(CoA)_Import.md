---
title: "Account Type (CoA) Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/account-type-(coa)-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/account-type-(coa)-import"
status_code: 200
fetched_at: "2026-04-09T12:00:32+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Account Type (CoA) Import"
---

# Account Type (CoA) Import

## Possible values

Item Invoice Matching Level
2-way, 3-way, 3-way-direct, none
Service Invoice Matching Level
2-way, 3-way, 3-way-direct, none

## Chart Of Accounts

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(50) | This is the name for the chart of accounts. Users can view this field through the user interface if they have access to more than one. | |
| Active | Yes | No | boolean | A false value will inactivate the chart of accounts, making it no longer available to users. A true value will make it active and available to users. | |
| Currency Code | Yes | No | | The accounting currency for the chart of accounts, specified as an ISO-standard currency code (e.g. USD) | |
| Primary Contact Email | No | No | | Email address for the primary contact. The primary contact is used as the default billing contact for purchase orders issued from this chart of accounts, unless the 'use_requester_as_billing_contact' is enabled. | |
| Primary Contact Work Phone | No | No | | Work phone number for the primary contact. The primary contact is used as the default billing contact for purchase orders issued from this chart of accounts, unless the 'use_requester_as_billing_contact' is enabled. | |
| Primary Contact Mobile Phone | No | No | | Mobile phone number for the primary contact. The primary contact is used as the default billing contact for purchase orders issued from this chart of accounts, unless the 'use_requester_as_billing_contact' is enabled. | |
| Primary Contact Fax Phone | No | No | | FAX number for the primary contact. The primary contact is used as the default billing contact for purchase orders issued from this chart of accounts, unless the 'use_requester_as_billing_contact' is enabled. | |
| Primary Contact Given Name | No | No | | Given or first name for the primary contact. The primary contact is used as the default billing contact for purchase orders issued from this chart of accounts, unless the 'use_requester_as_billing_contact' is enabled. | |
| Primary Contact Family Name | No | No | | Family or last name for the primary contact. The primary contact is used as the default billing contact for purchase orders issued from this chart of accounts, unless the 'use_requester_as_billing_contact' is enabled. | |
| Primary Address Location Code | No | No | | Location code for the primary address. This field is optional, but if specified will be used to look up an existing company address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address Street 1 | No | No | | First address line for the primary address. This field is required, unless a valid location code for an existing address is specified or the 'use_ship_to_as_bill_to' option is enabled. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address Street 2 | No | No | | Second address line for the primary address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address Street 3 | No | No | | Third address line for the primary address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address Street 4 | No | No | | Fourth address line for the primary address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address City | No | No | | City for the primary address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address State | No | No | | State or province for the primary address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address Postal Code | No | No | | ZIP or postal code for the primary address. The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address Country Code | No | No | | Country for the primary address, specified as an ISO-standard country code (e.g. US). The primary address is used as the default billing address for purchase orders issued from this chart of accounts. | |
| Primary Address VAT ID | No | No | | Primary Address VAT ID | |
| Primary Address Local Tax Number | No | No | | Primary Address Local Tax Number | |
| PO Boilerplate Terms | No | No | | Customizable text that will appear at the bottom of the default PO liquid template, intended to be used to include standard terms and conditions on all outbound purchase orders. | |
| Segment 1 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 1 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 2 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 2 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 3 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 3 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 4 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 4 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 5 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 5 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 6 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 6 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 7 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 7 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 8 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 8 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 9 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 9 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 10 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 10 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 11 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 11 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 12 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 12 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 13 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 13 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 14 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 14 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 15 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 15 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 16 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 16 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 17 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 17 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 18 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 18 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 19 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 19 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 20 Field Type Code | No | No | | Short code (max 8 characters) identifying what segment 20 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 1 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 1 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 2 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 2 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 3 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 3 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 4 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 4 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 5 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 5 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 6 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 6 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 7 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 7 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 8 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 8 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 9 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 9 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 10 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 10 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 11 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 11 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 12 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 12 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 13 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 13 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 14 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 14 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 15 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 15 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 16 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 16 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 17 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 17 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 18 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 18 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 19 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 19 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Segment 20 Field Type Name | No | No | | Short name (max 50 characters) identifying what segment 20 of this chart of accounts represents, if anything, e.g. ORG or PROJECT. | |
| Quantity-Based Line Quantity Percent Tolerance | No | No | | Quantity-Based Line Quantity Percent Tolerance | |
| Quantity-Based Line Price Amount Tolerance | No | No | | Quantity-Based Line Price Amount Tolerance | |
| Quantity-Based Line Price Percent Tolerance | No | No | | Quantity-Based Line Price Percent Tolerance | |
| Amount-Based Line Price Amount Tolerance | No | No | | Amount-Based Line Price Amount Tolerance | |
| Amount-Based Line Price Percent Tolerance | No | No | | Amount-Based Line Price Percent Tolerance | |
| Non-Backed Line Amount Tolerance | No | No | | Non-Backed Line Amount Tolerance | |
| Total Amount Tolerance | No | No | | Total Amount Tolerance | |
| Company Name | No | No | | Company Name | |
| Supplier Created Invoices Quantity-Based Line Quantity Percent Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Quantity Percent Tolerance | |
| Supplier Created Invoices Quantity-Based Line Price Amount Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Price Amount Tolerance | |
| Supplier Created Invoices Quantity-Based Line Price Percent Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Price Percent Tolerance | |
| Supplier Created Invoices Amount-Based Line Price Amount Tolerance | No | No | | Supplier Created Invoices Amount-Based Line Price Amount Tolerance | |
| Supplier Created Invoices Amount-Based Line Price Percent Tolerance | No | No | | Supplier Created Invoices Amount-Based Line Price Percent Tolerance | |
| Default Payment Term Code | No | No | | Default Payment Term Code | |
| Default Shipping Term Code | No | No | | Default Shipping Term Code | |
| Supplier Created Invoices Total Amount Tolerance | No | No | | Supplier Created Invoices Total Amount Tolerance | |
| Extras Amount Tolerance | No | No | | Extras Amount Tolerance | |
| Supplier Created Invoices Extras Amount Tolerance | No | No | | Supplier Created Invoices Extras Amount Tolerance | |
| Extras Percent Tolerance | No | No | | Extras Percent Tolerance | |
| Supplier Created Invoices Extras Percent Tolerance | No | No | | Supplier Created Invoices Extras Percent Tolerance | |
| Receiving Self-Service Quantity Percent PO Tolerance | No | No | | Receiving Self-Service Quantity Percent PO Tolerance | |
| Receiving Self-Service Amount Percent PO Tolerance | No | No | | Receiving Self-Service Amount Percent PO Tolerance | |
| Receiving Self-Service Amount Price PO Tolerance | No | No | | Receiving Self-Service Amount Price PO Tolerance | |
| Receiving Self-Service Quantity Percent Invoice Tolerance | No | No | | Receiving Self-Service Quantity Percent Invoice Tolerance | |
| Receiving Self-Service Amount Percent Invoice Tolerance | No | No | | Receiving Self-Service Amount Percent Invoice Tolerance | |
| Receiving Self-Service Amount Price Invoice Tolerance | No | No | | Receiving Self-Service Amount Price Invoice Tolerance | |
| Receiving Quantity Percent PO Tolerance | No | No | | Receiving Quantity Percent PO Tolerance | |
| Receiving Amount Percent PO Tolerance | No | No | | Receiving Amount Percent PO Tolerance | |
| Receiving Amount Price PO Tolerance | No | No | | Receiving Amount Price PO Tolerance | |
| Receiving Quantity Percent Invoice Tolerance | No | No | | Receiving Quantity Percent Invoice Tolerance | |
| Receiving Amount Percent Invoice Tolerance | No | No | | Receiving Amount Percent Invoice Tolerance | |
| Receiving Amount Price Invoice Tolerance | No | No | | Receiving Amount Price Invoice Tolerance | |
| Logo Image URL | No | No | | Logo Image URL | |
| Segment 1 Req Default Model | No | No | | Object to pull the default value for segment 1 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 1 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 1 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 2 Req Default Model | No | No | | Object to pull the default value for segment 2 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 2 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 1 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 3 Req Default Model | No | No | | Object to pull the default value for segment 3 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 3 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 1 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 4 Req Default Model | No | No | | Object to pull the default value for segment 4 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 4 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 4 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 5 Req Default Model | No | No | | Object to pull the default value for segment 5 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 5 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 5 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 6 Req Default Model | No | No | | Object to pull the default value for segment 6 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 6 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 6 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 7 Req Default Model | No | No | | Object to pull the default value for segment 7 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 7 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 7 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 8 Req Default Model | No | No | | Object to pull the default value for segment 8 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 8 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 8 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 9 Req Default Model | No | No | | Object to pull the default value for segment 9 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 9 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 9 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 10 Req Default Model | No | No | | Object to pull the default value for segment 10 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 10 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 10 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 11 Req Default Model | No | No | | Object to pull the default value for segment 11 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 11 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 11 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 12 Req Default Model | No | No | | Object to pull the default value for segment 12 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 12 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 12 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 13 Req Default Model | No | No | | Object to pull the default value for segment 13 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 13 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 13 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 14 Req Default Model | No | No | | Object to pull the default value for segment 14 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 14 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 14 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 15 Req Default Model | No | No | | Object to pull the default value for segment 15 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 15 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 15 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 16 Req Default Model | No | No | | Object to pull the default value for segment 16 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 16 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 16 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 17 Req Default Model | No | No | | Object to pull the default value for segment 17 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 17 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 17 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 18 Req Default Model | No | No | | Object to pull the default value for segment 18 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 18 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 18 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 19 Req Default Model | No | No | | Object to pull the default value for segment 19 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 19 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 19 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 20 Req Default Model | No | No | | Object to pull the default value for segment 20 from when attempting to default an account on a requisition line. This can be 'user', 'department', 'commodity', 'supplier', 'item', or 'address'. | |
| Segment 20 Req Default Column | No | No | | Attribute of the object to pull the default value for segment 20 from attempting to default an account on a requisition line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| PO Layout URL | No | No | | PO Layout URL | |
| Use Default PO Layout | No | No | | Use Default PO Layout | |
| Min Amount Tolerance | No | No | | Min Amount Tolerance | |
| Supplier Created Invoices Min Amount Tolerance | No | No | | Supplier Created Invoices Min Amount Tolerance | |
| Segment 1 Expense Default Model | No | No | | Object to pull the default value for segment 1 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 1 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 1 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 2 Expense Default Model | No | No | | Object to pull the default value for segment 2 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 2 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 2 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 3 Expense Default Model | No | No | | Object to pull the default value for segment 3 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 3 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 3 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 4 Expense Default Model | No | No | | Object to pull the default value for segment 4 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 4 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 4 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 5 Expense Default Model | No | No | | Object to pull the default value for segment 5 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 5 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 5 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 6 Expense Default Model | No | No | | Object to pull the default value for segment 6 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 6 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 6 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 7 Expense Default Model | No | No | | Object to pull the default value for segment 7 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 7 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 7 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 8 Expense Default Model | No | No | | Object to pull the default value for segment 8 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 8 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 8 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 9 Expense Default Model | No | No | | Object to pull the default value for segment 9 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 9 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 9 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 10 Expense Default Model | No | No | | Object to pull the default value for segment 10 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 10 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 10 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 11 Expense Default Model | No | No | | Object to pull the default value for segment 11 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 11 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 11 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 12 Expense Default Model | No | No | | Object to pull the default value for segment 12 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 12 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 12 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 13 Expense Default Model | No | No | | Object to pull the default value for segment 13 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 13 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 13 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 14 Expense Default Model | No | No | | Object to pull the default value for segment 14 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 14 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 14 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 15 Expense Default Model | No | No | | Object to pull the default value for segment 15 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 15 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 15 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 16 Expense Default Model | No | No | | Object to pull the default value for segment 16 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 16 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 16 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 17 Expense Default Model | No | No | | Object to pull the default value for segment 17 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 17 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 17 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 18 Expense Default Model | No | No | | Object to pull the default value for segment 18 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 18 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 18 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 19 Expense Default Model | No | No | | Object to pull the default value for segment 19 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 19 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 19 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 20 Expense Default Model | No | No | | Object to pull the default value for segment 20 from when attempting to default an account on an expense report line. This can be 'user', 'department', 'expense_category'. | |
| Segment 20 Expense Default Column | No | No | | Attribute of the object to pull the default value for segment 20 from attempting to default an account on an expense report line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 1 Invoice Default Model | No | No | | Object to pull the default value for segment 1 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 1 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 1 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 2 Invoice Default Model | No | No | | Object to pull the default value for segment 2 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 2 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 2 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 3 Invoice Default Model | No | No | | Object to pull the default value for segment 3 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 3 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 3 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 4 Invoice Default Model | No | No | | Object to pull the default value for segment 4 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 4 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 4 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 5 Invoice Default Model | No | No | | Object to pull the default value for segment 5 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 5 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 5 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 6 Invoice Default Model | No | No | | Object to pull the default value for segment 6 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 6 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 6 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 7 Invoice Default Model | No | No | | Object to pull the default value for segment 7 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 7 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 7 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 8 Invoice Default Model | No | No | | Object to pull the default value for segment 8 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 8 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 8 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 9 Invoice Default Model | No | No | | Object to pull the default value for segment 9 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 9 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 9 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 10 Invoice Default Model | No | No | | Object to pull the default value for segment 10 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 10 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 10 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 11 Invoice Default Model | No | No | | Object to pull the default value for segment 11 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 11 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 11 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 12 Invoice Default Model | No | No | | Object to pull the default value for segment 12 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 12 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 12 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 13 Invoice Default Model | No | No | | Object to pull the default value for segment 13 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 13 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 13 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 14 Invoice Default Model | No | No | | Object to pull the default value for segment 14 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 14 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 14 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 15 Invoice Default Model | No | No | | Object to pull the default value for segment 15 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 15 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 15 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 16 Invoice Default Model | No | No | | Object to pull the default value for segment 16 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 16 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 16 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 17 Invoice Default Model | No | No | | Object to pull the default value for segment 17 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 17 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 17 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 18 Invoice Default Model | No | No | | Object to pull the default value for segment 18 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 18 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 18 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 19 Invoice Default Model | No | No | | Object to pull the default value for segment 19 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 19 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 19 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Segment 20 Invoice Default Model | No | No | | Object to pull the default value for segment 20 from when attempting to default an account on an invoice line. This can be 'user', 'department', 'commodity', 'supplier', 'item', 'address'. 'user' and 'department' reference the requester and requester's department. | |
| Segment 20 Invoice Default Column | No | No | | Attribute of the object to pull the default value for segment 20 from attempting to default an account on an invoice line. For custom fields, this is the field name you specified when defining the field. To use a user's default account, use 'default_account.current_code'. | |
| Use Ship To as Bill To | No | No | | Use Ship To as Bill To | |
| Use Requester As Billing Contact | No | No | | Use Requester As Billing Contact | |
| Supplier Created Invoices Non-Backed Line Amount Tolerance | No | No | | Supplier Created Invoices Non-Backed Line Amount Tolerance | |
| Contract-Backed Line Amount Tolerance | No | No | | Contract-Backed Line Amount Tolerance | |
| Supplier Created Invoices Contract-Backed Line Amount Tolerance | No | No | | Supplier Created Invoices Contract-Backed Line Amount Tolerance | |
| Line Tax and Tax Engine Calculation Difference Percent Tolerance | No | No | | Line Tax and Tax Engine Calculation Difference Percent Tolerance | |
| Header Tax and Tax Engine Calculation Difference Percent Tolerance | No | No | | Header Tax and Tax Engine Calculation Difference Percent Tolerance | |
| Supplier Created Invoices Line Tax and Tax Engine Calculation Difference Percent Tolerance | No | No | | Supplier Created Invoices Line Tax and Tax Engine Calculation Difference Percent Tolerance | |
| Supplier Created Invoices Header Tax and Tax Engine Calculation Difference Percent Tolerance | No | No | | Supplier Created Invoices Header Tax and Tax Engine Calculation Difference Percent Tolerance | |
| Dynamic Flag | No | No | boolean | Flag specifying whether the accounts for this chart of accounts will be loaded as combinations (static) or specified segment-by-segment (dynamic). This should be specified as Yes or No. | |
| Segment 1 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 2 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 3 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 4 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 5 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 6 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 7 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 8 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 9 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 10 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 11 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 12 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 13 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 14 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 15 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 16 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 17 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 18 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 19 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 20 Lookup Name | No | No | | For dynamic charts of accounts, this specifies the name of the already-defined Lookup that contains valid values for this segment. | |
| Segment 2 Lookup Level | No | No | | Segment 2 Lookup Level | |
| Segment 2 Parent | No | No | | Segment 2 Parent | |
| Segment 3 Lookup Level | No | No | | Segment 3 Lookup Level | |
| Segment 3 Parent | No | No | | Segment 3 Parent | |
| Segment 4 Lookup Level | No | No | | Segment 4 Lookup Level | |
| Segment 4 Parent | No | No | | Segment 4 Parent | |
| Segment 5 Lookup Level | No | No | | Segment 5 Lookup Level | |
| Segment 5 Parent | No | No | | Segment 5 Parent | |
| Segment 6 Lookup Level | No | No | | Segment 6 Lookup Level | |
| Segment 6 Parent | No | No | | Segment 6 Parent | |
| Segment 7 Lookup Level | No | No | | Segment 7 Lookup Level | |
| Segment 7 Parent | No | No | | Segment 7 Parent | |
| Segment 8 Lookup Level | No | No | | Segment 8 Lookup Level | |
| Segment 8 Parent | No | No | | Segment 8 Parent | |
| Segment 9 Lookup Level | No | No | | Segment 9 Lookup Level | |
| Segment 9 Parent | No | No | | Segment 9 Parent | |
| Segment 10 Lookup Level | No | No | | Segment 10 Lookup Level | |
| Segment 10 Parent | No | No | | Segment 10 Parent | |
| Segment 11 Lookup Level | No | No | | Segment 11 Lookup Level | |
| Segment 11 Parent | No | No | | Segment 11 Parent | |
| Segment 12 Lookup Level | No | No | | Segment 12 Lookup Level | |
| Segment 12 Parent | No | No | | Segment 12 Parent | |
| Segment 13 Lookup Level | No | No | | Segment 13 Lookup Level | |
| Segment 13 Parent | No | No | | Segment 13 Parent | |
| Segment 14 Lookup Level | No | No | | Segment 14 Lookup Level | |
| Segment 14 Parent | No | No | | Segment 14 Parent | |
| Segment 15 Lookup Level | No | No | | Segment 15 Lookup Level | |
| Segment 15 Parent | No | No | | Segment 15 Parent | |
| Segment 16 Lookup Level | No | No | | Segment 16 Lookup Level | |
| Segment 16 Parent | No | No | | Segment 16 Parent | |
| Segment 17 Lookup Level | No | No | | Segment 17 Lookup Level | |
| Segment 17 Parent | No | No | | Segment 17 Parent | |
| Segment 18 Lookup Level | No | No | | Segment 18 Lookup Level | |
| Segment 18 Parent | No | No | | Segment 18 Parent | |
| Segment 19 Lookup Level | No | No | | Segment 19 Lookup Level | |
| Segment 19 Parent | No | No | | Segment 19 Parent | |
| Segment 20 Lookup Level | No | No | | Segment 20 Lookup Level | |
| Segment 20 Parent | No | No | | Segment 20 Parent | |
| Segment 2 Required | No | No | | Flag specifying whether segment 2 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 3 Required | No | No | | Flag specifying whether segment 3 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 4 Required | No | No | | Flag specifying whether segment 4 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 5 Required | No | No | | Flag specifying whether segment 5 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 6 Required | No | No | | Flag specifying whether segment 6 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 7 Required | No | No | | Flag specifying whether segment 7 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 8 Required | No | No | | Flag specifying whether segment 8 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 9 Required | No | No | | Flag specifying whether segment 9 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 10 Required | No | No | | Flag specifying whether segment 10 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 11 Required | No | No | | Flag specifying whether segment 11 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 12 Required | No | No | | Flag specifying whether segment 12 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 13 Required | No | No | | Flag specifying whether segment 13 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 14 Required | No | No | | Flag specifying whether segment 14 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 15 Required | No | No | | Flag specifying whether segment 15 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 16 Required | No | No | | Flag specifying whether segment 16 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 17 Required | No | No | | Flag specifying whether segment 17 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 18 Required | No | No | | Flag specifying whether segment 18 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 19 Required | No | No | | Flag specifying whether segment 19 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 20 Required | No | No | | Flag specifying whether segment 20 is required for all accounts in this chart of accounts. Segment 1 is always required. | |
| Segment 1 Locked | No | No | | Flag specifying whether segment 1 is locked for all accounts in this chart of accounts. | |
| Segment 1 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 1. | |
| Segment 2 Locked | No | No | | Flag specifying whether segment 2 is locked for all accounts in this chart of accounts. | |
| Segment 2 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 2. | |
| Segment 3 Locked | No | No | | Flag specifying whether segment 3 is locked for all accounts in this chart of accounts. | |
| Segment 3 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 3. | |
| Segment 4 Locked | No | No | | Flag specifying whether segment 4 is locked for all accounts in this chart of accounts. | |
| Segment 4 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 4. | |
| Segment 5 Locked | No | No | | Flag specifying whether segment 5 is locked for all accounts in this chart of accounts. | |
| Segment 5 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 5. | |
| Segment 6 Locked | No | No | | Flag specifying whether segment 6 is locked for all accounts in this chart of accounts. | |
| Segment 6 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 6. | |
| Segment 7 Locked | No | No | | Flag specifying whether segment 7 is locked for all accounts in this chart of accounts. | |
| Segment 7 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 7. | |
| Segment 8 Locked | No | No | | Flag specifying whether segment 8 is locked for all accounts in this chart of accounts. | |
| Segment 8 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 8. | |
| Segment 9 Locked | No | No | | Flag specifying whether segment 9 is locked for all accounts in this chart of accounts. | |
| Segment 9 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 9. | |
| Segment 10 Locked | No | No | | Flag specifying whether segment 10 is locked for all accounts in this chart of accounts. | |
| Segment 10 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 10. | |
| Segment 11 Locked | No | No | | Flag specifying whether segment 11 is locked for all accounts in this chart of accounts. | |
| Segment 11 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 11. | |
| Segment 12 Locked | No | No | | Flag specifying whether segment 12 is locked for all accounts in this chart of accounts. | |
| Segment 12 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 12. | |
| Segment 13 Locked | No | No | | Flag specifying whether segment 13 is locked for all accounts in this chart of accounts. | |
| Segment 13 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 13. | |
| Segment 14 Locked | No | No | | Flag specifying whether segment 14 is locked for all accounts in this chart of accounts. | |
| Segment 14 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 14. | |
| Segment 15 Locked | No | No | | Flag specifying whether segment 15 is locked for all accounts in this chart of accounts. | |
| Segment 15 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 15. | |
| Segment 16 Locked | No | No | | Flag specifying whether segment 16 is locked for all accounts in this chart of accounts. | |
| Segment 16 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 16. | |
| Segment 17 Locked | No | No | | Flag specifying whether segment 17 is locked for all accounts in this chart of accounts. | |
| Segment 17 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 17. | |
| Segment 18 Locked | No | No | | Flag specifying whether segment 18 is locked for all accounts in this chart of accounts. | |
| Segment 18 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 18. | |
| Segment 19 Locked | No | No | | Flag specifying whether segment 19 is locked for all accounts in this chart of accounts. | |
| Segment 19 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 19. | |
| Segment 20 Locked | No | No | | Flag specifying whether segment 20 is locked for all accounts in this chart of accounts. | |
| Segment 20 Apply Requisition Default to PO Change | No | No | | Flag specifying whether to apply Purchase Request Default to Purchase Order Change for Segment 20. | |
| PO Number Prefix | No | No | | Optional alphanumeric prefix displayed as part of the PO number, sometimes used for integration or disambiguation purposes. | |
| PO Number Length | No | No | | Optional numeric value used to specify a fixed length for the numeric portion of the PO number. If used, the PO number will be padded with 0's up to the specified length for display purposes. Valid values are between 6 and 15, inclusive. | |
| Item Invoice Matching Level | No | No | | Item Invoice Matching Level | |
| Service Invoice Matching Level | No | No | | Service Invoice Matching Level | |
| Line Units of Measure on Invoice and PO Match Boolean Tolerance | No | No | | Line Units of Measure on Invoice and PO Match Boolean Tolerance | |
| Supplier Created Invoices Line Units of Measure on Invoice and PO Match Boolean Tolerance | No | No | | Supplier Created Invoices Line Units of Measure on Invoice and PO Match Boolean Tolerance | |
| PO Email Actions Enabled | No | No | | PO Email Actions Enabled | |
| Days Backdating Tolerance | No | No | | Days Backdating Tolerance | |
| Supplier Created Invoices Days Backdating Tolerance | No | No | | Supplier Created Invoices Days Backdating Tolerance | |
| Extras Shipping Amount Tolerance | No | No | | Extras Shipping Amount Tolerance | |
| Extras Shipping Percent Tolerance | No | No | | Extras Shipping Percent Tolerance | |
| Extras Handling Amount Tolerance | No | No | | Extras Handling Amount Tolerance | |
| Extras Handling Percent Tolerance | No | No | | Extras Handling Percent Tolerance | |
| Extras Misc Amount Tolerance | No | No | | Extras Misc Amount Tolerance | |
| Extras Misc Percent Tolerance | No | No | | Extras Misc Percent Tolerance | |
| Extras Total Taxes Amount Tolerance | No | No | | Extras Total Taxes Amount Tolerance | |
| Extras Total Taxes Percent Tolerance | No | No | | Extras Total Taxes Percent Tolerance | |
| Supplier Created Invoices Extras Shipping Amount Tolerance | No | No | | Supplier Created Invoices Extras Shipping Amount Tolerance | |
| Supplier Created Invoices Extras Shipping Percent Tolerance | No | No | | Supplier Created Invoices Extras Shipping Percent Tolerance | |
| Supplier Created Invoices Extras Handling Amount Tolerance | No | No | | Supplier Created Invoices Extras Handling Amount Tolerance | |
| Supplier Created Invoices Extras Handling Percent Tolerance | No | No | | Supplier Created Invoices Extras Handling Percent Tolerance | |
| Supplier Created Invoices Extras Misc Amount Tolerance | No | No | | Supplier Created Invoices Extras Misc Amount Tolerance | |
| Supplier Created Invoices Extras Misc Percent Tolerance | No | No | | Supplier Created Invoices Extras Misc Percent Tolerance | |
| Supplier Created Invoices Extras Total Taxes Amount Tolerance | No | No | | Supplier Created Invoices Extras Total Taxes Amount Tolerance | |
| Supplier Created Invoices Extras Total Taxes Percent Tolerance | No | No | | Supplier Created Invoices Extras Total Taxes Percent Tolerance | |
| Invoice line unit price compared to Catalog unit price (Amount) | No | No | | Invoice line unit price compared to Catalog unit price (Amount) | |
| Invoice line unit price compared to Catalog unit price (Percent) | No | No | | Invoice line unit price compared to Catalog unit price (Percent) | |
| Distribute Tax | No | No | | Distribute Tax | |
| Distribute Shipping | No | No | | Distribute Shipping | |
| Distribute Handling | No | No | | Distribute Handling | |
| Distribute Misc | No | No | | Distribute Misc | |
| Allow Billing Notes | No | No | | Allow Billing Notes | |
| Enterprise Code | No | No | | Enterprise Code | |
| Currency Matches PO Currency Boolean Tolerance | No | No | | Currency Matches PO Currency Boolean Tolerance | |
| Supplier Created Invoices Currency Matches PO Currency Boolean Tolerance | No | No | | Supplier Created Invoices Currency Matches PO Currency Boolean Tolerance | |
| Quantity-Based Line Quantity Over Invoiced Quantity Tolerance | No | No | | Quantity-Based Line Quantity Over Invoiced Quantity Tolerance | |
| Quantity-Based Line Quantity Over Invoiced Percent Tolerance | No | No | | Quantity-Based Line Quantity Over Invoiced Percent Tolerance | |
| Amount-Based Line Price Over Invoiced Amount Tolerance | No | No | | Amount-Based Line Price Over Invoiced Amount Tolerance | |
| Amount-Based Line Price Over Invoiced Percent Tolerance | No | No | | Amount-Based Line Price Over Invoiced Percent Tolerance | |
| Supplier Created Invoices Quantity-Based Line Quantity Over Invoiced Quantity Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Quantity Over Invoiced Quantity Tolerance | |
| Supplier Created Invoices Quantity-Based Line Quantity Over Invoiced Percent Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Quantity Over Invoiced Percent Tolerance | |
| Supplier Created Invoices Amount-Based Line Price Over Invoiced Amount Tolerance | No | No | | Supplier Created Invoices Amount-Based Line Price Over Invoiced Amount Tolerance | |
| Supplier Created Invoices Amount-Based Line Price Over Invoiced Percent Tolerance | No | No | | Supplier Created Invoices Amount-Based Line Price Over Invoiced Percent Tolerance | |
| Weight-Based Line Amount Tolerance | No | No | | Weight-Based Line Amount Tolerance | |
| Weight-Based Line Amount Percent Tolerance | No | No | | Weight-Based Line Amount Percent Tolerance | |
| Weight-Based Line Price Amount Tolerance | No | No | | Weight-Based Line Price Amount Tolerance | |
| Weight-Based Line Price Percent Tolerance | No | No | | Weight-Based Line Price Percent Tolerance | |
| Line Weight Units of Measure on Invoice and Item Match Boolean Tolerance | No | No | | Line Weight Units of Measure on Invoice and Item Match Boolean Tolerance | |
| Line Supplier Part Number on Invoice and PO Match Boolean Tolerance | No | No | | Line Supplier Part Number on Invoice and PO Match Boolean Tolerance | |
| Supplier Created Invoices Weight-Based Line Amount Tolerance | No | No | | Supplier Created Invoices Weight-Based Line Amount Tolerance | |
| Supplier Created Invoices Weight-Based Line Amount Percent Tolerance | No | No | | Supplier Created Invoices Weight-Based Line Amount Percent Tolerance | |
| Supplier Created Invoices Weight-Based Line Price Amount Tolerance | No | No | | Supplier Created Invoices Weight-Based Line Price Amount Tolerance | |
| Supplier Created Invoices Weight-Based Line Price Percent Tolerance | No | No | | Supplier Created Invoices Weight-Based Line Price Percent Tolerance | |
| Supplier Created Invoices Line Weight Units of Measure on Invoice and Item Match Boolean Tolerance | No | No | | Supplier Created Invoices Line Weight Units of Measure on Invoice and Item Match Boolean Tolerance | |
| Supplier Created Invoices Line Supplier Part Number on Invoice and PO Match Boolean Tolerance | No | No | | Supplier Created Invoices Line Supplier Part Number on Invoice and PO Match Boolean Tolerance | |
| Header Tax and Tax Engine Calculation Difference Amount Tolerance | No | No | | Header Tax and Tax Engine Calculation Difference Amount Tolerance | |
| Supplier Created Invoices Header Tax and Tax Engine Calculation Difference Amount Tolerance | No | No | | Supplier Created Invoices Header Tax and Tax Engine Calculation Difference Amount Tolerance | |
| Line Tax and Tax Engine Calculation Difference Amount Tolerance | No | No | | Line Tax and Tax Engine Calculation Difference Amount Tolerance | |
| Supplier Created Invoices Line Tax and Tax Engine Calculation Difference Amount Tolerance | No | No | | Supplier Created Invoices Line Tax and Tax Engine Calculation Difference Amount Tolerance | |
| 3-Way Match Under Receiving Tolerance | No | No | | 3-Way Match Under Receiving Tolerance | |
| Supplier Created Invoices 3-Way Match Under Receiving Tolerance | No | No | | Supplier Created Invoices 3-Way Match Under Receiving Tolerance | |
| Invoice Contract Price Percent | No | No | | Invoice Contract Price Percent | |
| Supplier Created Invoice Contract Price Percent | No | No | | Supplier Created Invoice Contract Price Percent | |
| Invoice Contract Price Amount | No | No | | Invoice Contract Price Amount | |
| Supplier Created Invoice Contract Price Amount | No | No | | Supplier Created Invoice Contract Price Amount | |
| Invoice Exchange Rate compared to Coupa Exchange Rate (Percent) | No | No | | Invoice Exchange Rate compared to Coupa Exchange Rate (Percent) | |
| Supplier Created Invoices Invoice Exchange Rate compared to Coupa Exchange Rate (Percent) | No | No | | Supplier Created Invoices Invoice Exchange Rate compared to Coupa Exchange Rate (Percent) | |
| Legal Entity Name | No | No | | Name of the legal entity that this chart of accounts belongs to. The legal entity will provide billing address and tax registrations. | |
| Invoice Payment Terms compared to PO Payment Terms | No | No | | Invoice Payment Terms compared to PO Payment Terms | |
| Supplier Created Invoices Invoice Payment Terms compared to PO Payment Terms | No | No | | Supplier Created Invoices Invoice Payment Terms compared to PO Payment Terms | |
| Invoice Shipping Terms compared to PO Shipping Terms | No | No | | Invoice Shipping Terms compared to PO Shipping Terms | |
| Supplier Created Invoices Invoice Shipping Terms compared to PO Shipping Terms | No | No | | Supplier Created Invoices Invoice Shipping Terms compared to PO Shipping Terms | |
| Invoice account does not match PO account | No | No | | Invoice account does not match PO account | |
| Supplier Created Invoices Invoice account does not match PO account | No | No | | Supplier Created Invoices Invoice account does not match PO account | |
| Quantity-Based Line Amount Over Invoiced Amount Tolerance | No | No | | Quantity-Based Line Amount Over Invoiced Amount Tolerance | |
| Supplier Created Invoices Quantity-Based Line Amount Over Invoiced Amount Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Amount Over Invoiced Amount Tolerance | |
| Quantity-Based Line Amount Over Invoiced Percent Tolerance | No | No | | Quantity-Based Line Amount Over Invoiced Percent Tolerance | |
| Supplier Created Invoices Quantity-Based Line Amount Over Invoiced Percent Tolerance | No | No | | Supplier Created Invoices Quantity-Based Line Amount Over Invoiced Percent Tolerance | |
| Total Taxes Compared to Invoice Net Total Percent Tolerance | No | No | | Total Taxes Compared to Invoice Net Total Percent Tolerance | |
| Supplier Created Invoices Total Taxes Compared to Invoice Net Total Percent Tolerance | No | No | | Supplier Created Invoices Total Taxes Compared to Invoice Net Total Percent Tolerance | |
| Contract Max Spend Line Amount Tolerance | No | No | | Contract Max Spend Line Amount Tolerance | |
| Supplier Created Invoices Contract Max Spend Line Amount Tolerance | No | No | | Supplier Created Invoices Contract Max Spend Line Amount Tolerance | |
| Contract Max Spend Line Percent Tolerance | No | No | | Contract Max Spend Line Percent Tolerance | |
| Supplier Created Invoices Contract Max Spend Line Percent Tolerance | No | No | | Supplier Created Invoices Contract Max Spend Line Percent Tolerance | |
| Invoice Classification of Goods Code and PO Classification of Goods code differ | No | No | | Invoice Classification of Goods Code and PO Classification of Goods code differ | |
| Invoice Fiscal Code and PO Fiscal Code differ | No | No | | Invoice Fiscal Code and PO Fiscal Code differ | |
| Supplier Created Invoices Invoice Classification of Goods Code and PO Classification of Goods code differ | No | No | | Supplier Created Invoices Invoice Classification of Goods Code and PO Classification of Goods code differ | |
| Supplier Created Invoices Invoice Fiscal Code and PO Fiscal Code differ | No | No | | Supplier Created Invoices Invoice Fiscal Code and PO Fiscal Code differ | |
| Receipt Approval Required | No | No | | Receipt Approval Required | |
| Service Sheet Required | No | No | | Service Sheet Required for COA when used in req/po | |
| Service Sheet Budget Period Mode | No | No | | Service Sheet Budget Period Mode | |
