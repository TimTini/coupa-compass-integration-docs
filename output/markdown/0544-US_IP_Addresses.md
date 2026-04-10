---
title: "US IP Addresses"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-application-ip-addresses/us-ip-addresses"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-application-ip-addresses/us-ip-addresses"
status_code: 200
fetched_at: "2026-04-09T12:01:11+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Coupa Core Application IP Addresses"
  - "US IP Addresses"
---

# US IP Addresses

IP addresses that should be whitelisted by US suppliers and customers.

Use this list of Coupa Application sandbox and production environment IP addresses customers with restriction to access outside corporate networks and for the supplier's setup with cXML document exchange.

## IP Addresses

All addresses below should be whitelisted as data could come from any one of these IPs.

| **Address Ranges** | **Date Added** |
| --- | --- |
| 44.215.120.192/26 (44.215.120.193 through 44.215.120.254) | May 2023 |
| 8.246.104.128/25 (8.246.104.129 through 8.246.104.254) | May 2023 |
| 40.65.233.192/26 (40.65.233.192 through 40.65.233.207) | Feb 2020 |
| 40.65.242.192/26 (40.65.224.192 through 40.65.242.207) | Feb 2020 |
| 3.95.40.0/24 (3.95.40.0 through 3.95.40.255) | April 2019 |
| 34.239.145.192/26 (34.239.145.192 through 34.239.145.255) | December 2017 |
| 54.235.152.47/32 (54.235.152.47)<br>54.236.3.0/25 (54.236.3.0 through 54.236.3.127)<br>54.244.45.128/25 (54.244.45.128 through 54.244.45.255) | Aug 2015 |
| 23.21.150.196<br>23.23.79.1 through 23.23.79.127<br>23.23.177.14<br>23.23.177.16<br>23.23.177.21<br>23.23.177.27<br>23.23.177.29<br>23.23.177.30<br>23.23.177.47<br>23.23.177.48<br>23.23.177.49<br>23.23.189.128 through 23.23.189.143<br>40.67.128.210<br>40.67.137.207<br>50.16.243.194<br>50.16.243.195<br>50.16.243.196<br>50.16.243.201<br>50.16.243.202<br>50.16.243.203<br>50.16.243.204<br>50.16.243.205<br>50.16.243.206<br>50.16.87.82<br>54.160.18.145<br>54.237.22.143<br>54.82.68.87<br>54.83.205.196<br>54.83.206.121<br>54.83.206.99<br>54.91.72.144<br>75.101.135.143<br>75.101.138.205<br>107.20.174.167<br>107.20.174.177<br>107.20.174.184<br>107.20.240.202<br>107.20.250.110<br>107.20.250.44<br>107.20.88.1<br>107.21.245.135<br>107.21.245.137<br>107.21.245.138<br>107.22.249.25<br>174.129.218.114<br>174.129.221.185<br>184.72.245.48<br>184.72.245.50<br>184.72.245.53<br>184.72.249.69<br>184.72.88.201<br>184.73.170.127<br>184.73.189.66<br>184.73.219.218<br>184.73.235.133<br>184.73.244.248<br>184.73.244.251<br>184.73.245.25 | Non-ARIN Addresses |

## SFTP

Below is a list of Coupa SFTP service sandbox and production environment IPs, and applies ONLY to customers using Coupa SFTP.

| **Address Ranges** | **Date Added** |
| --- | --- |
| 34.239.145.241 and 34.239.145.242 for PCI Test SFTP<br>107.21.245.82 and 107.21.245.83 for PCI Production SFTP | Feb 2021 |
| 54.236.3.0 through 54.236.3.127<br>54.244.45.128 through 54.244.45.255 | Aug 2015 |
| 23.21.218.140<br>107.21.212.82<br>23.23.208.206<br>23.23.208.210<br>23.23.79.9<br>23.23.79.10 | Non-ARIN Addresses |

## Boomi

Below is a list of Boomi Integration platform IPs, and applies ONLY to customers who run integration on that platform and exchange data directly.

| **Address Ranges** | **Date Added** |
| --- | --- |
| 72.32.154.80 through 72.32.154.95<br>67.192.139.72 through 67.192.139.79 | Non-ARIN Addresses |

## LDAP

| **Address Ranges** | **Date Added** |
| --- | --- |
| 54.236.3.0 through 54.236.3.127<br>54.244.45.128 through 54.244.45.255 | Aug 2015 |
| 174.129.28.43<br>174.129.28.44 | Non-ARIN Addresses |

## Outbound Email from Coupa

Coupa uses Amazon SES as outbound-only email sending provider. The Amazon SES IP addresses are subject to change. To query a current list of IP addresses used to send outbound emails, see [Amazon SES IP addresses](https://aws.amazon.com/blogs/messaging-and-targeting/amazon-ses-ip-addresses/).
