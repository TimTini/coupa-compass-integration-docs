---
title: "Warehouse Location Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/warehouse-location-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/warehouse-location-import"
status_code: 200
fetched_at: "2026-04-09T12:00:49+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Warehouse Location Import"
---

# Warehouse Location Import

## Warehouse Location

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Aisle | Yes | Yes | string(255) | Identifier for Aisle Location | |
| Bin | No | No | string(255) | Identifier for Bin location | |
| Level | No | No | string(255) | Identifier for Level location | |
| Active | No | No | boolean | Active | |

## Warehouse Type

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | Yes | Yes | string(255) | Warehouse Type Name | |
| Description | Yes | No | string(255) | Description of this type of Warehouse | |
