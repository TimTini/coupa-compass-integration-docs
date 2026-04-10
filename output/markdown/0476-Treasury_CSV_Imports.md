---
title: "Treasury CSV Imports"
url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations/treasury-csv-imports"
final_url: "https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-sftp-integrations/treasury-csv-imports"
status_code: 200
fetched_at: "2026-04-09T12:00:56+00:00"
toc_path:
  - "Integration Technical Documentation"
  - "Treasury Integrations"
  - "Treasury sFTP Integrations"
  - "Treasury CSV Imports"
---

# Treasury CSV Imports

View available imports and download templates.

Use these guidelines when setting up Standard Treasury CSV imports:

- Use the templates in the table below to import content. Templates downloaded from the Treasury Management user interface (UI) are intended for UI upload only, as they are based on user language settings.

- Avoid loading dependency object files at the same time. For example, do not load the Project, Portfolio, and corresponding Cash Flow files at the same time, but load the Project and Portfolio files first, and then the Cash Flow file.

- For a small data set, create the data records manually through the UI instead of using a CSV import.

- Each inbound file has a 5000 row and 100 MB limit.

- The date format must be one of the following:

- yyyy-MM-dd

- MM/dd/yyyy

- dd.MM.yyyy

- You must use a period mark (.) as the decimal separator for all upload files.

- For more information on the elements for the CSV imports, refer to the API documentation in the Treasury application. See [View Treasury API Documentation](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/treasury-integrations/treasury-apis/view-treasury-api-documentation).

For more information, see [Using the Flat File Format](https://compass.coupa.com/en-us/products/product-documentation/integration-technical-documentation/coupa-core-flat-files-(csv)/getting-started/using-the-flat-file-format).

## Available imports

Inbound files are picked up every 3-6 minutes from your Coupa sFTP site for further processing. This schedule cannot be modified. Once the file corresponding to each object is processed, the file is moved to the corresponding /Archive folder.

Add files to the respective folders under the /Incoming folder. For example: /Incoming/FxRates.

| Export name and template download | Inbound folder |
| --- | --- |
| [Cash Flow](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/CashFlow_TreasImport_Jan26.csv) | /Incoming/CashFlows/ |
| [Intercompany Payment](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/InterCompanyPayment_TreasImport_Jan26.csv) | /Incoming/IntercompanyPayment |
| [Commodity Rates](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/CommodityRate_TreasImport_Jan26.csv) | /Incoming/CommodityRates |
| [Credit Spreads](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/CreditSpread_TreasImport_Jan26.csv) | /Incoming/CreditSpreads |
| [FX Forward Rates](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/FXForwardRate_TreasImport_Jan26.csv) | /Incoming/FxForwardRates |
| [FX Rates](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/FxRate_TreasImport_Jan26.csv) | /Incoming/FxRates |
| [Implied FX Volatilities](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/ImpliedFxVolatility.xlsx) | /Incoming/ImpliedFxVolatilities |
| [Interest Rates](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/InterestRate_TreasImport_Jan26.csv) | /Incoming/InterestRates |
| [Interest Volatilities](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/InterestVolatility_TreasImport_Jan26.csv) | /Incoming/InterestVolatilities |
| [Liquidity Planning Data](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/LiquidityPlanningData.csv) | /Incoming/LiquidityPlanningData |
| [Security Prices](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/SecurityPrices_TreasImport_Jan26.csv) | /Incoming/SecurityRates |
| [Categories](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/PlanningCategory.csv) | /Incoming/PlanningCategories |
| [Portfolio](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/Portfolio.csv) | /Incoming/TreasuryPortfolios |
| [Project](https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/treasury_integrations/misc/Project.csv) | /Incoming/TreasuryProjects |
