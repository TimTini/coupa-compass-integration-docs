---
title: "Open eSign Framework Overview"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/clm-open-esign-framework/open-esign-framework-overview"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/clm-open-esign-framework/open-esign-framework-overview"
status_code: 200
fetched_at: "2026-04-09T12:01:06+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "CLM Open eSign Framework"
  - "Open eSign Framework Overview"
---

# Open eSign Framework Overview

The purpose of this framework is to build an Open API definition
to allow e-signature providers to self-configure (build &
maintain) integration with Coupa CLM. In order to make this happen,
Coupa will Publish an Open API SDK, including a test harness to
ease the implementation of new eSign providers.

The Open eSign Framework provides an integration for the
e-signature provider to Coupa Platform. The Open API definition of
the eSign Framework contains all the details of the API
specifications that the e-signature provider would need to
implement for the integration.

## Coupa e-signing integration flow

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/clm_open_esign_famework/images/image1.png)

- **Provider Services:** This is the provider's
e-signature service.

- **Provider Hosted Service:** This is the new connector that the provider needs to build
and host as per the Coupa API Specification. For more information, see [Open eSign Connector Specifications](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/clm-open-esign-framework/open-esign-connector-specifications#open_api_specifications).

## Sequence diagram detailing flows

**Create e-signature account:** Create the e-signature account on the Coupa Platform that
will authenticate against the signing provider via the connector and subsequently initiate
all the API calls.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/clm_open_esign_famework/images/image2.png)

**Provider configuration details**: the e-signature provider configuration parameters
that the user will need to populate when creating the esignature account. These parameters
are then passed through to the e-signature provider as part of the authentication.

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/clm_open_esign_famework/images/image3.png)

**Contract e-signature integration flow:** Sender view

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/clm_open_esign_famework/images/image4.png)

**Contract signature status flow:** Callbacks

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/clm_open_esign_famework/images/image5.png)

**Contract withdraw signature**

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/clm_open_esign_famework/images/image6.png)
