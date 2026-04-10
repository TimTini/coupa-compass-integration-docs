---
title: "Quote Response Lines API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-response-lines-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)/quote-response-lines-api"
status_code: 200
fetched_at: "2026-04-09T12:00:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
  - "Quote Response Lines API"
---

# Quote Response Lines API

Use the quote responses API endpoint to view the supplier responses to your sourcing event
and award lines and lots.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Values** | **In** | **Out** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | false | false | false | | yes | integer |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | false | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | false | | yes | datetime |
| quantity | Quantity | false | false | false | | yes | decimal(30,6) |
| reporting-price-amount | Reporting price amount | false | false | false | | yes | decimal(30,6) |
| quote-request-line-id | Quote request line ID | false | false | false | | yes | integer |
| lot-id | Lot ID | false | false | false | | yes | integer |
| awarded | Awarded | false | false | false | | yes | boolean |
| easy-form-response | Form response | false | false | false | | yes | |
| shipping-term | Shipping term | false | false | false | | yes | |
| created-by | User who created | false | false | false | | yes | |
| updated-by | User who updated | false | false | false | | yes | |
| price-amount | Offered price | yes | false | any | yes | yes | decimal(30,6) |
| cost-element-values | Offered prices for cost elements | false | false | any | yes | yes | text |
| lead-time | Offered lead time | false | false | any | yes | yes | integer |
| supplier-item-name | Supplier name for offered item | false | false | any | yes | yes | string(255) |
| item-part-number | Supplier part number for offered item | false | false | any | yes | yes | string(255) |
| item-description | Supplier description for offered item | false | false | any | yes | yes | text |
| price-currency | Currency for the offered price | false | false | any | yes | yes | |
| attachments | Details about supplier attachments at the line level. | false | false | any | | yes | array |
