---
title: "Differences between XML and JSON in Coupa"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/differences-between-xml-and-json-in-coupa"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/differences-between-xml-and-json-in-coupa"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Differences between XML and JSON in Coupa"
---

# Differences between XML and JSON in Coupa

## Datatypes in JSON

For JSON, Coupa supports the following: null, boolean, number, and strings. Precision, version, and similar values use the number datatype, where decimal precision, for example, is a string. All values not explicitly called out use the string datatype.

There are four differences to be aware of between how Coupa’s REST APIs work when using JSON vs. using XML.

## JSON Doesn't Use a Parent Node

In XML we get parent node at the start and end of response. In JSON no parent node available in response.

## XML Response

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<id type="integer">41</id>
<created-at type="dateTime">2016-10-07T06:56:43-07:00</created-at>
<updated-at type="dateTime">2016-10-07T06:56:43-07:00</updated-at>
<name>account_1475848602.731066227</name>
<code>segment11475848602928</code>
<active type="boolean">true</active>
<segment-1>segment11475848602928</segment-1>
<segment-2 nil="true" />
---------------------------------------------
</account>
```

## JSON Response

```text
{
"id": 43,
"created-at": "2016-10-07T06:59:46-07:00",
"updated-at": "2016-10-07T06:59:46-07:00",
"name": "account_1475848721.456090234",
"code": "segment11475848721222",
"active": true,
"segment-1": "segment11475848721222"
}
```

## Different Response for No Results

When there are no results matching the GET query, our XML response throws a 404 error, where the JSON response provides a blank array.

**GET:** https://dashmaster17-0.coupadev.com/api/accounts?id=NON_EXISTING

## XML Response

```text
<?xml version="1.0" encoding="UTF-8"?>
<errors>
<error>No results match your search criteria.</error>
</errors>
```

## JSON GET API

```text
[ ]
```

## Different Nodes for Error Message

## XML Response

```text
<?xml version="1.0" encoding="UTF-8"?>
<errors>
<error>Segment 1 - Cost Center can't be blank.</error>
</errors>
```

## JSON Response

```text
{
"errors": {
"account": [
"Segment 1 - Cost Center can't be blank"
]
}
}
```

## Different response for Country in Address API call

Below are the two sets of responses for a POST API call: [http://localhost:3000/api/addresses](http://localhost:3000/api/addresses)

## XML Response

```text
<?xml version="1.0" encoding="UTF-8"?>
<address>
<id type="integer">97</id>
<created-at type="dateTime">2016-10-07T07:19:07-07:00</created-at>
<updated-at type="dateTime">2016-10-07T07:19:07-07:00</updated-at>
<name>address_1475849947.739228964</name>
<location-code nil="true" />
<street1>2 W 5th Ave</street1>
--------------------------------
<country>
<id type="integer">223</id>
<code>US</code>
<name>United States</name>
</country>
--------------------------------
</address>
```

## JSON Response

```text
{
"id": 99,
"name": "address_1475850128.91",
"street1": "2 W 5th Ave",
"street2": "Suite 300",
"city": "San Mateo",
"state": "CA",
"postal_code": "94404",
"country_id": 223,
"address_owner_type": "BusinessGroup",
"parent_address_id": null,
"country": "United States"
}
```
