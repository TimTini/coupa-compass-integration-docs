---
title: "Supplier Risk Aware Feed Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/supplier-risk-aware-feed-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/supplier-risk-aware-feed-import"
status_code: 200
fetched_at: "2026-04-09T12:00:47+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Supplier Risk Aware Feed Import"
---

# Supplier Risk Aware Feed Import

## Overview

The Supplier Risk Aware Import is used to load suppliers
for Risk Aware evaluation. This load can be performed via the User
Interface. The Supplier Risk Aware Import is not
available via SFTP.

## Keys

- Supplier number

- Supplier name

## Validations

The supplier must be active in Coupa. Records can be initially
loaded by specifying either `Supplier Number` or
`Supplier Name`. Subsequent updates require
`Supplier Number`.

## Supplier Risk Aware Feed

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Supplier Name | No | No | | Required if Supplier Number is not specified. | |
| Supplier Number | No | No | | Required if Supplier Name is not specified. | |
| Number Field 1 | No | No | decimal(32,4) | Number Field 1 | |
| Number Field 2 | No | No | decimal(32,4) | Number Field 2 | |
| Number Field 3 | No | No | decimal(32,4) | Number Field 3 | |
| Number Field 4 | No | No | decimal(32,4) | Number Field 4 | |
| Number Field 5 | No | No | decimal(32,4) | Number Field 5 | |
| Number Field 6 | No | No | decimal(32,4) | Number Field 6 | |
| Number Field 7 | No | No | decimal(32,4) | Number Field 7 | |
| Number Field 8 | No | No | decimal(32,4) | Number Field 8 | |
| Number Field 9 | No | No | decimal(32,4) | Number Field 9 | |
| Number Field 10 | No | No | decimal(32,4) | Number Field 10 | |
