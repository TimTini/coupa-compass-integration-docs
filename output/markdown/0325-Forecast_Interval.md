---
title: "Forecast Interval"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/forecast-interval"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/flat-file-(csv)-export/forecast-interval"
status_code: 200
fetched_at: "2026-04-09T12:00:18+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Flat Files (CSV)"
  - "Flat File (CSV) Export"
  - "Forecast Interval"
---

# Forecast Interval

Export of these records is included as a Standard CSV Export.

## Forecast Interval

| Field Name | Description | Field Type | Required/Unique | Possible Values |
| --- | --- | --- | --- | --- |
| type | Indicates record type | | No/No | |
| id | Coupa's Internal ID | integer | No/No | |
| start-date | Start Date of the Interval | datetime | Yes/No | |
| end-date | End Date of the Interval | datetime | No/No | |
| demand | Demand | decimal(10,0) | Yes/No | |
| promised | Promised | decimal(10,0) | No/No | |
| shortage | Shortage | boolean | No/No | |
| in-lead | In Lead | boolean | No/No | |
| in-fence | In Fence | boolean | No/No | |
| in-past | In Past | boolean | No/No | |
| forecast-collaboration-line-id | Coupa's Internal ID | integer | No/No | |
