---
title: "Lookup Values API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/lookup-values-api-(lookup_values)/lookup-values-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/lookup-values-api-(lookup_values)/lookup-values-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:15+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Lookup Values API (/lookup_values)"
  - "Lookup Values API Example Calls"
---

# Lookup Values API Example Calls

## Different Query Options for Lookup Values

Here are more examples of how to use the Lookup Values API to
query and get the result set you want.

This Query will give you the lookup values which are active

`https://.coupahost.com/api/lookup_values?active=true`

This query will give you the lookup values which were created
after a certain date

`https://.coupahost.com/api/lookup_values?created_at[gt]=2014-04-22`

This query will give you all the lookup values for all the
lookups which were created after a certain date

`https://.coupahost.com/api/lookup_values?[lookup][created-at][gt]=2014-04-22`

## Lookup Values API Get Example

In this example, we queried for a single lookup value with an ID
of 1.

We did a GET to the URL:

```text
https://<instance url>/api/lookup_values/1
```

or

```text
https://<instance url>/api/lookup_values?1
```

Here is the response matching the search criteria:

```text
<?xml version="1.0" encoding="UTF-8"?>
<lookup-value>
<id type="integer">1</id>
<created-at type="datetime">2014-04-23T11:24:10-07:00</created-at>
<updated-at type="datetime">2014-04-24T09:08:41-07:00</updated-at>
<active type="boolean">true</active>
<name>TestAccount1</name>
<description>DescAccountNo1</description>
<external-ref-num>ExtRefAccnt1</external-ref-num>
<external-ref-code>ExtRefAccnt1</external-ref-code>
<parent-id nil="true" />
<lookup-id type="integer">1</lookup-id>
<depth type="integer">0</depth>
<account-type nil="true" />
<lookup>
<id type="integer">1</id>
<created-at type="datetime">2014-04-23T11:22:10-07:00</created-at>
<updated-at type="datetime">2014-04-23T11:22:10-07:00</updated-at>
<active type="boolean">true</active>
<name>Account</name>
<description>Account</description>
<fixed-depth type="integer">0</fixed-depth>
<level-1-name />
<level-2-name />
<level-3-name />
<level-4-name />
<level-5-name />
<level-6-name />
<level-7-name />
<level-8-name />
<level-9-name />
<level-10-name />
</lookup>
<created-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade@coupa.com</email>
<employee-number nil="true" />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<mycustom-userfield />
</created-by>
<updated-by>
<id type="integer">1</id>
<login>coupasupport</login>
<email>upgrade@coupa.com</email>
<employee-number nil="true" />
<firstname>Coupa</firstname>
<lastname>Support</lastname>
<salesforce-id nil="true" />
<mycustom-userfield />
</updated-by>
</lookup-value>
```

## Lookup Values Create

In this example we are inserting a Lookup Values for one of the
existing Lookups in COUPA. We are not using any Coupa system ID's
for any of the reference objects.

We posted it to the URL:

```text
https://<instance url>/api/lookup_values.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<lookup-value>
<name>TestAccount2</name>
<description>DescAccountNo2</description>
<external-ref-num>ExtRefAccnt2</external-ref-num>
<external-ref-code>ExtRefAccnt2</external-ref-code>
<active>yes</active>
<lookup>
<name>Account</name>
</lookup>
</lookup-value>
```

## Lookup Values API PUT Example

Example for a PUT:

**To activate or deactivate a lookup value**

URL: `https:///api/lookup_values/`

**Sample Code for deactivating a lookup value**

```text
<?xml version="1.0" encoding="UTF-8"?>
<lookup-value>
<active>false</active>
</lookup-value>
```

To Update the description of a lookup value

URL:
`https:///api/lookup_values/`

**Sample Code to Update the lookup for a lookup
value**

```text
<?xml version="1.0" encoding="UTF-8"?>
<lookup-value>
<lookup-id>2</lookup-id>
</lookup-value>
```
