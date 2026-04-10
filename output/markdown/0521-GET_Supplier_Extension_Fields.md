---
title: "GET Supplier Extension Fields"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-suppliers/get-supplier-extension-fields"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-suppliers/get-supplier-extension-fields"
status_code: 200
fetched_at: "2026-04-09T12:01:04+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
  - "GET Suppliers"
  - "GET Supplier Extension Fields"
---

# GET Supplier Extension Fields

Retrieves all extension field records for a specific supplier using the CRA Entity ID.

## Endpoint

| **Endpoint** | `/api/suppliers/{entity_id}/extensionfields` |
| --- | --- |
| **Method** | GET |

## Headers

| **Header** | **Argument** |
| --- | --- |
| Authorization | Bearer token |
| Accept | application/json or application/xml |

## Parameters

| **Parameter** | **Description** |
| --- | --- |
| limit | (Optional) Maximum number of items in the response. Maximum: 50. |
| offset | (Optional) Number of items to skip from the start. Default: 0. |
| name | (Optional) Extension field name. |

## Get extension fields

Endpoint

GET `/api/{entity_id}/extensionfields`

Example cURL request

```text
curl --location 'https://<your-instance>.risk.com/api/suppliers/8df17abd-1ce4-47dd-96a9-03c310ddd230/extensionfields' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••'
```

Example response

```text
{
"result": {
"supplierName": "Auto_BulkUpload_BE_05032023234658_T2",
"supplierId": "8df17abd-1ce4-47dd-96a9-03c310ddd230",
"extensionFields": [
{
"name": "bitsight_data_breaches",
"value": ""
},
{
"name": "bitsight_ssl_certificates",
"value": ""
},
{
"name": "bitsight_monitoring_status",
"value": ""
},
{
"name": "tr_wc1_gender",
"value": ""
},
{
"name": "bitsight_rating_date",
"value": ""
},
{
"name": "bitsight_rating",
"value": ""
},
{
"name": "bitsight_spf",
"value": ""
},
{
"name": "bitsight_dnssec",
"value": ""
},
{
"name": "bitsight_file_sharing",
"value": ""
},
{
"name": "tr_wc1_matchcount",
"value": ""
},
{
"name": "tr_wc1_lastupdateddate",
"value": null
},
{
"name": "bitsight_ssl_configurations",
"value": ""
},
{
"name": "tr_wc1_placeofbirth",
"value": ""
},
{
"name": "r37restapitable2",
"value": ""
},
{
"name": "bitsight_mobile_software",
"value": ""
},
{
"name": "bitsight_mobile_application_security",
"value": ""
},
{
"name": "bitsight_patching_cadence",
"value": ""
},
{
"name": "bitsight_open_ports",
"value": ""
},
{
"name": "tr_wc1_nationality",
"value": ""
},
{
"name": "tr_wc1_monitoring",
"value": "true"
},
{
"name": "rulesdatetesting",
"value": null
},
{
"name": "r41restapitextbox",
"value": ""
},
{
"name": "bitsight_malware_servers",
"value": ""
},
{
"name": "bitsight_server_software",
"value": ""
},
{
"name": "bitsight_application_security",
"value": ""
},
{
"name": "bitsight_primary_domain",
"value": ""
},
{
"name": "tr_wc1_registeredcountry",
"value": ""
},
{
"name": "tr_wc1_nameidentifier",
"value": ""
},
{
"name": "r37restapitable",
"value": ""
},
{
"name": "tr_wc1_fieldscreenedfrom",
"value": ""
},
{
"name": "bitsight_spam_propagation",
"value": ""
},
{
"name": "bitsight_potentially_exploited",
"value": ""
},
{
"name": "bitsight_unsolicited_comm",
"value": ""
},
{
"name": "tr_wc1_nametype",
"value": ""
},
{
"name": "r41itemstatusselector",
"value": ""
},
{
"name": "bitsight_insecure_systems",
"value": ""
},
{
"name": "tr_wc1_countrylocation",
"value": ""
},
{
"name": "bitsight_botnet_infections",
"value": ""
},
{
"name": "bitsight_guid",
"value": ""
},
{
"name": "ssc_prif_supplier",
"value": ""
},
{
"name": "automigrationutilityprif_suppliers",
"value": ""
},
{
"name": "tr_wc1_dateofbirth",
"value": null
},
{
"name": "dj_lastupdateddate",
"value": null
},
{
"name": "bitsight_name",
"value": ""
},
{
"name": "tr_wc1_imonumber",
"value": ""
},
{
"name": "bitsight_dkim",
"value": ""
}
],
"totalCount": 46
},
"errors": [],
"success": true
}
```
