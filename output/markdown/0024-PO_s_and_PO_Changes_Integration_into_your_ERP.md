---
title: "PO's and PO Changes Integration into your ERP"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/orchestration-documents/pos-and-po-changes-integration-into-your-erp"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/orchestration-documents/pos-and-po-changes-integration-into-your-erp"
status_code: 200
fetched_at: "2026-04-09T11:59:06+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Orchestration Documents"
  - "PO's and PO Changes Integration into your ERP"
---

# PO's and PO Changes Integration into your ERP

Step-by-step instructions to integrate your Coupa PO's and PO Changes with your ERP.

## General API setup considerations

- [Get Started with the Coupa API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api)

- [Open Connect API Access](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/openid-connect-clients)
(R29 onward)

- [JSON/XML](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/differences-between-xml-and-json-in-coupa)

- [GraphQL](https://compass.coupa.com/x305489.xml) (R30 onward)

## Limited payload - fields & API filters

Coupa's API returns a lot of data by default (for example: full objects
for associated objects). The API return payloads can be very large and therefore
slow.

To make things easier, Coupa includes a Fields query parameter and API Filters
to return a limited JSON or XML response instead of the entire schema and all associations
for an object. For more information, see [API Response Filters.](https://compass.coupa.com/x285425.xml)

## Use cases described in this article

The assumption in this document is that the Purchase Order number in the
ERP is driven by the Coupa Purchase Order Number. This Article describes three different
options to Integrate Coupa Purchase Orders into your ERP (for both creation and
updates).

These options will change the way you can monitor your integrations from
Coupa:

- **Option 1**: Simple monitoring based on custom field(s) you define on the Order
Header

- **Option 2**: Advanced monitoring using Integration History records

- **Option 3**: Leverage full Coupa integration monitoring

For the three options, the Coupa POs are pushed to the ERP based on the Export
flag.

In case of an error, in the Integration of a PO, a manual change will be
required on the PO in the Coupa UI: this change will reset the Export flag, and the PO will
therefore be considered in the next run.

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip:

You can contact Coupa
Support to enable this option: **Reset PO last exported at for every change**. This
setting only applies to the UI. Changes made with API won’t change the Exported
status.

## Create dedicated Integration and Contact for API

For option 2 & 3 described above,
you need to create:

- A dedicated Integration for each API Orchestration you implement.

- One or several Integration contact(s) for each integration, that will be alerted for
any failed integration.

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip:

You can contact Coupa Support to enable this option: **Enable link
to Integration History by Document Type**. This setting adds a link in the setup page
to view full Integration History per document type

## Option 1: Simple monitoring based on custom field(s)

**Description**

In this
scenario, for each PO we will add the current Integration status in one or several PO header
custom field(s). We added a custom field `cf-integration-status` with the
name of `Integration Status`. Use the Standard PO Data Table to follow up the
Integration status of your documents at this
url:

```text
https://<your instance hostname>/order_headers
```

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/po-integration-01.png)

**Orchestration
diagram**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/po-orchistration.png)

**Steps / API calls details**

| **Step 1** | **Get the list and details of the Coupa Purchase Orders to create/update in the ERP. Selection criteria includes the Export Flag and PO Status. Query parameter *show_deleted_lines* can be necessary to handle the PO update in the ERP** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | `filter=`<br>`offset=10`<br>`exported=false`<br>`show_deleted_lines=true*`<br>`status[in]=issued,canceled,closed` |
| **Sample URL** | https://*<your instance hostname>*/api/purchase_orders?filter=*<your API filter name>*&offset=10&exported=false&show_deleted_lines=true&status[in]=issued,canceled,closed |
| **Response body sample** | ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/step-1.png) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: The `show_deleted_lines=true` query parameter is
for PO changes.

| **Step 2** | **Mark individual PO as exported** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | `exported=true`<br>`fields=["id","exported"]` |
| **Sample URL** | `https:///api/purchase_orders/?exported=true&fields=["id","exported"]` |
| **Query Body sample** | N/A * |
| **Response Body sample** | @@BLOCK_1@@ |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

For this call you do not need a payload if you include `?exported=true` in
the URL. That’s where the creation/update of the PO in the ERP happens.

| **Step 3** | **Update a Custom Fields for Reporting** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | @@BLOCK_2@@ |
| **Sample URL** | @@BLOCK_3@@ |
| **Query Body sample** | @@BLOCK_4@@<br>or<br>@@BLOCK_5@@ |
| **Response Body sample** | @@BLOCK_6@@<br>or<br>@@BLOCK_7@@ |

## Option 2: Advanced monitoring using Integration History

**Description**

In this scenario, for each PO
we:

- Resolve the previous Integration History Record for the document

- Create an Integration History Record

- Create an Alert to the Integration Contact in case of an error

Use the Standard PO Integration History Data Table to follow up the Integration status
of your documents. You can find it at:

```text
https://<your instance hostname>/integration_history_records/purchase_orders
```

You can use a
filter on Response Code to differentiate between documents successfully replicated and
documents that failed.

**Orchestration Diagram**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/po-int-orchistration.png)

**Steps / API calls details**

| **Step 1** | **Get the list and details of the Coupa Purchase Orders to create/update in the ERP. Selection criteria includes the Export Flag and PO Status. Query parameter *show_deleted_lines* can be necessary to handle the PO update in the ERP** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | `filter=`<br>`offset=10`<br>`exported=false`<br>`show_deleted_lines=true`<br>`status[in]=buyer_hold,issued,canceled,closed,soft_closed` |
| **Sample URL** | `https:///api/purchase_orders?filter=&offset=10&exported=false&show_deleted_lines=true&status[in]=buyer_hold,issued,canceled,closed,soft_closed` |
| **Response body sample** | ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/step-2.png) |

| **Step 2** | **Mark individual PO as exported** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | `exported=true`<br>`fields=["id","exported"]` |
| **Sample URL** | `https:///api/purchase_orders/?exported=true&fields=["id","exported"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_9@@ |

This is where the creation/update of the PO in the ERP happens.

| **Step 3a** | **Get unresolved Integration History Record** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `resolved=false`<br>`document-type=OrderHeader`<br>`document-id=`<br>`fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records?resolved=false&document-type=OrderHeader&document-id=&fields=["id","document-id","status","resolved"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_10@@ |

| **Step 3b** | **Resolve previous Integration History Record** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_history_records//resolve` |
| **Query Params** | `fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records//resolve?fields=["id","document-id","status","resolved"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_11@@ |

| **Step 4a** | **Create Integration History (Success)** |
| --- | --- |
| **Method** | POST |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `fields=["id","document-id","status"]` |
| **Sample URL** | `https:///api/integration_history_records?fields=["id","document-id","status"]` |
| **Query Body sample** | @@BLOCK_12@@ |
| **Response Body sample** | @@BLOCK_13@@ |

| **Step 4b** | **Create Integration History (Error) and alert to Integration Contact** |
| --- | --- |
| **Method** | POST |
| **API** | `https:///api/integration_history_records/create_alert` |
| **Query Params** | `fields=["id","document-id","status"]` |
| **Sample URL** | `https:///api/integration_history_records/create_alert?fields=["id","document-id","status"]` |
| **Query Body sample** | @@BLOCK_14@@ |
| **Response Body sample** | @@BLOCK_15@@ |

## Option 3: Leverage full Coupa integration monitoring

**Description**

In this scenario, we create
an Integration run that tracks

- The status of the Integration (pending/started/errored/successful/failed)

- The total number of PO processed

- The number of Success and Errors

- The list of Integration Errors and their statuses (resolved or not)

For each PO we:

- Resolve the previous Integration History Record for the document

- Create an Integration History Record

- In case of an error, create an Integration Error and an Alert to the Integration
Contact

You can monitor all Integration Runs for your Integration
at:

```text
https://<your instance hostname>/integrations/<your integration id>/integration_runs
```

Use
the Standard PO Integration Error Data Table to list all POs with Integration Error pending
resolution. It's located
at:

```text
https://<your instance hostname>/integration_errors
```

Use
the Standard PO Integration History Data Table to list all POs successfully Integrated. It's
located
at:

```text
https://<your instance hostname>/integration_history_records/purchase_orders
```

**Orchestration
diagram**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/orchestration-3.png)

**Steps / API calls details**

| **Step 1** | **Create Integration Run** |
| --- | --- |
| **Method** | POST |
| **API** | `https:///api/integration_runs` |
| **Query Params** | N/A |
| **Query Body sample** | @@BLOCK_19@@ |
| **Response Body sample** | @@BLOCK_20@@ |

| **Step 2** | **Get the list and details of the Coupa Purchase Orders to create/update in the ERP. Selection criteria includes the Export Flag and PO Status. Query parameter *show_deleted_lines* can be necessary to handle the PO update in the ERP** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | `filter=`<br>`offset=10`<br>`exported=false`<br>`show_deleted_lines=true`<br>`status[in]=buyer_hold,issued,canceled,closed,soft_closed` |
| **Sample URL** | `https:///api/purchase_orders?filter=&offset=10&exported=false&show_deleted_lines=true&status[in]=buyer_hold,issued,canceled,closed,soft_closed` |
| **Response body sample** | ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/step-3.png) |

| **Step 3** | **Start Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_runs//run` |
| **Query Params** | N/A |
| **Query Body sample** | @@BLOCK_21@@ |
| **Response Body sample** | @@BLOCK_22@@ |

| **Step 4** | **Mark individual PO as exported** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/purchase_orders/` |
| **Query Params** | `exported=true`<br>`fields=["id","exported"]` |
| **Sample URL** | `https:///api/purchase_orders/?exported=true&fields=["id","exported"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_23@@ |

This is where the creation/update of the PO in the ERP happens.

| **Step 5a** | **Get unresolved Integration History Record** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `resolved=false`<br>`document-type=OrderHeader`<br>`document-id=`<br>`fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records?resolved=false&document-type=OrderHeader&document-id=&fields=["id","document-id","status","resolved"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_24@@ |

| **Step 5b** | **Resolve previous Integration History Record** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_history_records//resolve` |
| **Query Params** | `fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records//resolve?fields=["id","document-id","status","resolved"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_25@@ |

| **Step 6a** | **Get unresolved Integration Error Record** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/integration_errors` |
| **Query Params** | `resolved=false`<br>`document-type=OrderHeader`<br>`document-id=` |
| **Sample URL** | `https:///api/integration_errors?resolved=false&document-type=OrderHeader&document-id=` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_26@@ |

| **Step 6b** | **Resolve previous Integration History Record** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_errors//resolve` |
| **Query Params** | N/A |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_27@@ |

| **Step 7a** | **Create Integration History (Success) It must reference the Integration Run** |
| --- | --- |
| **Method** | POST |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `fields=["id","document-id","status"]` |
| **Sample URL** | `https:///api/integration_history_records?fields=["id","document-id","status"]` |
| **Query Body sample** | @@BLOCK_28@@ |
| **Response Body sample** | @@BLOCK_29@@ |

| **Step 7b** | **Create Integration Error and alert to Integration Contact It must reference the Integration Run** |
| --- | --- |
| **Method** | POST |
| **API** | `https:///api/integration_errors/create_alert` |
| **Query Params** | N/A |
| **Query Body sample** | @@BLOCK_30@@ |
| **Response Body sample** | @@BLOCK_31@@ |

| **Step 8** | **Successfully End Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_runs//success` |
| **Query Params** | N/A |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_32@@ |

If there is a general failure during the Integration run

| **Step x** | **Raise Failure for the Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_runs//fail` |
| **Query Params** | N/A |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_33@@ |
