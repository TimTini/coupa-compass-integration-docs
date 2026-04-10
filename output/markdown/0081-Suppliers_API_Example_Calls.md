---
title: "Suppliers API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/suppliers-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/suppliers-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Suppliers API Example Calls"
---

# Suppliers API Example Calls

## GET Supplier Query Options

Here are more examples of how to use the supplier API to query
and get the result set you want.

This query will return all suppliers with PO method set to
cXML:

```text
https://<instance url>/api/suppliers?po-method=cxml
```

This query will return all suppliers with payment term of Net
30:

```text
https://<instance url>/api/suppliers?payment-term[code]=Net+30
```

This query will return all suppliers where payment discount is given if within 10 days of
invoicing and the supplier is currently active in the system:

```text
https://<instance url>/api/suppliers?payment-term[days-for-discount-payment]=10&status=active
```

This query will return all suppliers that was created after January 1, 2010 12:00:00:

```text
https://<instance url>/api/suppliers?created-at[gt]=2010-01-01T12:00:00
```

This query will return all suppliers whose PO method is set to cXML and where the buyer
domain value contains the word "domain":

```text
https://<instance url>/api/suppliers?po-method=cxml&cxml-domain[contains]=domain
```

This query will return all suppliers who are allowed cXML invoicing and where the cXML
invoice setup of the supplier domain value contains the word "supplier":
`https://.coupahost.com/api/suppliers?allow-cxml-invoicing=true&cxml-supplier-domain[contains]=supplier`

This query will return all suppliers whose primary contact email contains the value
"coupa.com" and the supplier address where the city is Charleston:

```text
https://<instance url>/api/suppliers?primary-contact[email][contains]=coupa.com&primary-address[city]=Charleston
```

This query will return all suppliers who has at least 5 user reviews in the system.

```text
https://<instance url>/api/suppliers?reviews-count[gt]=5
```

## Get Supplier

In this example, we queried for a single supplier record with an
ID of 6.

We did a GET to the URL:

`https:///api/suppliers/6`

or

`https:///api/suppliers?id=6`

Here is the response matching the search
criteria:

```text
<?xml version="1.0" encoding="UTF-8"?>
<suppliers type="array">
<supplier>
<id type="integer">6</id>
<created-at type="datetime">2008-10-27T12:56:39-07:00</created-at>
<updated-at type="datetime">2009-07-01T11:59:33-07:00</updated-at>
<name>VWR</name>
<number></number>
<status>active</status>
<website></website>
<po-method>cxml</po-method>
<cxml-url>http://www.dummy.com</cxml-url>
<cxml-domain>http://demo.coupahost.com</cxml-domain>
<cxml-identity>Coupa</cxml-identity>
<cxml-supplier-domain>http://www.vwr.com</cxml-supplier-domain>
<cxml-supplier-identity>VWR-Test</cxml-supplier-identity>
<cxml-secret>test</cxml-secret>
<cxml-protocol>cXML</cxml-protocol>
<po-email>upgrade@coupa.com</po-email>
<account-number></account-number>
<duns></duns>
<tax-id></tax-id>
<coupa-connect-secret></coupa-connect-secret>
<invoice-matching-level>2-ay</invoice-matching-level>
<primary-contact>
<email>upgrade@coupa.com</email>
<id type="integer">6</id>
<name-additional nil="true"></name-additional>
<name-family>Frontage</name-family>
<name-fullname nil="true"></name-fullname>
<name-given>Dawn</name-given>
<name-prefix nil="true"></name-prefix>
<name-suffix nil="true"></name-suffix>
<notes nil="true"></notes>
</primary-contact>
<primary-address>
<attention nil="true"></attention>
<city>Portland</city>
<id type="integer">6</id>
<name>VWR</name>
<postal-code>82323</postal-code>
<state>OR</state>
<street1>09 Addison Ave</street1>
<street2></street2>
<country>
<code>US</code>
<id type="integer">223</id>
<name>United States</name>
</country>
</primary-address>
<payment-term>
<code>2/10 Net 30</code>
<days-for-discount-payment type="integer">10</days-for-discount-payment>
<days-for-net-payment type="integer">30</days-for-net-payment>
<discount-rate type="float">2.0</discount-rate>
<id type="integer">3</id>
</payment-term>
</supplier>
</suppliers>
```

## Supplier Create - Active and Detail

In this example we are creating an active supplier. We are not
using any Coupa system ID's for any of the reference objects.

We posted it to the URL:

```text
https://<instance url>/api/suppliers.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<name>CDW</name>
<number>cdw2323</number>
<status>active</status>
<po-method>prompt</po-method>
<po-email />
<account-number>2323</account-number>
<duns />
<tax-id>283923</tax-id>
<invoice-matching-level>3-way</invoice-matching-level>
<payment-term>
<code>Net 30</code>
</payment-term>
<primary-contact>
<email>joe.smith@cdw.com</email>
<name-family>Smith</name-family>
<name-given>Joe</name-given>
<name-prefix nil="true" />
<name-suffix nil="true" />
<notes nil="true" />
<phone-work>
<area-code>650</area-code>
<country-code>1</country-code>
<extension nil="true" />
<number>4442932</number>
</phone-work>
<phone-mobile>
<area-code nil="true" />
<country-code>1</country-code>
<extension nil="true" />
<number />
</phone-mobile>
<phone-fax>
<area-code nil="true" />
<country-code>1</country-code>
<extension nil="true" />
<number />
</phone-fax>
</primary-contact>
<primary_address>
<street1>1234 Concur Drive</street1>
<street2 />
<city>San Mateo</city>
<state>CA</state>
<postal_code>93325</postal_code>
<country>
<code>US</code>
</country>
</primary_address>
</supplier>
```

## Supplier Create- Draft and Basic

In this example we are creating a draft supplier. We are not
using any Coupa system ID's for any of the reference objects.

We posted it to the URL:

```text
https://<instance url>/api/suppliers. This created the supplier in a draft status.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<name>CDW</name>
<po-method>prompt</po-method>
<account-number>2323</account-number>
<duns />
<tax-id />
<invoice-matching-level>3-way</invoice-matching-level>
<payment-term>
<code>Net 30</code>
</payment-term>
</supplier>
```

## Update Supplier - full update

In these examples, we are updating different information on the
supplier record.

We did a PUT to the URL:

```text
https://<instance url>/api/suppliers/<supplier id>
```

For example, to update the supplier's PO method to cXML for
supplier id 83:

URL:

```text
https://<instance url>/api/suppliers/83
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<po-method>cxml</po-method>
<cxml-url>https://testurl.com</cxml-url>
<cxml-domain>NetworkID</cxml-domain>
<cxml-identity>coupa</cxml-identity>
<cxml-supplier-domain>NetworkID</cxml-supplier-domain>
<cxml-supplier-identity>supplierID1</cxml-supplier-identity>
<cxml-secret>shhhhh</cxml-secret>
<cxml-protocol>cxml</cxml-protocol>
</supplier>
```

For example, to update the supplier's primary contact
information and several other pieces of supplier profile
information for supplier id 83:

URL:

```text
https://<instance url>/api/suppliers/83
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<account-number>123456</account-number>
<duns>DUNS-123</duns>
<tax-id>taxid-123</tax-id>
<invoice-matching-level>none</invoice-matching-level>
<primary-contact>
<email>supplier@test.com</email>
<name-family>Donovan</name-family>
<name-given>Fred</name-given>
<phone-work>
<area-code>415</area-code>
<country-code>1</country-code>
<extension nil="true" />
<number>4471010</number>
</phone-work>
<phone-fax>
<area-code>415</area-code>
<country-code>1</country-code>
<extension nil="true" />
<number>4471012</number>
</phone-fax>
</primary-contact>
</supplier>
```

For example, to update the supplier profile including address
update for supplier id 83:

URL:

```text
https://<instance url>/api/suppliers/83
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<name>Petra (US)</name>
<number>1-112</number>
<primary-address>
<street1>425 Market Street # 2250</street1>
<street2 />
<city>San Francisco</city>
<state>CA</state>
<postal_code>94105</postal_code>
<country>
<code>US</code>
</country>
</primary-address>
</supplier>
```

For example, to update the payment term and shipping term for
supplier id 83:

URL:

```text
https://<instance url>/api/suppliers/83
```

```text
<supplier>
<shipping-term>
<id>1</id>
</shipping-term>
<payment-term>
<id>5<id>
</payment-term>
</supplier>
```

## Update Supplier - simple update

In these examples, we are updating a single attribute on the
supplier record.

We did a PUT to the URL:

```text
https://<instance url>/api/suppliers/<supplier id>
```

For example, to update the supplier status to inactive for
supplier with supplier id 83:

**Update Supplier - Set to Inactive**

URL:

```text
https://<instance url>/api/suppliers/83
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<status>inactive</status>
</supplier>
```

For example, to update the supplier PO method to prompt with
supplier id 83:

**Update Supplier - Change PO Method**

URL: https://<instance
url>/api/suppliers/83

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<po-method>prompt</po-method>
</supplier>
```

For example, to update the primary supplier contact's email
address with supplier id 83:

**Update Supplier - Change Contact Email**

URL:

```text
https://<instance url>/api/suppliers/83
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<supplier>
<primary-contact>
<email>test@test.com</email>
</primary-contact>
</supplier>
```
