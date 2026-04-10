---
title: "Introducing GraphQL"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/introducing-graphql"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/introducing-graphql"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Introducing GraphQL"
---

# Introducing GraphQL

GraphQL is an open specification for an API query language that allows you to request only the data you need when you need it. GraphQL can also reduce the number of calls by fetching all of the resources you need in a single call.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

API filters continue to be a key feature that should still be used to reduce resource usage when making REST API GET calls.

## Authentication

Coupa’s GraphQL query endpoint is authenticated using OIDC and authorization is handled using OAuth 2.0 scopes. For more information, see [Set Up an OpenID Connect Client](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc/set-up-an-openid-connect-client). Currently, only the client credentials grant type and read scopes are supported.

## GraphQL clients

After you have an access token, there are many tools available that can be used to make GraphQL requests. These tools include cURL, Postman, and GraphiQL.

In the following examples, we will be using GraphiQL. One of the main advantages to using GraphiQL is that it fetches the schema and allows you to explore the schema in a user friendly way.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/graphiiQ.png)

Things to note in the above image:

- Provide your instance URL and append it with `/api/graphql` in the **GraphQL Endpoint** address bar.

- Edit the HTTP headers to add your access token to the Authorization header (See image below).

- Click on **Docs** to expand to show the schema.

When editing the header, add an authorization header by clicking the **Add Header** button and the following information:

- Header name: Authorization

- Header value: bearer {your access token}

Make sure to prefix the Header value with `bearer` or you won't be able to authorize.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/auth-header.png)

## Schema

Expanding the Docs in GraphiQL will allow you to explore the schema. With the schema, you can find out what is queryable and the return types for the queries.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Warning:

Mutations are not supported and should not be used.

## Queries

With GraphQL, you can query specifically for the data you need. You can query for data for a single object, or a collection of objects.

## Single objects

To query for a single object, use the singular form of the object name in lower camel case and specify the object ID. For example, user(id: 1), expenseReport(id: 1).

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/single-object.png)

Data is returned in JSON format with the data for the fields queried.

## Collections

To query for a collection of objects, use the plural form of the object name in lower camel case. For example, *users, expenseReports*.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/collections.png)

## Associations

GraphQL allows you to query for nested data:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/associations.png)

The image above shows a query for a single expense report (this also works for a collection of objects). In the expense report, we are querying for who created it and additional information on the report’s expense lines. Notice that even within expense lines we are querying for nested data.

## Custom Fields

Objects may have custom fields that can be queried by the field name *customFields:*

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/custom-fields.png)

Custom fields can be any of a number of types (eg: text, datetime, user, etc…). The *customFields* field can reveal what the type is for that specific custom field, which will allow you to query for those types specifically using fragments.

## Fragments

Fragments let you construct sets of fields, and then include them in queries. For `customFields`, you can specify fragments at the type level:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/fragments.png)

In the above example, we specify two fragments: **… on User { … }** and **… on StringValue { … }**. The fragments tell Coupa to attempt to convert the custom fields to the specified types (if applicable). If it can be converted to that given type, then the fields requested will be returned.

## Advanced filtering and querying options

Collection queries have the additional option parameter called *query* that further filters out responses. The format for the *query* option is in the form of a query string parameter that’s also used to filter out values in our REST APIs.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/advanced-filtering-querying.png)

The above example uses *"id[lt_or_eq]=5"* for the query parameter which filters out ID values to less than 5. This can also be dropped straight into our REST APIs in the form of */api/invoices?id[lt_or_eq]=5.*

## Errors

When checking responses, you should always check to see if the JSON response has any errors. If there are errors, a message and details of the error are shown:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/coupa_core_api/images/errors.png)

## Introspection

You can also query GraphQL for the schema itself. This is what GraphQL does to generate the schema for its clients. Here is an example of typical introspection query:

```text
query IntrospectionQuery {
__schema {
queryType { name }
mutationType { name }
subscriptionType { name }
types {
...FullType
}
directives {
name
description
args {
...InputValue
}query IntrospectionQuery {
__schema {
queryType {
name
}
mutationType {
name
}
subscriptionType {
name
}
types {
...FullType
}
directives {
name
description
args {
...InputValue
}
onOperation
onFragment
onField
}
}
}

fragment FullType on __Type {
kind
name
description
fields(includeDeprecated: true) {
name
description
args {
...InputValue
}
type {
...TypeRef
}
isDeprecated
deprecationReason
}
inputFields {
...InputValue
}
interfaces {
...TypeRef
}
enumValues(includeDeprecated: true) {
name
description
isDeprecated
deprecationReason
}
possibleTypes {
...TypeRef
}
}

fragment InputValue on __InputValue {
name
description
type {
...TypeRef
}
defaultValue
}

fragment TypeRef on __Type {
kind
name
ofType {
kind
name
ofType {
kind
name
ofType {
kind
name
}
}
}
}

onOperation
onFragment
onField
}
}
}

fragment FullType on __Type {
kind
name
description
fields(includeDeprecated: true) {
name
description
args {
...InputValue
}
type {
...TypeRef
}
isDeprecated
deprecationReason
}
inputFields {
...InputValue
}
interfaces {
...TypeRef
}
enumValues(includeDeprecated: true) {
name
description
isDeprecated
deprecationReason
}
possibleTypes {
...TypeRef
}
}

fragment InputValue on __InputValue {
name
description
type { ...TypeRef }
defaultValue
}

fragment TypeRef on __Type {
kind
name
ofType {
kind
name
ofType {
kind
name
ofType {
kind
name
}
}
}
}
```

## Design considerations

- All requests are POST requests.

- All responses are in JSON only.

- Always check the response body for errors, even if the response code of 200 was returned.
