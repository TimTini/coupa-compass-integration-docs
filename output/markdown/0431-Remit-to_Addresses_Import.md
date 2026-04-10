---
title: "Remit-to Addresses Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/remit-to-addresses-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/remit-to-addresses-import"
status_code: 200
fetched_at: "2026-04-09T12:00:45+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Remit-to Addresses Import"
---

# Remit-to Addresses Import

## Overview

The Remit To Address Import process read files
from `./Incoming/RemitToAddresses/` in the
SFTP. These files will be moved to the archive folder located
at `./Incoming/Archive/RemitToAddresses/` before
being processed in alphanumeric order.

## Keys

- Id

- Supplier Number

- Remit To Code.

## Validations

You can update any field if you specify `Id`. If there's no
`Id`, then Coupa uses the combination of `Supplier Number`
and `Remit To Code` to lookup an existing record.

## Remit To Address

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Name | No | No | string(255) | Nickname that will help users identify the address | |
| Id | No | No | integer | Coupa Generated Unique Id | |
| Active | No | No | boolean | Possible values are yes or no | |
| Line1 | Yes | No | string(255) | Street Line 1 of the address | |
| Line2 | No | No | string(255) | Street Line 2 of the address | |
| Line3 | No | No | string(255) | Street Line 3 of the address | |
| Line4 | No | No | string(255) | Street Line 4 of the address | |
| City | Yes | No | string(255) | City of the address | |
| State | No | No | string(255) | State of the address | |
| State ISO Code | No | No | string(255) | ISO Code for the State | |
| Postal Code | Yes | No | string(255) | Enter in the zip code or postal code | |
| Country Code | Yes | No | | Enter in 2-digit ISO standard Country Code | |
| Attention | No | No | | Fill in if you want a specific person or group to be in the attention field on the address | |
| Address Type | No | No | | Address Type. Should be RemitToAddress | |
| Supplier Number | Yes | No | | Enter supplier number for remit to address | |
| Remit To Code | Yes | Yes | string(255) | Unique identifying code per supplier | |
| Tax Number | No | No | | Remit To Address Tax Number | |
| Tax Country Code | No | No | | Remit To Address Tax Country Code | |
| Local Tax Number | Yes | No | string(255) | Local Tax Number | |
| External Src Ref | No | No | string(255) | External Src Ref | |
| External Src Name | No | No | string(255) | External Src Name | |
