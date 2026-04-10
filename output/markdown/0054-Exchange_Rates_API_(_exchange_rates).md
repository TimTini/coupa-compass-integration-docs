---
title: "Exchange Rates API (/exchange_rates)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/exchange-rates-api-(exchange_rates)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/exchange-rates-api-(exchange_rates)"
status_code: 200
fetched_at: "2026-04-09T11:59:13+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Exchange Rates API (/exchange_rates)"
---

# Exchange Rates API (/exchange_rates)

Use the budget lines API to manage exchange rates for currencies
your company uses to pay for goods.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

The Exchange Rates API only supports the creation of one-way exchange rates. For example,
if you make a call for EUR > USD, you'll have that rate populated in your Coupa instance,
but the reverse rate (USD > EUR) won't be created. You need to make a separate call for
USD > EUR.

The URL to access exchange rates is:

```text
https://<instance>/api/exchangerates
```

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Exchange Rates API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/exchange_rates` | create | Create exchange rate |
| GET | `/api/exchange_rates` | index | Query exchange rates |
| GET | `/api/exchange_rates/:id` | show | Show exchange rate |
| PUT | `/api/exchange_rates/:id` | update | Update exchange rate |

## Elements

The following elements are available for the Exchange Rates
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| from-currency | Source for Currency Code | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| id | Coupa unique identifier | | | | | yes | integer |
| rate | Exchange Rate | | | | yes | yes | decimal |
| rate-date | Effective Date | | yes | | yes | yes | datetime |
| to-currency | Target for Currency Code | yes | | | yes | yes | [Currency](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/currencies-api-(currencies)) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | yes | datetime | | | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- For large data set and performance optimization, always limit your result with some
GET criteria.

- The reference object Currency and the respective currency code or ID must already
exist in the system.
