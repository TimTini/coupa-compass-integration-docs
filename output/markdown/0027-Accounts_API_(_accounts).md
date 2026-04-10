---
title: "Accounts API (/accounts)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/accounts-api-(accounts)"
status_code: 200
fetched_at: "2026-04-09T11:59:07+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Accounts API (/accounts)"
---

# Accounts API (/accounts)

Use the accounts API to create and manage accounts to mimic your
business' financial structure. For example, if marketing, IT, and
sales have their own budgets, you may want to create a separate
account for each in Coupa.

The URL to access accounts
is: `https:///api/accounts`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

Dynamic accounts are created or updated at time of use based on the backing lookup values.
You would manage dynamic accounts by managing the lookup values. There is no need to create
an account using the API for dynamic accounts. If you do, you may encounter an error
message.

## Actions

The Accounts API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/accounts` | create | Create account |
| GET | `/api/accounts/favorites` | favorites | Favorites |
| GET | `/api/accounts` | index | Query accounts |
| GET | `/api/accounts/recent` | recent | Recent |
| GET | `/api/accounts/:id` | show | Show account |
| PUT | `/api/accounts/:id` | update | Update account |

## Elements

The following elements are available for the Accounts API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| account-type | account_type | yes | | | yes | yes | [AccountType](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/account-types-api-(account_types)) |
| account-type-id | The ID of the account type. This field may or may not appear, depending on your account configuration. | | | | yes | yes | integer |
| active | A false value inactivates the account making it no longer available to users. A true value makes it active and available to users. | | | | yes | yes | boolean |
| code | All segments concatenated with a hyphen ( - )<br>It's recommended not to use hyphens as part of the external ref. code of the lookup otherwise the system will interprete it as a separate segment | | | | | yes | string |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | This is the nickname for the account. Users can view and search against this field only through the user interface. | | | | yes | yes | string |
| segment-1 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-10 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-11 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-12 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-13 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-14 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-15 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-16 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-17 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-18 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-19 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-2 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-20 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-3 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-4 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-5 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-6 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-7 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-8 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| segment-9 | Each segment represents the segment of the account code (e.g. code: 99-9023-100132, where segment-1 is 99, segment-2 is 9023, and segment-3 is 100132) | | | | yes | yes | string(100) |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

- When dealing with large data sets of accounts, always limit your GET with some
criteria.

- The account type (chart of accounts) must already exist in the system; you cannot create
an account type using the API.

- The account type (chart of accounts) must already exist in the system; you cannot create
an account type using the API.
