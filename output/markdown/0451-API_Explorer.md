---
title: "API Explorer"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/api-explorer"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/api-explorer"
status_code: 200
fetched_at: "2026-04-09T12:00:50+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The CCW API"
  - "API Explorer"
---

# API Explorer

CCW's REST API Explorer is an interactive tool that allows users to test and explore the CCW
API in the following ways:

- Browse available REST API resources and end points

- Learn about the methods available for each API, along with supported parameters and
inline documentation

- Experiment by submitting sample requests for any available API endpoint, and see
responses in real time

- Make authenticated and authorized API calls through an intuitive framework that doesn't
require a technical background

To use the API Explorer, access to CCW's REST API must first be requested from CCW support.
Please review the [CCW API Overview documentation](https://compass.coupa.com/x298143.xml) to learn more about how to access and
use the API.

## Accessing the Explorer

To get started,
navigate to: **Integration Toolkit > Integration Documentation** . Click **REST API
Explorer.**

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Specific access to the Explorer can be given to any CCW user
and/or role by assigning the right, **Integration Toolkit > Integration
Documentation** .

The APIs currently available are displayed:

- Candidate Lookup (/api/candidates/search)

- Candidate Confirm (/api/candidates/{id}/confirm)

- Contingent Worker Lookup (/api/contingent_workers)

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_api/images/image1.png)

The **Base URL** , used for submitting API
requests, represents your current CCW testing environment.

As CCW adds more APIs, the
**Filter by Tag** bar will allow you to find a specific API by entering key words that
match section headers.

## Testing APIs

Click the API you want to test, and a
form is expanded showing the **Names** and **Descriptions** of available
parameters:

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_api/images/image2.png)

Certain parameters include an
**Example Value** (displayed by default) and **Model** (click to see the properties
of each field listed).

The **Responses** section includes code numbers (with
descriptions) that could be included in API responses from CCW.

Click **Try it
Out** to manually edit an example request on the Explorer form.

For proper
formatting and other requirements of CCW API requests, please review each specific API's
documentation:

- [Candidate Lookup API](https://compass.coupa.com/x298145.xml)

- [Candidate Confirm API](https://compass.coupa.com/x298147.xml)

- [Contingent Worker Lookup API](https://compass.coupa.com/x298151.xml)

![](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/ccw_api/images/image3.png)

**X-Correlation ID,** a mandatory field,
auto-generates when **Try it Out** is clicked.

**Authorization,** also
mandatory, requires an access token which must be generated outside the Explorer. Once
generated, the access token lasts 1 hour.

![](https://compass.coupa.com/DITARoot/icons/tip.png)
Tip:

An application such as
*Postman* can be used to generate the access token and copy it into the
Authorization field. In Postman, enter the API access credentials provided to you by
Coupa, including Access Token URL, Secret and Scope.

Click **Execute** to
submit your request to the Base URL with the additional parameters you entered. Or click
**Cancel** to discard your changes.

After executing, the **Response** section
includes the response body, headers (and errors, if applicable) sent in response to your API
request. Please review the documentation linked above for more detail.
