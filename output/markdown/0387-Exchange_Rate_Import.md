---
title: "Exchange Rate Import"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/exchange-rate-import"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-import/exchange-rate-import"
status_code: 200
fetched_at: "2026-04-09T12:00:36+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Import"
  - "Exchange Rate Import"
---

# Exchange Rate Import

## Overview

The Exchange Rate Import process read files from `./Incoming/ExchangeRates/`
in the SFTP. These files will be moved to the archive folder located at
`./Incoming/Archive/ExchangeRates/` before being processed in alphanumeric
order.

Coupa does not support modifying existing exchange rates, only creating new rates.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: The Exchange Rates loader only supports the creation of one-way
exchange rates. For example, if you include for EUR > USD in the loader, you'll have
that rate populated in your Coupa instance, but the reverse rate (USD > EUR) won't be
created. You need to explicitly include USD > EUR for it to be included.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note: Although the allowable values for the `Rate Date`
column are in the `YYYY-MM-DDTHH :MM:SS+HH:MM` format, the column floors
the date and time to the beginning of the day (`00:00`).

## Exchange Rate

| Field Name | Required Field | Unique? | Field Type | Field Description | Possible Values |
| --- | --- | --- | --- | --- | --- |
| From Currency | Yes | No | | Base Currency Code | |
| To Currency | Yes | No | | Target Currency Code | |
| Rate | Yes | No | decimal(30,9) | Exchange Rate | |
| Rate Date | Yes | Yes | datetime | Exchange Rate Effective Start Date | |
