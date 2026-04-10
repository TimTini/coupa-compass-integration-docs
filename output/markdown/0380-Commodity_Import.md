---
title: "Commodity Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/commodity-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/commodity-import"
status_code: 200
fetched_at: "2026-04-09T12:00:34+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Commodity Import"
---

# Commodity Import

## Overview

The commodity import process reads files from the `./Incoming/Commodity/` in
the SFTP. These files will be moved to the archive folder located at
`./Incoming/Archive/Commodity/` before being processed in alpha-numeric
order.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:
`Name` is the key.

## Commodity

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(255) | Name of the commodity. | |
| ID | No | No | integer | Unique identifier Coupa assigns when a new record is created. Cannot be modified, but can be used to update the record. | |
| Description | No | No | text | No Description Found | |
| Active | Yes | No | boolean | Whether the commodity is active. | true, false |
| Parent commodity | No | No | | Name of the Parent Commodity. Can also be left blank if this commodity is not a child. | |
| Deductibility | No | No | string(255) | Deductibility | fully_deductible, partially_deductible, not_deductible |
| Category | No | No | string(255) | Category | goods, services |
| Subcategory | No | No | string(255) | Subcategory | raw_materials, investment_goods, services_exceptions |
| Preferred | No | No | string(255) | Mark/unmark a commodity as preferred. Set to Automatic to allow the system to mark preferred. Automatic option is available only if Automatic Guided Experiences configuration is enabled on the Company Information page. | Yes, No, Automatic, Always, Never |
| Use in Search | No | No | boolean | No Description Found | |
| Tags | No | No | | Commodity Tags. Separate tags with spaces. For tags with more than one word, surround the tag in double quotations. | |
