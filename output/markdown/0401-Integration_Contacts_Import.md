---
title: "Integration Contacts Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/integration-contacts-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/integration-contacts-import"
status_code: 200
fetched_at: "2026-04-09T12:00:39+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Integration Contacts Import"
---

# Integration Contacts Import

## Integration Contact

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Integration | Yes | No | | Integration Name. Must Exist In Coupa | |
| Id | No | No | integer | Coupa Unique Integration Contact Id | |
| Contactable Type | Yes | No | string(255) | Type of Contact: User, ApprovalGroup, Supplier | User, UserGroup, ApprovalGroup, Supplier, SupplierUser |
| Contactable | Yes | No | string | Coupa User login name or Approval Group name for Contact | |
| Contact Alert Type | Yes | No | string(255) | Type of alerts to send | Technical, Functional, Both |
