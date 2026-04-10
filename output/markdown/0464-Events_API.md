---
title: "Events API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/events-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-cso-api/events-api"
status_code: 200
fetched_at: "2026-04-09T12:00:53+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The CSO API"
  - "Events API"
---

# Events API

Use the Events API's to create, update, or query the Event Data. This includes specific
endpoints to take action (create/update/delete) as well as events related to fact-sheets ,
rows, fields and labels.

The URL to access the API's is :
https://<instance>.cso.coupahost.com/api/events

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET | `/api/events` | index | Performs Get action to retrieve all Events |
| POST | `/api/events` | create | Creates one or more events objects. |
| PUT | `/api/events` | update | Updates one or more events . Can perform mass updates. |
| DELETE | `/api/events` | delete | Deletes one more more events. Can perform mass deletes. |
| GET | `/api/events/:id` | show | Show one event data. |
| PUT | `/api/events/:id` | update | Update one event at a time using the ID |
| DELETE | `/api/events/:id` | delete | Delete one event at a time. |

## Elements

These are the elements available for
the Events API

| **Field Name** | **Field Description** | **Req'd** | **Unique?** | **Allowable Values** | **In** | **Out *** | **Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| id | ID of the Event | | Yes | | | yes | integer |
| market-id | The id of the market that the event belongs to. Once set, it cannot be modified. | | Yes | | yes | yes | string |
| state | Status / Current Phase of the event | | | Setup,Active,Terminated (Case-Sensitive) | yes | yes | string |
| name | Name of the Event | | | | yes | yes | string |
| description | Short Description of the Event | | | | yes | yes | string |
| reference-number | A field for a reference number for identifying the event | | | | yes | yes | string |
| event-number | A unique id of the event. This value is an incremental value | | yes | | | yes | integer |
| time-zone | Timezone for the event | | | | yes | yes | string |
| settings | Settings for the event | | | | yes | yes | string |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Response payload does not show null values.

## Examples

In this example, we queried for a
Events API. We did a GET to the
URL:

https://<instance>.cso.coupahost.com/api/events

## Events GET Response

```text
{
"total": 5,
"events": [
{
"id": "9219595375673293031",
"market-id": "9219595214580536433",
"state": "Setup",
"name": "APC Training Project",
"description": "For Bids",
"event-number": 10,
"settings": {
"currency": "USD"
}
},
{
"id": "9219601944812992706",
"market-id": "9219596879086622384",
"state": "Setup",
"name": "API - Data storage",
"description": "Hamno Testing",
"event-number": 11,
"time-zone": "Europe/Stockholm",
"settings": {
"currency": "EUR"
}
},
{
"id": "9219592828238410706",
"market-id": "9219592396342653837",
"state": "Active",
"name": "**IT Hardware and Services 2014",
"description": "Indirect Services",
"reference-number": "MC-IN-15/02",
"event-number": 613,
"settings": {
"currency": "GBP"
}
},
{
"id": "9219593444808990596",
"market-id": "9219593040793966498",
"state": "Terminated",
"name": "!*** Test procedures ***! (for backup purposes only)",
"description": "Tasks to be performed when a new release is about to be launched",
"event-number": 1602,
"settings": {
"currency": "USD"
}
},
{
"id": "9219594228963465852",
"market-id": "9219592396342653837",
"state": "Setup",
"name": "**Air Freight Tender example - sanitised 9/12/15",
"description": "Example Air Freight tender",
"reference-number": "MC-A15-01",
"event-number": 13,
"settings": {
"currency": "SEK"
}
}
]
}
```

## Create/Update/Delete

The following describes
how you can use the Coupa API to perform actions on Events.

## Create

`/api/events`

The
below payload creates two
Events.

```text
Payload:
{
"events": [
{
"market-id": "9220538753220565329",
"name": "IT Hardware and Services 2021",
"description": "direct Services",
"reference-number": "DEMO-ref1",
"settings": {
"currency": "USD"
}
},
{
"market-id": "9220538753220565329",
"state": "Setup",
"name": "Services ONLY",
"description": "same market with state, timezone and no reference number ",
"time-zone": "Europe/Stockholm",
"settings": {
"currency": "EUR"
}
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
"events": [
{
"id": "9220538753252871154"
},
{
"id": "9220538753252871160"
}
]
}
```

## Update

`/api/events`

The
below payload updates a
Events.

```text
To update one or more Event at a time:
Payload:
{
"events": [
{
"id": "9220538753252871154",
"state": "Active",
"name": "IT Hardware and Services 2021-ABC",
"description": "direct Services - ABC",
"reference-number": "DEMO-reference"
},
{
"id": "9220538753252871160",
"name": "Services channges ONLY"
}
]
}

Response: 200 OK
{
"result": [
{
"type": "api.put.updated",
"description": "2 objects updated."
}
],
"updated": 2
}

You can update all fields except event-number and market-id.
```

## Delete

`/api/events`

The above API
can be used to delete more than one event at a
time.

```text
Payload:
{
"events": [
{
"id": "9220538753252871154"
}
]
}

Response: 200 OK
{
"result": [
{
"type": "event.deleted.logMsg",
"description": "The event IT Hardware and Services 2021-ABC was deleted."
}
],
"deleted": 1
}
```

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Updates
are done in a lenient manner, i.e. if updating one resource fails, the other ones might be
successful. The payload deleted one event. For deletion or updates, event ID is
required.

Successful requests will return `HTTP 200 Response`.
The body of the response will include the created requisition. Unsuccessful requests will
return

```text
HTTP 400 Bad
Request
```

. The body of the response will include validation errors formatted as
XML.
