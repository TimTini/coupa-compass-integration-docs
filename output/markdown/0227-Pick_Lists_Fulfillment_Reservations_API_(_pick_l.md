---
title: "Pick Lists/Fulfillment Reservations API (/pick lists)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)"
status_code: 200
fetched_at: "2026-04-09T11:59:53+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Pick Lists/Fulfillment Reservations API (/pick lists)"
---

# Pick Lists/Fulfillment Reservations API (/pick lists)

## Overview

Use the Pick Lists API to get a list of pick lists and update
fulfillments. The URL to access pick lists
is: `https://{your_instance_name}/api/pick_lists`

See [Pick Lists](https://compass.coupa.com/x298279.xml) for more info.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | /api/pick_lists | Index | Query fulfillment reservations |
| POST | /api/pick_lists/update_fulfillments | Update Fulfillments | Update fulfillment reservations |

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Time of Fulfillment Reservation Creation in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| id | Coupa's internal unique identified | | | | | yes | integer |
| inventory-balance | The item's inventory balance | | | | | yes | [Inventory Balance](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/inventory-balance-api) |
| item | Item | | | | | yes | [Item](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/items-api-(items)) |
| order-line | The order line | | | | | yes | OrderLine |
| qty-fulfilled | The fulfilled quantity | | | | | yes | decimal(30,6) |
| qty-ordered | The ordered quantity | yes | | | | yes | decimal(30,6) |
| status | Values can be 'active' or 'closed'. | | | | | yes | string(255) |
| type | Type of Fulfillment Reservation. Values can be 'FulfillmentReservation' or 'FulfillmentShortfall' | | | | | yes | string(255) |
| updated-at | Time of Fulfillment Reservation Updation in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| warehouse | The warehouse where the item is located | | | | | yes | [Warehouse](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api) |
| warehouse-location | The location within the warehouse where the item is located | | | | | yes | [Warehouse Location](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-location-api) |

## Sample calls

## Get a specific pick list

GET
`https://{your_instance_name}/api/pick_lists?id={id}`.

## Output

```text
<?xml version="1.0" encoding="UTF-8"?>
<fulfillment-reservations type="array">
<fulfillment-reservation>
<id type="integer">3</id>
<created-at type="dateTime">2020-02-17T06:52:16+01:00</created-at>
<updated-at type="dateTime">2020-04-01T09:14:19+02:00</updated-at>
<type>FulfillmentReservation</type>
<status>active</status>
<qty-ordered type="decimal">1.0</qty-ordered>
<qty-fulfilled type="decimal">0.1</qty-fulfilled>
<item> ... </item>
<inventory-balance>
<id type="integer">211</id>
<created-at type="dateTime">2019-12-02T21:24:05+01:00</created-at>
<updated-at type="dateTime">2020-04-01T09:14:19+02:00</updated-at>
<quantity type="decimal">23.689</quantity>
<allocated type="decimal">0.9</allocated>
<available type="decimal">22.789</available>
<item> ... </item>
<inventory-valuations type="array">
<inventory-valuation>
<id type="integer">206</id>
<created-at type="dateTime">2019-12-02T21:24:05+01:00</created-at>
<updated-at type="dateTime">2020-04-01T09:14:19+02:00</updated-at>
<unit-price type="decimal">12.26</unit-price>
<total type="decimal">290.427140</total>
<currency> ... </currency>
</inventory-valuation>
</inventory-valuations>
<warehouse> ... </warehouse>
<warehouse-location> ... </warehouse-location>
<created-by> ... </created-by>
<updated-by> ... </updated-by>
</inventory-balance>
<warehouse> ... </warehouse>
<warehouse-location> ... </warehouse-location>
</fulfillment-reservation>
</fulfillment-reservations>
```

## Update a fulfillment plan

POST
to `https://{your_instance_name}/api/pick_lists/update_fulfillments`.

## Payload

```text
<?xml version="1.0" encoding="UTF-8"?>
<fulfillment-reservation>
<id type="integer">999</id>
<qty-pick-amt>5</qty-pick-amt>
</fulfillment-reservation>
```

- [Inventory Balance API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/inventory-balance-api)

- [Inventory Valuation API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/inventory-valuation-api)

- [Warehouse API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-api)

- [Warehouse Location API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-location-api)

- [Warehouse Type API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/pick-listsfulfillment-reservations-api-(pick-lists)/warehouse-type-api)
