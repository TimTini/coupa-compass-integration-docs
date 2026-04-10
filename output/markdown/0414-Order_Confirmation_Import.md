---
title: "Order Confirmation Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/order-confirmation-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/order-confirmation-import"
status_code: 200
fetched_at: "2026-04-09T12:00:42+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Order Confirmation Import"
---

# Order Confirmation Import

## Order Confirmation

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| Header | No | No | | Header | |
| PO number | No | No | | PO number | |
| Action On Behalf of Supplier | No | No | | Action On Behalf of Supplier | |
| Reason Code | No | No | | Reason Code | |
| Reason Comment | No | No | | Reason Comment | |
| Line | No | No | | Line | |
| Order Line Number | No | No | | Order Line Number | |
| Action On Behalf of Supplier | No | No | | Action On Behalf of Supplier | |
| Quantity On Behalf of Supplier | No | No | | Quantity On Behalf of Supplier | |
| Price On Behalf of Supplier | No | No | | Price On Behalf of Supplier | |
| Promise date On Behalf of Supplier | No | No | | Promise date On Behalf of Supplier | |
| Item On Behalf of Supplier | No | No | | Item On Behalf of Supplier | |
| Supplier Part Number On Behalf of Supplier | No | No | | Supplier Part Number On Behalf of Supplier | |
| Supplier Auxiliary Part Number On Behalf of Supplier | No | No | | Supplier Auxiliary Part Number On Behalf of Supplier | |
| Manufacturer Name On Behalf of Supplier | No | No | | Manufacturer Name On Behalf of Supplier | |
| Manufacturer Part Number On Behalf of Supplier | No | No | | Manufacturer Part Number On Behalf of Supplier | |
| UOM Code On Behalf of Supplier | No | No | | UOM Code On Behalf of Supplier | |
| Schedule Line | No | No | | Schedule Line | |
| Schedule Line Reference | No | No | | Schedule Line Reference | |
| Delivery Date On Behalf of Supplier | No | No | | Delivery Date On Behalf of Supplier | |

## Order Header Confirmations

| **Column Name** | **Description** | **Data Type** | **Required** | **Allowable Values** |
| --- | --- | --- | --- | --- |
| Header | Always has the same value as Header | String | Yes | Header |
| PO number | Coupa PO Number that is available in the CSP portal | String(20) | Yes | any |
| Action | Three actions are supported in total: accept, reject, and line_level where line_level means confirmation details will be provided at the line level and not the header level | String | Yes | accept, reject or line_level |
| Reason Code | Reason code is required only if rejecting the confirmation | String(255) | No | any |
| Reason Comment | Comment is required only if rejecting the confirmation | String | No | any |

## Order Line Confirmations

| **Column Name** | **Description** | **Data Type** | **Required** | **Allowable Values** |
| --- | --- | --- | --- | --- |
| Line | Always has the same value as Line | String | Yes | Line |
| Line Number | Coupa PO Line Number that is being cofirmed | String | Yes | any |
| Action | Three actions are supported in total: accept, reject, and propose change | String | Yes | accept, reject, propose_change |
| Quantity | Quantity that is being confirmed | decimal(30,6) | No | any |
| Price | Price that is being confirmed | decimal(30,6) | No | any |
| Promise Date | Delivery date of the goods | Date | No | any |
| Reason Code | Reason code is required only if rejecting the line | String(255) | No | any |
| Reason Comment | Comment is required only if rejecting the line | String | No | any |

## Schedule Lines

| **Column Name** | **Description** | **Data Type** | **Required** | **Allowable Values** |
| --- | --- | --- | --- | --- |
| Schedule Line | Always has the same value as Schedule Line | String | Yes | Schedule Line |
| Order Line Number | Coupa PO Line Number that is being confirmed | String | Yes | any |
| Id | | | | |
| Action | Three actions are supported in total: add, update, and delete | String | Yes | add, update, delete |
| Quantity | Quantity that wil be delivered for this specific schedule line | decimal(30,6) | Yes | any |
| Delivery Date | Delivery date for the quantity mentiond in the schedule line | Date | Yes | any |

## Order Confirmation CSV Example

```text
Header,PO number,Action,Reason Code,Reason Comment
```

```text
Line,Line Number,Action,Quantity,Price,Promise date,Reason Code,Reason Comment
```

```text
Schedule Line,Order Line Number,Id,Action,Quantity,Delivery Date
```

```text
Header,3175,line_level,,,,,
```

```text
Line,1,propose_change,24,20,6/15/23,Out of stock,preparing them
```

```text
Line,2,propose_change,123,230,,Out of stock,preparing them
```

```text
Schedule Line,2,,add,100,6/20/23,,
```

```text
Schedule Line,2,,add,23,6/22/23,,
```
