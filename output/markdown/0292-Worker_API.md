---
title: "Worker API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api"
status_code: 200
fetched_at: "2026-04-09T12:00:07+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Worker API"
---

# Worker API

Access and update worker data. For example, you can work with worker avatars, create, query, and invite workers, and update worker records.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| DELETE | `/api/workers/:id/avatar` | avatar_delete | Get all worker assigments. |
| GET | `/api/workers/:id/avatar` | avatar_show | Get assignment data for a single worker. |
| POST | `/api/workers/:id/avatar` | avatar_update | Update worker avatar. |
| PUT | `/api/workers/:id/avatar` | avatar_update | Update worker avatar. |
| POST | `/api/workers` | create | Create worker. |
| GET | `/api/workers` | index | Query worker. |
| POST | `/api/workers/:id/invite_worker` | invite_worker | Invite a worker. |
| GET | `/api/workers/:id` | show | Show a worker. |
| PATCH | `/api/workers/:id` | update | Show a worker. |
| PUT | `/api/workers/:id` | update | Show a worker. |

## Scopes

This API requires the following scopes:

- core.services_procurement.workers.read

- core.services_procurement.workers.write

## Elements

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | Active | | | | | yes | boolean |
| avatar-content-type | Avatar Content Type | | | | | yes | string(255) |
| avatar-file-name | Avatar File Name | | | | | yes | string(255) |
| country-of-citizenship | Worker Nationality | | | | yes | | Country |
| country-of-residence | Country of residence | | | | yes | yes | Country |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| current-title | Current title | | | | yes | yes | string(255) |
| date-of-birth | Date of Birth | yes | | | yes | yes | date |
| external-identifiers | External identifiers | | | | yes | yes | Worker::WorkerExternalReferenceIdentifier |
| first-name | First name | yes | | | yes | yes | string(255) |
| gender | Gender | | | | | yes | string |
| gender-code | Gender code | yes | | | yes | yes | string(255) |
| id | Coupa unique identifier | | | | | yes | integer |
| last-name | Last name | yes | | | yes | yes | string(255) |
| middle-name | Middle name | | | | yes | yes | string(255) |
| national-identifiers | National identifiers | | | | yes | yes | Worker::WorkerNationalIdentifier |
| nationality | Nationality | | | | | yes | Country |
| portal-access | Portal access | | | | | yes | string |
| portal-access-info | Portal Access Info | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| status | Status | | | | | yes | string(50) |
| supplier | supplier | | | | yes | yes | [Supplier](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797) |
| total-experience-in-years | Total experience in years | yes | | | yes | yes | decimal(19,2) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| worker-addresses | Worker addresses | | | | yes | yes | [Worker::WorkerAddress](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-address-api) |
| worker-documents | Worker documents | | | | | yes | [Worker::WorkerDocument](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-documents-api) |
| worker-emails | Worker emails | | | | yes | yes | [Worker::WorkerEmail](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-email-api) |
| worker-phone-numbers | Worker phone numbers | | | | yes | yes | [Worker::WorkerPhoneNumber](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-phone-number-api) |
| worker-skills | Worker skills | | | | yes | yes | Worker::WorkerSkill |

## Get workers

Method

GET `/api/workers`

Example cURL request

```text
curl --location 'https://<your-instance>.coupadev.com/api/workers' \
--header 'Accept: application/json' \
--header 'Accept: application/xml' \
--header 'Accept: application/octet-stream' \
--header 'Authorization: ••••••' \
--header 'Cookie: _mkra_ctxt=e02b500d225375af25ce02956b7b1cae29525e55fa9ff4667d28169023f67f60--200'
```

Example response

```text
[
{
"id": 1,
"created-at": "2025-07-28T03:43:08-07:00",
"updated-at": "2025-07-30T18:00:44-07:00",
"first-name": "Test",
"last-name": "Worker",
"middle-name": null,
"active": true,
"status": "assigned",
"current-title": "",
"total-experience-in-years": "10.0",
"portal-access": "Not Registered",
"date-of-birth": "2000-07-01",
"avatar-file-name": null,
"avatar-content-type": null,
"gender-code": "m",
"gender": "Male",
"supplier": {
"id": 132,
"name": "FieldQA supplier SM",
"display-name": "FieldQA Supplier SM"
},
"country-of-residence": {
"id": 222,
"code": "AE",
"name": "United Arab Emirates"
},
"nationality": null,
"portal-access-info": null,
"worker-emails": [
{
"id": 1,
"created-at": "2025-07-28T03:43:08-07:00",
"updated-at": "2025-07-28T03:43:08-07:00",
"email-address": "stage@coupa.com",
"email-type": "work"
}
],
"worker-skills": [],
"worker-addresses": [
{
"id": 382,
"created-at": "2025-07-28T03:43:08-07:00",
"updated-at": "2025-07-28T03:43:08-07:00",
"street1": "abc",
"street2": null,
"street3": null,
"street4": null,
"city": "asd",
"state": "AZ",
"state-iso-code": null,
"postal-code": "1237710",
"active": true,
"worker-address-purpose": {
"id": 33,
"code": "Home",
"name": "Home"
}
}
],
"external-identifiers": [],
"worker-documents": [],
"worker-phone-numbers": [
{
"id": 1,
"created-at": "2025-07-28T03:43:08-07:00",
"updated-at": "2025-07-28T03:43:08-07:00",
"phone-type": "mobile",
"phone-number": {
"number": "022345678",
"extension": "",
"country-code": "AL"
}
}
],
"national-identifiers": [],
"created-by": {
"id": 371,
"login": "amandeep.vashishtha@coupa.com",
"employee-number": null,
"fullname": "Amandeep V"
},
"updated-by": {
"id": 371,
"login": "amandeep.v@coupa.com",
"employee-number": null,
"fullname": "Amandeep V"
}
},
{
"id": 2,
"created-at": "2025-07-30T03:54:59-07:00",
"updated-at": "2025-07-30T03:54:59-07:00",
"first-name": "Test 2",
"last-name": "Worker",
"middle-name": null,
"active": true,
"status": "open",
"current-title": "",
"total-experience-in-years": "4.0",
"portal-access": "Not Registered",
"date-of-birth": "1990-07-03",
"avatar-file-name": null,
"avatar-content-type": null,
"gender-code": "f",
"gender": "Female",
"supplier": {
"id": 132,
"name": "FieldQA supplier SM",
"display-name": "FieldQA Supplier SM"
},
"country-of-residence": {
"id": 223,
"code": "US",
"name": "United States"
},
"nationality": null,
"portal-access-info": null,
"worker-emails": [
{
"id": 2,
"created-at": "2025-07-30T03:54:59-07:00",
"updated-at": "2025-07-30T03:54:59-07:00",
"email-address": "stage+testworker@Coupa.com",
"email-type": "personal"
}
],
"worker-skills": [],
"worker-addresses": [
{
"id": 399,
"created-at": "2025-07-30T03:54:59-07:00",
"updated-at": "2025-07-30T03:54:59-07:00",
"street1": "abc",
"street2": null,
"street3": null,
"street4": null,
"city": "new york",
"state": "NY",
"state-iso-code": null,
"postal-code": "1112223",
"active": true,
"worker-address-purpose": {
"id": 33,
"code": "Home",
"name": "Home"
}
}
],
"external-identifiers": [],
"worker-documents": [],
"worker-phone-numbers": [
{
"id": 2,
"created-at": "2025-07-30T03:54:59-07:00",
"updated-at": "2025-07-30T03:54:59-07:00",
"phone-type": "mobile",
"phone-number": {
"number": "07410410123",
"extension": "",
"country-code": "IN"
}
}
],
"national-identifiers": [],
"created-by": {
"id": 371,
"login": "amandeep.v@coupa.com",
"employee-number": null,
"fullname": "Amandeep V"
},
"updated-by": {
"id": 371,
"login": "amandeep.v@coupa.com",
"employee-number": null,
"fullname": "Amandeep V"
}
}
]
```

- [Worker Address API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-address-api)

Access Worker address data when working with the Worker API.

- [Worker Documents API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-documents-api)

Access and worker document data, such as worker attachments and document type.

- [Worker Email API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-email-api)

Access Worker email data when working with the Worker API.

- [Worker Phone Number API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-phone-number-api)

Access Worker phone number data when working with the Worker API.

- [Worker Derived Phone Number API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/worker-api/worker-derived-phone-number-api)

Access Worker derived phone number data when working with the Worker API.
