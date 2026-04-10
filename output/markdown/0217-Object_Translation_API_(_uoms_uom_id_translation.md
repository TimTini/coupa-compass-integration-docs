---
title: "Object Translation API (/uoms/uom_id/translations)"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/object-translation-api-(uomsuom_idtranslations)"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/the-coupa-core-api/resources/transactional-resources/object-translation-api-(uomsuom_idtranslations)"
status_code: 200
fetched_at: "2026-04-09T11:59:51+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "The Coupa Core API"
  - "Resources"
  - "Transactional Resources"
  - "Object Translation API (/uoms/uom_id/translations)"
---

# Object Translation API (/uoms/uom_id/translations)

## Introduction

Use the Object Translation API to create, update, or query
the translations for your Units of Measure (UOM).

The URL to access the Object Translation API
is: `/api/uoms/:uom_id/translations/`

See [Integration Best Practices](https://compass.coupa.com/x285417.xml) for more info.

## Actions

| **Verb** | **Path** | **Action** | **Description** |
| --- | --- | --- | --- |
| POST | `/api/uoms/:uom_id/translations` | create | Create a new translation for a Unit of Measure (UOM) |
| DELETE | `/api/uoms/:uom_id/translations/:id` | destroy | Remove a UOM translation |
| GET | `/api/uoms/:uom_id/translations` | index | Lists all of the UOM translations |
| GET | `/api/uoms/:uom_id/translations/:id` | show | Lists an individual UOM translation |
| PATCH | `/api/uoms/:uom_id/translations/:id` | update | Modify an existing UOM |
| PUT | `/api/uoms/:uom_id/translations/:id` | update | Modify an existing UOM |

## Elements (Object Translation)

| **Element** | **Description** | **Req'd** | **Unique** | **Allowable Value** | **In** | **Out** | **Data Type** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| locale | Locale of this translation | | | * see below | yes | yes | string(255) |
| key | Model attribute to be translated (example: name) | yes | yes | any | yes | yes | string(255) |
| value | Model attribute value of the translation | yes | | any | yes | yes | string(1024) |
| id | Coupa unique identifier | | | any | yes | yes | integer |
| created_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | yes | yes | datetime |
| updated_at | Automatically created by Coupa in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ | | | any | yes | yes | datetime |
| created_by | User who created | | | any | yes | yes | |
| updated_by | User who updated | | | any | yes | yes | |

* en, tr, ja, bg, cs, da, de-AT, de-BE, de-CH, de-LU, de,
el, en-AE, en-AU, en-BD, en-BH, en-CA, en-CO, en-CN, en-DE, en-DK,
en-FI, en-GB, en-HK, en-IE, en-IN, en-ME, en-MM, en-MT, en-MY,
en-NA, en-NL, en-NO, en-NZ, en-PH, en-PK, en-SE, en-SG, en-TW,
en-UA, en-ZA, es-CO, es-IC, es-MX, es-PR, es, et, fi, fr-BE, fr-CA,
fr-CH, fr-LU, fr, hr, hu, it-CH, it, ko, lt, lv, mt, nl-BE, nl, no,
pl, pt-BR, pt, ro, ru, ru-UA, sk, sl, sr-ME, sr, sv-FI, sv,
th, vi, zh-CN, zh-HK, zh-TW
