---
title: "Departments API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)/departments-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/departments-api-(departments)/departments-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Departments API (/departments)"
  - "Departments API Example Calls"
---

# Departments API Example Calls

## Different Query Options for Departments

Here are more examples of how to use the Departments API to
query and get the result set you want.

This query will give you the departments with name=Marketing

`https://.coupahost.com/api/departments?name=Marketing`

This query will give you the departments updated by a particular
user with Login = coupasupport

`https://.coupahost.com/api/departments?created_by[login]=coupasupport`

This query will give you all the expense reports created after
Jan 1st 2007

`https://.coupahost.com/api/departments?created_at[gt]=2007-01-01`

## Get Single Department

In this example, we queried for a single department with an ID
of 1.

We did a GET to the URL:

`https://.coupahost.com/api/departments/1`

or

`https://.coupahost.com/api/departments?id=1`

```text
<?xml version="1.0" encoding="UTF-8"?>
<department>
<id type="integer">1</id>
<created-at type="datetime">2008-10-27T13:00:48-07:00</created-at>
<updated-at type="datetime">2014-03-28T08:53:19-07:00</updated-at>
<name>Marketing</name>
<active type="boolean">true</active>
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
<id type="integer">69</id>
<login>coupasupport+rohitdemo@coupa.com</login>
<email>coupasupport+rohitdemo@coupa.com</email>
<employee-number nil="true" />
<firstname>Integration</firstname>
<lastname>User</lastname>
<salesforce-id nil="true" />
<mycustom-userfield />
</updated-by>
</department>
```

## Departments Create

In this example we are creating a Department. We are not using
any Coupa system ID's for any of the reference objects.

We posted it to the URL:

```text
https://<instance url>/api/departments/.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<department>
<name>Marketing</name>
<active>false</active>
</department>
```

## Departments Update

In these examples, we are updating a single Department
record.

We did a PUT to the URL: [https://instance.coupahost.com/api/departments/](https://instance.coupahost.com/api/departments/)
``

For Example, to deactivate an existing department with ID
195

```text
<?xml version="1.0" encoding="UTF-8"?>
<department>
<id>195</id>
<active>false</active>
</department>
```

For Example, to update the name of an existing department with
ID 195

```text
<?xml version="1.0" encoding="UTF-8"?>
<department>
<id>195</id>
<name>new name</name>
</department>
```
