---
title: "Open eSign Provider Prerequisites"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/clm-open-esign-framework/open-esign-provider-prerequisites"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/clm-open-esign-framework/open-esign-provider-prerequisites"
status_code: 200
fetched_at: "2026-04-09T12:01:08+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "CLM Open eSign Framework"
  - "Open eSign Provider Prerequisites"
---

# Open eSign Provider Prerequisites

To have Coupa add a new e-signature provider as an available
Open eSign option, the provider must satisfy the following
requirements:

- Provide a UI for signing and integrating the User workflow from
Coupa to the provider.

- Provide a default configuration that ensures that the
integration with Coupa works without expecting any additional
configuration or parameters for the integration.

- Provide an API endpoint for Coupa to connect to

Additionally, the API must meet the following authentication
requirements:

- Custom - Basic Authentication

- Callback mechanism to call Coupa endpoints for signing
statuses

Finally, the provider must be able to build and host the Open
eSign Connector that implements Coupa's Open eSign API. The coding
language and infrastructure can be of the provider's choosing, as
long as Coupa is able to call the connector's API, just as we would
any other external API.
