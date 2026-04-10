---
title: "Accounts API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)/accounts-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)/accounts-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:07+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Accounts API (/accounts)"
  - "Accounts API Example Calls"
---

# Accounts API Example Calls

## Query Options

Here are some examples on how to use the account API to query
for a set of accounts.

This will return all inactive accounts:

```text
https://<instance name>.coupahost.com/api/accounts?active=false
```

This will return all account codes with a value of 'SF' in
segment-1:

```text
https://<instance name>.coupahost.com/api/accounts?segment-1=SF
```

## GET Single Account

In this example we queried for a single account with an id of 13.

We did a GET to the URL:
`https://.coupahost.com/api/accounts/13`

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<active type="boolean">false</active>
<code>SF-Marketing-Indirect</code>
<id type="integer">13</id>
<name />
<segment-1>SF</segment-1>
<segment-10 nil="true" />
<segment-11 nil="true" />
<segment-12 nil="true" />
<segment-13 nil="true" />
<segment-14 nil="true" />
<segment-15 nil="true" />
<segment-16 nil="true" />
<segment-17 nil="true" />
<segment-18 nil="true" />
<segment-19 nil="true" />
<segment-2>Marketing</segment-2>
<segment-20 nil="true" />
<segment-3>Indirect</segment-3>
<segment-4 nil="true" />
<segment-5 nil="true" />
<segment-6 nil="true" />
<segment-7 nil="true" />
<segment-8 nil="true" />
<segment-9 nil="true" />
<account-type>
<id type="integer">1</id>
<name>Ace Corporate</name>
</account-type>
</account>
```

## Account Create With An Account Name

In this example we are creating an account with the account name
specified.

We posted it to the URL: [https://.coupahost.com/api/accounts](https://.coupahost.com/api/accounts)

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<active type="boolean">true</active>
<name>demo account name</name>
<segment-1>SF</segment-1>
<segment-2>Marketing</segment-2>
<segment-3>Expense</segment-3>
<account-type>
<name>Ace Corporate</name>
</account-type>
</account>
```

Below is the response from the above POST

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<active type="boolean">true</active>
<code>SF-Marketing-Expense</code>
<id type="integer">206</id>
<name>demo account name</name>
<segment-1>SF</segment-1>
<segment-10 nil="true" />
<segment-11 nil="true" />
<segment-12 nil="true" />
<segment-13 nil="true" />
<segment-14 nil="true" />
<segment-15 nil="true" />
<segment-16 nil="true" />
<segment-17 nil="true" />
<segment-18 nil="true" />
<segment-19 nil="true" />
<segment-2>Marketing</segment-2>
<segment-20 nil="true" />
<segment-3>Expense</segment-3>
<segment-4 nil="true" />
<segment-5 nil="true" />
<segment-6 nil="true" />
<segment-7 nil="true" />
<segment-8 nil="true" />
<segment-9 nil="true" />
<account-type>
<id type="integer">1</id>
<name>Ace Corporate</name>
</account-type>
</account>
```

## Create Account with 3 Segments

In this example we are creating an account with 3 segments.

We posted it to the URL:
`https://.coupahost.com/api/accounts`

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<active type="boolean">true</active>
<segment-1>SF</segment-1>
<segment-2>Marketing</segment-2>
<segment-3>Direct</segment-3>
<account-type>
<name>Ace Corporate</name>
</account-type>
</account>
```

Below is the response that I received back when I posted the
above:

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<active type="boolean">true</active>
<code>SF-Marketing-Direct</code>
<id type="integer">205</id>
<name nil="true" />
<segment-1>SF</segment-1>
<segment-10 nil="true" />
<segment-11 nil="true" />
<segment-12 nil="true" />
<segment-13 nil="true" />
<segment-14 nil="true" />
<segment-15 nil="true" />
<segment-16 nil="true" />
<segment-17 nil="true" />
<segment-18 nil="true" />
<segment-19 nil="true" />
<segment-2>Marketing</segment-2>
<segment-20 nil="true" />
<segment-3>Direct</segment-3>
<segment-4 nil="true" />
<segment-5 nil="true" />
<segment-6 nil="true" />
<segment-7 nil="true" />
<segment-8 nil="true" />
<segment-9 nil="true" />
<account-type>
<id type="integer">1</id>
<name>Ace Corporate</name>
</account-type>
</account>
```

## Update Account Change Segment 2

In this example we are updating an account by changing segment 2 of the account to
'9999'

We posted it to the URL:

```text
https://<instance>.coupahost.com/api/accounts/<account id>
```

.

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<segment-2>9999</segment-2>
</account>
```

## Update Account Set Active

In this example we are updating an account and setting it to
active.

We posted it to the URL:

```text
https://<instance>.coupahost.com/api/accounts/<account id>
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<account>
<active>true</active>
</account>
```
