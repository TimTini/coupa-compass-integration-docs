---
title: "Exchange Rates API Example Calls"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/exchange-rates-api-(exchange_rates)/exchange-rates-api-example-calls"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/exchange-rates-api-(exchange_rates)/exchange-rates-api-example-calls"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Exchange Rates API (/exchange_rates)"
  - "Exchange Rates API Example Calls"
---

# Exchange Rates API Example Calls

## Get Exchange Rates Query Options

Here are some more examples of how to use the exchange rate API to query and get the result
set you want.

This query will return all exchange rates created after the date November 15, 2010. The
creation date is different than the effective rate date.

```text
https://<instance url>/api/exchange_rates?created_at[gt]=2010-11-15T00:00:00
```

This query will return all exchange rates where the effective rate date is after November
11, 2010.

```text
https://<instance url>/api/exchange_rates?rate-date[gt]=2010-11-11T00:00:00
```

This query will return all exchange rates where the 'from' rate is USD.

```text
https://<instance url>/api/exchange_rates?from-currency[code]=USD
```

This query will return all exchange rate where the exchange rate is less than 1.00

```text
https://<instance url>/api/exchange_rates?rate[lt]=1
```

This query will return no results as it is currently not supported:

```text
https://<instance url>/api/exchange_rates?from-currency[code]=USD&to-currency[code]=EUR
```

## Get Exchange Rates

In this example, we queried for exchange rate record with an ID of 9.

We did a GET to the URL:

```text
https://<instance url>/api/exchange_rates/9
```

or

```text
https://<instance url>/api/exchange_rates?id=9
```

Here is the response matching the search criteria:

```text
<?xml version="1.0" encoding="UTF-8"?>
<exchange-rates type="array">
<exchange-rate>
<id type="integer">9</id>
<from-currency>
<code>EUR</code>
<id type="integer">46</id>
</from-currency>
<to-currency>
<code>USD</code>
<id type="integer">1</id>
</to-currency>
<rate type="decimal">1.0</rate>
<rate-date type="datetime">2010-11-10T00:00:00-08:00</rate-date>
</exchange-rate>
</exchange-rates>
```

## Exchange Rate Create

In this example, we are creating an exchange rate from EUR to USD.

We posted it to the URL

```text
https://<instance url>/api/exchange_rates.
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<exchange-rate>
<from-currency>
<code>EUR</code>
</from-currency>
<to-currency>
<code>USD</code>
</to-currency>
<rate type="decimal">42.247599959</rate>
<rate-date type="datetime">2009-12-30</rate-date>
</exchange-rate>
```
