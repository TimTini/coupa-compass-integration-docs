---
title: "Diversity Category and Subcategory APIs"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/diversity-category-and-subcategory-apis"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)/diversity-category-and-subcategory-apis"
status_code: 200
fetched_at: "2026-04-09T11:59:19+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Reference Data Resources"
  - "Suppliers API (/suppliers)"
  - "Diversity Category and Subcategory APIs"
---

# Diversity Category and Subcategory APIs

## Associations

These APIs are associated with the [Suppliers API](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/reference-data-resources/suppliers-api-(suppliers)-da-5797-da-5797).

## Diversity Category API Elements

The following elements are available for the Diversity Category
API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category | Diversity Category non-translated name | | | | | yes | |
| code | Code to refer to a particular diversity category | yes | yes | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |
| diversity-subcategories | Diversity Category list of possible subcategory sub object | | | | | yes | DiversitySubcategory |
| id | Diversity Category identifier | | | | yes | yes | integer |
| parent-category | Name of parent category for this diversity category | | | | | yes | |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | | | yes | datetime |

## Diversity Categories

You can use the following `category` values:

| **Code** | **Description** | **Country** |
| --- | --- | --- |
| ABILITYONE | Ability One Program | US |
| ACDBE | Airport Concession Disadvantaged Business Enterprise | US |
| AMS | Aboriginal and Minority Supplier | CA |
| ANC | Alaskan Native Corporation | US |
| BOB | Black owned business | ZA |
| DBE | Disadvantaged Business Enterprise | US |
| DOB | Disability Owned Businesses | INT |
| DVBE | Disabled Veteran Business Enterprise | US |
| EDWOSB | Economically Disadvantaged Women Owned Small Business | US |
| EMB | Ethnic minority businesses (EMBs) | GB |
| HBCU | Historically Black College or University / Minority Institution | US |
| HUBZone | Historically Underutilized Business Zone | US |
| IOB | Indigenous owned business | AU |
| LGBTBE | Lesbian, Gay, Bisexual, Transgender Business Enterprise | INT |
| LSA | Labor Surplus Area | US |
| MBE | Minority Owned Business Enterprise | INT |
| MGOB | Minority group owned business | CN |
| NPO | Non-profit Organization | US |
| SBA8A | SBA-8(A) | US |
| SBE | Small Business Enterprise | INT |
| SDB | Small Disadvantaged Business | US |
| SDVBE | Service Disabled Veteran Owned Business Enterprise | US |
| SDVOSB | Service Disabled Veteran Owned Small Business | US |
| VOB | Veteran Owned Business | US |
| VVO | Vietnam Veteran Owned | US |
| WBE | Woman Owned Business Enterprise | INT |
| WOSB | Woman Owned Small Business | US |

## Diversity Subcategory API Elements

The following elements are available for the Diversity
Subcategory API:

| **Element** | **Description** | **Required Field?** | **Unique?** | **Allowable Value** | **Api_In Field?** | **Api_Out Field?** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| category | Diversity Category non-translated name | | | | | yes | |
| code | Code | yes | yes | | yes | yes | string(255) |
| created-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ of the user who created it | | | | | yes | datetime |
| designation | Designation | | | | | | |
| diversity-subcategories | Diversity Category list of possible subcategory sub object | | | | yes | yes | DiversitySubcategory |
| id | Diversity Category ID | | | | yes | yes | integer |
| parent-category | Name of parent category for this diversity category | | | | | yes | |
| updated-at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ of the user who updated it | | | | | yes | datetime |

## Diversity Subcategories

You can use the following `subcategory` values:

![](https://compass.coupa.com/DITARoot/icons/important.png)
Note:

If you are located in Canada, the United Kingdom, or the United States, subcategories are
available for Minority Owned Business (CA, US) or Ethnic Minority (UK) diversity
types.

| **Code** | **Description** | **Country** |
| --- | --- | --- |
| B | Black | CA |
| C | Chinese | CA |
| F | Filipino | CA |
| JK | Japanese Korean | CA |
| LATAM | Latin American | CA |
| PI | Pacific Islander | CA |
| SA | South Asian | CA |
| WAA | West Asian/Arab | CA |
| AAB | Asian/Asian British | UK |
| BACBB | Black/African/Caribbean/Black British | UK |
| MMEG | Mixed/Multiple Ethnic Group | UK |
| OEG | Other Ethnic Group | UK |
| AABLK | African-American/Black | US |
| AAIA | Asian American/Indian American | US |
| APA | Asian-Pacific American | US |
| HLA | Hispanic/Latin American | US |
| NAO | Native American owned | US |
| FN | First Nations | US |
| N | Inuit | |
| MT | Metis | |
