---
title: "Amount Component API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/amount-component-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/amount-component-api"
status_code: 200
fetched_at: "2026-04-09T11:59:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Amount Component API"
---

# Amount Component API

Use this API to specify asset tags on some transactional and reference objects.

## Associations

This API is associated with [Currency API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies))
and [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| amount | Amount | yes | | | yes | yes | decimal(30,6) |
| amount-type | Amount Type | yes | yes | supplier_net_paid, supplier_net_received, supplier_fees, msp_net_paid, msp_net_received, msp_fees, vms_net_paid, vms_net_received, vms_fees | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| currency | Currency | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| id | Coupa unique identifier | | | | | yes | integer |
| source-id | Source Id | | | | yes | yes | integer |
| source-type | Source Type | | | | yes | yes | string(255) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
