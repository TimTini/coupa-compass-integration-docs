---
title: "Shippable Tracker Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/shippable-tracker-import-da-3544-da-3544"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/shippable-tracker-import-da-3544-da-3544"
status_code: 200
fetched_at: "2026-04-09T12:00:47+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Shippable Tracker Import"
---

# Shippable Tracker Import

## Possible values

Carrier
fedex, usps, ups, dhl, ontrac, asendia, apc, firstmile, newgistics, globegistics,
rr_donnelley, purolator_ca
Document Type
Order, ASN

## Shippable Tracker

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Tracking Number* | Yes | No | | Tracking number | |
| Carrier* | Yes | No | | carrier | |
| Document Type* | Yes | No | | Document type Order or ASN | |
| Document Number* | Yes | No | | Order/ASN number | |
| Note | No | No | | Note optional | |
| Delete | No | No | | Delete the tracker if present in system | |

## Shipping Terms

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Code | Yes | Yes | string(255) | Shipping Code | |
| Description | No | No | text | Shipping Code Description | |
| Content Groups | No | No | | Enter in content groups (for security) | |
| Active | Yes | No | boolean | Is this shipping code available for use? | true |
