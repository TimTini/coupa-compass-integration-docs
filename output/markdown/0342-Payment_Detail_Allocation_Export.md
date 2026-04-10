---
title: "Payment Detail Allocation Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/payment-detail-allocation-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/payment-detail-allocation-export"
status_code: 200
fetched_at: "2026-04-09T12:00:25+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Payment Detail Allocation Export"
---

# Payment Detail Allocation Export

## Payment Detail Allocation

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Type | Describes the type of row. Possible values are Payment, Payment Details or Payment Detail Allocation | | No/No | |
| Payment Detail Allocation ID | The ID of the payment detail allocation | integer | No/No | |
| Payment ID | The ID of the payment the payment detail belongs to | | No/No | |
| Payment Detail ID | The ID of the payment detail the allocation belongs to | | No/No | |
| Source Transaction From ID | The ID of the transaction that emitted the allocation | | No/No | |
| Source Transaction From Type | The type of the transaction that emitted the allocation. Possible values are InvoiceHeader. | | No/No | |
| Source Transaction From Number | The reference ID of the transaction that emitted the allocation | | No/No | |
| Source Transaction From Amount | The amount sent by the transaction that emitted the allocation | | No/No | |
| Source Transaction From Currency | The currency for the amount sent by the transaction that emitted the allocation | | No/No | |
| Source Transaction To ID | The ID of the receiving transaction | | No/No | |
| Source Transaction To Type | The type of the receiving transaction. Possible values are InvoiceHeader. | | No/No | |
| Source Transaction To Number | The reference ID of the receiving transaction | | No/No | |
| Source Transaction To Amount | The amount sent to the receiving transaction | | No/No | |
| Source Transaction To Currency | The currency for the amount sent to the receiving transaction | | No/No | |
| Source | The source of this allocation. Possible values are coupa_pay. | string(255) | No/No | coupa_pay, erp, ui, api, csv, early_pay_discount |
| Reason Code | The reason code for the most recent change to this allocation. | string(40) | No/No | payment, auto_payment, epr, epr_rejected, manual |
