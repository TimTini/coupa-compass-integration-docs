---
title: "Delegations Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/delegations-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/delegations-export"
status_code: 200
fetched_at: "2026-04-09T12:00:16+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Delegations Export"
---

# Delegations Export

Export of these records is included as a Standard CSV
Export.

## Delegation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Delegator ID | The user ID that made the delegator | integer | No/No | |
| Delegator Login | The user login that made the delegateor | | No/No | |
| Delegate ID | The delegate ID that made the approval (if applicable) | integer | No/No | |
| Delegate Login | The delegate login that made the approver | | No/No | |
| Delegation Start Date | The day the delegation period begins | datetime | Yes/No | |
| Delegation End Date | The day the delegation period ends | datetime | Yes/No | |
| Delegation Reason | The reason for the approval | string(255) | Yes/No | |
| Approval Delegate | Approval permissions of delegate | boolean | No/No | |
| Receiving Delegate | Receiving permissions of delegate | boolean | No/No | |
| Created By ID | The user ID that created the approval delegation | integer | No/No | |
| Created By Login | The user login that created the approval delegate | | No/No | |
| Created Date | The date the user create the approval delegation | datetime | No/No | |
| Updated By ID | The user ID that most recently updated the approval delegation | integer | No/No | |
| Updated By Login | Ther user login that most recently updated the approval delegate | | No/No | |
| Updated Date | The date the approval delegation was most recently updated | datetime | No/No | |
