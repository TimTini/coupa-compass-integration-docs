---
title: "Commodity Translation Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/commodity-translation-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/commodity-translation-import"
status_code: 200
fetched_at: "2026-04-09T12:00:34+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Commodity Translation Import"
---

# Commodity Translation Import

## Overview

The commodity import process reads files from the `./Incoming/Commodity/` in
the SFTP. These files will be moved to the archive folder located at
`./Incoming/Archive/Commodity/` before being processed in alpha-numeric
order.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:
`Name` is the key.

## Commodity Translation

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Original Name | No | No | | Original Name of the master record | |
| Locale | Yes | No | string(255) | Coupa Locale Code | |
| Name | Yes | No | string(255) | Translated Name | |
