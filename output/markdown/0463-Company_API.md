---
title: "Company API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/company-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/company-api"
status_code: 200
fetched_at: "2026-04-09T12:00:53+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The CSO API"
  - "Company API"
---

# Company API

Use the Company API's to create, update, or query the Company Data.

The URL to access the API's is : https://<instance>.cso.coupahost.com/api/companies

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/companies` | index | Performs Get action to retrieve all Companies |
| POST | `/api/companies` | create | Creates one or more Companies objects. |
| PUT | `/api/companies` | update | Updates one or more Companies . Can perform mass updates. |
| GET | `/api/companies/:id` | show | Show one Company data. |
| PUT | `/api/companies/:id` | update | Update one Company at a time using the ID |

## Elements

These are the elements available for the Company API

| **Field Name** | **Field Description** | **Req'd** | **Unique?** | **Allowable Values** | **In** | **Out *** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | ID of the Company | | Yes | | | yes | integer |
| state | Status of the company | | | Active, Removed (Case-Sensitive) | yes | yes | string |
| name | Name of the Company | | Yes | | yes | yes | string |
| phone-number | Phone number of the company | | | | yes | yes | string |
| email | Email of the company | | | | yes | yes | string |
| street | Street part of the company address | | | | yes | yes | string |
| zipcode | Zip code part of the company address | | | | yes | yes | string |
| city | City part of the company address | | | | yes | yes | string |
| country | Country part of the company address | | | | yes | yes | string |
| duns-scac | The duns scac code for the company. | | | | yes | yes | string |
| keywords | Keywords associated to the company | | | | yes | yes | string |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Response payload does not show null values.

## Examples

In this example, we queried for a company API. We did a GET to the URL:

https://<instance>.cso.coupahost.com/api/companies

## Company GET Response

```text
{
"total": 7,
"compannies": [
{
"id": "9219592888303484960",
"state": "Active",
"name": "! New Supplier (Spanish)"
},
{
"id": "9219594398656586067",
"state": "Active",
"name": "! Simon Test Organization",
"email": "simon@kepgames.com"
},
{
"id": "9219592919623127484",
"state": "Active",
"name": "! SKF (test bidders)"
},
{
"id": "9219592881350550871",
"state": "Active",
"name": "! Spanish bidder",
"email": "heloisa.spanish@tradeext.com"
},
{
"id": "9219592230193035378",
"state": "Active",
"name": "! TE",
"email": "lorena@te.se",
"duns-scac": "testing123456789",
"keywords": "test"
},
{
"id": "9219596145584379778",
"state": "Active",
"name": "! TE Test Company"
},
{
"id": "9219592639285418804",
"state": "Active",
"name": "! TE Test Company 2",
"phone-number": "123-234-3456",
"email": "testcompany2+upg@coupa.com",
"street": "street address1",
"zip-code": "12345",
"city": "valahalla",
"country": "United States Minor Outlying Islands",
"keywords": "Carrier"
}
]
}
```

## Create/Update

The following describes how you can use the Coupa API to perform actions on Company.

## Create

`/api/companies`

The below payload creates two Companies.

```text
Payload:
{
"companies": [
{
"state": "Active",
"name": "Yes Heloisa",
"duns-scac": "Shall be updated"
},
{
"name": "TE Test Company 2",
"phone-number": "123-234-3456",
"email": "testcompany2+upg@coupa.com"
}
]
}

Response: 201
{
"result": [
{
"type": "api.post.added",
"description": "2 objects created."
}
],
"added": 2,
"companies": [
{
"id": "9220538753256092391"
},
{
"id": "9220538753250662192"
}
]
}
```

## Update

`/api/companies`

The below payload updates a Company(ies).

```text
To update one or more Company at a time:
Payload:
{
"companies": [
{
"id": "9219594319065198091",
"state": "Active",
"name": "! (TE) Heloisa",
"duns-scac": "Shall be updated"
},
{
"id": "9219596218212801426",
"state": "Active",
"name": "! (TE) Org only with bidders (Italian)",
"duns-scac": "Shall be updated",
"email": "testbidders_itl@coupa.com"
},
{
"id": "9219596218212801429",
"state": "Active",
"name": "! (TE) Org with only bidders",
"duns-scac": "Shall be updated",
"keywords": "Bidders"
}
]
}

Response: 200 OK
{
"result": [
{
"type": "api.put.updated",
"description": "3 objects updated."
}
],
"updated": 3
}
```

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Updates are done in a lenient manner, i.e. if updating one resource fails, the other ones might be successful. Company ID is required for updates.

Successful requests will return `HTTP 200 Response`. The body of the response will include the created requisition. Unsuccessful requests will return

```text
HTTP 400 Bad
Request
```

. The body of the response will include validation errors formatted as XML.
