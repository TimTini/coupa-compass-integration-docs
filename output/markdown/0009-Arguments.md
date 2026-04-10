---
title: "Arguments"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/arguments"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/arguments"
status_code: 200
fetched_at: "2026-04-09T11:59:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Get Started with the API"
  - "Arguments"
---

# Arguments

Learn about the types of arguments that Coupa supports in conjunction with operators.

Arguments are made up of attributes, operators and values. They can be appended to any request to limit the results, the available attributes are listed in each business object's detailed documentation. Coupa supports a number of [operators](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/get-started-with-the-api/api-operators) in addition to the default equality/exact match.

## General Request Format

```text
<url>?<attribute><[operator]>=<value>&...
```

The first example returns the first 50 active suppliers start with id=1. The second example returns the first 50 POs with a updated-at dategreater than or equal to the specified date.

Examples:

```text
https://example.coupahost.com/api/suppliers?status=active
https://example.coupahost.com/api/purchase_orders?updated_at[gt_or_eq]=2010-12-31
https://example.coupahost.com/api/purchase_orders?offset=50
https://example.coupahost.com/api/purchase_orders?offset=100
```

## Searching on a collection

For collections of elements, such as order-lines in this case, use the plural form and ignore the nested singular form.

Example:

```text
<order-header>
<order-lines>
<order-line>
<account>
<code>a-c</code>
</account>
</order-line>
</order-lines>
</order-header>
```

Becomes:

```text
https://example.coupahost.com/api/purchase_orders?order-lines[account][code]=a-c
```

## Underscores

When using elements from resources in your arguments any dashes should be converted to underscores.

Example:

```text
<exchange-rate>
<from-currency>
<code>USD</code>
<id type="integer">1</id>
</from-currency>
</exchange-rate>
```

Becomes:

```text
https://example.coupahost.com/api/exchange_rates?from_currency_id=1
```
