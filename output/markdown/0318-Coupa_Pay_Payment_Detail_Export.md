---
title: "Coupa Pay Payment Detail Export"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/coupa-pay-payment-detail-export"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/coupa-pay-payment-detail-export"
status_code: 200
fetched_at: "2026-04-09T12:00:16+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Coupa Pay Payment Detail Export"
---

# Coupa Pay Payment Detail Export

## Coupa Pay-Payment Detail

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| Type | Describes the type of row. Possible values are Payment, Payment Details or Payment Detail Allocation | | No/No | |
| Payment Detail ID | The ID of the payment detail | integer | No/No | |
| Payment ID | The ID of the payment the payment detail belongs to | string(255) | No/No | |
| Payment Batch ID | The ID of the payment batch the payment detail belongs to | | No/No | |
| Source Transaction ID | The ID of source for the payment detail | | No/No | |
| Source Transaction Type | The type of source for the payment detail. Possible values are Payables::Invoice or Payables::Expense. Legacy values are CoupaPay::Invoice or CoupaPay::Expense | | No/No | |
| Source Transaction Number | The reference ID of the source for the payment detail | | No/No | |
| Transaction Total | The total transaction amount for the payment detail | decimal | No/No | |
| Discount Total | The total discount amount for the payment detail | decimal | No/No | |
| Adjustment Total | The total adjusted amount for the payment detail | decimal | No/No | |
| Currency Code | The currency of the payment to the recipient | | No/No | |
| Payment Total | The total payment amount for the payment detail | decimal | No/No | |
