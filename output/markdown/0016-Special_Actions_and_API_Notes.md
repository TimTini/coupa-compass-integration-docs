---
title: "Special Actions and API Notes"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/special-actions-and-api-notes"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/special-actions-and-api-notes"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Special Actions and API Notes"
---

# Special Actions and API Notes

Additional info on how to use the Coupa API.

Certain functions or actions are available via the API and require additional explanation.
These will be documented below.

**Mark Object as Exported** - Marking an object as exported requires its own request. Any
other changes included may be ignored during the update.

- A PUT to the record's URL with `exported=true` as a
parameter:

*HTTP PUT
-->*
`https://.coupahost.com/api/purchase_orders/25?exported=true`
where 25 is the purchase order number to set exported.

**Submit Requisition For Approval - **Requisitions can be automatically submitted for
approval when they are created via the API. To submit a requisition, add the following to the
URL you when you are creating the requsition: "`/new/submit_for_approval`"

- HTTP POST -->
`https://.coupahost.com/api/requisitions/new/submit_for_approval`

**Void a Receipt (release 008) - **Existing Inventory_Transactions can be voided via the
API. Add the following to the URL you when you are making a PUT to the receipt:
`/void`

- HTTP PUT -->
`https://.coupahost.com/api/inventory_transactions/123/void`
where 123 is the Coupa ID of the Receipt.

**Purchase Order Version - **An edit to a Purchase Order which results in a new Purchase
Order Version (resend to supplier) will reset the exported flag to false.

**Error Response** - If an error occurs, Coupa will return a message in the following
format:

```text
<?xml version="1.0" encoding="UTF-8"?>
<errors>
<error>This is a sample error message from the API.</error>
</errors>
```

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Coupa generally recommends that customers send POs to suppliers from the Coupa system,
rather than issuing POs to suppliers from their ERP system.
