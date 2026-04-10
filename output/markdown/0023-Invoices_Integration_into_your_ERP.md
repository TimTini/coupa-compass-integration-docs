---
title: "Invoices Integration into your ERP"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/orchestration-documents/invoices-integration-into-your-erp"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/orchestration-documents/invoices-integration-into-your-erp"
status_code: 200
fetched_at: "2026-04-09T11:59:06+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Orchestration Documents"
  - "Invoices Integration into your ERP"
---

# Invoices Integration into your ERP

Step-by-step instructions to integrate your Coupa Invoices with your ERP.

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip:

You can also download this document as a Microsoft Word document: [Coupa Invoices to ERP.docx](https://a/90229)

## General API setup considerations

- [Get Started with the Coupa API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api)

- [Open Connect API Access](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/openid-connect-clients) (R29 onward)

- [JSON/XML](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/differences-between-xml-and-json-in-coupa)

- [GraphQL](https://compass.coupa.com/x305489.xml) (R30 onward)

## Limited payload: fields & API filters

Coupa's API returns a lot of data by default (for example: full objects for associated objects). The API return payloads can be very large and therefore slow. This can be a problem for customers that do not need the extraneous data not to mention the unnecessary consumption of resources.

To make things easier, Coupa has the concept of the “fields” parameter & API Filters that return a limited JSON or XML response instead of the entire schema, and all associations, for an object.

- [API Response Filters](https://compass.coupa.com/x285425.xml)

- API: Using the new API query parameter "fields", Alternative to "return object"

## Use cases described in this article

The Invoices usually have an internal number in the ERP. In this document we take the assumption that this ERP Document number is a Custom field in the Coupa Invoice Header. In our example the custom field `cf_erp_invoice_number` was created with name `ERP Invoice Number`. This Article describes the 3 different options to Integrate Coupa Invoices into your ERP(for both creation and updates).

These options will change the way you can monitor your integrations from Coupa:

- **Option 1**: Simple monitoring based on custom field(s) you define on the Invoice Header

- **Option 2**: Advanced monitoring using Integration History records

- **Option 3**: Leverage full Coupa Integrations monitoring

For the 3 options, the Coupa Invoices are pushed to the ERP based on the Export Flag. In case of an error, in the Integration of a Invoice, a manual change will be required on the Invoice in the Coupa UI: this change will reset the Export Flag, and the Invoice will therefore be considered in the next run.

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip:

Coupa suggests that you contact Coupa Support to have them enable this option: **Reset Invoice last exported at for every change**. This setting only applies to the UI. Changes made with API won’t change the Exported status.

## Create dedicated Integration and Contact for API

For option 2 & 3, you will need to create:

- A dedicated Integration for each API Orchestration you implement

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/invoice-integration-01.png)

- One or several Integration contact(s) for each integration, that will be alerted for any failed integration.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/invoice-integration-contact.png)

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip:

Coupa suggests that you contact Coupa Support to have them enable this option: **Enable link to Integration History by Document Type**. This setting adds a link in the setup page to view full Integration History per document type.

## Option 1: Simple monitoring based on custom field(s)

**Description**

In this scenario, for each Invoice we add the current Integration status in one or several Invoice header custom field(s). We added the custom field `cf-integration-status` was created with the name of `Integration Status`. Use the Standard Invoice Data Table to follow up the Integration status of your documents at this url:

```text
https://<your instance hostname>/invoices
```

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/invoices-01.png)

**Orchestration diagram**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/orchestration-01.png)

**Steps / API calls details**

| **Step 1** | **Get the list and details of the Coupa Invoices to create/update in the ERP.**<br>**Selection criteria includes the Export Flag and Invoice Status.** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/invoices/` |
| **Query Params** | `fields=`<br>`offset=10`<br>`exported=false`<br>`status[in]=approved,voided` |
| **Sample URL** | `https:///api/invoices?filter=&offset=10&exported=false&status[in]=approved,voided` |
| **Query Body sample** | N/A |
| **Response Body sample** | ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/response-01.png) |

| **Step 2** | **Mark individual Invoice as exported** |
| --- | --- |
| **Method** | PUT |
| **API** | https://*<your instance hostname>*/api/invoices/*<Invoice id>* |
| **Query Params** | `exported=true`<br>`fields=["id","exported"]` |
| **Sample URL** | `https:///api/invoices/?exported=true&fields=["id","exported"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_1@@ |

| **Step 3** | **Update a Custom Fields for Reporting and ERP document number** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/invoices/` |
| **Query Params** | @@BLOCK_2@@ |
| **Sample URL** | @@BLOCK_3@@ |
| **Query Body sample** | @@BLOCK_4@@<br>or<br>@@BLOCK_5@@ |
| **Response Body sample** | @@BLOCK_6@@<br>or<br>@@BLOCK_7@@ |

## Option 2: Advanced monitoring using Integration History

**Description**

In this scenario, for each Invoice we:

- Resolve the previous Integration History Record for the document

- Create an Integration History Record

- Create an Alert to the Integration Contact in case of an error

Each document includes the Integration History details.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/invoice-int-hist-02.png)

Use the Standard Invoice Integration History Data Table to follow up the Integration status of your documents. You can find it at:

```text
https://<your instance hostname>/integration_history_records/invoices
```

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/invoice-int-records-01.png)You can use a filter on Response Code to differentiate between documents successfully replicated and documents that failed.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/invoice-int-records-02.png)

**Orchestration diagram**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/orchestration-02.png)

**Steps / API calls details**

| **Step 1** | **Get the list and details of the Coupa Invoices to create/update in the ERP. Selection criteria includes the Export Flag and Invoice Status.** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/invoices/` |
| **Query Params** | `filter=`<br>`offset=10`<br>`exported=false`<br>`status[in]=approved,voided` |
| **Sample URL** | `https:///api/invoices?filter=&offset=10&exported=false&status[in]=approved,voided` |
| **Query Body sample** | N/A |
| **Response Body sample** | ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/response-02.png) |

| **Step 2** | **Mark individual Invoice as exported** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/invoices/` |
| **Query Params** | `exported=true`<br>`fields=["id","exported"]` |
| **Sample URL** | `https:///api/invoices/?exported=true&fields=["id","exported"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_9@@ |

This is where the creation/update of the Invoice in the ERP happens.

| **Step 3a** | **Get unresolved Integration History Record** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `resolved=false`<br>`document-type=InvoiceHeader`<br>`document-id=`<br>`fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records?resolved=false&document-type=InvoiceHeader&document-id=&fields=["id","document-id","status","resolved"]` |
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

| **Step 4a** | **Update a Custom Fields for ERP document number (Success)** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/invoices/` |
| **Query Params** | @@BLOCK_12@@ |
| **Sample URL** | @@BLOCK_13@@ |
| **Query Body sample** | @@BLOCK_14@@ |
| **Response Body sample** | @@BLOCK_15@@ |

| **Step 4b** | **Create Integration History (Success)** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `fields=["id","document-id","status"]` |
| **Sample URL** | `https:///api/integration_history_records?fields=["id","document-id","status"]` |
| **Query Body sample** | @@BLOCK_16@@ |
| **Response Body sample** | @@BLOCK_17@@ |

| **Step 4c** | **Create Integration History (Error) and alert to Integration Contact** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_history_records/create_alert` |
| **Query Params** | `fields=["id","document-id","status"]` |
| **Sample URL** | `https:///api/integration_history_records/create_alert?fields=["id","document-id","status"]` |
| **Query Body sample** | @@BLOCK_18@@ |
| **Response Body sample** | @@BLOCK_19@@ |

## Option 3: Leverage full Coupa Integrations monitoring

**Description**

In this scenario, we create an Integration run that tracks

- The status of the Integration (pending/started/errored/successful/failed)

- The total number of Invoice processed

- The number of Success and Errors

- The list of Integration Errors and their statuses (resolved or not)

For each Invoice we:

- Resolve the previous Integration History Record for the document

- Create an Integration History Record

- In case of an error, create an Integration Error and an Alert to the Integration Contact

You will be able to monitor all Integration Runs for your Integration with this URL:

```text
https://<your instance
hostname>/integrations/<your integration
id>/integration_runs
```

.![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/po-api-integration-01.png)

You will use the Standard Invoice Integration Error Data Table to list all Invoices with Integration Error pending resolution. You can find it at:

```text
https://<your
instance hostname>/integration_errors
```

.![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/inoice-int-records-03.png)

**Orchestration diagram**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/orchestration-03.png)

**Steps / API calls details**

| **Step 1** | **Create Integration Run** |
| --- | --- |
| **Method** | POST |
| **API** | `https:///api/integration_runs` |
| **Query Params** | N/A |
| **Query Body sample** | @@BLOCK_22@@ |
| **Response Body sample** | @@BLOCK_23@@ |

| **Step 2** | **Get the list and details of the Coupa Invoices to create/update in the ERP. Selection criteria includes the Export Flag and Invoice Status.** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/invoices/` |
| **Query Params** | `filter=`<br>`offset=10`<br>`exported=false`<br>`status[in]=approved,voided` |
| **Sample URL** | `https:///api/invoices?filter=&offset=10&exported=false&status[in]=approved,voided` |
| **Query Body sample** | N/A |
| **Response Body sample** | ![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/response-03.png) |

| **Step 3** | **Start Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_runs//run` |
| **Query Params** | N/A |
| **Query Body sample** | @@BLOCK_24@@ |
| **Response Body sample** | @@BLOCK_25@@ |

| **Step 4** | **Mark individual Invoice as exported** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/invoices/` |
| **Query Params** | `exported=true`<br>`fields=["id","exported"]` |
| **Sample URL** | `https:///api/invoices/?exported=true&fields=["id","exported"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_26@@ |

This is where the creation/update of the Invoice in the ERP happens.

| **Step 5a** | **Get unresolved Integration History Record** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `resolved=false`<br>`document-type=InvoiceHeader`<br>`document-id=`<br>`fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records?resolved=false&document-type=InvoiceHeader&document-id=&fields=["id","document-id","status","resolved"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_27@@ |

| **Step 5b** | **Resolve previous Integration History Record** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_history_records//resolve` |
| **Query Params** | `fields=["id","document-id","status","resolved"]` |
| **Sample URL** | `https:///api/integration_history_records//resolve?fields=["id","document-id","status","resolved"]` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_28@@ |

| **Step 6a** | **Get unresolved Integration Error Record** |
| --- | --- |
| **Method** | GET |
| **API** | `https:///api/integration_errors` |
| **Query Params** | `resolved=false`<br>`document-type=InvoiceHeader`<br>`document-id=` |
| **Sample URL** | `https:///api/integration_errors?resolved=false&document-type=InvoiceHeader&document-id=` |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_29@@ |

| **Step 6b** | **Resolve previous Integration History Record** |
| --- | --- |
| **Method** | PUT |
| **API** | https://*<your instance hostname>*/api/integration_errors/*<Old Integration Error Record id>*/resolve |
| **Query Params** | N/A |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_30@@ |

| **Step 7a** | **Update a Custom Fields for ERP document number (Success)** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/invoices/` |
| **Query Params** | @@BLOCK_31@@ |
| **Sample URL** | @@BLOCK_32@@ |
| **Query Body sample** | @@BLOCK_33@@ |
| **Response Body sample** | @@BLOCK_34@@ |

| **Step 7b** | **Create Integration History (Success) It must reference the Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_history_records` |
| **Query Params** | `fields=["id","document-id","status"]` |
| **Sample URL** | `https:///api/integration_history_records?fields=["id","document-id","status"]` |
| **Query Body sample** | @@BLOCK_35@@ |
| **Response Body sample** | @@BLOCK_36@@ |

| **Step 7c** | **Create Integration Error and alert to Integration Contact It must reference the Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_errors/create_alert` |
| **Query Params** | N/A |
| **Query Body sample** | @@BLOCK_37@@ |
| **Response Body sample** | @@BLOCK_38@@ |

| **Step 8** | **Successfully End Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_runs//success` |
| **Query Params** | N/A |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_39@@ |

If there is a general failure during the Integration run.

| **Step x** | **Raise Failure for the Integration Run** |
| --- | --- |
| **Method** | PUT |
| **API** | `https:///api/integration_runs//fail` |
| **Query Params** | N/A |
| **Query Body sample** | N/A |
| **Response Body sample** | @@BLOCK_40@@ |
