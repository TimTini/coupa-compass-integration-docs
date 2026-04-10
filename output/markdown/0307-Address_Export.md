---
title: "Address Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/address-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/address-export"
status_code: 200
fetched_at: "2026-04-09T12:00:12+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Address Export"
---

# Address Export

Export of these records is included as a Standard CSV Export.

## Address

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Name | Nickname to help identify the address | string(255) | No/No | |
| Location Code | External Address Id | string(255) | No/Yes | |
| Line 1 | Street Line 1 of the address | string(255) | Yes/No | |
| Line 2 | Street Line 2 of the address | string(255) | No/No | |
| City | City of the address | string(255) | Yes/No | |
| State | State of the address | string(255) | No/No | |
| Postal Code | Zip code or postal code | string(255) | Yes/No | |
| Country Code | ISO standard Country Code | | No/No | |
| Attention | Attention | string(255) | No/No | |
| Active | Active address? | boolean | No/No | |
| Content Groups | List of content group names seperated by semicolon | BusinessGroup | No/No | |
| VAT Number | VAT Number | string(255) | No/No | |
| Local Tax Number | Local Tax Number | string(255) | Yes/No | |
| VAT Country Code | VAT Country Code | | No/No | |
| Tax Numbers | Tax Numbers | | No/No | |
| Tax Countries | Tax Countries | | No/No | |
