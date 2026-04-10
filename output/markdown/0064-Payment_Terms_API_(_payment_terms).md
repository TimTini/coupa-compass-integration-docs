---
title: "Payment Terms API (/payment_terms)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/payment-terms-api-(payment_terms)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/payment-terms-api-(payment_terms)"
status_code: 200
fetched_at: "2026-04-09T11:59:15+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Payment Terms API (/payment_terms)"
---

# Payment Terms API (/payment_terms)

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| GET\|POST | `/api/payment_terms(/:action(/:id))` | {:index=>"Query payment terms", :create=>"Create payment term", :show=>"Show payment term", :update=>"Update payment term", :destroy=>"Delete payment term"} | |
| POST | `/api/payment_terms` | create | Create payment term |
| GET | `/api/payment_terms` | index | Query payment terms |
| GET | `/api/payment_terms/:id` | show | Show payment term |
| PUT | `/api/payment_terms/:id` | update | Update payment term |

## Elements

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api-In Field?** | **Api-Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| active | A false value will inactivate the account making it no longer available to users. A true value will make it active and available to users. | | | true | yes | yes | boolean |
| code | code | yes | yes | | yes | yes | string(255) |
| content-groups | Content groups | | | | yes | yes | [BusinessGroup](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/content-groups-api-(business_groups)/content-groups-api-example-calls) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| days-for-discount-payment | days-for-discount-payment | yes | | | yes | yes | integer |
| days-for-net-payment | days-for-net-payment | yes | | | yes | yes | integer |
| description | description | | | | yes | yes | string(255) |
| discount-cutoff-day | Document before this day are eligible for discount else they will fall into the next month | | | 1 through 31 | yes | yes | integer |
| discount-due-day | This field is used to calculate the document's discount due date. | | | 1 through 31 | yes | yes | integer |
| discount-due-month | This field is used to calculate the document's discount due date along with the discount due day. | yes | | 0 through 6 | yes | yes | integer |
| discount-rate | discount-rate | | | | yes | yes | float |
| id | Coupa unique identifier | | | | | yes | integer |
| net-cutoff-day | This helps to determine payment due date if the document should be counted against this month or next | | | 1 through 31 | yes | yes | integer |
| net-due-month | This helps to determine the document's payment due date | yes | | 0 through 6 | yes | yes | integer |
| net-due-day | This helps to determine the document's payment due date | yes | | 1 through 31 | yes | yes | integer |
| type | Type can be either DaysAfterNetPaymentTerm or SpecificDayPaymentTerm | yes | | DaysAfterNetPaymentTerm, SpecificDayPaymentTerm | | yes | string(50) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| type | Type can be either DaysAfterNetPaymentTerm or SpecificDayPaymentTerm | Yes | No | DaysAfterNetPaymentTerm, SpecificDayPaymentTerm, DaysToBaseEomPaymentTerm, BaseEomToDaysPaymentTerm | | Yes | string(50) |
