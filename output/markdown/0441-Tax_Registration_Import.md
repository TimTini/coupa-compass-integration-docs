---
title: "Tax Registration Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/tax-registration-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/tax-registration-import"
status_code: 200
fetched_at: "2026-04-09T12:00:48+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Tax Registration Import"
---

# Tax Registration Import

## Overview

The Tax Registration Import process reads files from
the `./Incoming/TaxRegistration/` in the SFTP.
These files will be moved to the archive folder located
at `./Incoming/Archive/TaxRegistration/` before
being processed in alpha-numeric order.

## Keys

- Number

## Validations

You can update any field if you specify Number. Number can
only be updated from the User Interface.

## Tax Registration

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Number | Yes | No | string(47) | The registered tax number | |
| Country Code | Yes | No | | The country code of the tax registration | |
| Owner ID | Yes | No | integer | Coupa ID of the entity to which the tax registration belongs. | |
| Owner Type | Yes | No | string(255) | The type of the owning entity. Examples are Address and SupplierRemitTo | |
| Active | No | No | boolean | Determines if the tax registration is enabled or disabled | |
| Local | No | No | boolean | Set to true if this tax number cannot be used for cross-border invoices | |
