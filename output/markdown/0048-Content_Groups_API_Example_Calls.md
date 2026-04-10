---
title: "Content Groups API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)/content-groups-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)/content-groups-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:11+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Content Groups API (/business_groups)"
  - "Content Groups API Example Calls"
---

# Content Groups API Example Calls

## Different Query Options for Content Groups

Here are more examples of how to use the Content Groups API to
query and get the result set you want.

This query will give you the content groups with name as
test

`https://.coupahost.com/api/business_groups?name[contains]=test`

This query will give you the content groups updated by a
particular user with Login = testsupport

`https://.coupahost.com/api/business_groups?created_by[login]=testsupport`

This query will give you all the business groups created after
March 1st 2014

`https://.coupahost.com/api/business_groups?created-at[gt]=2014-03-01T12:00:00`

## GET Single Content Group

In this example, we queried for a single expense report with an
ID of 9.

We did a GET to the URL:

`https://.coupahost.com/api/business_groups/9`

or

`https://.coupahost.com/api/business_groups?id=9`

The Result:

**Query Content Group Sample Result**

```text
<?xml version="1.0" encoding="UTF-8"?>
<business-group>
<id type="integer">9</id>
<created-at type="datetime">2014-04-04T14:04:20-07:00</created-at>
<updated-at type="datetime">2014-04-04T14:04:20-07:00</updated-at>
<name>Test1</name>
<description>test1 group</description>
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
</business-group>
```

## Content Groups Creation

In this example we are creating a Content Group. We are not
using any Coupa system ID's for any of the reference objects.

We posted it to the URL:

```text
https://<instance url>/api/business_groups/.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<business-group>
<name>test sample content group</name>
<description>What Pattern Group</description>
</business-group>
```
