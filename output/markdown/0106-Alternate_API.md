---
title: "Alternate API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/alternate-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/shared-resources/alternate-api"
status_code: 200
fetched_at: "2026-04-09T11:59:26+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Shared Resources"
  - "Alternate API"
---

# Alternate API

Use this API to export alternate suggested item information on search results.

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | Coupa unique identifier | no | no | any | | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | no | no | any | | yes | datetime |
| requisition_line_id | | no | no | any | | yes | integer |
| type_flag | | no | no | any | | yes | string(255) |
| description | | no | no | any | | yes | string(255) |
| quantity | | no | no | any | | yes | decimal(30,6) |
| unit_price | | no | no | any | | yes | decimal(30,6) |
| total | | no | no | any | | yes | decimal(32,4) |
| source_part_num | | no | no | any | | yes | string(255) |
| unspsc_code | | no | no | any | | yes | string(255) |
| manufacturer_name | | no | no | any | | yes | string(255) |
| manufacturer_part_number | | no | no | any | | yes | string(255) |
| minimum_order_quantity | | no | no | any | | yes | decimal(30,6) |
| order_increment | | no | no | any | | yes | decimal(30,6) |
| realtime_item_key | | no | no | any | | yes | string(255) |
| summary | | no | no | any | | yes | string(255) |
| image_url | | no | no | any | | yes | string(255) |
| currency | | no | no | any | | yes | |
| uom | | no | no | any | | yes | |
| supplier | | no | no | any | | yes | |
| punchout_site | | no | no | any | | yes | |
| contract | | no | no | any | | yes | |
| created_by | User who created | no | no | any | | yes | |
| updated_by | User who updated | no | no | any | | yes | |
