---
title: "Sourcing API (/quote_requests)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/sourcing-api-(quote_requests)"
status_code: 200
fetched_at: "2026-04-09T12:00:01+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Sourcing API (/quote_requests)"
---

# Sourcing API (/quote_requests)

## Overview

Use the sourcing API to:

- Create RFP, RFI, or RFQ type events.

- Extract supplier responses to the event.

- Award events to suppliers at the line level.

For the Coupa back end, a sourcing event is known as a quote
request.

## Endpoints

The following endpoints are available for sourcing API.

| **Resource** | **Path** | **Description** |
| --- | --- | --- |
| Sourcing events | `/api/quote_requests` | Endpoint for creating new sourcing events and managing existing events |
| Supplier responses | `/api/quote_responses` | Endpoint for working with supplier responses |
| Sourcing suppliers | `/api/quote_suppliers` | Endpoint for getting info about suppliers on a sourcing event |

## Example calls

## Create a new sourcing event

`POST /api/quote_requests/`

To create a new event, you can send a basic POST. Include the
`` element or else Coupa will default
to an RFI.

## Payload

```text
<?xml version="1.0" encoding="UTF-8" ?>
<quote-request>
<event-type type="symbol">RFQ</event-type>
</quote-request>
```

## 201 Success response

Coupa returns the newly-created sourcing event, with a unique
`` .

```text
<?xml version="1.0" encoding="UTF-8"?>
<quote-request>
<id type="integer">1434</id>
<created-at type="dateTime">2018-04-11T10:37:25-07:00</created-at>
<updated-at type="dateTime">2018-04-11T10:46:58-07:00</updated-at>
<description nil="true" />
<start-time type="dateTime">2018-04-11T17:00:00-07:00</start-time>
<start-on-submit type="boolean">true</start-on-submit>
<event-type type="symbol">rfi</event-type>
<end-time type="dateTime">2018-04-25T17:00:00-07:00</end-time>
<state>draft</state>
<comments nil="true" />
<allow-multiple-response type="boolean">true</allow-multiple-response>
<sealed-bids type="boolean">true</sealed-bids>
<allow-award-individual-line-items type="boolean">false</allow-award-individual-line-items>
<automatic-bid-unsealing type="boolean">true</automatic-bid-unsealing>
<timezone>US/Pacific</timezone>
<currency>...</currency>
<lots type="array" />
<lines type="array" />
<quote-suppliers type="array" />
<attachments type="array" />
<forms type="array" />
<quote-request-attachments type="array" />
<tags type="array" />
<business-partners type="array" />
</business-partners>
<created-by>...</created-by>
<updated-by>...</updated-by>
<custom-fields />
</quote-request>
```

## See all the supplier responses for a specific event

```text
GET /api/quote_requests/{event_id}/quote_responses
```

## 200 OK response

```text
<?xml version="1.0" encoding="UTF-8"?>
<quote-responses type="array">
<quote-response>
<id type="integer">1080</id>
<created-at type="dateTime">2018-04-10T05:51:28-07:00</created-at>
<updated-at type="dateTime">2018-04-10T05:51:34-07:00</updated-at>
<quote-request-id type="integer">1429</quote-request-id>
<submitted-at type="dateTime">2018-04-10T05:51:34-07:00</submitted-at>
<state>submitted</state>
<position type="integer">2</position>
<comments nil="true" />
<lines type="array">
<line>
<id type="integer">7447</id>
<created-at type="dateTime">2018-04-10T05:51:28-07:00</created-at>
<updated-at type="dateTime">2018-04-10T05:51:33-07:00</updated-at>
<price-amount type="decimal">200.0</price-amount>
<quantity type="decimal">1.0</quantity>
<reporting-price-amount type="decimal">200.0</reporting-price-amount>
<price-currency>...</price-currency>
<quote-request-line-id type="integer">5834</quote-request-line-id>
<lot-id type="integer">0</lot-id>
</line>
</lines>
<quote-supplier>
<id type="integer">1714</id>
<created-at type="dateTime">2018-04-10T05:50:21-07:00</created-at>
<updated-at type="dateTime">2018-04-10T05:51:34-07:00</updated-at>
<name>bnew</name>
<display-name>bnew</display-name>
<email>irairaira666555@gmail.com</email>
<contact-name />
<supplier nil="true" />
<created-by>...</created-by>
<updated-by>...</updated-by>
</quote-supplier>
</quote-response>
</quote-responses>
```

## Award an event to a supplier

`POST /api/quote_responses/{response_id}/award`

Once you've got the response `` , you can
use it to award the response.

## Payload to award

```text
<?xml version="1.0" encoding="UTF-8"?>
<root>
<quote_response_line_ids>7447</quote_response_line_ids>
</root>
```

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

If you don't specify any quote response line IDs (7447 as per example above) you can
award all lines at once.

## 200 OK Response

Coupa returns a 200 OK with no body.
