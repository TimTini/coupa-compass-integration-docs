---
title: "CCW API Overview"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/ccw-api-overview"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-ccw-api/ccw-api-overview"
status_code: 200
fetched_at: "2026-04-09T12:00:50+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The CCW API"
  - "CCW API Overview"
---

# CCW API Overview

Using CCW's REST API customers and partners can build new applications and integrate with CCW in new ways, to improve their capabilities around managing a contingent workforce. CCW's APIs are HTTP-based RESTful APIs that use OAuth 2.0 for authentication and TLS 1.2 for transport layer security. This documentation explains how to access CCW's API and make requests to obtain the data you need.

## Authentication

Customers who want to access the CCW REST API can [register their API consumer app](https://compass.coupa.com/x298153.xml) and receive the OAuth 2.0 client credentials to use in combination with two additional layers of security - Scopes and User/Role access rights - to authenticate requests to the CCW API.

| **Authentication Requirement** | **Description** |
| --- | --- |
| OAuth 2.0 credentials | Includes a Client ID and Client Secret |
| Scopes | The end points pointing to the specific module/functionality within CCW being requested |
| User/Role access rights | Assigned within the CCW application. Once you are authenticated by the API (see below), another layer of security determines access to the specific functionality being requested |

## Access Token

The first step in accessing the CCW API is to request an access token by making a call with the OAuth credentials and scope(s), as in the following example:

```text
curl -XPOST -H "Content-type: application/json" -d '{"client_id": "<<clientID>>", "client_secret": "<<secret>>",
"scope":"ccw.candidate", "grant_type":"client_credential"}' 'Auth_Url'
```

For 'Auth_Url', use the following, depending on your environment:

- **Sandbox:**

- [https://identity-stg0-na10001.io.coupahost.com/realms/ccw-na-stg/protocol/openid-connect/token](https://identity-stg0-na10001.io.coupahost.com/realms/ccw-na-stg/protocol/openid-connect/token) (North America)

- [https://identity-stg0-eu10009.io.coupahost.com/realms/ccw-eu-stg/protocol/openid-connect/token](https://identity-stg0-eu10009.io.coupahost.com/realms/ccw-eu-stg/protocol/openid-connect/token) (Europe)

- **Production:**

- [https://identity-prd0-na10001.io.coupahost.com/realms/ccw-na-prd/protocol/openid-connect/token](https://identity-prd0-na10001.io.coupahost.com/realms/ccw-na-prd/protocol/openid-connect/token) (North America)

- [https://identity-prd0-eu10009.io.coupahost.com/realms/ccw-eu-prd/protocol/openid-connect/token](https://identity-prd0-eu10009.io.coupahost.com/realms/ccw-eu-prd/protocol/openid-connect/token) (Europe)

The authorization server returns a JSON payload containing the following:

| **Property** | **Value** |
| --- | --- |
| token_type | Prefixed with "Bearer" |
| access_token | String to be included in the authorization header when making API requests |
| expires_in | Number of seconds until the token expires (typically 3600, or 1 hour) |

## API End Points

Include the access token received in calls to CCW API endpoints.

End Point format: `https:///api/`

Examples:

- **Candidate Confirmation:** https://{hostname}/API/candidates/{id}/confirm

- **Candidate Lookup:** https://{hostname}/API/candidates/search

- **Contingent Worker (CW) Lookup:** https://{hostname}/API/contingent_workers

## Request Headers

The following HTTP request headers are required:

| **Header** | **Description** |
| --- | --- |
| Authorization | Used to request access for API calls. Include the bearer token with the authentication scheme: **Bearer: <Token>** |
| Content-Type | Set to: **application/json** in all requests. JSON is the only exchange format currently supported |
| X-Correlation-id | An identifier of 36 characters maximum, generated to enable tracking and auditing of the API request |

## Sample error response

```text
{
"error_code": "string",
"error_summary": "string",
"error_causes": [
{
"error_sub_code": "string",
"error_sub_code_desc": "string"
}
]
}
```

## Rate limiting

CCW REST API’s do not have explicit rate limiting, however, throttling of API requests is recommended for a timely response. Coming soon, Individual API endpoints will be updated with recommended rate limiting.

## Best practices

Below are some tips to ensure best results when building applications on top of CCW using our REST APIs:

- **Avoid Schema Validation:** CCW API's are constantly evolving, with new optional properties added to the API. For extensibility purposes, applications should not perform a schema validation, which can trigger errors when the API sends new properties that may not be required.

- **Use HTTP Status Codes:** Consumer applications should rely on HTTP status codes for handling API errors, rather than contents of the response body which are for diagnostic and logging purposes only.

- **Avoid depending on order of properties in API response:** CCW API's only support JSON content. The order of properties in an API response may change due to the introduction of new properties.
