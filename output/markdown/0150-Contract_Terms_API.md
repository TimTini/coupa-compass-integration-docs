---
title: "Contract Terms API"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-terms-api"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/contracts-api-(contracts)/contract-terms-api"
status_code: 200
fetched_at: "2026-04-09T11:59:36+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Contracts API (/contracts)"
  - "Contract Terms API"
---

# Contract Terms API

The URL to access contract terms is
`/api/contracts/{id}/contract_terms`.

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

The Contract Terms API allows you to:

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | /api/contracts/:contract_id/contract_terms | create | Create contract term |
| GET | /api/contracts/:contract_id/contract_terms | index | Query contract terms |
| GET | /api/contracts/:contract_id/contract_terms/:id | show | Show contract term |
| PUT | /api/contracts/:contract_id/contract_terms/:id | update | Update contract term |

## Elements

The following elements are available for the Contract Terms
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| contract-term-type | contract_term_type | yes | PerOrderContractTerm, TotalQtyContractTerm, TotalAmtContractTerm | yes | | | |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | yes | datetime | |
| created-by | User who created | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| id | Coupa unique identifier | | | | | yes | integer |
| name | name | yes | | | yes | yes | string |
| tier-10-disc-pct | tier_10_disc_pct | | | | yes | yes | decimal |
| tier-10-upper-bound | tier_10_upper_bound | | | | yes | yes | decimal |
| tier-11-disc-pct | tier_11_disc_pct | | | | yes | yes | decimal |
| tier-11-upper-bound | tier_11_upper_bound | | | | yes | yes | decimal |
| tier-12-disc-pct | tier_12_disc_pct | | | | yes | yes | decimal |
| tier-12-upper-bound | tier_12_upper_bound | | | | yes | yes | decimal |
| tier-13-disc-pct | tier_13_disc_pct | | | | yes | yes | decimal |
| tier-13-upper-bound | tier_13_upper_bound | | | | yes | yes | decimal |
| tier-14-disc-pct | tier_14_disc_pct | | | | yes | yes | decimal |
| tier-14-upper-bound | tier_14_upper_bound | | | | yes | yes | decimal |
| tier-15-disc-pct | tier_15_disc_pct | | | | yes | yes | decimal |
| tier-15-upper-bound | tier_15_upper_bound | | | | yes | yes | decimal |
| tier-16-disc-pct | tier_16_disc_pct | | | | yes | yes | decimal |
| tier-16-upper-bound | tier_16_upper_bound | | | | yes | yes | decimal |
| tier-17-disc-pct | tier_17_disc_pct | | | | yes | yes | decimal |
| tier-17-upper-bound | tier_17_upper_bound | | | | yes | yes | decimal |
| tier-18-disc-pct | tier_18_disc_pct | | | | yes | yes | decimal |
| tier-18-upper-bound | tier_18_upper_bound | | | | yes | yes | decimal |
| tier-19-disc-pct | tier_19_disc_pct | | | | yes | yes | decimal |
| tier-19-upper-bound | tier_19_upper_bound | | | | yes | yes | decimal |
| tier-1-disc-pct | tier_1_disc_pct | | | | yes | yes | decimal |
| tier-1-upper-bound | tier_1_upper_bound | yes | | | yes | yes | decimal |
| tier-20-disc-pct | tier_20_disc_pct | | | | yes | yes | decimal |
| tier-20-upper-bound | tier_20_upper_bound | | | | yes | yes | decimal |
| tier-2-disc-pct | tier_2_disc_pct | | | | yes | yes | decimal |
| tier-2-upper-bound | tier_2_upper_bound | | | | yes | yes | decimal |
| tier-3-disc-pct | tier_3_disc_pct | | | | yes | yes | decimal |
| tier-3-upper-bound | tier_3_upper_bound | | | | yes | yes | decimal |
| tier-4-disc-pct | tier_4_disc_pct | | | | yes | yes | decimal |
| tier-4-upper-bound | tier_4_upper_bound | | | | yes | yes | decimal |
| tier-5-disc-pct | tier_5_disc_pct | | | | yes | yes | decimal |
| tier-5-upper-bound | tier_5_upper_bound | | | | yes | yes | decimal |
| tier-6-disc-pct | tier_6_disc_pct | | | | yes | yes | decimal |
| tier-6-upper-bound | tier_6_upper_bound | | | | yes | yes | decimal |
| tier-7-disc-pct | tier_7_disc_pct | | | | yes | yes | decimal |
| tier-7-upper-bound | tier_7_upper_bound | | | | yes | yes | decimal |
| tier-8-disc-pct | tier_8_disc_pct | | | | yes | yes | decimal |
| tier-8-upper-bound | tier_8_upper_bound | | | | yes | yes | decimal |
| tier-9-disc-pct | tier_9_disc_pct | | | | yes | yes | decimal |
| tier-9-upper-bound | tier_9_upper_bound | | | | yes | yes | decimal |
| type | type | | | | | yes | string |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | yes | datetime | |
| updated-by | User who updated | | | | | yes | [User](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/users-api-(users)) |
| use-pct-discounts | use_pct_discounts | | | | yes | yes | boolean |
