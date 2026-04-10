---
title: "Contracts Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/contracts-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/contracts-export"
status_code: 200
fetched_at: "2026-04-09T12:00:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Contracts Export"
---

# Contracts Export

Export of these records is included as a Standard CSV Export.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

CSV exports for SFTP only include a known issue where the Expires field adds an extra day to the expiry date. This does not affect exports made using the UI.

## Contract

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Record Type | Record Type | | No/No | |
| Contract # | The contract number | string(50) | Yes/No | |
| Contract Name | The name of the contract | string(100) | Yes/No | |
| Content Groups | The content groups that can view this contract | | No/No | |
| Status | The status of the contract | string(50) | Yes/No | |
| Supplier | The supplier ID assocaited with the contract | integer | No/No | |
| Supplier Number | Supplier Number | | No/No | |
| Supplier Account # | The supplier account for the contract | string(255) | No/No | |
| Starts | The date the contract begins | datetime | No/No | |
| Expires | The date the contract expires | datetime | No/No | |
| Owner | The currency ID associated with the contract | integer | No/No | |
| Owner Login | The user login that owns the contract | | No/No | |
| Currency Code | Currency Code | | No/No | |
| Savings % | The % savings created by the contract | decimal(20,2) | No/No | |
| Version | The version number of the contract | integer | No/No | |
| Created By | The user ID that created the contract | | No/No | |
| Created By Login | Created By Login | | No/No | |
| Created Date | The date the contract was created | datetime | No/No | |
| Updated By | The user ID that most recently updated the contract | | No/No | |
| Updated By Login | The user login that most recently updated the contract | | No/No | |
| Updated Date | The date the contract was most recently updated | datetime | No/No | |
| Submitted Date | The date the contract was submitted | datetime | No/No | |
| Submitted By | The user ID of the person that submitted the contract | | No/No | |
| Submitted By Login | Ther user login that submitted the approval | | No/No | |
| Is Default | Is this the detault (Y/N) | boolean | No/No | |
| Default Account ID | The default account ID for the contract | integer | No/No | |
| Default Account Code | The default account code for the contract | | No/No | |
| Linked Projects | List of Project IDs linked to this contract | | No/No | |
| Linked Events | List of Event IDs linked to this contract | | No/No | |

## Contract Term

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |

## Per Order Contract Term

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |

## Price Range Contract Term

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
