---
title: "Risk Assess REST API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api"
status_code: 200
fetched_at: "2026-04-09T12:01:03+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Risk Assess Integrations"
  - "Risk Assess REST API"
---

# Risk Assess REST API

Retrieve Risk Assess data such as suppliers associated with the tenant and supplier extension fields.

## Overview

The Coupa Risk Assess REST API allows you to retrieve Rist Assess data. Using this API, you can:

- Retrieve a paginated and filtered/unfiltered list of suppliers belonging to a tenant.

- Retrieve extension fields associated with a specific supplier.

- Retrieve evaluation data, such as evaluation scores, comments, and attachments

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Risk Assess SOAP APIs are still currently supported.

## Prerequisites

The Risk Assess REST API requires a Coupa Core instance. To turn on the REST API functionality for your tenant, submit a Risk Assess support ticket.

## Authentication flow

The Risk Assess REST API uses Coupa Core OpenID Connect (OIDC) authentication in your Coupa Core instance. Use the following authentication flow:

- Create an OIDC client in your Coupa Core instance with a **Grant Type** set to **Client Credentials**. Apply scopes to your client depending on which endpoint you need to access. For specific steps for creating a client in Coupa Core and accessing a token, see [OAuth 2.0 and OIDC](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/oauth-2.0-and-oidc).

- Generate the access token using your Coupa Core instance.

- Send subsequent Risk Assess API requests to your Coupa Risk Assess tenant URL. See the Base URL section below.

Scopes are associated with each API endpoint:

- **riskassess.supplier.read**: Read supplier data.

- **riskassess.supplier.write**: Update supplier data.

- **riskassess.evaluation.read**: Access evaluations data.

- **riskassess.relationship.read**: Access relationship data.

## Base URL

The Risk Assess REST API uses your Risk Assess instance URL, for example: 

`https://.risk.coupahost.com/api/suppliers`

- [GET Evaluations](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-evaluations)

Retrieve evaluation data from your Coupa Risk Assess tenant, such as evaluation scores, comments, and attachments.

- [GET Suppliers](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-suppliers)

Retrieve a list of suppliers belonging to the tenant.

- [GET Relationships](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/risk-assess-integrations/risk-assess-rest-api/get-relationships)

Retrieve a list of up to 50 relationships. Each relationship includes associated objects, such as organizations, supplier, internal manager, and external manager.
