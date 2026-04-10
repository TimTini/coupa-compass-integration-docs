---
title: "Departments Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/departments-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/departments-import"
status_code: 200
fetched_at: "2026-04-09T12:00:35+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Departments Import"
---

# Departments Import

## Overview

The Departments Import process read files from the `./Incoming/Departments/`
in the SFTP. These files will be moved to the archive folder located at
`./Incoming/Archive/Departments/` before being processed in alpha-numeric
order.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:
`Id` and `Name` are the
keys.

## Department

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(255) | Department Name | |
| Id | No | No | integer | Coupa Unique Department Id | |
| Active | Yes | No | boolean | possible values are Yes or No | true, false |
