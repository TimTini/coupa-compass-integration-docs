---
title: "Suppliers API (/suppliers)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797"
status_code: 200
fetched_at: "2026-04-09T11:59:17+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
---

# Suppliers API (/suppliers)

## Overview

Use the suppliers API to create, update, and query the suppliers in Coupa.

The URL to access suppliers is: `https:///api/suppliers`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Supplier API GET calls include Supplier Sites in response payloads. For more information, see [Postman Collection for Coupa APIs](https://compass.coupa.com/x285429.xml).

## Actions

The Suppliers API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/suppliers` | create | Create supplier |
| POST | `/api/suppliers/create_supplier_user_preferences` | create_supplier_user_preferences | Create supplier user preferences |
| GET | `/api/suppliers` | index | Query suppliers |
| DELETE | `/api/suppliers/logout_iframe_session` | logout_iframe_session | Log out (CSP)iframe session |
| GET | `/api/suppliers/:id` | show | Show supplier |
| POST | `/api/suppliers/sync_supplier_user_locale` | sync_supplier_user_locale | Sync supplier user locale |
| PUT | `/api/suppliers/:id` | update | Update supplier |

## Elements

The following elements are available for the Suppliers API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-number | Account number | | | | yes | yes | string |
| account-types | Account Types | | | | yes | yes | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| allow-change-requests | Allows suppliers to create change requests from CSP | | | | yes | yes | boolean |
| allow-cn-no-backing-doc-from-connect | If yes, then the supplier can create Credit Notes without backing invoice. | | | | yes | yes | boolean |
| allow-csp-access-without-two-factor | Allows supplier to access Customer's data from CSP without Two Factor | | | | yes | yes | boolean |
| allow-cxml-invoicing | Allow cXML invoicing for Supplier | | | | yes | yes | boolean |
| allow-inv-choose-billing-account | Allow inv choose billing account | | | | yes | yes | boolean |
| allow-inv-from-connect | If yes, then the supplier can create invoices against their POs or Contracts in the CSP | | | | yes | yes | boolean |
| allow-inv-no-backing-doc-from-connect | If yes, then the supplier can create invoices without a backing PO or Contract in the CSP. | | | | yes | yes | boolean |
| allow-inv-unbacked-lines-from-connect | If yes, then the supplier can create unbacked invoices without a backing PO or Contract in the CSP. | | | | yes | yes | boolean |
| allow-order-confirmation-item-substitutions | Allow supplier to propose item substitute on Order Confirmations | | | | yes | yes | boolean |
| business-groups | business groups | | | | yes | yes | [ContentGroup](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)) |
| buyer-hold | Hold all POs for buyer review | | | | yes | yes | boolean |
| contacts | | no | no | any | yes | | [Supplier Information Contacts](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-contact-api) |
| commodity | Default commodity, selectable from drop-down | | | | yes | yes | |
| corporate-url | Corporate URL | | | | yes | | string |
| coupa-connect-secret | Coupa connect secret | | | | | yes | string |
| coupa-pay-financing-only | Only pay financed invoices via Coupa Pay | | | | yes | yes | boolean |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| cxml-domain | "From" , our domain<br>cXML domain | | | | yes | yes | string |
| cxml-http-password | cXML HTTP password | | | | yes | | |
| cxml-http-username | cXML HTTP username | | | | yes | yes | string |
| cxml-identity | "From", our identity<br>cXML identity | | | | yes | yes | string |
| cxml-invoice-buyer-domain | Buyer Domain for cXML Invoicing | | | | yes | yes | string |
| cxml-invoice-buyer-identity | Buyer Identity for cXML Invoicing | | | | yes | yes | string |
| cxml-invoice-secret | Secret Key for cXML Invoicing Authentication | | | | yes | yes | string |
| cxml-invoice-supplier-domain | Supplier Domain for cXML Invoicing | | | | yes | yes | string |
| cxml-invoice-supplier-identity | Supplier Identity for cXML Invoicing | | yes | | yes | yes | string |
| cxml-protocol | Transmission protocol | | | | yes | yes | string |
| cxml-secret | Shared secret | | | | yes | yes | string |
| cxml-ssl-version | cXML SSL version | | | | yes | yes | string |
| cxml-supplier-domain | "To", supplier domain<br>cXML supplier domain | | | | yes | yes | string |
| cxml-supplier-identity | "To", supplier identity<br>cXML supplier identity | | | | yes | yes | string |
| cxml-url | URL where POs are sent if PO transmission is "cxml" | | | | yes | yes | string |
| default-locale | Default Locale for sending emails to this supplier | no | no | any | yes | | string(255) |
| disable-cert-verify | Disable cert verify | | | | yes | yes | boolean |
| display-name | Display name | | | | yes | yes | string |
| duns | Supplier DUNS number | | | | yes | yes | string |
| enterprise | Enterprise | True | | | yes | yes | Enterprise |
| hold-invoices-for-ap-review | Prevent invoices from this supplier from being approved before AP reviews them. | | | | yes | | boolean |
| id | Coupa Internal ID | | | | | yes | integer |
| invoice-emails | Registered email addresses allowed to send invoices via email to invoices@yourhost.coupahost.com. | | | | yes | yes | |
| invoice-matching-level | Invoice matching level | yes | | 2-way, 3-way, 3-way-direct, none | yes | yes | string |
| name | Supplier name | yes | yes | | yes | yes | string(100) |
| number | Supplier number | | yes | | yes | yes | string |
| on-hold | Supplier On Hold | | | | yes | yes | boolean |
| online-store | Supplier website | yes | | | yes | yes | |
| parent | parent | | | | yes | yes | Supplier |
| payment-method | Default payment method, selectable from drop down | yes | | invoice, pcard, invoice_only, pcard_only, virtual_card | yes | yes | string(255) |
| payment-term | Default payment term, selectable from drop down | | | | yes | yes | [PaymentTerm](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/payment-terms-api-(payment_terms)) |
| payment-term-id-for-api | Payment term ID for API | | | | yes | | |
| payment-types | Payment types | | | | yes | yes | Payment Type |
| po-change-method | Purchase order change transmission method | true | false | cxml, xml, email, prompt, mark_as_sent, buy_online | yes | yes | string(255) |
| po-email | Email where POs are sent if PO transmission is "email" | | | | yes | yes | string(255) |
| po-method | Purchase order transmission method | | | cxml, xml, email, prompt, mark_as_sent, buy_online | yes | yes | string(255) |
| price-amount | Price amount | yes | | | yes | | |
| primary-address | Primary address | yes | | Supplier Address | yes | yes | [Supplier Information Address](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/supplier-information-api-(supplier_information)/supplier-information-address-api-da-5812-da-5812) |
| primary-contact | Primary supplier contact email | yes | | | yes | yes | |
| remit-to-addresses | Remit to addresses | | | | yes | yes | [RemitToAddress](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/remit-to-addresses-api-(suppliersaddresses)) |
| restricted-account-types | Restricted account types | | | | yes | yes | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| savings-pct | Savings for using this supplier | | | | yes | yes | decimal |
| send-invoices-to-approvals | If yes, then invoices will all be sent thru approvals, regardless of total amount. | | | | yes | yes | boolean |
| scf-configs | Supply chain finance configurations whitelisted for supplier | | | | yes | yes | string |
| shipping-term | Supplier shipping term, selectable from drop down | | | | yes | yes | [ShippingTerm](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/shipping-terms-api-(shipping_terms)) |
| status | Supplier status | | | | | yes | string |
| storefront-url | Supplier website | | | | yes | | string |
| supplier-addresses | | no | no | any | yes | | [] |
| supplier_classification_detail | Supplier Classification Sub-Object for Custom Fields | | | | yes | yes | SupplierClassificationDetail |
| supplier_enterprise_detail | Enterprise Supplier Data Sub-Object for Custom Fields | | | | yes | yes | SupplierEnterpriseDetail |
| supplier_insurance_detail | Insurance Sub-Object for Custom Fields | | | | yes | yes | SupplierInsuranceDetail |
| supplier_risk_detail | Risk Sub-Object for Custom Fields | | | | yes | yes | SupplierRiskDetail |
| supplier_tax_detail | Tax Sub-Object for Custom Fields | | | | yes | yes | SupplierTaxDetail |
| supplier-community-enablement | Indicates community enablement status for the supplier | | | | yes | yes | integer |
| supplier-status | Supplier status | | | | yes | | draft |
| strategic_supplier | Strategic Supplier | | | | | | |
| tax-code | Supplier tax code | | | | yes | yes | |
| tax-id | Supplier DUNS number | | | | yes | yes | string |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| website | Supplier website | | | | yes | yes | string |
| whitelist-dd | Whitelist suppliers for Dynamic Discounting | false | false | any | yes | yes | boolean |
| dd-settings | Dynamic Discounting Settings whitelisted for supplier | | | | yes | yes | string |
| customer-support-contacts | Contains list of supplier account owners (customer support contacts) with their purpose | | | | yes | yes | [] |
| diversities | List of Supplier Diversities. | | | Refer to Diversity Marker Codes below. | yes | yes | [] |
| business-entity-id | Business Entity | | | | yes | yes | integer |
| payment-terms | | | | | | yes | string |
| preferred-commodities | List of Preferred Commodities | | | | yes | yes | string |
| tags | List of Tags | | | | yes | yes | string |
| taggings | List of Tags | | | | | yes | [] |
| type | Type | | | | | yes | string(255) |
| diversity-categories | Diversity categories | | | | | yes | [] |
| inventory-organization | Inventory organization | | | | | yes | |
| order_confirmation_level | Order Confirmation Level | | | not_applicable, header, line | yes | | integer |
| confirm_by_hrs | Confirm By (In Hours) | | | , | yes | yes | decimal(10,0) |
| one_time_supplier | Indicates whether the supplier is a One Time Supplier | | | | yes | yes | boolean |
| scope_three_emissions | Indicates whether the supplier tracks Scope Three Emissions | | | | yes | yes | boolean |
| do_not_accelerate | Do not accelerate the payment terms. This field corresponds to "Do Not Offer Static Discounting". | no | | | | yes | boolean |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- There are dependent fields that can become queryable based on the value from the source field. For example, if you query against po-method=email, then po-email can be added as an additional query criteria. Please see fields with Yes*.

- For large data set and performance optimization, always limit your result with some GET criteria.

- If you do not set a status for the supplier, the system defaults to draft.

- If you do not set a default payment method, the system defaults to invoice.

- For the API to recognize custom fields, the fields must be set as API editable in the setup.

- If you have Coupa Supplier Portal (CSP) enabled in your environment, the **Allow Supplier to Create Invoice** field defaults to checked.

- When updating the primary address of the supplier, you can update every attribute on the address object, but you cannot associate a different address ID to the supplier record.

- When updating the primary contact on the supplier record, you can update every attribute on the contact information, but you cannot assign a completely different contact ID to the supplier record.

## Diversity marker codes

| **Diversity Marker Code** | **Description** |
| --- | --- |
| MBE | Minority-Owned Business Enterprise |
| WBE | Woman-Owned Business Enterprise |
| SBE | Small Business Enterprise |
| LGBTBE | Lesbian, Gay, Bisexual, Transgender Business Enterprise |
| DOB | Disability Owned Businesses |
| NPO | Non-profit Organization |
| DBE | Disadvantaged Business Enterprise |
| SDB | Small Disadvantaged Business |
| SDVBE | Service Disabled Veteran Owned Business Enterprise |
| WOSB | Woman-Owned Small Business |
| VOB | Veteran Owned Business |
| DVBE | Disabled Veteran Business Enterprise |
| SDVOSB | Service Disabled Veteran Owned Small Business |
| HUBZone | Historically Underutilized Business Zone |
| SBA8A | SBA-8(A) |
| ACDBE | Airport Concession Disadvantaged Business Enterprise |
| ANC | Alaskan Native Corporation |
| HBCU | Historically Black College or University / Minority Institution |
| LSA | Labor Surplus Area |
| VVO | Vietnam Veteran Owned |
| ABILITYONE | Ability One Program |
| EDWOSB | Economically Disadvantaged Women-Owned Small Business |
| NAO | Native American owned |
| IOB | Indigenous-owned business |
| AMS | Aboriginal and Minority Supplier |
| BOB | Black-owned business |
| MGOB | Minority group owned business |
| EMB | Ethnic minority businesses (EMBs) |
