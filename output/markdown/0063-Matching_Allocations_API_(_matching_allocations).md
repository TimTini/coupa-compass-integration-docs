---
title: "Matching Allocations API (/matching_allocations)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/matching-allocations-api-(matching_allocations)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/matching-allocations-api-(matching_allocations)"
status_code: 200
fetched_at: "2026-04-09T11:59:15+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Matching Allocations API (/matching_allocations)"
---

# Matching Allocations API (/matching_allocations)

## Actions

The Matching Allocation API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/matching_allocations/invoice_line_id=` | | |
| GET | `/api/matching_allocations/invoice_line[invoice_header_id][in]=` | | |

## Elements

The following elements are available for the Matching
Allocation API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | false | false | | false | true | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | | false | true | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | false | false | | false | true | datetime |
| status | | false | false | | false | true | string(50) |
| inventory_transaction_id | | false | false | | false | true | integer |
| quantity | | true | false | | false | true | decimal(32,4) |
| amount | | true | false | | false | true | decimal(32,4) |
| invoice_line_total | | false | false | | false | true | decimal |
| asn_line_id | | false | false | | false | true | integer |
| invoice_line_id | | false | false | | false | true | integer |
| order_line_id | | false | false | | false | true | integer |
| manual_match | | false | false | | false | true | integer |
| status_reason | | false | false | | false | true | string(512) |
| inventory_transaction_match_reference | | false | false | | false | true | string(255) |
| uom | | false | false | | false | true | string(255) |
