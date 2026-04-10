---
title: "Addresses API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)/addresses-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/address-api-(addresses)/addresses-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:09+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Address API (/addresses)"
  - "Addresses API Example Calls"
---

# Addresses API Example Calls

## Get Address Query Options

Here are some more examples of how to use the address API to
query and get the result set you want.

This query will return all company addresses created after the
date, November 1, 2010.

```text
https://<instance url>/api/addresses?created_at[gt]=2010-11-01T00:00:00
```

This query will return all active and where the nickname of the
company addresses contains the words "San Francisco".

```text
https://<instance url>/api/addresses?active=true&name[contains]=San+Francisco
```

This query will return all company addresses in United States
and in the state of California

```text
https://<instance url>/api/addresses?country[name]=United+States&state=CA
```

This query will return all personal addresses where the nickname
of the address contains the word "Home Office"

```text
https://<instance url>/api/users/85/addresses?name=Home+Office
```

## Get Address

In this example, we queried for a company address record with an
ID of 6.

We did a GET to the URL:

`https:///api/addresses/6`

or

`https:///api/addresses?id=6`

Here is the response matching the search
criteria:

```text
<?xml version="1.0" encoding="UTF-8"?>
<addresses type="array">
<address>
<attention />
<city>San Francisco</city>
<id type="integer">14</id>
<name>San Francisco Office</name>
<postal-code>94450</postal-code>
<state>CA</state>
<street1>150 Main Street</street1>
<street2 />
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</address>
</addresses>
```

In this example, we queried for all the personal address records
for user with an ID of 85.

We did a GET to the URL:

```text
https://<instance url>/api/users/85/addresses
```

Here is the response matching the search
criteria:

```text
<?xml version="1.0" encoding="UTF-8"?>
<addresses type="array">
<address>
<attention>Margret Patrick</attention>
<city>San Mateo</city>
<id type="integer">123</id>
<name>Home Office</name>
<postal-code>94402</postal-code>
<state>CA</state>
<street1>111 Main Street</street1>
<street2 />
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</address>
<address>
<attention>Margret Patrick</attention>
<city>San Francisco</city>
<id type="integer">124</id>
<name>test2</name>
<postal-code>94103</postal-code>
<state>CA</state>
<street1>2600 Polk Street</street1>
<street2 />
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</address>
</addresses>
```

## Address Create

In this example, we are creating a company address.

We posted it to the URL

```text
https://<instanceurl>/api/addresses.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<address>
<name>Silicon Valley</name>
<city>San Mateo</city>
<postal-code>94404</postal-code>
<state>CA</state>
<street1>2 W 5th Ave</street1>
<street2>Suite 300</street2>
<country>
<code>US</code>
<name>United States</name>
</country>
</address>
```

In this example, we are creating a personal address for User
with the User ID of 85.

We post it to the URL

```text
https://<instance url>/api/users/85/addresses
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<address>
<attention nil="true" />
<city>San Mateo</city>
<id type="integer">125</id>
<name>Silicon Valley</name>
<postal-code>94400</postal-code>
<state>CA</state>
<street1>2 W 5th Ave</street1>
<street2 nil="true" />
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</address>
```

## Remit-To Address Create

In this example, we are creating a Remit-To address for a
specific supplier

We posted it to the URL

```text
https://<instance url>/api/suppliers/<supplier id>/addresses
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<remit-to-address>
<remit-to-code>100</remit-to-code>
<name>100 Ellsworth</name>
<street1>100 Ellsworth Ave.</street1>
<city>SAN MATEO</city>
<state>CA</state>
<postal-code>94404</postal-code>
<active type="boolean">true</active>
<country>
<code>US</code>
</country>
</remit-to-address>
```

## Address Update

In these examples, we are updating a single company address
record.

We did a PUT to the URL:

```text
https://<instance url>/api/addresses/<address ID>
```

For example, to update the address record with a nickname and
Line 2 for address ID 122:

URL:

```text
https://<instance url>/api/addresses/122
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<address>
<name>South Bay Office</name>
<street2>Suite 200</street2>
</address>
```

For example, to deactivate a company address with ID
122:

URL:

```text
https://<instance url>/api/addresses/122
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<address>
<active>false</active>
</address>
```

For example, to deactivate a personal address for user ID 85 and
address ID 125:

URL:

```text
https://<instance url>/api/users/85/addresses/125
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<address>
<active>false</active>
</address>
```

## Supplier Remit-To Address Update

In these examples, we are updating a single Supplier Remit-To address. The way to update
the remit-to address, while just as simple as regular address, it does require knowing both
the supplier and remit-to id

We did a PUT to the URL:

```text
https://<instance url>/api/suppliers/<supplier id>/addresses/<remit-to
address ID>
```

For example, to update the Remit-To Address to fix the remit-to code from whatever the
current value is to "001" for Remit-To Address ID 23287 for Supplier with ID 12

URL:

```text
https://<instance url>/api/suppliers/12/remit_to_addresses/23287
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<remit-to-address>
<remit-to-code>001</remit-to-code>
</remit-to-address>
```

For example, to deactivate a remit-to address with ID 232887 for supplier with id 12:

URL:

```text
https://<instance url>/api/suppliers/12/remit_to_addresses/23287
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<remit-to-address>
<remit-to-code>001</remit-to-code>
<active>false</active>
</remit-to-address>
```
