---
title: "Registered Company API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/registered-company-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/registered-company-api"
status_code: 200
fetched_at: "2026-04-09T11:59:50+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Invoices API (/invoices)"
  - "Registered Company API"
---

# Registered Company API

## Associations

This API resource is available through [Invoices API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)-da-5926-da-5926) and
[Invoice Lines API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/invoices-api-(invoices)/invoice-line-api).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| authorized-person-address | Authorized Person Address | | | | | yes | string(255) |
| authorized-person-name | Authorized Person Name | | | | | yes | string(255) |
| authorized-person-vat-id | Authorized Person Vat Id | | | | | yes | string(255) |
| chairman-of-the-board | Chairman of the Board | | | | | yes | string(255) |
| commercial-register-number | Commercial Register & Number | | | | | yes | string(255) |
| company-in-examinership | Company in examinership | | | | | yes | boolean |
| company-is-being-wound-up | Company is being wound up | | | | | yes | boolean |
| company-receiver-appointed | Receiver of the property of a company has been appointed | | | | | yes | boolean |
| company-registration-number | Company Registration Number | | | | | yes | string(20) |
| company-type | Type of Company | | | | | yes | string(255) |
| country | country | yes | | | | yes | [Country](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/country-subdivision-api) |
| court-of-registration | Court of Registration | | | | | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| date-of-registration | Date of Registration | | | | | yes | date |
| file-reference-number | File Reference No. | | | | | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| issued-share-capital | Unpaid Share Capital | | | | | yes | decimal(32,4) |
| legal-type | Legal Type of Company | | | | | yes | string(255) |
| liable-company | Liable Company | | | | | yes | string(255) |
| license-number | License Number | | | | | yes | string(255) |
| liquidation-remark | Remark if Company in Liquidation | | | | | yes | string(255) |
| liquidator-name | Liquidator Name | | | | | yes | string(255) |
| managing-directors | Managing Directors | | | | | yes | string(255) |
| name | Registered company legal name | yes | | | | yes | string(255) |
| number-of-issued-stocks | Number of Issued Stocks | | | | | yes | integer |
| permanent_account_number | | | | | | yes | string(255) |
| permit-date | Permit Date | | | | | yes | string(255) |
| permit-number | Permit Number | | | | | yes | string(255) |
| place-of-registration | Place of Registration | | | | | yes | string(255) |
| preference-agreement | Preference Agreement | | | | | yes | string(255) |
| register-legal-entities | Register Legal Entities | | | | | yes | string(255) |
| registered-seat | Registered Seat | | | | | yes | string(255) |
| registration-authority | QST Registration Number | | | | | yes | string(255) |
| share-capital | Share Capital | | | | | yes | string(255) |
| sole-registration-code | Sole Registration Code | | | | | yes | string(255) |
| supplier-phone-number | Supplier Telephone Number | | | | | yes | string(255) |
| tax-regime | Tax Regime | | | | | yes | string(255) |
| unique-shareholder | Unique Shareholder | | | | | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
