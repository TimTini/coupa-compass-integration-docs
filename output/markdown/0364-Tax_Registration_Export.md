---
title: "Tax Registration Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/tax-registration-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/tax-registration-export"
status_code: 200
fetched_at: "2026-04-09T12:00:31+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Tax Registration Export"
---

# Tax Registration Export

Export of these records is included as a Standard CSV
Export.

| **Column** | **Description** | **Req'd** | **Unique** | **Type** | **Allowable Values** |
| --- | --- | --- | --- | --- | --- |
| Number | The registered tax number | true | false | string(47) | any |
| Country Code | The country code of the tax registration | false | false | | any |
| Active | Determines if the tax registration is enabled or disabled | false | false | boolean | any |
| Local | Set to true if this tax number cannot be used for cross-border invoices | false | false | boolean | any |
| Owner ID | Coupa ID of the entity to which the tax registration belongs. | false | false | integer | any |
| Owner Type | The type of the owning entity. Examples are Address and SupplierRemitTo | false | false | string(255) | any |
| custom-field-1 | Integration Custom Field 1 | false | false | | any |
| custom-field-2 | Integration Custom Field 2 | false | false | | any |
| custom-field-3 | Integration Custom Field 3 | false | false | | any |
| custom-field-4 | Integration Custom Field 4 | false | false | | any |
| custom-field-5 | Integration Custom Field 5 | false | false | | any |
| custom-field-6 | Integration Custom Field 6 | false | false | | any |
| custom-field-7 | Integration Custom Field 7 | false | false | | any |
| custom-field-8 | Integration Custom Field 8 | false | false | | any |
| custom-field-9 | Integration Custom Field 9 | false | false | | any |
| custom-field-10 | Integration Custom Field 10 | false | false | | any |
