---
title: "Enterprise Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/enterprise-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/enterprise-import"
status_code: 200
fetched_at: "2026-04-09T12:00:36+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Enterprise Import"
---

# Enterprise Import

To understand how enterprises work in Coupa, see [Multiple ERP Support](https://compass.coupa.com/x294296.xml).

## Enterprise

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(100) | The name of the enterprise, as it will appear to users. | |
| Code | Yes | Yes | string(6) | The code for the enterprise. Must be unique. | |
| Description | No | No | string(255) | Description of the enterprise for users. | |
| Active | No | No | boolean | When active, the enterprise can be selected for COAs or suppliers. | |
| Vendor Remit-To Required | No | No | string | Specifies whether the vendor remit-to address is required for the enterprise. | |
| Tax Coding Enabled | No | No | string | Specifies whether the tax encoding is required for the enterprise. | |
