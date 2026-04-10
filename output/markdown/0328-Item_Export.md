---
title: "Item Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/item-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/item-export"
status_code: 200
fetched_at: "2026-04-09T12:00:20+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Item Export"
---

# Item Export

Export of these records is included as a Standard CSV
Export.

## Item

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Name | Item's Name | string(255) | Yes/No | |
| Description | Item's Description | text | Yes/No | |
| UOM Code | Item's Unit Of Measure Code | | No/No | |
| Purchasable | Flag if item is purchasable | boolean | No/No | |
| Item Number | Item Number | string(255) | No/Yes | |
| Image Url | Item's Image Url | | No/No | |
| Commodity | Item's Commodity Name | string | No/No | |
| Tags | Item's Tags | Tag | No/No | |
| Require Inspection? | Does the item require an Inspection? | boolean | No/No | |
| Require Asset Tag? | Does the item require an Asset Tag? | boolean | No/No | |
| Require RFID? | Does the item require an RFID tag? | boolean | No/No | |
| Created At | Date document was created | datetime | No/No | |
| Updated At | Date document was last updated | datetime | No/No | |
