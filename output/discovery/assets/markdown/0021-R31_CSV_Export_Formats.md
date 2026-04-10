---
title: "R31_CSV_Export_Formats.xlsx"
url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/CSV/R31_CSV_Export_Formats.xlsx"
final_url: "https://compass.coupa.com/_dita_/en-us/documentation/plat/integ/core_api_and_csv_download_formats/misc/CSV/R31_CSV_Export_Formats.xlsx"
content_type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
classification: "xlsx_asset"
fetched_at: "2026-04-10T01:55:24+00:00"
---

# R31_CSV_Export_Formats.xlsx

- Raw file: `assets\raw\0021-R31_CSV_Export_Formats.xlsx`
- Extracted text: `assets\text\0021-R31_CSV_Export_Formats.txt`

## Extracted content

```text
# Sheet: Addresses
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Name	Nickname to help identify the address	0	0	string(255)	any
2.0	Location Code	External Address Id	0	1	string(255)	any
3.0	Line 1	Street Line 1 of the address	1	0	string(100)	any
4.0	Line 2	Street Line 2 of the address	0	0	string(100)	any
5.0	City	City of the address	1	0	string(50)	any
6.0	State	State of the address	0	0	string(50)	any
7.0	Postal Code	Zip code or postal code	1	0	string(50)	any
8.0	Country Code	ISO standard Country Code	0	0	string(6)	any
9.0	Attention	Attention	0	0	string(255)	any
10.0	Active	Active address?	0	0	boolean	any
11.0	Content Groups	List of content group names seperated by semicolon	0	0		any
12.0	VAT Number	VAT Number	0	0	string(255)	any
13.0	Local Tax Number	Local Tax Number	1	0	string(255)	any
14.0	VAT Country Code	VAT Country Code	0	0	string(6)	any
15.0	custom-field-1	Integration Custom Field 1	0	0	string(255)	any
16.0	custom-field-2	Integration Custom Field 2	0	0	string(255)	any
17.0	custom-field-3	Integration Custom Field 3	0	0	string(255)	any
18.0	custom-field-4	Integration Custom Field 4	0	0	string(255)	any
19.0	custom-field-5	Integration Custom Field 5	0	0	string(255)	any
20.0	custom-field-6	Integration Custom Field 6	0	0	string(255)	any
21.0	custom-field-7	Integration Custom Field 7	0	0	string(255)	any
22.0	custom-field-8	Integration Custom Field 8	0	0	string(255)	any
23.0	custom-field-9	Integration Custom Field 9	0	0	string(255)	any
24.0	custom-field-10	Integration Custom Field 10	0	0	string(255)	any
















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Advance Ship Notices
ASN Header Columns
Position	Column Name	Description	Type	Req'd/Unique	Allowable Values
1.0	Record Type	Indicates record type	-	No/No	Header
2.0	Id	Coupa's internal ID	integer(11)	No/No
3.0	ASN Number	ASN Number	string(40)	Yes/Yes
4.0	Status	ASN Header Status	string(50)	No/No
5.0	Ship to date	Ship to date	datetime	Yes/No
6.0	Delivery date	Delivery date	datetime	No/No
7.0	Supplier id	Supplier Coupa internal ID number	integer(11)	No/No
8.0	Supplier name	Supplier Name	string(100)	No/No
9.0	Supplier number	Supplier Number	string(255)	No/No
10.0	Created by employee number	Employee Number of User who created ASN	string(255)	No/No
11.0	Created by id	Coupa ID of User who created ASN	integer(11)	No/No
12.0	Created by login	Login name of User who created ASN	string(255)	No/No
13.0	Created at	Date record was created in Coupa.	datetime	No/No
14.0	Updated by employee number	Employee Number of User last updated by	string(255)	No/No
15.0	Updated by id	Coupa ID of User last updated by	integer(11)	No/No
16.0	Updated by login	Login name of User last updated by	string(255)	No/No
17.0	Updated at	Last Updated at Date	datetime	No/No
18.0	Ship to user employee number	Employee Number of Ship To User	string(255)	No/No
19.0	Ship to user id	Coupa ID of Ship To User	integer(11)	No/No
20.0	Ship to user login	Login name of Ship To User	string(255)	No/No
21.0	ASN Lines Count	ASN Lines Count	integer(11)	No/No
22.0	Gross weight	Gross weight	decimal(30,6)	No/No
23.0	Carrier	Carrier for the shipment	string(255)	No/No
24.0	Tracking Number	Tracking Number	string(255)	No/No
25.0	Standard carrier alpha code	Unique two-to-four-letter code used to identify transportation companies	string(255)	No/No
26.0	Container	Container or LPN for the shipped material	string(255)	No/No
27.0	Version	Version	integer(11)	No/No
28.0	Channel	Channel	string(255)	No/No
29.0	Trailer	Trailer number for the shipment	string(255)	No/No
30.0	Bill of lading	Document issued by a carrier to acknowledge receipt of cargo for shipment	string(255)	No/No
31.0	Packing slip	Delivery list	string(255)	No/No
32.0	Ship to attention	Ship to attention	string(255)	No/No
33.0	Ship method	Ship method	string(255)	No/No
34.0	Ship note	Ship note	string(255)	No/No
35.0	Uom code	Uom code	string(255)	No/No
ASN Line Columns
Position	Column Name	Description	Type	Req'd/Unique	Allowable Values
1.0	Record Type	Indicates record type	-	No/No	Line
2.0	Id	Coupa's internal ID	integer(11)	No/No
3.0	Line num	Line num	string(255)	Yes/Yes
4.0	Status	ASN Line Status	string(255)	No/No
5.0	Description	Description	string(255)	No/No
6.0	Quantity	Quantity	decimal(30,6)	Yes/No
7.0	Uom code	Uom code	string(6)	No/No
8.0	Asn Header Id	Asn Header Id	integer(11)	No/No
9.0	Asn Header Number	Asn Header Number	string(40)	No/No
10.0	Order Line Id	Order Line Id	integer(11)	No/No
11.0	Description	Description	string(255)	No/No
12.0	Created by Employee Number	Employee Number of User who created ASN	string(255)	No/No
13.0	Created By Id	Coupa ID of User who created ASN	integer(11)	No/No
14.0	Created By Login	Login name of User who created ASN	string(255)	No/No
15.0	Created At	Date record was created in Coupa.	datetime	No/No
16.0	Updated_by Employee Number	Employee Number of User last updated by	string(255)	No/No
17.0	Updated By Id	Coupa ID of User last updated by	integer(11)	No/No
18.0	Updated By Login	Login name of User last updated by	string(255)	No/No
19.0	Updated At	Last Updated at Date	datetime	No/No
20.0	Received Qty	Received Qty	decimal(30,6)	Yes/No
21.0	Item Id	Item Id	integer(11)	No/No
22.0	Item Name	Item Name	string(255)	No/No
23.0	Item Number	Item Number	string(255)	No/No
24.0	Invoice Header Id	Invoice Header Id	integer(11)	No/No
25.0	Invoice Line Id	Invoice Line Id	integer(11)	No/No
26.0	Invoice Line Num	Invoice Line Num	string(255)	No/No
27.0	Invoice Number	Invoice Number	string(255)	No/No
28.0	Version	ASN Version Number	integer(11)	No/No
29.0	Container	Container or LPN for the shipped material	string(255)	No/No
30.0	Supplier Part Num	Supplier Part Num	string(255)	No/No
31.0	Supplier Aux Part Num	Supplier Aux Part Num	string(255)	No/No
32.0	Comments	Comments	string(255)	No/No
33.0	Order Quantity	Order Quantity	decimal(30,6)	No/No
34.0	Match Reference	Three-way match attribute to connect with Receipt and Invoice Header	string(255)	No/No






























































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Approvals
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	Approval Chain ID	ID of the approval chain this approval is located in	integer(11)	No/No
2.0	Approval Chain Name	The name of the approval chain	string(255)	No/No
3.0	Document Number	The document ID that was approved	integer(11)	No/No
4.0	Document Type	The document type that was approved (requisition, purchase order, etc)	string(255)	No/No
5.0	Document Status	The document status	string(255)	No/No
6.0	Approver ID	The user ID that made the approval	integer(11)	No/No
7.0	Approver Login	The user name that made the approval	string(255)	No/No
8.0	Approver Role	The role of the approver	string(255)	No/No
9.0	Delegate	The ID of the delegate approval when there is only a single approval delegate	integer(11)	No/No
10.0	Delegate Approval Ids	The IDs of all the delegate approvals when there are multiple approval delegates	string(255)	No/No
11.0	Delegate Approver Names	Names of users who are delegates of the approver on the approval	text	No/No
12.0	Override Approver	Name of the user who bypassed the approval	string(255)	No/No
13.0	Approval Date (UTC)	The date the approval occurred	datetime	No/No
14.0	Position	The position in the approval chain this approval occurred	integer(11)	No/No
15.0	Approval Method	The method in which this approval occurred	string(255)	No/No
16.0	Approver Type	How the approval occured (override approval, approval chain approval, etc)	string(255)	No/No
17.0	Approval Key	The key used to authenticate email approvals	string(100)	No/No
18.0	Status	The status of the approval (approved, escalated, rejected, etc)	string(50)	No/No
19.0	Approval Reason	Explains why an approver was added as an approver for the document	text	No/No
20.0	Document Currency	The currency of the document that was approved	string(6)	No/No
21.0	Created By ID	The user ID that created the approval	integer(11)	No/No
22.0	Created By Login	The user login that created the approval	string(255)	No/No
23.0	Created Date	The date the user create the approval	datetime	No/No
24.0	Last Updated By ID	The user ID that most recently updated the approval	integer(11)	No/No
25.0	Updated By Login	The user login that most recently updated the approval	string(255)	No/No
26.0	Last Updated Date	The date the approval was most recently updated	datetime	No/No
27.0	Owned By ID	The owner of the approval	integer(11)	No/No
28.0	Owned By Login	The user login that owns the approval	string(255)	No/No
29.0	Assigned By ID	Who the approval was assigned to	integer(11)	No/No
30.0	Assigned By Login	The user login that is assigned to the approval	string(255)	No/No
31.0	Assigned Date	The date the approval was assigned to the user	datetime	No/No
32.0	First Notification (UTC)	The date the user was first notified that they can approve	datetime	No/No
33.0	Last Reminded Date	The date the user was last reminded that they can approve	datetime	No/No
34.0	Skip Escalation	If the approval was a skip escalation (Y/N)	boolean	No/No
35.0	Submission Date	The date the document was submitted	datetime	No/No










































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Charge
Position	Column Name	Type	Description	Req/Unique	Allowable Values
1.0	type		Describes the type of row. Possible values are Statement, Charge, ChargeAllocation, or ChargeTaxLine.	No/No	any
2.0	id	integer	Coupa internal ID for the charge	No/No	any
3.0	coupa-pay-statement-id	integer	Coupa Pay internal ID for the statement	No/No	any
4.0	statement-external-ref-id		A statement ID or Reference from the payment partner	No/No	any
5.0	statement-name		The name of the statement	No/No	any
6.0	coupa-pay-id	integer	Coupa Pay's Internal ID for the Statement	No/No	any
7.0	external-ref-id	string(255)	A charge ID or Reference from the payment partner	Yes/No	any
8.0	charge-date	datetime	Date of the charge	Yes/No	any
9.0	virtual-card-name		Name of the Virtual Card	No/No	any
10.0	virtual-card-coupa-pay-id		Coupa Pay internal ID of the virtual card	No/No	any
11.0	virtual-card-external-ref-id		A card ID or Reference from the payment partner	No/No	any
12.0	virtual-card-type		Type of the virtual card	No/No	any
13.0	virtual-card-order-header-po-number		PO number on the associated order header	No/No	any
14.0	virtual-card-po-id		Coupa internal ID of the associated order header	No/No	any
15.0	amount	decimal(30,6)	The amount in the credit card currency that was charged	No/No	any
16.0	currency		The currency the card card is issued in	Yes/No	any
17.0	merchant-amount	decimal(30,6)	The amount the merchant charged in the transaction	No/No	any
18.0	merchant-currency		The currency the merchant used in the transaction	Yes/No	any
19.0	mcc	string(255)	Merchant Category Code	No/No	any
20.0	supplier-name		The name from Coupa's supplier record for the supplier that charged the card	No/No	any
21.0	supplier-number		The number from Coupa's supplier record for the supplier that charged the card	No/No	any
22.0	merchant-reference	string(255)	The description provided by the credit card processor of who charged the card	No/No	any
23.0	tax-amount	decimal(30,6)	The tax amount charged in the transaction	No/No	any
24.0	tax-currency		The currency for the tax	No/No	any
25.0	custom-field-1		Integration Custom Field 1	No/No	any
26.0	custom-field-2		Integration Custom Field 2	No/No	any
27.0	custom-field-3		Integration Custom Field 3	No/No	any
28.0	custom-field-4		Integration Custom Field 4	No/No	any
29.0	custom-field-5		Integration Custom Field 5	No/No	any
30.0	custom-field-6		Integration Custom Field 6	No/No	any
31.0	custom-field-7		Integration Custom Field 7	No/No	any
32.0	custom-field-8		Integration Custom Field 8	No/No	any
33.0	custom-field-9		Integration Custom Field 9	No/No	any
34.0	custom-field-10		Integration Custom Field 10	No/No	any
35.0	accounting-total	decimal	Amount of charge in Chart Of Accounts Accounting Currency	No/No	any
36.0	accounting-currency		Currency Code for Accounting Total	No/No	any
37.0	virtual-card-document-id		The ID of the transactional document the card is associated with	No/No	any
38.0	issuer-bank-name		The name from Coupa's supplier record for the bank that issued the card	No/No	any
39.0	issuer-bank-number		The number from Coupa's supplier record for the bank that issued the card	No/No	any
40.0	issuer-reconciliation-id	string(255)	The charge reference as provided by the issuer bank	No/No	any

































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Charge Allocation
Position	Column Name	Type	Description	Req/Unique	Allowable Values
1.0	type		Describes the type of row. Possible values are Statement, Charge, ChargeAllocation, or ChargeTaxLine.	No/No	any
2.0	id	integer	Coupa internal ID for the charge allocation	No/No	any
3.0	statement-id		Coupa Pay internal ID for the associated Statement	No/No	any
4.0	statement-external-ref-id		A statement ID or Reference from the payment partner	No/No	any
5.0	statement-name		The name of the statement	No/No	any
6.0	charge-coupa-pay-id		Coupa Pay internal ID of the charge	No/No	any
7.0	charge-external-ref-id		external ref id of the charge	No/No	any
8.0	period-name		Name of the period	No/No	any
9.0	amount	decimal(30,6)	amount of the charge allocation	No/No	any
10.0	currency		currency of the charge allocation	Yes/No	any
11.0	pct	decimal(16,10)	the percentage of the total charge amount	Yes/No	any
12.0	account-name		The name of the account associated to the charge allocation	No/No	any
13.0	account-code		The code of the account associated to the charge allocation	No/No	any
14.0	account-type-name		The name of the COA associated to the charge allocation	No/No	any
15.0	custom-field-1		Integration Custom Field 1	No/No	any
16.0	custom-field-2		Integration Custom Field 2	No/No	any
17.0	custom-field-3		Integration Custom Field 3	No/No	any
18.0	custom-field-4		Integration Custom Field 4	No/No	any
19.0	custom-field-5		Integration Custom Field 5	No/No	any
20.0	custom-field-6		Integration Custom Field 6	No/No	any
21.0	custom-field-7		Integration Custom Field 7	No/No	any
22.0	custom-field-8		Integration Custom Field 8	No/No	any
23.0	custom-field-9		Integration Custom Field 9	No/No	any
24.0	custom-field-10		Integration Custom Field 10	No/No	any

# Sheet: Charge Tax Line
Position	Column Name	Type	Description	Req/Unique	Allowable Values
1.0	type		Describes the type of row. Possible values are Statement, Charge, ChargeAllocation, or ChargeTaxLine.	No/No	any
2.0	id	integer	The unique identifier Coupa assigns to the tax line.	No/No	any
3.0	charge-id		The unique identifier Coupa assigns to the charge.	No/No	any
4.0	charge-coupa-pay-id		Coupa Pay internal ID of the charge.	No/No	any
5.0	line-number	integer	The line number of the corresponding of the tax line.	No/No	any
6.0	tax-amount		The amount of tax calculated on the line.	No/No	any
7.0	tax-currency		The currency of tax amount on the line.	No/No	any
8.0	tax-rate		The tax rate indicated on the line.	No/No	any
9.0	tax-code		The tax rate code for the line tax rate.	No/No	any
10.0	tax-code-country		The tax rate code country for the line tax rate	No/No	any
11.0	tax-code-description		The tax rate code description for the line tax rate.	No/No	any
12.0	custom-field-1		Integration Custom Field 1	No/No	any
13.0	custom-field-2		Integration Custom Field 2	No/No	any
14.0	custom-field-3		Integration Custom Field 3	No/No	any
15.0	custom-field-4		Integration Custom Field 4	No/No	any
16.0	custom-field-5		Integration Custom Field 5	No/No	any
17.0	custom-field-6		Integration Custom Field 6	No/No	any
18.0	custom-field-7		Integration Custom Field 7	No/No	any
19.0	custom-field-8		Integration Custom Field 8	No/No	any
20.0	custom-field-9		Integration Custom Field 9	No/No	any
21.0	custom-field-10		Integration Custom Field 10	No/No	any

# Sheet: Contracts
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	Contract #	The contract number	string(50)	Yes/Yes
2.0	Contract Name	The name of the contract	string(100)	Yes/Yes
3.0	Content Groups	The content groups that can view this contract	string	No/No
4.0	Status	The status of the contract	string(50)	Yes/No
5.0	Supplier	The supplier ID assocaited with the contract	integer(11)	No/No
6.0	Supplier Number	Supplier Number	string(255)	No/No
7.0	Supplier Account #	The supplier account for the contract	string(255)	No/No
8.0	Starts	The date the contract begins	datetime	Yes/No
9.0	Expires	The date the contract expires	datetime	Yes/No
10.0	Owner	The currency ID associated with the contract	integer(11)	No/No
11.0	Owner Login	The user login that owns the contract	string(255)	No/No
12.0	Currency Code	Currency Code	string(6)	No/No
13.0	Savings %	The % savings created by the contract	decimal(20,2)	No/No
14.0	Version	The version number of the contract	integer	No/No
15.0	Created By	The user ID that created the contract	integer	No/No
16.0	Created By Login	Created By Login	string(255)	No/No
17.0	Created Date	The date the contract was created	datetime	No/No
18.0	Updated By	The user ID that most recently updated the contract	integer(11)	No/No
19.0	Updated By Login	The user login that most recently updated the contract	string(255)	No/No
20.0	Updated Date	The date the contract was most recently updated	datetime	No/No
21.0	Submitted Date	The date the contract was submitted	datetime	No/No
22.0	Submitted By	The user ID of the person that submitted the contract	integer(11)	No/No
23.0	Submitted By Login	The user login that submitted the approval	string(255)	No/No
24.0	Is Default	Is this the default (Y/N)	boolean	No/No
25.0	Default Account ID	The default account ID for the contract	integer(11)	No/No
26.0	Default Account Code	The default account code for the contract	string(21024)	No/No
27.0	Linked Projects	List of Project IDs linked to this contract		No/No
28.0	Linked Events	List of Event IDs linked to this contract		No/No

# Sheet: Coupa PayPayment
Column Name	Description	Req/Unique	Type	Allowable Values
Type	Describes the type of row. Possible values are Payment, Payment Details or Payment Detail Allocation.	No/No		any
Payment ID	The ID of the payment	No/No	integer	any
Payment Batch ID	The ID of the Payment Batch the payment belongs to	Yes/No	integer	any
Payment Batch Type	The type of Payment Batch the payment belongs to. It can be an Invoice Payment Batch or Expense Payment Batch	No/No		any
Payment Batch Status	The status of the Payment Batch the payment belongs to	No/No		any
Payment Status	The status of the payment	No/No	string(255)	any
Created At	The date the payment was created on	No/No	datetime	any
Updated At	The date the payment was last updated on	No/No	datetime	any
Exported	A flag to check if the payment was already exported	No/No		any
Pay From Account Name	The company payment account name used for the payment	No/No		any
Pay From Account Kind	The company payment account type used for the payment	No/No		any
Pay From Account Currency	The company payment account currency used for the payment	No/No		any
Pay From Account Total	The total amount to be used for the payment from the company payment account	No/No		any
Pay To Account Name	The payee's payment account name	No/No		any
Pay To Account Kind	The payee's payment account type	No/No		any
Pay to Account Currency	The payee's payment account currency	No/No		any
Pay To Account Total	The total amount the payee is to be paid in its account currency	No/No		any
Reporting Pay To Currency	The reported currency for the payee	No/No		any
Reporting Pay To Total	The reported total amount to be paid based on payee's currency	No/No	decimal	any
Exchange Rate	The exchange rate used for the payment	No/No	decimal(30,9)	any
Payee ID	A unique number identifing the payee. This is unique within each source transaction type	Yes/No	integer	any
Payee Name	The name of the payee	No/No		any
Payee Display Name	A commonly used name for the payee	No/No		any
Payee Login	The login ID used for employees. This is blank for suppliers	No/No		any
Payee Email	The email used by the payee to receive payment notifications	No/No		any
Payee Number	A unique number identifing the payee. This is unique within each source transaction type	No/No		any
Pay To Total	The total amount to be paid	No/No	decimal	any
Error Text	Error text on completed with error payments	No/No	string(255)	any
Digital Check Number	The digital check number when there is one attached to the payment	No/No		any
Estimated Pay From Total	The estimated pay from total based on exchange rates loaded in the system	No/No	decimal	any
custom-field-1	Integration Custom Field 1	No/No		any
custom-field-2	Integration Custom Field 2	No/No		any
custom-field-3	Integration Custom Field 3	No/No		any
custom-field-4	Integration Custom Field 4	No/No		any
custom-field-5	Integration Custom Field 5	No/No		any
custom-field-6	Integration Custom Field 6	No/No		any
custom-field-7	Integration Custom Field 7	No/No		any
custom-field-8	Integration Custom Field 8	No/No		any
custom-field-9	Integration Custom Field 9	No/No		any
custom-field-10	Integration Custom Field 10	No/No		any

# Sheet: Coupa PayPayment Detail
Column Name	Description	Req/Unique	Type	Allowable Values
Type	Describes the type of row. Possible values are Payment or Payment Details	No/No		any
Payment Detail ID	The ID of the payment detail	No/No	integer	any
Payment ID	The ID of the payment the payment detail belongs to	Yes/No	string(255)	any
Payment Batch ID	The ID of the payment batch the payment detail belongs to	No/No		any
Source Transaction ID	The ID of source for the payment detail	No/No		any
Source Transaction Type	The type of source for the payment detail. Possible values are Paybles::Invoice or Payables::Expense	No/No		any
Source Transaction Number	The reference ID of the source for the payment detail	No/No		any
Transaction Total	The total transaction amount for the payment detail	No/No	decimal	any
Discount Total	The total discount amount for the payment detail	No/No	decimal	any
Adjustment Total	The total adjusted amount for the payment detail	No/No	decimal	any
Currency Code	The currency of the payment to the recipient	No/No		any
Payment Total	The total payment amount for the payment detail	No/No	decimal	any
custom-field-1	Integration Custom Field 1	No/No		any
custom-field-2	Integration Custom Field 2	No/No		any
custom-field-3	Integration Custom Field 3	No/No		any
custom-field-4	Integration Custom Field 4	No/No		any
custom-field-5	Integration Custom Field 5	No/No		any
custom-field-6	Integration Custom Field 6	No/No		any
custom-field-7	Integration Custom Field 7	No/No		any
custom-field-8	Integration Custom Field 8	No/No		any
custom-field-9	Integration Custom Field 9	No/No		any
custom-field-10	Integration Custom Field 10	No/No		any

# Sheet: Coupa PayPayment Detail Allocat
Column Name	Description	Req/Unique	Type	Allowable Values
Type	Describes the type of row. Possible values are Payment, Payment Details or Payment Detail Allocation	No/No		any
Payment Detail Allocation ID	The ID of the payment detail allocation	No/No	integer	any
Payment ID	The ID of the payment the payment detail belongs to	No/No		any
Payment Detail ID	The ID of the payment detail the allocation belongs to	No/No		any
Source Transaction From ID	The ID of the transaction that emitted the allocation	No/No		any
Source Transaction From Type	The type of the transaction that emitted the allocation. Possible values are InvoiceHeader.	No/No		any
Source Transaction From Number	The reference ID of the transaction that emitted the allocation	No/No		any
Source Transaction From Amount	The amount sent by the transaction that emitted the allocation	No/No		any
Source Transaction From Currency	The currency for the amount sent by the transaction that emitted the allocation	No/No		any
Source Transaction To ID	The ID of the receiving transaction	No/No		any
Source Transaction To Type	The type of the receiving transaction. Possible values are InvoiceHeader.	No/No		any
Source Transaction To Number	The reference ID of the receiving transaction	No/No		any
Source Transaction To Amount	The amount sent to the receiving transaction	No/No		any
Source Transaction To Currency	The currency for the amount sent to the receiving transaction	No/No		any
Source	The source of this allocation. Possible values are coupa_pay.	No/No	string(255)	any
Reason Code	The reason code for the most recent change to this allocation.	No/No	string(40)	payment, auto_payment, epr, epr_rejected
custom-field-1	Integration Custom Field 1	No/No		any
custom-field-2	Integration Custom Field 2	No/No		any
custom-field-3	Integration Custom Field 3	No/No		any
custom-field-4	Integration Custom Field 4	No/No		any
custom-field-5	Integration Custom Field 5	No/No		any
custom-field-6	Integration Custom Field 6	No/No		any
custom-field-7	Integration Custom Field 7	No/No		any
custom-field-8	Integration Custom Field 8	No/No		any
custom-field-9	Integration Custom Field 9	No/No		any
custom-field-10	Integration Custom Field 10	No/No		any

# Sheet: Coupa PayStatements
Position	Column Name	Type	Description	Req/Unique	Allowable Values
1.0	type		Describes the type of row. Possible values are Statement, Charge, or ChargeAllocation.	No/No	any
2.0	id	integer	Coupa internal ID for the statement	No/No	any
3.0	status	string(255)	The status of the	No/No	any
4.0	payment-partner-name		The name of the payment partner	No/No	any
5.0	payment-partner-issuing-bank		The issuing bank of the payment partner	No/No	any
6.0	payment-partner-supplier-name		The name of the supplier associated to the payment partner	No/No	any
7.0	payment-partner-supplier-number		The number of the supplier associated to the payment partner	No/No	any
8.0	external-ref-id	string(255)	Third party or partner document reference	Yes/No	any
9.0	coupa-pay-id	integer	Coupa Pay Internal ID of statement	No/No	any
10.0	name	string(255)	The name of the statement	No/Yes	any
11.0	statement-date	datetime	Date of statement	Yes/No	any
12.0	number-of-lines	integer	Number of charges in statement	No/No	any
13.0	amount	decimal(30,6)	Total amount of statement	No/No	any
14.0	currency		Currency of statement	No/No	any
15.0	unbacked-amount	decimal(30,6)	Sum of charges on statement that are not associated to a PO	No/No	any
16.0	number-of-unbacked-lines	integer	Number of charges that do not have an associated PO	No/No	any
17.0	custom-field-1		Integration Custom Field 1	No/No	any
18.0	custom-field-2		Integration Custom Field 2	No/No	any
19.0	custom-field-3		Integration Custom Field 3	No/No	any
20.0	custom-field-4		Integration Custom Field 4	No/No	any
21.0	custom-field-5		Integration Custom Field 5	No/No	any
22.0	custom-field-6		Integration Custom Field 6	No/No	any
23.0	custom-field-7		Integration Custom Field 7	No/No	any
24.0	custom-field-8		Integration Custom Field 8	No/No	any
25.0	custom-field-9		Integration Custom Field 9	No/No	any
26.0	custom-field-10		Integration Custom Field 10	No/No	any

# Sheet: Delegations
Column Name	Type	Description	Req'd	Unique	Allowable Values
Delegator ID	integer	The user ID that made the delegator	0	0	any
Delegator Login		The user login that made the delegator	0	0	any
Delegate ID	integer	The delegate ID that made the approval (if applicable)	0	0	any
Delegate Login		The delegate login that made the approver	0	0	any
Delegation Start Date	datetime	The day the delegation period begins	1	0	any
Delegation End Date	datetime	The day the delegation period ends	1	0	any
Delegation Reason	string(255)	The reason for the approval	1	0	any
Created By ID	integer	The user ID that created the approval delegation	0	0	any
Created By Login		The user login that created the approval delegate	0	0	any
Created Date	datetime	The date the user create the approval delegation	0	0	any
Updated By ID	integer	The user ID that most recently updated the approval delegation	0	0	any
Updated By Login		Ther user login that most recently updated the approval delegate	0	0	any
Updated Date	datetime	The date the approval delegation was most recently updated	0	0	any
custom-field-1		Integration Custom Field 1	0	0	any
custom-field-2		Integration Custom Field 2	0	0	any
custom-field-3		Integration Custom Field 3	0	0	any
custom-field-4		Integration Custom Field 4	0	0	any
custom-field-5		Integration Custom Field 5	0	0	any
custom-field-6		Integration Custom Field 6	0	0	any
custom-field-7		Integration Custom Field 7	0	0	any
custom-field-8		Integration Custom Field 8	0	0	any
custom-field-9		Integration Custom Field 9	0	0	any
custom-field-10		Integration Custom Field 10	0	0	any
Approval Delegate	boolean	Approval Delegate	0	0	Yes/No
Receiving Delegate	boolean	Receiving Delegate	0	0	Yes/No

# Sheet: Easy Form Widget Response
Easy Form Widget Response Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	The type of record type found in each row	0	0		any
Id	Easy form widget respond ID	0	0	integer	any
Created At	The time of record creation in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
Updated At	Time that the record was updated in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
Widget Type	The type of widget added by admin to the expense preapproval form	0	0		any
Widget Name	The name of the widget added to the expense preapproval form	0	0		any
User Response	User's response to the widget on form response	0	0		any
custom-field-1	Integration Custom Field 1	0	0		any
custom-field-2	Integration Custom Field 2	0	0		any
custom-field-3	Integration Custom Field 3	0	0		any
custom-field-4	Integration Custom Field 4	0	0		any
custom-field-5	Integration Custom Field 5	0	0		any
custom-field-6	Integration Custom Field 6	0	0		any
custom-field-7	Integration Custom Field 7	0	0		any
custom-field-8	Integration Custom Field 8	0	0		any
custom-field-9	Integration Custom Field 9	0	0		any
custom-field-10	Integration Custom Field 10	0	0		any



























































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Expense Preapproval
Expense Preapproval Header Colummns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	The type of record type found in each row	0	0		any
ID	ID for the expense preapproval	0	0	integer	any
Description	The description entered by the user often describing why they are requesting expense preapproval	1	0	string(255)	any
Type	The type of form that the admin has configured for its users when requesting expense preapprovals	0	0	string(255)	any
Preapproved Amount	Total amount requested by the user on expense preapproval form	0	0		any
Currency	Currency code related to requested preapproval amount	0	0		any
Available Amount	The available amount left on a preapproval after a portion of the expense preapproval has been reconciled with an Expense Report	0	0		any
Available Amount Currency	Currency code related to remaining requested preapproval amount	0	0		any
Available	When Preapproval is archived then Available is set to No; however, when it is still active, is set to Yes	0	0	boolean	any
Start Date	The start date entered by user on expense preapproval in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
End Date	The end date entered by user on expense preapproval in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
Preapproval User Fullname	Full name of the user for whom the preapproval is created	0	0		any
Created By Fullname	Full name of the user who created the expense preapproval	0	0		any
Updated By Fullname	Full name of the user who updated the expense preapproval	0	0		any
Created At	Time of record creation in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
Updated At	Time that the record was updated in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
Reporting Total	The total expense preapproval amount requested in the company's dashboard currency	0	0	decimal(32,4)	any
Form Response	The form response name set by the admin when publishing expense preapproval form	0	0		any
Expense Reports	One or many expense reports that the expense preapproval is associated to	0	0	[]	any
Cash Advance Applied Amount	The total cash advance amount requested on expense preapproval form	0	0		any
Cash Advance Applied Amount Currency	Currency code related to requested cash advance amount	0	0		any
Cash Advance Outstanding Amount	The available cash advance amount left on a preapproval after a portion of the expense preapproval has been reconciled with an Expense Report	0	0		any
Cash Advance Outstanding Amount Currency	Currency code related to remaining cash advance amount on expense preapproval	0	0		any
Virtual Card Applied Amount	The total amount of the virtual card that was applied to the expense preapproval	0	0		any
Virtual Card Applied Amount Currency	Currency code related to virtual card amount applied to the expense preapproval	0	0		any
Virtual Card Outstanding Amount	The available virtual card amount left on a preapproval after a portion of the expense preapproval has been reconciled with an Expense Report	0	0		any
Virtual Card Outstanding Amount Currency	Currency code related to remaining virtual card amount on expense preapproval	0	0		any
custom-field-1	Integration Custom Field 1	0	0		any
custom-field-2	Integration Custom Field 2	0	0		any
custom-field-3	Integration Custom Field 3	0	0		any
custom-field-4	Integration Custom Field 4	0	0		any
custom-field-5	Integration Custom Field 5	0	0		any
custom-field-6	Integration Custom Field 6	0	0		any
custom-field-7	Integration Custom Field 7	0	0		any
custom-field-8	Integration Custom Field 8	0	0		any
custom-field-9	Integration Custom Field 9	0	0		any
custom-field-10	Integration Custom Field 10	0	0		any
Expense Preapproval Line

Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	The type of record type found in each row	0	0		any
ID	ID for the expense preapproval line	0	0	integer	any
Expense Preapproval ID	ID for the expense preapproval	0	0	integer	any
Type	The type of expense preapproval line: Flight, Hotel, Car Rental, Train, Transportation, or None	0	0	string(255)	any
Estimated Amount	The estimated price of a segment predicted by Coupa's Community Intelligence Price Prediction	0	0		any
Estimated Amount Currency	Currency code related to the estimated amount requested on expense preapproval	0	0		any
Requested Amount	Total amount requested by the user on expense preapproval form	0	0		any
Requested Amount Currency	Currency code related to the requested amount on expense preapproval line	0	0		any
Account Type Name	The COA of the account selected in account code	0	0		any
Account Code	The accounting string that is assigned to the expense preapproval line	0	0		any
Accounting Total	The total expense preapproval amount requested in the COAs currency	0	0		any
Accounting Total Currency	Currency code related to the accounting total on the expense preapproval line	0	0		any
Created At	The time of record creation in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
Updated At	Time that the record was updated in the format YYYY-MM-DDTHH:MM:SS+HH:MM	0	0	datetime	any
custom-field-1	Integration Custom Field 1	0	0		any
custom-field-2	Integration Custom Field 2	0	0		any
custom-field-3	Integration Custom Field 3	0	0		any
custom-field-4	Integration Custom Field 4	0	0		any
custom-field-5	Integration Custom Field 5	0	0		any
custom-field-6	Integration Custom Field 6	0	0		any
custom-field-7	Integration Custom Field 7	0	0		any
custom-field-8	Integration Custom Field 8	0	0		any
custom-field-9	Integration Custom Field 9	0	0		any
custom-field-10	Integration Custom Field 10	0	0		any













































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Expense Reports
Expense Report Header Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Describes the type of row. Possible values are Header, Line, or Line Split.	0	0	string	Header, Line, or Line Split.
ID	Coupa Generated Document ID	0	0	integer(11)	any
Created-At	When the expense report was created in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	0	0	datetime	any
Updated-At	When the expense report was last updated in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ	0	0	datetime	any
Title	The title of the expense report.	0	0	string(255)	any
Status	The current status of the expense report. Possible values are: draft, working, pending_approval, pending_info, approved, accounting_review, approved_for_payment, scheduled_for_payment, paid	0	0	string(255)	draft, working, pending_approval, pending_info, approved, accounting_review, approved_for_payment, scheduled_for_payment, paid
Submitted-at	When the expense report was submitted for approval in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ.	0	0	datetime	any
auditor-note	Auditor comments on the expense report.	0	0	text(2^24)	any
Rejection-Reason	The reason why the expense report was rejected.	0	0	text(2^24)	any
Paid	Flag to indicate if the expense report has been paid. True or False.	0	0	boolean	any
total	The total amount of the expense report in the transaction currency.	0	0	decimal(32,4)	any
audit-score	The audit-score Coupa assigns to the expense report.	0	0	decimal(30,2)	any
currency	The currency of the transaction.	0	0	string(6)	any
Expensed-By_email	The email address of the user to be reimbursed.	0	0	string(255)	any
Expensed-By_employee_number	The employee number of the user to be reimbursed.	0	0	string(255)	any
Expensed-By_id	The Coupa User ID of the user to be reimbursed.	0	0	integer(11)	any
Expensed-By_login	The username of the user to be reimbursed.	0	0	string(255)	any
Expensed-By_Fullname	The full name of the user to be reimbursed.	0	0	string(81)	any
Created-By_email	The email address of the user who created the report.	0	0	string(255)	any
Created-By_employee_number	The employee number of the user who created the report.	0	0	string(255)	any
Created-By_id	The Coupa User ID of the user who created the report.	0	0	integer(11)	any
Created-By_login	The username of the user who created the report.	0	0	string(255)	any
Created-By_Fullname,_Firstname	The full name of the user who created the report.	0	0	string(81)	any
Updated-By_email	The email address of the user who last updated the report.	0	0	string(255)	any
Updated-By_employee_number	The employee number of the user who last updated the report.	0	0	string(255)	any
Updated-By_id	The Coupa User ID of the user who last updated the report.	0	0	integer(11)	any
Updated-By_login	The username of the user who last updated the report.	0	0	string(255)	any
Updated-By_Fullname	The full name of the user who last updated the report.	0	0	string(81)	any
Event_-_ID	The list of the event IDs.	0	0	integer(11)	any
Event_-_Status	The list of the event statuses	0	0	string(255)	any
Event_-_Created_at	The list of event created dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ	0	0	datetime	any
Event_-_Updated_at	The list of event updated dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ	0	0	datetime	any
Event_-_Created-By_email	List of Email of user creating report event	0	0	string(255)	any
Event_-_Created-By_employee_number	List of Employee Number of user creating event	0	0	string(255)	any
Event_-_Created-By_id	List of Internal Coupa User ID creating event	0	0	integer(11)	any
Event_-_Created-By_login	List of Login of user creating event	0	0	string(255)	any
Event_-_Created-By_Fullname	List of Employee Name of user creating event	0	0	string(81)	any
Event_-_Updated-By_email	List of Email of user who last updated event	0	0	string(255)	any
Event_-_Updated-By_employee_number	List of Employee Number of user who last updated event	0	0	string(255)	any
Event_-_Updated-By_id	List of Internal Coupa User ID who last updated event	0	0	integer(11)	any
Event_-_Updated-By_login	List of Login of user who last updated event	0	0	string(255)	any
Event_-By_Fullname	List of Employee Name of user who last updated event	0	0	string(81)	any
Approval_Created-AT	List of Approval Created-At Dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ	0	0	datetime	any
Approval_Updated-At	List of Approval Updated-At Dates in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ	0	0	datetime	any
Position	Approval Order	0	0	integer(11)	any
approval-chain-id	Approval Chain ID	0	0	integer(11)	any
Approval_status	Approval Status	0	0	string(50)	any
approval-date	Approval Date in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ	0	0	datetime	any
Approval_Notes	Approval Notes	0	0	string(text-2^16)	any
Approval_Type	Type of Approval Hierarchy	0	0	string(255)	any
Approvable_Type	Type of Approvable	0	0	string(255)	any
Approvable_ID	ID of Approvable	0	0	integer(11)	any
Approver_-_Updated-By_email	List of Email of user who last updated event	0	0	string(255)	any
Approver_-_Updated-By_employee_number	List of Employee Number of user who last updated event	0	0	string(255)	any
Approver_-_Updated-By_id	List of Internal Coupa User ID who last updated event	0	0	integer(11)	any
Approver_-_Updated-By_login	List of Login of user who last updated event	0	0	string(255)	any
Approver_Updated-By_Fullname	List of Employee Name of user who last updated event	0	0	string(81)	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Reimbursable-Total	Total amount reimbursable to the employee.	0	0	decimal	any
Reimbursable-Total-Currency	The currency code of the reimbursable amount.	0	0		any
Payment Channel	The payment channel used to reimburse the employee.	0	0	string(255)	any
Expense Report Line Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Describes the type of row. Possible values are Header, Line, or Line Split.	0	0	string	Header, Line, or Line Split.
ID	Coupa's Expense Report ID	0	0	integer(11)	any
Line-ID	Coupa's Expense Report Line ID	0	0	integer(11)	any
Line-Number	Line Number	0	0	integer(11)	any
PO-Order-Line-ID	If pre approved, Coupa Order Line ID	0	0	integer(11)	any
Created-at	Time of Record Creation in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	0	0	datetime	any
Updated-At	Time Record was last updated in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	0	0	datetime	any
Description	Description of Expense Report Line Item	1	0	string(1550)	any
Merchant	Merchant on line	0	0	string(255)	any
Reason	Reason for Expense	0	0	string(255)	any
Transaction-Amount	The amount paid when the transaction was made.	0	0	decimal(32,4)	any
Transaction-Currency	The currency that the transaction was made in.	0	0	string(6)	any
Amount	Amount in user's default currency	0	0	decimal(32,4)	any
Currency	User's default currency	0	0	string(6)	any
Account-Total	Total of Amount in Chart of Accounts Currency	0	0	decimal(32,4)	any
Accounting-Currency	Currency Code	0	0	string(6)	any
Expense-Date	Expense Report Date in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	1	0	datetime	any
Expense-Category-Name	Expense Category Name	0	0	string(255)	any
Account-Code	Account Code	0	0	string(1024)	any
Account-Segment-1	Account Segment 1	0	0	string(100)	any
Account-Segment-2	Account Segment 2	0	0	string(100)	any
Account-Segment-3	Account Segment 3	0	0	string(100)	any
Account-Segment-4	Account Segment 4	0	0	string(100)	any
Account-Segment-5	Account Segment 5	0	0	string(100)	any
Account-Segment-6	Account Segment 6	0	0	string(100)	any
Account-Segment-7	Account Segment 7	0	0	string(100)	any
Account-Segment-8	Account Segment 8	0	0	string(100)	any
Account-Segment-9	Account Segment 9	0	0	string(100)	any
Account-Segment-10	Account Segment 10	0	0	string(100)	any
Account-Segment-11	Account Segment 11	0	0	string(100)	any
Account-Segment-12	Account Segment 12	0	0	string(100)	any
Account-Segment-13	Account Segment 13	0	0	string(100)	any
Account-Segment-14	Account Segment 14	0	0	string(100)	any
Account-Segment-15	Account Segment 15	0	0	string(100)	any
Account-Segment-16	Account Segment 16	0	0	string(100)	any
Account-Segment-17	Account Segment 17	0	0	string(100)	any
Account-Segment-18	Account Segment 18	0	0	string(100)	any
Account-Segment-19	Account Segment 19	0	0	string(100)	any
Account-Segment-20	Account Segment 20	0	0	string(100)	any
Account Type	Chart of Account	0	0	string(50)	any
Period Name	Budget Period	0	0	string(100)	any
External Source Name	The corp card template name like corporate_credit_card_amex etc.	0	0	string(255)	any
External Source Data	The file name of the credit card file that we received from cc company.	0	0	string(255)	any
External Source Ref	The unique transaction identifier for each credit card transaction	0	1	string(255)	any
Imported-Amount	Imported Amount	0	0	decimal(32,4)	any
Account Number	Credit Card Account number	0	0	string(255)	any
Employee Number	Employee number	0	0	string(255)	any
First Name	First Name	0	0	string(255)	any
Last Name	Last Name.	0	0	string(255)	any
Parent-Expense-Line-Id	ID of the expense line that was itemized	0	0	integer(11)	any
Supplier Reference Number	Supplier Reference Number	0	0	string(255)	any
Company Tax Id	The merchant ABN number or Federal Tax ID	0	0	string(255)	any
Corp Card Integration Name	The integration name that is used received the transaction	0	0	string(255)	any
Applied Expense Preapproval Id	Applied Expense Preapproval Id	0	0	integer(11)	any
Applied Expense Preapproval Description	Applied Expense Preapproval Description	0	0	string(255)	any
Applied Expense Preapproval Amount	Applied Expense Preapproval Amount	0	0	decimal(32,4)	any
Applied Expense Preapproval Currency Code	Applied Expense Preapproval Currency Code	0	0	string(6)	any
Applied Expense Line Cash Advance Amount	Applied Expense Line Cash Advance Amount	0	0	decimal(32,4)	any
Applied Expense Line Cash Advance Currency Code	Applied Expense Line Cash Advance Currency Code	0	0	string(6)	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Reimbursable to Employee	Is the Expense Line reimbursable to the employee?	0	0	boolean	any
Expense Report Line Allocation Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Describes the type of row. Possible values are Header, Line, or Line Split.	0	0	string	Header, Line, or Line Split.
expense-id	Coupa's Expense Report ID	0	0	integer(11)	any
expense-line-id	Coupa's Expense Report Line ID	0	0	integer(11)	any
line-num	Line Number	0	0	integer(11)	any
order-header-num	If pre approved, Coupa's Order Header Number	0	0	integer(11)	any
order-line-id	If pre approved, Coupa's Order Line ID	0	0	integer(11)	any
order-line-num	If pre approved, Coupa's Order Line Number	0	0	string(255)	any
account-allocation-id	Account Allocation ID	0	0	integer(11)	any
account-allocation-sequence	Position in the Account Allocation Sequence	0	0	integer(11)	any
account-allocation-amount	Amount allocated to the account	0	0	decimal(32,4)	any
account-allocation-percent	Percentage allocated to the account	0	0	decimal(16,10)	any
account-code	The whole account code of the account	0	0	string(1024)	any
account-active	Flag indicating if the account is active. True or False.	0	0	boolean	any
segment-1	Account Segment 1	0	0	string(100)	any
segment-2	Account Segment 2	0	0	string(100)	any
segment-3	Account Segment 3	0	0	string(100)	any
segment-4	Account Segment 4	0	0	string(100)	any
segment-5	Account Segment 5	0	0	string(100)	any
segment-6	Account Segment 6	0	0	string(100)	any
segment-7	Account Segment 7	0	0	string(100)	any
segment-8	Account Segment 8	0	0	string(100)	any
segment-9	Account Segment 9	0	0	string(100)	any
segment-10	Account Segment 10	0	0	string(100)	any
segment-11	Account Segment 11	0	0	string(100)	any
segment-12	Account Segment 12	0	0	string(100)	any
segment-13	Account Segment 13	0	0	string(100)	any
segment-14	Account Segment 14	0	0	string(100)	any
segment-15	Account Segment 15	0	0	string(100)	any
segment-16	Account Segment 16	0	0	string(100)	any
segment-17	Account Segment 17	0	0	string(100)	any
segment-18	Account Segment 18	0	0	string(100)	any
segment-19	Account Segment 19	0	0	string(100)	any
segment-20	Account Segment 20	0	0	string(100)	any
account-name	Nickname for the account	0	0	string(1024)	any
currency_code	Currency Code	0	0	string(6)	any
accounting-total	Total of Amount in Chart of Accounts Currency	0	0	decimal(32,4)	any
accounting_currency	Currency Code	0	0	string(6)	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any

Expense Report Line Taxes Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Expense Line Tax	0	0		any
tax-line-id	Coupa's Expense Line Tax ID	0	0	integer	any
expense-line-id	Coupa's Expense Line ID	0	0	integer	any
expense-line-number	Expense Line Number	0	0		any
expense-report-id	Coupa's Expense Report ID	0	0		any
tax-code	The Tax Code for the invoice line tax rate. Must match an existing tax rate code within Coupa.	0	0		any
tax-type-description	The Tax Rate Type description on the line.	0	0		any
tax-rate-description	The Tax Rate description on the line.	0	0		any
tax-line-currency	Tax Line Currency	0	0		any
country-code	Country Code	0	0		any
tax-rate	Tax Rate	0	0	decimal(8,3)	any
tax-amount	Tax Amount	0	0	decimal(32,4)	any
estimated-tax-amount	Estimated Tax Amount	0	0	decimal(32,4)	any
custom-field-1	Integration Custom Field 1	0	0		any
custom-field-2	Integration Custom Field 2	0	0		any
custom-field-3	Integration Custom Field 3	0	0		any
custom-field-4	Integration Custom Field 4	0	0		any
custom-field-5	Integration Custom Field 5	0	0		any
custom-field-6	Integration Custom Field 6	0	0		any
custom-field-7	Integration Custom Field 7	0	0		any
custom-field-8	Integration Custom Field 8	0	0		any
custom-field-9	Integration Custom Field 9	0	0		any
custom-field-10	Integration Custom Field 10	0	0		any



























































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Inventory Transactions (Receipt
Inventory Transaction Header Columns
Position	Column Name	Description	Req'd/Unique	Type	Allowable Values
1.0	Record Type	Describes the type of row. Possible value is Inventory Transaction.	No/No	-	Inventory Transaction
2.0	ID	Coupa's Internal Inventory Transaction ID	No/No	integer	any
3.0	Barcode	Barcode Value	No/No	string(255)	any
4.0	Created at	Time of Inventory Transaction Creation	No/No	datetime	any
5.0	Created-By email	Email of user who created transaction record	No/No	string(255)	any
6.0	Created-By employee number	Employee Number of user who created transaction record	No/No	string(255)	any
7.0	Created-By id	Internal Coupa User ID for user who created transaction	No/No	int(11)	any
8.0	Created-By login	Login of user who created transaction record	No/No	string(255)	any
9.0	Created-By Lastname, Firstname	Employee Name who created transaction record	No/No	string(255)	any
10.0	Price	Item Price	No/No	decimal(30,6)	any
11.0	Quantity	Receipt Quantity	No/No	decimal(30,6)	any
12.0	RFID Tag	RFID Tag Value	Yes/No	string(255)	any
13.0	Total	Receipt Total	No/No	decimal(30,6)	any
14.0	Type	Inventory Transaction Type	Yes/No	string(255)	InventoryReceipt, ReceivingConsumption, ReceivingAmountConsumption, ReceivingQuantityConsumption ReceivingReturnToSupplier, ReceivingAmountReturnToSupplier, ReceivingQuantityReturnToSupplier, ReceivingDisposal, ReceivingAmountDisposal, ReceivingQuantityDisposal
15.0	Status	Inventory Transaction Status. Default is Created	No/No	string(255)	any
16.0	Updated-At	Time of Inventory Transaction Updation	No/No	datetime	any
17.0	Updated-By email	Email of user who updated transaction record	No/No	string(255)	any
18.0	Updated-By employee number	Employee Number of user who updated transaction record	No/No	string(255)	any
19.0	Updated-By id	Internal Coupa User ID for user who updated transaction	No/No	int(11)	any
20.0	Updated-By login	Login of user who updated transaction record	No/No	string(255)	any
21.0	Updated-By Lastname, Firstname	Employee Name who updated transaction record	No/No	string(255)	any
22.0	Exported	Has the transaction been exported?	No/No	boolean	any
23.0	Account Code	Receipt Account Code	No/No	string(255)	any
24.0	Chart of Accounts	Chart of Accounts Name	No/No	Int(11)	any
25.0	From Warehouse Location ID	Coupa's Internal To-Warehouse-Location ID	No/No	int(11)	any
26.0	From Warehouse Aisle	Warehouse Aisle Location	No/No	string(255)	any
27.0	From Warehouse Bin	Warehouse Bin Location	No/No	string(255)	any
28.0	From Warehouse Level	Warehouse Level Location	No/No	string(255)	any
29.0	From Warehouse - Warehouse ID	Warehouse ID	No/No	int(11)	any
30.0	From Warehouse - Warehouse Description	Warehouse Description	No/No	string(255)	any
31.0	From Warehouse - Warehouse Name	Warehouse Name	No/No	string(255)	any
32.0	From Warehouse Type ID	Coupa's Internal Warehouse Type ID	No/No	int(11)	any
33.0	From Warehouse Type Name	Warehouse Type Name	No/No	string(255)	any
34.0	From Warehouse Type Description	Warehouse Type Description	No/No	string(255)	any
35.0	Order Line ID	Coupa Internal ID of line received against	No/No	int(11)	any
36.0	Order Line Accounting-Total	Total Line value in Accounting Currency	No/No	decimal(32,4)	any
37.0	Order Line Created-At	Date Line was Created	No/No	datetime	any
38.0	Order Line Description	Order Line Description	No/No	string(255)	any
39.0	Order Line Qty Invoiced	Order Line Quantity Invoiced	No/No	decimal(30,6)	any
40.0	Order Line Number	Line Number on Order	No/No	string(255)	any
41.0	Order Line Need By Date	Date Line was Updated	No/No	datetime	any
42.0	Order Line PO ID	Coupa's Internal PO Header ID	No/No	int(11)	any
43.0	Order Line Price	Order Line Unit Price	No/No	decimal(30,6)	any
44.0	Order Line Quantity	Quantity Ordered on Order Line	No/No	decimal(30,6)	any
45.0	Order Line Received	Quantity Received against order line	No/No	decimal(32,4)	any
46.0	Order Line Source Part Number	Source Part Number for Order Line	No/No	string(255)	any
47.0	Order Line Status	Status for Order Line	No/No	string(50)	any
48.0	Order Line Sub-line-num	Reserved for future use	No/No	int(11)	any
49.0	Order Line Supp-Aux-Part-Num	Supplier Auxiliary Part Number for Order Line	No/No	string(255)	any
50.0	Order Line Total	Total for Order Line	No/No	decimal(32,4)	any
51.0	Order Line Type	Type of Order Line (Quanity or Service)	No/No	string(100)	any
52.0	Order Line Updated-At	Date Order Line was last updated	No/No	datetime	any
53.0	Order Line Version	Order Line version Number	No/No	int(11)	any
54.0	Order Line Account Code	Account Code on PO Line	No/No	string(1024)	any
55.0	Order Line Chart of Accounts	Chart of Accounts Name on PO Line	No/No	string(50)	any
56.0	Order Line Accounting Total Currency	Accounting Currency Code for Order Line	No/No	string(6)	any
57.0	Order Line Currency	Currency Code for Order Line amounts	No/No	string(6)	any
58.0	Order Line Commodity Name	Commodity Name for Item on Order Line	No/No	string(255)	any
59.0	Order Line Department Name	Department Name for Item on Order Line	No/No	string(255)	any
60.0	Order Line Item ID	Coupa's Internal Item ID for Item on Order Line	No/No	int(11)	any
61.0	Order Line Item Number	Item Number	No/No	string(255)	any
62.0	Order Line Item Name	Item Name	No/No	string(255)	any
63.0	Order Line Supplier Name	Supplier Name	No/No	string(100)	any
64.0	Order Line Item Supplier Number	Supplier Number	No/No	string(255)	any
65.0	To Warehouse Location ID	Coupa's Internal To-Warehouse-Location ID	No/No	int(11)	any
66.0	To Warehouse Aisle	Warehouse Aisle Location	No/No	string(255)	any
67.0	To Warehouse Bin	Warehouse Bin Location	No/No	string(255)	any
68.0	To Warehouse Level	Warehouse Level Location	No/No	string(255)	any
69.0	To Warehouse - Warehouse ID	Warehouse ID	No/No	int(11)	any
70.0	To Warehouse - Warehouse Description	Warehouse Description	No/No	string(255)	any
71.0	To Warehouse - Warehouse Name	Warehouse Name	No/No	string(255)	any
72.0	To Warehouse Type ID	Coupa's Internal Warehouse Type ID	No/No	int(11)	any
73.0	To Warehouse Type Name	Warehouse Type Name	No/No	string(255)	any
74.0	To Warehouse Type Description	Warehouse Type Description	No/No	string(255)	any
75.0	UOM Code	Unit of Measure Code	No/No	string(6)	any
76.0	Inspection Code	Inspection Code	No/No	string(255)	any
77.0	Inspection Code ID	Coupa's Internal Inspection Code ID	No/No	int(11)	any
78.0	Inspection Code Description	Inspection Code Description	No/No	string(255)	any
79.0	Inspection Code Created-By email	email of user who created inspection code record	No/No	string(255)	any
80.0	Inspection Code Created-By employee number	Employee Number of user who created inspection code record	No/No	string(255)	any
81.0	Inspection Code Created-By id	Internal Coupa User ID for user who created inspection code	No/No	int(11)	any
82.0	Inspection Code Created-By login	Login of user who created inspection code record	No/No	string(255)	any
83.0	Inspection Code Created-By Lastname, Firstname	Employee Name who created inspection code record	No/No	string(255)	any
84.0	Inspection Code Created-At	Date Inspection Code was created.	No/No	datetime	any
85.0	Inspection Code Updated-By email	email of user who updated inspection code record	No/No	string(255)	any
86.0	Inspection Code Updated-By employee number	Employee Number of user who updated inspection code record	No/No	string(255)	any
87.0	Inspection Code Updated-By id	Internal Coupa User ID for user who updated inspection code	No/No	int(11)	any
88.0	Inspection Code Updated-By login	Login of user who updated inspection code record	No/No	string(255)	any
89.0	Inspection Code Updated-By Lastname, Firstname	Employee Name who updated inspection code record	No/No	string(255)	any
90.0	Inspection Code Updated-At	Date Inspection Code was Updated.	No/No	datetime	any
91.0	Asset Tag	Semi Colon seperated list of Asset Tag Identifiers	No/No	int(11)	any
92.0	Asset Tag Serial Number	Semi Colon seperated list of Asset Serial Number	No/No	string(255)	any
93.0	Asset Tag Owner	Semi Colon seperated list of Asset Owner	No/No	string(255)	any
94.0	Asset Tag Note	Semi Colon seperated list of Additional Notes	No/No	text(2^16)	any
95.0	Transaction Reason	Inventory Code Name	No/No	string(255)	any
96.0	Transaction Code	Inventory Code	No/No	string(255)	any
97.0	Received Weight	Received Weight	No/No	decimal(30,6)	any
98.0	Match Reference	Three-way match attribute to connect with Receipt and Invoice Header.	No/No	string(255)	any
99.0	custom-field-1	Integration Custom Field 1	No/No	string(255)	any
100.0	custom-field-2	Integration Custom Field 2	No/No	string(255)	any
101.0	custom-field-3	Integration Custom Field 3	No/No	string(255)	any
102.0	custom-field-4	Integration Custom Field 4	No/No	string(255)	any
103.0	custom-field-5	Integration Custom Field 5	No/No	string(255)	any
104.0	custom-field-6	Integration Custom Field 6	No/No	string(255)	any
105.0	custom-field-7	Integration Custom Field 7	No/No	string(255)	any
106.0	custom-field-8	Integration Custom Field 8	No/No	string(255)	any
107.0	custom-field-9	Integration Custom Field 9	No/No	string(255)	any
108.0	custom-field-10	Integration Custom Field 10	No/No	string(255)	any
109.0	Transaction Reference	ID of original transaction	No/No	integer	any
110.0	Reason Insight	Reason Insight Code	No/No		any
111.0	Inventory Request Number	Inventory Request Number	No/No		any
112.0	Inventory Request RMA	Inventory Request RMA	No/No		any
113.0	Inventory Request Address Location Code	Inventory Request Address Location Code	No/No		any
114.0	Inventory Request Address Attention	Inventory Request Address Attention	No/No		any
115.0	Inventory Request Address Name	Inventory Request Address Name	No/No		any
116.0	Inventory Request Address Street1	Inventory Request Address Street1	No/No		any
117.0	Inventory Request Address Street2	Inventory Request Address Street2	No/No		any
118.0	Inventory Request Address City	Inventory Request Address City	No/No		any
119.0	Inventory Request Address State	Inventory Request Address State	No/No		any
120.0	Inventory Request Address Postal Code	Inventory Request Address Postal Code	No/No		any
121.0	Inventory Request Address Country Code	Inventory Request Address Country Code	No/No		any
Inventory Transaction Allocation (Line Split) Columns
Position	Field Name	Description	Required/Unique	Field Type	Possible Values
1.0	Record Type	Describes the type of row. Possible value is Line Split.	No/No	-	Line Split
2.0	Inventory Transaction Id	Coupa's Inventory Transaction ID.	No/No	integer(11)
3.0	PO Number	Coupa's Order Header Number.	No/No	string(20)
4.0	Order Line Id	Coupa's Order Line ID.	No/No	integer(11)
5.0	Order Line Number	Coupa's Order Line Number.	No/No	string(255)
6.0	Id	Account Allocation ID	No/No	integer(11)
7.0	Allocation Number	Position in the Account Allocation Sequence	No/No	integer(11)
8.0	Amount	Amount allocated to the account	No/No	decimal(32,4)
9.0	Percent	Percentage allocated to the account	Yes/No	decimal(16,10)
10.0	Currency	Currency Code	No/No	string(6)
11.0	Account Code	Account Code	No/No	string(1024)
12.0	Account Active	Account Active	No/No	boolean
13.0	Account Segment 1	Account Segment 1	No/No	string(100)
14.0	Account Segment 2	Account Segment 2	No/No	string(100)
15.0	Account Segment 3	Account Segment 3	No/No	string(100)
16.0	Account Segment 4	Account Segment 4	No/No	string(100)
17.0	Account Segment 5	Account Segment 5	No/No	string(100)
18.0	Account Segment 6	Account Segment 6	No/No	string(100)
19.0	Account Segment 7	Account Segment 7	No/No	string(100)
20.0	Account Segment 8	Account Segment 8	No/No	string(100)
21.0	Account Segment 9	Account Segment 9	No/No	string(100)
22.0	Account Segment 10	Account Segment 10	No/No	string(100)
23.0	Account Segment 11	Account Segment 11	No/No	string(100)
24.0	Account Segment 12	Account Segment 12	No/No	string(100)
25.0	Account Segment 13	Account Segment 13	No/No	string(100)
26.0	Account Segment 14	Account Segment 14	No/No	string(100)
27.0	Account Segment 15	Account Segment 15	No/No	string(100)
28.0	Account Segment 16	Account Segment 16	No/No	string(100)
29.0	Account Segment 17	Account Segment 17	No/No	string(100)
30.0	Account Segment 18	Account Segment 18	No/No	string(100)
31.0	Account Segment 19	Account Segment 19	No/No	string(100)
32.0	Account Segment 20	Account Segment 20	No/No	string(100)
33.0	Account Name	Account Name	No/No	string(1024)
34.0	Account Type	Account Type	No/No	string(50)

Inventory Transaction (Barcode Scanning) Columns
Position	Field Name	Description	Required/Unique	Field Type	Possible Values
1.0	Type	Describes the type of row. Possible values are Payment, Payment Details or Payment Detail Allocation	No/No		any
2.0	Payment Detail Allocation ID	The ID of the payment detail allocation	No/No	integer	any
3.0	Payment ID	The ID of the payment the payment detail belongs to	No/No		any
4.0	Payment Detail ID	The ID of the payment detail the allocation belongs to	No/No		any
5.0	Source Transaction From ID	The ID of the transaction that emitted the allocation	No/No		any
6.0	Source Transaction From Type	The type of the transaction that emitted the allocation. Possible values are InvoiceHeader.	No/No		any
7.0	Source Transaction From Number	The reference ID of the transaction that emitted the allocation	No/No		any
8.0	Source Transaction From Amount	The amount sent by the transaction that emitted the allocation	No/No		any
9.0	Source Transaction From Currency	The currency for the amount sent by the transaction that emitted the allocation	Yes/No		any
10.0	Source Transaction To ID	The ID of the receiving transaction	No/No		any
11.0	Source Transaction To Type	The type of the receiving transaction. Possible values are InvoiceHeader.	No/No		any
12.0	Source Transaction To Number	The reference ID of the receiving transaction	No/No		any
13.0	Source Transaction To Amount	The amount sent to the receiving transaction	No/No		any
14.0	Source Transaction To Currency	The currency for the amount sent to the receiving transaction	No/No		any
15.0	Source	The source of this allocation. Possible values are coupa_pay.	No/No	string(255)	coupa_pay, erp
16.0	custom-field-1	Integration Custom Field 1	No/No		any
17.0	custom-field-2	Integration Custom Field 2	No/No		any
18.0	custom-field-3	Integration Custom Field 3	No/No		any
19.0	custom-field-4	Integration Custom Field 4	No/No		any
20.0	custom-field-5	Integration Custom Field 5	No/No		any
21.0	custom-field-6	Integration Custom Field 6	No/No		any
22.0	custom-field-7	Integration Custom Field 7	No/No		any
23.0	custom-field-8	Integration Custom Field 8	No/No		any
24.0	custom-field-9	Integration Custom Field 9	No/No		any
25.0	custom-field-10	Integration Custom Field 10	No/No		any






























































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Inventory Transaction Valuation
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Record Type	Describes the type of row. Possible value is Line Split.	0	0	-	Line Split
2.0	Inventory Transaction Id	Coupa's Inventory Transaction ID.	0	0	integer	any
3.0	Quantity	Quantity of Valuation	1	0	decimal(30,6)	any
4.0	Uom Code	Uom Code from Coupa	0	0	string(6)	any
5.0	Currency	The currency code of the valuation.	0	0	string(6)	any
6.0	Price	Price of Valuation	0	0	decimal(30,6)	any
7.0	custom-field-1	Integration Custom Field 1	0	0		any
8.0	custom-field-2	Integration Custom Field 2	0	0		any
9.0	custom-field-3	Integration Custom Field 3	0	0		any
10.0	custom-field-4	Integration Custom Field 4	0	0		any
11.0	custom-field-5	Integration Custom Field 5	0	0		any
12.0	custom-field-6	Integration Custom Field 6	0	0		any
13.0	custom-field-7	Integration Custom Field 7	0	0		any
14.0	custom-field-8	Integration Custom Field 8	0	0		any
15.0	custom-field-9	Integration Custom Field 9	0	0		any
16.0	custom-field-10	Integration Custom Field 10	0	0		any
























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Invoices
Invoice Header Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, or Line Split or Tax Line.	-	No/No	Header
2.0	id	The unique identifier Coupa assigned to the invoice.	integer(11)	No/No	Any
3.0	created-at	When the invoice was created in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ.	datetime	No/No	Any
4.0	updated-at	When the invoice was last updated in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ.	datetime	No/No	Any
5.0	status	The current status of the invoice. Possible values are: new, ap_hold, draft, on_hold, pending_receipt, disputed, pending_approval, approved, voided, booking_hold, save_as_draft	string(50)	No/No	Any
6.0	internal-note	Text field for comments made by employees. Not visible to the supplier.	text	No/No	Any
7.0	invoice-date	The date of the invoice in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ.	datetime	Yes/No	Any
8.0	invoice-number	The user-created invoice number.	string(40)	Yes/No	Any
9.0	line-level-taxation	Flag indicating if the invoice has taxes at the line level. True or False. If True, adds fourth header: Tax Line.	boolean	Yes/No	True/False
10.0	supplier-note	Text field for comments from the supplier. Visible to both Coupa users and the supplier.	text	No/No	Any
11.0	header-tax-amount	The amount of tax calculated on the invoice summary.	decimal	No/No	Any
12.0	header-tax-rate	The tax rate indicated on the invoice summary.	string(255)	No/No	Must exist in Coupa
13.0	header-tax-code	The tax rate code for the invoice summary tax rate. Must match an existing tax rate code within Coupa.	string(255)	No/No	Must exist in Coupa
14.0	paid	Flag indicating if the invoice was paid or not. Manually set. True or False. Default is False.	boolean	No/No	True/False
15.0	payment-date	The date of the invoice was marked as paid in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	Any
16.0	payment-notes	Text field for comments on the payment. Visible only to Coupa users.	text	No/No	Any
17.0	exported	Flag indicating if the invoice was exported to the ERP. True or False.	boolean	No/No	True/False
18.0	account-type-id	The unique identifier Coupa assigned to the Chart of Accounts.	integer	No/No	Any
19.0	account-type-name	The name of the Chart of Accounts within Coupa.	string(50)	No/No	Any
20.0	payment-term	The payment term code on the invoice.	string(255)	No/No	Must exist in Coupa
21.0	handling-amount	Summary handling amount added to the invoice by the supplier.	decimal(32,4)	No/No	Any
22.0	misc-amount	Summary charge added to the invoice by the supplier.	decimal(32,4)	No/No	Any
23.0	shipping-amount	Summary shipping charge added to the invoice by the supplier.	decimal(32,4)	No/No	Any
24.0	total	The total amount of the invoice, including all summary amounts.	decimal(46,20)	No/No	Any
25.0	currency	The currency code of the transaction.	string(6)	No/No	Any
26.0	accounting-total-amount	The total amount of the invoice using the Chart of Accounts currency. Doesn't include line and summary amounts.	decimal(30,4)	No/No	Any
27.0	accounting-total-currency	The currency code of the Chart of Accounts.	string(6)	No/No	Any
28.0	supplier-id	The unique identifier Coupa assigned to the supplier.	integer(11)	Yes/No	Any
29.0	supplier-name	The name of the supplier.	string(100)	No/No	Any
30.0	supplier-number	The number of the supplier.	string(255)	No/No	Any
31.0	created-by-email	The email address of the user who created the invoice.	string(255)	No/No	Any
32.0	created-by-employee-number	The employee number of the user who created the invoice.	string(255)	No/No	Any
33.0	created-by-login	The login name of the user who created the invoice.	string(255)	No/No	Any
34.0	updated-by-email	The email address of the user who last updated the invoice.	string(255)	No/No	Any
35.0	updated-by-employee-number	The employee number of the user who last updated the invoice.	string(255)	No/No	Any
36.0	updated-by-login	The login name of the user who last updated the invoice.	string(255)	No/No	Any
37.0	attachment-texts	The URLs of the attached files. The files can be set to the supplier, but cannot be downloaded as part of the CSV export.	string(255)	No/No	Any
38.0	comments	Not currently used.	string(255)	No/No	Any
39.0	remit-to-address-code	Remit to Address Code	string(255)	No/No	Any
40.0	remit-to-address-attention	Remit to Address Attention	string(255)	No/No	Any
41.0	remit-to-address-street1	Remit to Address Line 1	string(100)	No/No	Any
42.0	remit-to-address-street2	Remit to Address Line 2	string(100)	No/No	Any
43.0	remit-to-address-city	Remit to Address City	string(50)	No/No	Any
44.0	remit-to-address-state	Remit to Address State	string(50)	No/No	Any
45.0	remit-to-address-postal-code	Remit to Address Postal Code	string(50)	No/No	Any
46.0	remit-to-address-country-code	Remit to Address Country Code	string(4)	No/No	Any
47.0	remit-to-address-country-name	Remit To Address Country Name	string(100)	No/No	Any
48.0	remit-to-address-name	Remit To Address Name	string(255)	No/No	Any
49.0	remit-to-address-vat-number	The VAT number associated with the remit-to address (for tax and compliance purposes).	string(255)	No/No	Any
50.0	remit-to-address-vat-country-code	The country code for the remit-to address (for tax and compliance purposes).	string(4)	No/No	Any
51.0	remit-to-address-vat-country-name	The country name for the remit-to address (for tax and compliance purposes).	string(100)	No/No	Any
52.0	supplier-vat-number	The VAT number of the supplier.	string(255)	No/No	Any
53.0	supplier-vat-country-code	The VAT country code of the supplier.	string(4)	No/No	Any
54.0	document-type	The type of document. Possible values are Invoice or Credit Note, or nil.	string(255)	No/No	Invoice, Credit Note
55.0	original-invoice-number	The credit note must refer to the original invoice. Required if document-type is set to Credit Note.	string(40)	Yes/No	Any
56.0	original-invoice-date	The date that the original invoice was issued.	datetime	Yes/No	YYYY-MM-DDTHH:MM:SS+HH:MM
57.0	bill-to-address-legal-entity-name	The legal name of the bill-to address company. This is often different the then company name	string(255)	No/No	Any
58.0	bill-to-address-attention	The contact person at the bill-to address.	string(255)	No/No	Any
59.0	bill-to-address-street1	The first bill-to address line.	string(100)	No/No	Any
60.0	bill-to-address-street2	The second bill-to address line.	string(100)	No/No	Any
61.0	bill-to-address-city	The bill-to address city.	string(50)	No/No	Any
62.0	bill-to-address-state	The bill-to address state.	string(50)	No/No	Any
63.0	bill-to-address-postal-code	The bill-to address zip or postal code.	string(50)	No/No	Any
64.0	bill-to-address-country-code	The bill-to address country code.	string(4)	No/No	Any
65.0	bill-to-address-country-name	The bill-to address country name.	string(100)	No/No	Any
66.0	bill-to-address-name	The user-friendly name given to the bill-to address to make it more easily identifiable.	string(255)	No/No	Any
67.0	ship-to-address-attention	The contact person at the bill-to address.	string(255)	No/No	Any
68.0	ship-to-address-street1	The first ship-to address line.	string(100)	No/No	Any
69.0	ship-to-address-street2	The second ship-to address line.	string(100)	No/No	Any
70.0	ship-to-address-city	The ship-to address city.	string(50)	No/No	Any
71.0	ship-to-address-state	The ship-to address state or province.	string(50)	No/No	Any
72.0	ship-to-address-postal-code	The ship-to address zip or postal code.	string(50)	No/No	Any
73.0	ship-to-address-country-code	The ship-to address country code.	string(4)	No/No	Any
74.0	ship-to-address-country-name	The ship-to address country name.	string(100)	No/No	Any
75.0	ship-to-address-name	The user-friendly name given to the ship-to address to make it more easily identifiable.	string(255)	No/No	Any
76.0	supplier-remit-to-code	The name/code given to the supplier remit-to address by the supplier	string(255)	No/No	Any
77.0	supplier-remit-to-supplier-name	The user-friendly name given to the remit-to address by the supplier to make it more easily identifiable	string(255)	No/No	Any
78.0	supplier-remit-to-street1	The supplier-created remit-to first address line.	string(255)	No/No	Any
79.0	supplier-remit-to-street2	The supplier-created remit-to second address line.	string(255)	No/No	Any
80.0	supplier-remit-to-city	The supplier-created remit-to city.	string(255)	No/No	Any
81.0	supplier-remit-to-state	The supplier-created remit-to state.	string(255)	No/No	Any
82.0	supplier-remit-to-postal-code	The supplier-created remit-to zip or postal code.	string(255)	No/No	Any
83.0	supplier-remit-to-country-code	The supplier-created remit-to country code.	string(4)	No/No	Any
84.0	supplier-remit-to-country-name	The supplier-created remit-to country name.	string(100)	No/No	Any
85.0	Fiscal Rep. Name	Fiscal Rep. Name	string(255)	No/No	Any
86.0	Fiscal Rep. VAT ID	Fiscal Rep. Vat Id	string(255)	No/No	Any
87.0	Fiscal Rep. Address Code	Fiscal Rep. Address Code	string(255)	No/No	Any
88.0	Fiscal Rep. Address Street 1	Fiscal Rep. Address Street 1	string(100)	No/No	Any
89.0	Fiscal Rep. Address Street 2	Fiscal Rep. Address Street 2	string(100)	No/No	Any
90.0	Fiscal Rep. Address City	Fiscal Rep. Address City	string(50)	No/No	Any
91.0	Fiscal Rep. Address State	Fiscal Rep. Address State	string(50)	No/No	Any
92.0	Fiscal Rep. Address Postal Code	Fiscal Rep. Address Postal Code	string(50)	No/No	Any
93.0	Fiscal Rep. Address Country Code	Fiscal Rep. Address Country Code	string(4)	No/No	Any
94.0	discount_due_date	The date the invoice needs to be paid by in order to get the early-payment discount. Calculated by Coupa based on payment-term in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
95.0	net_due_date	The date the invoice needs to be paid by. Calculated by Coupa based payment-term in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
96.0	discount_amount	The value of the discount if the invoice is paid by the discount_due_date. Calculated by Coupa basedtotal and payment-term.	decimal(32,4)	No/No	Any
97.0	late-payment-penalties	Late Payment Penalties	string(255)	No/No	Any
98.0	margin-scheme	A reference to the margin scheme used	string(255)	No/No	Any
99.0	cash-accounting-scheme-reference	A reference to the cash accounting scheme used	string(255)	No/No	Any
100.0	exchange-rate	Exchange Rate	decimal(30,9)	No/No	Any
101.0	pre-payment-date	Pre-Payment Date	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
102.0	reverse-charge-reference	Reverse Charge Reference	string(255)	No/No	Any
103.0	discount-percent	Discount %	float	No/No	Any
104.0	credit-note-differences-with-original-invoice	Credit Note differences with Original Invoice	decimal(30,4)	No/No	Any
105.0	customs-declaration-number	Customs Declaration Number	string(255)	No/No	Any
106.0	customs-office	Customs Office	text	No/No	Any
107.0	customs-declaration-date	Customs Declaration Date	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
108.0	payment-order-reference	A code given by banks to use it instead of a bank account transfer.	string(255)	No/No
109.0	advance-payment-received-amount	Amount of advance payment received	decimal(30,4)	No/No	Any
110.0	series	The serial number used by the Company for internal control of the information.	string(30)	No/No	Any
111.0	folio-number	The internal folio number used by the Company.	string(20)	No/No	Any
112.0	use-of-invoice	The purpose invoice is going to be used for.	string(10)	No/No	Any
113.0	form-of-payment	The specific code in accordance with a catalogue: cash, check, transfer of funds, etc.	string(10)	No/No	Any
114.0	type-of-receipt	Type of the invoice: income, expense, transfer, payroll or payment.	string(10)	No/No	Any
115.0	payment-method	Installments or lump sum payments.	string(10)	No/No	Any
116.0	issuance-place	Issuance Place	string(255)	No/No	Any
117.0	confirmation	This is a unique number provided by the Tax Authorities or the PAC.	string(255)	No/No	Any
118.0	withholding-tax-override	Withholding Tax Override	decimal(30,3)	No/No	Any
119.0	type-of-relationship	Relationship of this document to its parent invoice. Chosen from a catalog.	string(10)	No/No	Any
120.0	gross-total	Gross Total	decimal	No/No	Any
121.0	registered-company-registration-number	Registration number of the registered company	string(255)	No/No	Any
122.0	registered-company-place-of-registration	Place of registration of the registered company	string(255)	No/No	Any
123.0	registered-company-type	The type of the registered company	string(255)	No/No	Any
124.0	registered-company-managing-directors	A list of managing directors of the registered company	string(255)	No/No	Any
125.0	credit-reason	The reason of creating the credit	string(255)	No/No	Any
126.0	registered-company-permit-number	Permit number of the registered company	string(255)	No/No	Any
127.0	registered-company-permit-date	Permit date of the registered company	string(255)	No/No	Any
128.0	registered-company-liquidator-name	Liquidator name of the registered company	string(255)	No/No	Any
129.0	registered-company-share-capital	Share capital of the registered company	string(255)	No/No	Any
130.0	Tax Nature	Estonia compliance required field	string(255)	No/No	Any
131.0	registered-company-unique-shareholder	Unique shareholder of the registered company	string(255)	No/No	Any
132.0	registered-company-liable-company	Liable company of the registered company	string(255)	No/No	Any
133.0	registered-company-tax-regime	Tax Regime of the registered company	string(255)	No/No	Any
134.0	registered-company-legal-status	Legal status of the company (for tax and compliance purposes).	string(255)	No/No	Any
135.0	QST Registration Number	QST Registration Number	string(255)	No/No	Any
136.0	Authorised Person	Authorised Person	string(255)	No/No	Any
137.0	Authorised Person Address	Authorised Person Address	string(255)	No/No	Any
138.0	Authorised Person VAT ID	Authorised Person VAT ID	string(255)	No/No	Any
139.0	Date of Registration	Date of Registration	string(255)	No/No	Any
140.0	Sole Registration Code	Sole Registration Code	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
141.0	origin-currency-net	Net Amount in local currency	decimal(32,4)	Yes/No	Any
142.0	taxes-in-origin-country-currency	Tax Amount in local currency	decimal(32,4)	Yes/No	Any
143.0	origin-currency-gross	Gross Amount in local currency	decimal(32,4)	Yes/No	Any
144.0	self-billing-reference	Self billing reference - used for compliant countries like The Netherlands	string(191)	No/No	Any
145.0	registered-company-legal-type	Legal type of the company (for tax and compliance purposes).	string(255)	No/No	Any
146.0	registered-company-registered-seat	Registered seat of the company (for tax and compliance purposes).	string(255)	No/No	Any
147.0	registered-company-chairman-of-the-board	Name of the chairperson of the board (for tax and compliance purposes).	string(255)	No/No	Any
148.0	registered-company-court-of-registration	Court where the company is registered (for tax and compliance purposes).	string(255)	No/No	Any
149.0	registered-company-liquidation-remark	Remark if the company is in liquidation (for tax and compliance purposes).	string(255)	No/No	Any
150.0	registered-company-commercial-register-number	Commercial register number of the company (for tax and compliance purposes).	string(255)	No/No	Any
151.0	Disputed Invoice Number	Disputed Invoice Number	string(40)	No/No	Any
152.0	Channel	Channel the invoice was created from	string(80)	No/No	Any
153.0	Taxable Amount	Taxable Amount	decimal(32,4)	No/No	Any
154.0	invoice-from-code	The name/code given to the supplier invoice-from address by the supplier.	string(255)	No/No	Any
155.0	invoice-from-supplier-name	The user-friendly name given to the invoice-from address by the supplier to make it more easily identifiable	string(100)	No/No	Any
156.0	invoice-from-street1	The supplier-created invoice-from first address line.	string(100)	No/No	Any
157.0	invoice-from-street2	The supplier-created invoice-from second address line.	string(100)	No/No	Any
158.0	invoice-from-city	The supplier-created invoice-from city.	string(50)	No/No	Any
159.0	invoice-from-state	The supplier-created invoice-from state.	string(50)	No/No	Any
160.0	invoice-from-postal-code	The supplier-created invoice-from zip or postal code.	string(50)	No/No	Any
161.0	invoice-from-country-code	The supplier-created invoice-from country code.	string(4)	No/No	Any
162.0	invoice-from-country-name	The supplier-created invoice-from country name.	string(100)	No/No	Any
163.0	ship-from-code	The name/code given to the supplier ship-from address by the supplier	string(255)	No/No	Any
164.0	ship-from-supplier-name	The user-friendly name given to the ship-from address by the supplier to make it more easily identifiable	string(100)	No/No	Any
165.0	ship-from-street1	The supplier-created ship-from first address line.	string(100)	No/No	Any
166.0	ship-from-street2	The supplier-created ship-from second address line.	string(100)	No/No	Any
167.0	ship-from-city	The supplier-created ship-from city.	string(50)	No/No	Any
168.0	ship-from-state	The supplier-created ship-from state.	string(50)	No/No	Any
169.0	ship-from-postal-code	The supplier-created ship-from zip or postal code.	string(50)	No/No	Any
170.0	ship-from-country-code	The supplier-created ship-from country code.	string(4)	No/No	Any
171.0	ship-from-country-name	The supplier-created ship-from country name.	string(100)	No/No	Any
172.0	supplier-tax-registration-number	The supplier-created supplier-tax-number.	string(255)	No/No	Any
173.0	supplier-tax-registration-country-code	The supplier-created supplier-tax-registration country code.	string(100)	No/No	Any
174.0	supplier-tax-registration-country-name	The supplier-created supplier-tax-registration country name.	string(4)	No/No	Any
175.0	supplier-tax-registration-local	The supplier-created supplier-tax-registration local indicator.	boolean	No/No	Yes/No, True/False
176.0	buyer-tax-registration-number	The buyer-created buyer-tax-number.	string(255)	No/No	Any
177.0	buyer-tax-registration-country-code	The buyer-created buyer-tax-registration country code.	string(100)	No/No	Any
178.0	buyer-tax-registration-country-name	The buyer-created buyer-tax-registration country name.	string(4)	No/No	Any
179.0	buyer-tax-registration-local	The buyer-created buyer-tax-registration local indicator.	boolean	No/No	Yes/No, True/False
180.0	delivery-date	The date of supply in the format YYYY-MM-DDTHH:MM:SS+HH:MMZ.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MMZ
181.0	registered-company-license-number	Company License Number		No/No	any
182.0	registered-company-register-legal-entities	Register Legal Entities		No/No	any
183.0	registered-company-name	Registered Company Name		No/No	any
184.0	dispute-method	Dispute Method, Possible values are: Auto, Manual	string(10)	No/No	Auto, Manual
185.0	date-received	The date when the invoice is received by enterprise via email	date	No/No	any
186.0	sender-email	The sender email who sent the invoice to enterprise via email		No/No	any
187.0	inbox-name	Inbox which the invoice was received into		No/No	any
188.0	amount-due	Amount due to the supplier - Invoice Total without withholding and customer accounting taxes		No/No	any
189.0	tax-due-to-supplier	Tax due to the supplier	decimal(46,6)	No/No	any
190.0	customer-accounting-tax	Customer accounting tax	decimal(46,6)	No/No	any
191.0	payment-channel	Where the invoice payment will be handled. Examples are ERP, Coupa Pay Virtual Card, Coupa Pay Invoice	string(40)	No/No	any
192.0	status	New allowable type: abandoned
193.0	invoice_reference_number	The Invoice Reference Number (IRN) is a unique ID generated using SHA256 algorithm and based on the parameters GST reg number, document number, financial year, and document type	string(255)	No/No	any
194.0	invoice-reference-number	The IRN is a unique ID generated using SHA256 algorithm and based on the parameters GST reg number, document number, financial year, and document type	string(255)	No/No	any
195.0	supplier-telephone-number	Supplier Telephone Number		No/No	any
196.0	endorsement-on-invoices	Endorsement On Invoices	string(255)	No/No	any
197.0	new-means-of-transport	New Means Of Transport	string(255)	No/No	any
198.0	place-of-issuance	Place Of Issuance	string(255)	No/No	any
199.0	amount-of-advance-payment	Amount Of Advance Payment	decimal(46,20)	No/No	any
200.0	transaction-uuid	Unique identifier created by the tax authority's system for a specific document	string(50)	No/No	any
201.0	transaction-notification-date	Date on which the invoice is received from the tax authority's system	datetime	No/No	any
202.0	supplier-invoice-issuer-name	Supplier Invoice Issuer Name	string(255)	No/No	any
203.0	supplier-invoice_reviewer-name	Supplier Invoice Reviewer Name	string(255)	No/No	any
204.0	supplier-payment-collector-name	Supplier Payment Collector Name	string(255)	No/No	any
205.0	permanent-account-number	Permanent Account Number (PAN)		No/No	any
206.0	invoice-issuance-time	Invoice Issuance Time		No/No	any
207.0	cash-register-operator-id	Cash Register Operator		No/No	any
208.0	means-of-payment	Means Of Payment		No/No	any
209.0	unique-identification-code-of-cash-receipt	Unique Identification Code Of Cash Receipt		No/No	any
210.0	security-code-of-issuer	Security Code Of Issuer		No/No	any
211.0	Payment Order Number	Payment Order Number	string	No/No	any
212.0	state-tax-number	State Tax ID Number		No/No	any
213.0	state-tax-number-for-substitute-taxpayer	State Tax ID Number for Substitute Taxpayer		No/No	any
214.0	municipal-tax-number	Municipality Tax ID Number		No/No	any
215.0	serial-code-of-fiscal-invoice	Serial Code of Fiscal Invoice		No/No	any
216.0	verification-code	Verification Code		No/No	any
217.0	type-of-document	Type of Document		No/No	any
218.0	protocol-number	Protocol Number		No/No	any
219.0	nature-of-operation	Nature of Operation		No/No	any
220.0	type-of-operation	Type of Operation		No/No	any
221.0	freight-type	Freight Type		No/No	any
222.0	vehicle-license-plate	Vehicle License Plate		No/No	any
223.0	national-enrollment-of-conveyor	National Enrollment of Conveyor		No/No	any
224.0	volume-amount	Volume Amount		No/No	any
225.0	volume-gross-weight	Volume Gross Weight		No/No	any
226.0	volume-liquid-weight	Volume Liquid Weight		No/No	any
227.0	volume-brand	Volume Brand		No/No	any
228.0	volume-type	Volume Type		No/No	any
229.0	volume-numbering	Volume Numbering		No/No	any
230.0	payment-agreement-notes	Payment Agreement Notes	string(255)	No/No	*Fully paid via Prepayment Agreement, Partially paid via Prepayment Agreement, Already paid for a Recurring Agreement, and Retain payment per agreement.

Invoice Line Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment.	-	No/No	Line
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.	integer(11)	No/No	Any
3.0	invoice-line-id	The unique identifier Coupa assigns to the invoice line.	integer(11)	No/No	Any
4.0	created-at	When the invoice line was created at in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
5.0	updated-at	When the invoice line was last updated at in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
6.0	total	The total amount of the invoice, including all distributed summary amounts.	decimal(46,20)	No/No	Any
7.0	accounting-total	The total amount of the invoice line using the Chart of Accounts currency.	decimal(30,3)	No/No	Any
8.0	accounting-total-currency	The currency code of the Chart of Accounts.	string(6)	No/No	Must exist in Coupa
9.0	line-num	The line number of the invoice line, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice.	integer(11)	No/No	Any
10.0	description	The invoice line description, usually taken from the description of the item.	varchar(1550)	Yes/No	Any
11.0	order-header-num	The number given to the corresponding purchase order within Coupa (if any).	string(20)	No/No	Any
12.0	order-header-requested-by-email	The email address of the user who created the corresponding purchase order.	string(255)	No/No	Any
13.0	order-header-requested-by-employee-number	The employee number of the user who created the purchase order.	string(255)	No/No	Any
14.0	order-header-requested-by-login	the username of the person who created the purchase order.	string(255)	No/No	Any
15.0	order-line-id	The unique identifier Coupa assigns to the corresponding line on the purchase order (if any).	integer(11)	No/No	Any
16.0	order-line-num	The line number of the corresponding purchase order line (if any).	integer(11)	No/No	Any
17.0	order-line-commodity	The commodity ID of the line item on the purchase order (if any).	integer(11)	No/No	Any
18.0	price	The price of the invoice.	decimal(46,20)	Yes/No	Any
19.0	quantity	The quantity of the invoice.	decimal(30,6)	No/No	Any
20.0	uom	The unit of measure code. it must already exist in Coupa.	string(6)	No/No	Any
21.0	price-per-weight	The price per weight of the order line item.	decimal(30,6)	No/No	Any
22.0	net-weight	The net weight of the order line item.	decimal(30,6)	No/No	Any
23.0	weight-uom	The unit of measure code of weight. it must already exist in Coupa.	string(6)	No/No	Any
24.0	bulk-price	Describes the non unit quantity price. This can be used to provide price agreed for a bulk quantity. This should be accompanied with 'Bulk Price Quantity' and optionally 'Bulk Price UoM', 'Bulk Price Conversion Numerator' and 'Bulk Price Conversion Denominator'.	decimal(30,6)	No/No	Any
25.0	bulk-price-qty	Describes the number of units on the line item that the 'Bulk Price' describes the price for.	decimal(30,6)	No/No	Any
26.0	status	The current status of the invoice line. Possible values are: new, ap_hold, draft, on_hold, pending_receipt, disputed, pending_approval, approved, voided, booking_hold, save_as_draft	string(255)	No/No	Any
27.0	tax-rate	The tax rate indicated on the invoice line. Only has a value if the header item line level taxation is set toTrue.	decimal(30,6)	No/No	Must exist in Coupa
28.0	tax-location	Only has a value if the header item line level taxation is enabled.	string(255)	No/No	Any
29.0	tax-code	The tax rate code for the line tax rate. Must match an existing tax rate code within Coupa. Only has a value if the header item line level taxation is enabled.	string(255)	No/No	Must exist in Coupa
30.0	tax-amount	Only has a value if the header item line level taxation is enabled.	decimal(32,4)	No/No	Any
31.0	tax-description	The line level tax description.	string(255)	No/No	Any
32.0	tax-supply-date	The line level tax supply date in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
33.0	account-code	The account code from Coupa. All segments are concatenated with a hyphen ( - ).	string(1024)	No/No	Any
34.0	account-active	A flag in Coupa to indicate if the account is active and can be selected. True or False.	boolean	No/No	Yes/No, True/False
35.0	original-date-of-supply	Original Date of Supply	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
36.0	delivery-note-number	Delivery Note Number	string(255)	No/No	Any
37.0	discount-amount	Discount Amount	decimal(30,3)	No/No	Any
38.0	company-uom	The unit of measurement that the company uses internally (for comercial purposes).	string(255)	No/No	Any
39.0	property-tax-account	Property Tax Account	string(255)	No/No	Any
40.0	commodity-name	The Name of the Invoice Line Commodity	string(255)	No/No	Any
41.0	supplier-part-number	Part or identification number of the goods.	string(255)	No/No	Any
42.0	customs-declaration-number	Customs Declaration Number	string(60)	No/No	Any
43.0	hsn-sac	HSN/SAC	string(255)	No/No	Any
44.0	unspsc	UNSPSC	string(255)	No/No	Any
45.0	category	Used to automate tax codes in Coupa Invoicing. Acceptable values: Goods or Services.	string(255)	No/No	goods, services
46.0	subcategory	Used to automate tax codes in Coupa Invoicing. Acceptable values: Raw materials, Investment goods or Services exceptions.	string(255)	No/No	raw_materials, investment_goods, services_exceptions
47.0	deductibility	Used to automate tax codes in Coupa Invoicing. Acceptable values: Fully, Partially or Not.	string(255)	No/No	fully_deductible, partially_deductible, not_deductible
48.0	billing-notes	A text field for adding notes to a billing line.	text(65,535)	No/No	Any
49.0	segment-1	Account segment within Coupa.	string(100)	No/No	Any
50.0	segment-2	Account segment within Coupa.	string(100)	No/No	Any
51.0	segment-3	Account segment within Coupa.	string(100)	No/No	Any
52.0	segment-4	Account segment within Coupa.	string(100)	No/No	Any
53.0	segment-5	Account segment within Coupa.	string(100)	No/No	Any
54.0	segment-6	Account segment within Coupa.	string(100)	No/No	Any
55.0	segment-7	Account segment within Coupa.	string(100)	No/No	Any
56.0	segment-8	Account segment within Coupa.	string(100)	No/No	Any
57.0	segment-9	Account segment within Coupa.	string(100)	No/No	Any
58.0	segment-10	Account segment within Coupa.	string(100)	No/No	Any
59.0	segment-11	Account segment within Coupa.	string(100)	No/No	Any
60.0	segment-12	Account segment within Coupa.	string(100)	No/No	Any
61.0	segment-13	Account segment within Coupa.	string(100)	No/No	Any
62.0	segment-14	Account segment within Coupa.	string(100)	No/No	Any
63.0	segment-15	Account segment within Coupa.	string(100)	No/No	Any
64.0	segment-16	Account segment within Coupa.	string(100)	No/No	Any
65.0	segment-17	Account segment within Coupa.	string(100)	No/No	Any
66.0	segment-18	Account segment within Coupa.	string(100)	No/No	Any
67.0	segment-19	Account segment within Coupa.	string(100)	No/No	Any
68.0	segment-20	Account segment within Coupa.	string(100)	No/No	Any
69.0	account-name	The account name from Coupa.	string(1024)	No/No	Any
70.0	created-by-email	The email address of the user who created the invoice.	string(255)	No/No	Any
71.0	created-by-employee-number	The employee number of the user who created the invoice.	string(255)	No/No	Any
72.0	created-by-login	The username of the user who created the invoice.	string(255)	No/No	Any
73.0	updated-by-email	The email address of the user who last updated the invoice.	string(255)	No/No	Any
74.0	updated-by-employee-number	The employee number of the user who last updated the invoice.	string(255)	No/No	Any
75.0	updated-by-login	The username of the user who last updated the invoice.	string(255)	No/No	Any
76.0	distributed-tax-amount	The amount of tax for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
77.0	distributed-shipping-amount	The amount of shipping for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
78.0	distributed-handling-amount	The amount of handling for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
79.0	distributed-misc-amount	The amount of misc for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
80.0	match-reference	Three-way match attribute to connect with Receipt and Invoice Header.	string(255)	No/No	Any
81.0	bulk-price-uom	Describes the UoM to express the Bulk Price. This is required if the line UoM is different than 'Bulk Price UoM'.	string(6)	No/No	Any
82.0	bulk-price-conversion-numerator	Numerator value for the ratio to convert from 'Bulk Price UoM' to line UoM. Value defaults from corresponding PO line if invoice line UoM matches PO line UoM and the PO Bulk Price UoM matches the invoice 'Bulk Price UoM'.		No/No	Any
83.0	bulk-price-conversion-denominator	Denominator value for the ratio to convert from 'Bulk Price UoM' to line UoM. A blank is interpreted as 1 as long as 'Bulk Price UoM' is present.		No/No	Any
84.0	po-number	The number given to the corresponding purchase order within Coupa (if any).		No/No	Any
85.0	fiscal-code	Fiscal Code	string(4)	No/No	Any
86.0	classification-of-goods	Classification of Goods	string(8)	No/No	Any
87.0	municipality-taxation-code	Municipality Taxation Code	string(255)	No/No	Any
88.0	item-barcode	Item Barcode	string(14)	No/No	Any
Invoice Line Allocation (Split) Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, or Line Split or Tax Line.	-	No/No	Line Split
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.	integer(11)	No/No	Any
3.0	invoice-line-id	The unique identifier Coupa assigns to the invoice line.	integer(11)	No/No	Any
4.0	line-num	The line number of the invoice line, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice.	integer(11)	No/No	Any
5.0	order-header-num	The number given to the corresponding purchase order within Coupa (if any).	string(20)	No/No	Any
6.0	order-line-id	The unique identifier Coupa assigns to the corresponding line on the purchase order (if any).	integer(11)	No/No	Any
7.0	order-line-num	The line number of the corresponding purchase order line (if any).	integer(11)	No/No	Any
8.0	account-allocation-id	The unique identifier Coupa assigns to the account allocation. Split line accounting must be enabled.	integer(11)	No/No	Any
9.0	account-allocation-sequence	The unique sequential counter Coupa assigns to the account allocation split. Split line accounting must be enabled.	integer(11)	No/No	Any
10.0	account-allocation-amount	The dollar amount for this account allocation. Split line accounting must be enabled.	decimal(32,4)	No/No	Any
11.0	account-allocation-percent	The percentage of the total amount allocated to this split. Split line accounting must be enabled.	decimal(16,10)	Yes/No	Any
12.0	account-code	The account code from Coupa. All segments are concatenated with a hyphen ( - ).	string(1024)	No/No	Any
13.0	account-active	A flag in Coupa to indicate if the account is active and can be selected. True or False.	boolean	No/No	Yes/No, True/False
14.0	billing-notes	A note to capture any information on this account allocation split.	text	No/No	Any
15.0	segment-1	Account segment within Coupa.	string(100)	No/No	Any
16.0	segment-2	Account segment within Coupa.	string(100)	No/No	Any
17.0	segment-3	Account segment within Coupa.	string(100)	No/No	Any
18.0	segment-4	Account segment within Coupa.	string(100)	No/No	Any
19.0	segment-5	Account segment within Coupa.	string(100)	No/No	Any
20.0	segment-6	Account segment within Coupa.	string(100)	No/No	Any
21.0	segment-7	Account segment within Coupa.	string(100)	No/No	Any
22.0	segment-8	Account segment within Coupa.	string(100)	No/No	Any
23.0	segment-9	Account segment within Coupa.	string(100)	No/No	Any
24.0	segment-10	Account segment within Coupa.	string(100)	No/No	Any
25.0	segment-11	Account segment within Coupa.	string(100)	No/No	Any
26.0	segment-12	Account segment within Coupa.	string(100)	No/No	Any
27.0	segment-13	Account segment within Coupa.	string(100)	No/No	Any
28.0	segment-14	Account segment within Coupa.	string(100)	No/No	Any
29.0	segment-15	Account segment within Coupa.	string(100)	No/No	Any
30.0	segment-16	Account segment within Coupa.	string(100)	No/No	Any
31.0	segment-17	Account segment within Coupa.	string(100)	No/No	Any
32.0	segment-18	Account segment within Coupa.	string(100)	No/No	Any
33.0	segment-19	Account segment within Coupa.	string(100)	No/No	Any
34.0	segment-20	Account segment within Coupa.	string(100)	No/No	Any
35.0	account-name	The account name from Coupa.	integer(11)	No/No	Any
36.0	currency_code	The currency code of the transaction.	string(6)	No/No	Must exist in Coupa
37.0	accounting-total	The total amount of the invoice using the Chart of Accounts currency. Doesn't include line and summary amounts.	decimal(32,4)	No/No	Any
38.0	accounting_currency	The currency code of the Chart of Accounts.	string(6)	No/No	Must exist in Coupa
39.0	distributed-tax-amount	The amount of tax for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
40.0	distributed-shipping-amount	The amount of shipping for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
41.0	distributed-handling-amount	The amount of handling for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
42.0	distributed-misc-amount	The amount of misc for the line item based on weighted summary expense distribution.	decimal(32,4)	No/No	Any
43.0	billing-notes	A note to capture any information on this account allocation split.	text	No/No	Any
Invoice Charge Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, Line Split, Charge, Charge Split, Tax Line, Witholding, or Payment.	-	No/No	Charge
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.	integer(11)	No/No	Any
3.0	invoice-charge-id	The unique identifier Coupa assigns to the invoice charge.	integer(11)	No/No	Any
4.0	line-type	The kind of charge. Possible values are InvoiceShippingCharge, InvoiceHandlingCharge, or InvoiceMiscCharge.	string(255)	No/No	Any
5.0	created-at	When the invoice charge was created at in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
6.0	updated-at	When the invoice charge was last updated at in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
7.0	total	The total amount of the charge.	decimal(30,4)	No/No	Any
8.0	percent	The percent value of this charge (only for percent-based charges & allowances. Not yet used.)	decimal(16,10)	No/No	Any
9.0	accounting-total	The total amount of the invoice charge using the Chart of Accounts currency.	decimal(30,4)	No/No	Any
10.0	accounting-total-currency	The currency code of the Chart of Accounts.	string(6)	No/No	Any
11.0	line-num	The line number of the invoice charge, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice.	integer(11)	No/No	Any
12.0	description	The invoice charge description.	string(1550)	No/No	Any
13.0	tax-rate	The tax rate indicated on the invoice charge.	decimal(16,10)	No/No	Any
14.0	tax-location	The location for tax on this charge	string(255)	No/No	Any
15.0	tax-code	The tax rate code for the charge tax rate. Must match an existing tax rate code within Coupa.	string(255)	No/No	Any
16.0	tax-amount	The amount of the tax on this charge	decimal(32, 4)	No/No	Any
17.0	tax-description	The charge level tax description.	string(255)	No/No	Any
18.0	tax-supply-date	The charge level tax supply date in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
19.0	account-code	The account code from Coupa. All segments are concatenated with a hyphen ( - ).	string(1024)	No/No	Any
20.0	account-active	A flag in Coupa to indicate if the account is active and can be selected. True or False.	boolean	No/No	Yes/No, True/False
21.0	billing-notes	A text field for adding notes to a billing line.	text(65535)	No/No	Any
22.0	segment-1	Account segment within Coupa.	string(100)	No/No	Any
23.0	segment-2	Account segment within Coupa.	string(100)	No/No	Any
24.0	segment-3	Account segment within Coupa.	string(100)	No/No	Any
25.0	segment-4	Account segment within Coupa.	string(100)	No/No	Any
26.0	segment-5	Account segment within Coupa.	string(100)	No/No	Any
27.0	segment-6	Account segment within Coupa.	string(100)	No/No	Any
28.0	segment-7	Account segment within Coupa.	string(100)	No/No	Any
29.0	segment-8	Account segment within Coupa.	string(100)	No/No	Any
30.0	segment-9	Account segment within Coupa.	string(100)	No/No	Any
31.0	segment-10	Account segment within Coupa.	string(100)	No/No	Any
32.0	segment-11	Account segment within Coupa.	string(100)	No/No	Any
33.0	segment-12	Account segment within Coupa.	string(100)	No/No	Any
34.0	segment-13	Account segment within Coupa.	string(100)	No/No	Any
35.0	segment-14	Account segment within Coupa.	string(100)	No/No	Any
36.0	segment-15	Account segment within Coupa.	string(100)	No/No	Any
37.0	segment-16	Account segment within Coupa.	string(100)	No/No	Any
38.0	segment-17	Account segment within Coupa.	string(100)	No/No	Any
39.0	segment-18	Account segment within Coupa.	string(100)	No/No	Any
40.0	segment-19	Account segment within Coupa.	string(100)	No/No	Any
41.0	segment-20	Account segment within Coupa.	string(100)	No/No	Any
42.0	account-name	The account name from Coupa.	string(1024)	No/No	Any
43.0	created-by-email	The email address of the user who created the invoice.	string(255)	No/No	Any
44.0	created-by-employee-number	The employee number of the user who created the invoice.	string(255)	No/No	Any
45.0	created-by-login	The username of the user who created the invoice.	string(255)	No/No	Any
46.0	updated-by-email	The email address of the user who last updated the invoice.	string(255)	No/No	Any
47.0	updated-by-employee-number	The employee number of the user who last updated the invoice.	string(255)	No/No	Any
48.0	updated-by-login	The username of the user who last updated the invoice.	string(255)	No/No	Any
Invoice Charge Allocations (Split) Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, or Line Split or Tax Line.	-	No/No	Charge Split
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.	integer(11)	No/No	Any
3.0	invoice-charge-id	The unique identifier Coupa assigns to the invoice charge.	integer(11)	No/No	Any
4.0	line-num	The line number of the invoice charge, as it appears on the invoice. Line numbers aren't necessarily listed sequential, but will appear sequentially on the invoice.	integer(11)	No/No	Any
5.0	account-allocation-id	The unique identifier Coupa assigns to the account allocation. Split line accounting must be enabled.	integer(11)	No/No	Any
6.0	account-allocation-sequence	The unique sequential counter Coupa assigns to the account allocation split. Split line accounting must be enabled.	integer(11)	No/No	Any
7.0	account-allocation-amount	The dollar amount for this account allocation. Split line accounting must be enabled.	decimal(30,4)	No/No	Any
8.0	account-allocation-percent	The percentage of the total amount allocated to this split. Split line accounting must be enabled.	decimal(16,10)	Yes/No	Any
9.0	account-code	The account code from Coupa. All segments are concatenated with a hyphen ( - ).	string(1024)	No/No	Any
10.0	account-active	A flag in Coupa to indicate if the account is active and can be selected. True or False.	boolean	No/No	Yes/No, True/False
11.0	billing-notes	A note to capture any information on this account allocation split.	text(65535)	No/No	Any
12.0	segment-1	Account segment within Coupa.	string(100)	No/No	Any
13.0	segment-2	Account segment within Coupa.	string(100)	No/No	Any
14.0	segment-3	Account segment within Coupa.	string(100)	No/No	Any
15.0	segment-4	Account segment within Coupa.	string(100)	No/No	Any
16.0	segment-5	Account segment within Coupa.	string(100)	No/No	Any
17.0	segment-6	Account segment within Coupa.	string(100)	No/No	Any
18.0	segment-7	Account segment within Coupa.	string(100)	No/No	Any
19.0	segment-8	Account segment within Coupa.	string(100)	No/No	Any
20.0	segment-9	Account segment within Coupa.	string(100)	No/No	Any
21.0	segment-10	Account segment within Coupa.	string(100)	No/No	Any
22.0	segment-11	Account segment within Coupa.	string(100)	No/No	Any
23.0	segment-12	Account segment within Coupa.	string(100)	No/No	Any
24.0	segment-13	Account segment within Coupa.	string(100)	No/No	Any
25.0	segment-14	Account segment within Coupa.	string(100)	No/No	Any
26.0	segment-15	Account segment within Coupa.	string(100)	No/No	Any
27.0	segment-16	Account segment within Coupa.	string(100)	No/No	Any
28.0	segment-17	Account segment within Coupa.	string(100)	No/No	Any
29.0	segment-18	Account segment within Coupa.	string(100)	No/No	Any
30.0	segment-19	Account segment within Coupa.	string(100)	No/No	Any
31.0	segment-20	Account segment within Coupa.	string(100)	No/No	Any
32.0	account-name	The account name from Coupa.	string(1024)	No/No	Any
33.0	currency_code	The currency code of the transaction.	string(6)	No/No	Any
34.0	accounting-total	The total amount of the invoice using the Chart of Accounts currency. Doesn't include line and summary amounts.	decimal(30,4)	No/No	Any
35.0	accounting_currency	The currency code of the Chart of Accounts.	string(6)	No/No	Any
Tax Line Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment.	-	No/No	Tax
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.	integer(11)	No/No	Any
3.0	invoice-number	The user-created invoice number.	string(40)	No/No	Any
4.0	invoice-line-id	The unique identifier Coupa assigns to the invoice line.	integer(11)	No/No	Any
5.0	invoice-line-number	The line number of the corresponding purchase order line (if any).	integer(11)	No/No	Any
6.0	tax-line-number	The line number of the corresponding of the tax line.	integer(11)	No/No	Any
7.0	tax-line-id	The unique identifier Coupa assigns to the tax line.	integer(11)	No/No	Any
8.0	amount	The amount of tax calculated on the line.	decimal(32,4)	No/No	Any
9.0	rate	The tax rate indicated on the invoice line.	decimal(16,10)	No/No	Any
10.0	tax-rate-type	The tax rate type description on the line	string(255)	No/No	Any
11.0	code	The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa.	string(255)	No/No	Any
12.0	description	The tax line description.	string(255)	No/No	Any
13.0	location	The taxable location for this tax line.	string(255)	No/No	Any
14.0	date	The tax line date in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
15.0	kind-of-factor	Kind of Factor indicates the specific type of Withholding which applies to the line item	string(255)	No/No	Any
16.0	basis	Basis indicates the base amount of the invoice or line item to which you must apply the withholding tax	decimal(30,6)	No/No	Any
17.0	Withholding Base	Base indicates the base amount of the invoice or line item to which withholding tax was applied	decimal(30,4)	No/No	Any
18.0	Supplier Withholding Rate	CFDI Withholding Rate	decimal(32,4)	No/No	Any
19.0	Supplier Withholding Amount	CFDI Withholding Amount	decimal(30,4)	No/No	Any
20.0	nature-of-tax	Nature of Tax indicates the specific type of tax which applies to the line item e.g. VAT or Withholding	string(255)	No/No	Any
21.0	Withholding Amount	Withholding Amount	decimal(30,4)	No/No	Any
22.0	Direct/Withholding Tax	WithholdingTaxLine or TaxLine	string(255)	No/No	Any
Withholding Tax Line Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment.	-	No/No	Witholding
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.	integer(11)	No/No	Any
3.0	invoice-number	The user-created invoice number.	string(40)	No/No	Any
4.0	invoice-line-id	The unique identifier Coupa assigns to the invoice line.	integer(11)	No/No	Any
5.0	invoice-line-number	The line number of the corresponding purchase order line (if any).	integer(11)	No/No	Any
6.0	tax-line-number	The line number of the corresponding of the tax line.	integer(11)	No/No	Any
7.0	tax-line-id	The unique identifier Coupa assigns to the tax line.	integer(11)	No/No	Any
8.0	amount	The amount of tax calculated on the line.	decimal(32,4)	No/No	Any
9.0	rate	The tax rate indicated on the invoice line.	decimal(16,10)	No/No	Any
10.0	code	The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa.	string(255)	No/No	Any
11.0	description	The tax line description.	string(255)	No/No	Any
12.0	location	The taxable location for this tax line.	string(255)	No/No	Any
13.0	date	The tax line date in the format YYYY-MM-DDTHH:MM:SS+HH:MM.	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
14.0	kind-of-factor	Kind of Factor indicates the specific type of Withholding which applies to the line item	string(255)	No/No	Any
15.0	basis	Basis indicates the base amount of the invoice or line item to which you must apply the withholding tax	decimal(30,6)	No/No	Any
16.0	Withholding Base	Base indicates the base amount of the invoice or line item to which withholding tax was applied	decimal(30,4)	No/No	Any
17.0	Supplier Withholding Rate	CFDI Withholding Rate	decimal(32,4)	No/No	Any
18.0	Supplier Withholding Amount	CFDI Withholding Amount	decimal(30,4)	No/No	Any
19.0	nature-of-tax	Nature of Tax indicates the specific type of tax which applies to the line item e.g. VAT or Withholding	string(255)	No/No	Any
20.0	Withholding Amount	Withholding Amount	decimal(30,4)	No/No	Any
21.0	Direct/Withholding Tax	WithholdingTaxLine or TaxLine	string(255)	No/No	Any
Matching Allocation
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row	-	No/No	Matching Allocation
2.0	order-line-id	The unique identifier Coupa assigns to the corresponding line on the purchase order (if any).	integer(11)	No/No	Any
3.0	order-header-number	The order header number.	string(20)	No/No	Any
4.0	order-line-num	The order line number	string(255)	No/No	Any
5.0	invoice-line-id	The unique identifier Coupa assigns to the invoice line.	integer(11)	No/No	Any
6.0	receipt-id	The unique identifier Coupa assigns to the receipt.	integer(11)	No/No	Any
7.0	match-reference-key	The match reference key as described in the receipt used to trigger a match attempt to a candidate invoice line.	string(255)	No/No	Any
8.0	quantity	The quantity of the invoice line item.	decimal(32,6)	Yes/No	Any
9.0	amount	The total amount of the receipt allocation to this invoice line.	decimal(32,4)	Yes/No	Any
10.0	uom	The unit of measure code. It must already exist in Coupa.	string(6)	No/No	Must exist in Coupa
11.0	currency	The currency code of the transaction.	string(6)	No/No	Must exist in Coupa
12.0	status	Describes the current status of this allocation record, If the allocation described in this record is active or has been voided. Can have values in Void, Matched.	string(50)	No/No	Any
Failed Tolerance Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	code	Code	string(255)	Yes/No	Any
2.0	failable-id	Failable ID	integer(11)	No/No	Any
3.0	failable-type	Failable Type	string(255)	No/No	Any
4.0	resolved	Resolved	boolean	No/No	Yes/No, True/False
5.0	resolution-strategy	Resolution Strategy	string(25)	No/No	Any
6.0	breach-amount	Breach Amount	string(255)	No/No	Any
7.0	breach-limit	Breach Limit	string(255)	No/No	Any
8.0	breach-detail-1	Breach Detail 1	string(255)	No/No	Any
9.0	breach-detail-2	Breach Detail 2	string(255)	No/No	Any
10.0	breach-detail-3	Breach Detail 3	string(255)	No/No	Any

Invoices Reconciliation Line Columns
#	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	Type	Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or ReconciliationLine.		No/No	Any
2.0	Adjustment Date	The date the payment was made	datetime	No/No	Any
3.0	Type of document	The type of document that was paid	InvoiceHeader	No/No	Any
4.0	Amount	The total amount paid	decimal(46,20)	No/No	Any
5.0	Invoice ID	The document ID that is being paid		No/No	Any
6.0	Created By ID	The user ID that created the payment	integer	No/No	Any
7.0	Created By Login	The user login that created the invoice payment		No/No	Any
8.0	Created Date	The date the payment initially drafted	datetime	No/No	Any
9.0	Updated By ID	The user ID that most recently updated the payment	integer	No/No	Any
10.0	Updated By Login	Ther user login that most recently updated the invoice payment		No/No	Any
11.0	Updated Date	The date the payment was most recently updated	datetime	No/No	Any
12.0	Note	Note associated with the payment	string(255)	No/No	Any
13.0	custom-field-1	Integration Custom Field 1		No/No	Any
14.0	custom-field-2	Integration Custom Field 2		No/No	Any
15.0	custom-field-3	Integration Custom Field 3		No/No	Any
16.0	custom-field-4	Integration Custom Field 4		No/No	Any
17.0	custom-field-5	Integration Custom Field 5		No/No	Any
18.0	custom-field-6	Integration Custom Field 6		No/No	Any
19.0	custom-field-7	Integration Custom Field 7		No/No	Any
20.0	custom-field-8	Integration Custom Field 8		No/No	Any
21.0	custom-field-9	Integration Custom Field 9		No/No	Any
22.0	custom-field-10	Integration Custom Field 10		No/No	Any


















































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Object Translation
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	Object Name	Object to be translated (example: Uom)	string(255)	No/No	any
2.0	Object ID	A unique identifier for the value to be translated.	integer	No/No	any
3.0	Field Name	Model attribute to be translated (example: name)	string(255)	No/No	any
4.0	Original Value	Model attribute value of the translation	string(1024)	No/No	any
5.0	Locale	Locale of this translation	string(255)	No/No	* see below
6.0	Translated Value	Model attribute value of the translation	string(1024)	No/No	any
* en, tr, ja, bg, cs, da, de-AT, de-BE, de-CH, de-LU, de, el, en-AE, en-AU, en-BD, en-BH, en-CA, en-CN, en-DK, en-FI, en-GB, en-HK, en-IE, en-IN, en-ME, en-MM, en-MT, en-MY, en-NA, en-NL, en-NO, en-NZ, en-PH, en-PK, en-SE, en-SG, en-TW, en-ZA, es-CO, es-IC, es-MX, es-PR, es, et, fi, fr-BE, fr-CA, fr-CH, fr-LU, fr, hr, hu, it-CH, it, ko, lt, lv, mt, nl-BE, nl, no, pl, pt-BR, pt, ro, ru, sk, sl, sr-ME, sr, sv-FI, sv, th, vi, zh-CN, zh-HK, zh-TW

# Sheet: Payables  Expense Preapproval
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	type	Describes the type of row. Possible value is ExpensePreapproval		No/No	any
2.0	id	The ID of the payable expense preapproval	integer	No/No	any
3.0	created-at	The date the payable Expense Preapproval was created on	datetime	No/No	any
4.0	updated-at	The date the payable expense preapproval was last updated on	datetime	No/No	any
5.0	status	The status of the payable expense preapproval	string(255)	No/No	any
6.0	paid-date	The date the payable expense preapproval was marked as fully paid	datetime	No/No	any
7.0	paid-total	The total amount paid	decimal	No/No	any
8.0	remaining-total	The total amount remaining to be paid	decimal	No/No	any
9.0	remittance-total	The total remittance amount required	decimal	No/No	any
10.0	accounting-total	The total of the payable expense preapproval in the CoA currency	decimal	No/No	any
11.0	exported	A flag indicating if the payable expense preapproval has been marked as exported		No/No	any
12.0	last-exported-at	The date that the payable expense preapproval was last marked as exported	datetime	No/No	any
13.0	type	the type of payable	string(255)	No/No	any
14.0	payment-channel	The payment channel on the payable expense preapproval	string(255)	No/No	any
15.0	payable-type	The type of associated payable. Value can be ExpensePreapproval		No/No	any
16.0	payable-id	The ID of the associated ExpensePreapproval		No/No	any
17.0	user-fullname	The user fullname from the associated ExpensePreapproval		No/No	any
18.0	chart-of-account-code	The Chart of Accounts name		No/No	any
19.0	custom-field-1	Integration Custom Field 1		No/No	any
20.0	custom-field-2	Integration Custom Field 2		No/No	any
21.0	custom-field-3	Integration Custom Field 3		No/No	any
22.0	custom-field-4	Integration Custom Field 4		No/No	any
23.0	custom-field-5	Integration Custom Field 5		No/No	any
24.0	custom-field-6	Integration Custom Field 6		No/No	any
25.0	custom-field-7	Integration Custom Field 7		No/No	any
26.0	custom-field-8	Integration Custom Field 8		No/No	any
27.0	custom-field-9	Integration Custom Field 9		No/No	any
28.0	custom-field-10	Integration Custom Field 10		No/No	any

# Sheet: PayablesInvoice
Position	Column Name	Type	Description	Req/Unique	Allowable Values
1.0	type		Describes the type of row. Possible value is Invoice	No/No	any
2.0	id	integer	The ID of the invoice	No/No	any
3.0	created-at	datetime	The date the invoice was created on	No/No	any
4.0	updated-at	datetime	The date the invoice was last updated on	No/No	any
5.0	status	string(255)	The status of the invoice	No/No	any
6.0	paid-date	datetime	The date the invoice was marked as fully paid	No/No	any
7.0	paid-total	decimal	The total amount paid	No/No	any
8.0	remaining-total	decimal	The total amount remaining to be paid	No/No	any
9.0	remittance-total	decimal	The total remittance amount required	No/No	any
10.0	accounting-total	decimal	The total of the invoice in the CoA currency	No/No	any
11.0	exported		A flag indicating if the invoice has been marked as exported	No/No	any
12.0	last-exported-at	datetime	The date that the invoice was last marked as exported	No/No	any
13.0	discount-amount		The discount amount taken	No/No	any
14.0	discount-rate		The discount rate taken	No/No	any
15.0	document-type		The type of invoice	No/No	any
16.0	payment-channel		The payment channel on the associated InvoiceHeader	No/No	any
17.0	payable-type		The type of associated payable. Value is InvoiceHeader	No/No	any
18.0	payable-id		The ID of the associated InvoiceHeader	No/No	any
19.0	net-due-date		The net due date of the invoice	No/No	any
20.0	supplier-name		The suppliers name from the associated InvoiceHeader	No/No	any
21.0	supplier-number		The suppliers number from the associated InvoiceHeader	No/No	any
22.0	invoice-number		The invoice number from the associated InvoiceHeader	No/No	any
23.0	chart-of-account-code		The Chart of Accounts name	No/No	any
24.0	legal-entity-name		The Chart of Accounts Legal Entity name	No/No	any
25.0	custom-field-1		Integration Custom Field 1	No/No	any
26.0	custom-field-2		Integration Custom Field 2	No/No	any
27.0	custom-field-3		Integration Custom Field 3	No/No	any
28.0	custom-field-4		Integration Custom Field 4	No/No	any
29.0	custom-field-5		Integration Custom Field 5	No/No	any
30.0	custom-field-6		Integration Custom Field 6	No/No	any
31.0	custom-field-7		Integration Custom Field 7	No/No	any
32.0	custom-field-8		Integration Custom Field 8	No/No	any
33.0	custom-field-9		Integration Custom Field 9	No/No	any
34.0	custom-field-10		Integration Custom Field 10	No/No	any

# Sheet: Payments
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	Type	Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment.	-	No/No
2.0	Payment Date	The date the payment was made	datetime	No/No
3.0	Payment Type	The type of payment that was made	string(255)	No/No
4.0	Amount Paid	The total amount paid	decimal(32,4)	No/No
5.0	Payable ID	The document ID that is being paid	integer(11)	No/No
6.0	Created By ID	The user ID that created the payment	integer(11)	No/No
7.0	Created By Login	The user login that created the invoice payment	string(255)	No/No
8.0	Created Date	The date the payment initially drafted	datetime	No/No
9.0	Updated By ID	The user ID that most recently updated the payment	integer(11)	No/No
10.0	Updated By Login	Ther user login that most recently updated the invoice payment	string(255)	No/No
11.0	Updated Date	The date the payment was most recently updated	datetime	No/No
12.0	Notes	Notes associated with the payment	string(255)	No/No

# Sheet: Procurement Milestone
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	record-type	Milestone		No/No	any
2.0	type	Type	string(255)	No/No	any
3.0	status	Status	string(255)	No/No	any
4.0	percent	Percent	decimal(30,6)	No/No	any
5.0	amount	Amount	decimal(30,6)	No/No	any
6.0	description	Description	text	No/No	any
7.0	due-date	Due date	date	No/No	any
8.0	external-reference-code	External reference code	string(255)	No/No	any
9.0	payment-terms-code	Payment Terms		No/No	any
10.0	payment-terms-days-for-discount-payment	Number of days to pay to receive discount		No/No	any
11.0	payment-terms-days-for-net-payment	Net Days for Payment		No/No	any
12.0	payment-terms-discount-rate	Discount Rate for payment within Discount Terms		No/No	any
13.0	custom-field-1	Integration Custom Field 1	string(255)	No/No	any
14.0	custom-field-2	Integration Custom Field 2	string(255)	No/No	any
15.0	custom-field-3	Integration Custom Field 3	string(255)	No/No	any
16.0	custom-field-4	Integration Custom Field 4	string(255)	No/No	any
17.0	custom-field-5	Integration Custom Field 5	string(255)	No/No	any
18.0	custom-field-6	Integration Custom Field 6	string(255)	No/No	any
19.0	custom-field-7	Integration Custom Field 7	string(255)	No/No	any
20.0	custom-field-8	Integration Custom Field 8	string(255)	No/No	any
21.0	custom-field-9	Integration Custom Field 9	string(255)	No/No	any
22.0	custom-field-10	Integration Custom Field 10	string(255)	No/No	any

# Sheet: Project
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	id	Project ID	integer	No/No	any
2.0	name	Project Name	string(255)	Yes/Yes	any
3.0	Mention Name	Mention Name	string(255)	No/Yes	any
4.0	Description	Description	text	No/No	any
5.0	Active	Active	boolean	No/No	any
6.0	Open	Open	boolean	No/No	any
7.0	Start date	Start date	datetime	No/No	any
8.0	End date	End date	datetime	No/No	any
9.0	Commodity ID	Commodity ID the project is associated with	integer	No/No	any
10.0	Created By ID	The user ID that created the project	integer	No/No	any
11.0	Created Date	The date the user create the project	datetime	No/No	any
12.0	Last Updated By ID	The user ID that most recently updated the project	integer	No/No	any
13.0	Last Updated Date	The date the project was most recently updated	datetime	No/No	any
14.0	custom-field-1	Integration Custom Field 1	string(255)	No/No	any
15.0	custom-field-2	Integration Custom Field 2	string(255)	No/No	any
16.0	custom-field-3	Integration Custom Field 3	string(255)	No/No	any
17.0	custom-field-4	Integration Custom Field 4	string(255)	No/No	any
18.0	custom-field-5	Integration Custom Field 5	string(255)	No/No	any
19.0	custom-field-6	Integration Custom Field 6	string(255)	No/No	any
20.0	custom-field-7	Integration Custom Field 7	string(255)	No/No	any
21.0	custom-field-8	Integration Custom Field 8	string(255)	No/No	any
22.0	custom-field-9	Integration Custom Field 9	string(255)	No/No	any
23.0	custom-field-10	Integration Custom Field 10	string(255)	No/No	any

# Sheet: Project Link
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	id	Project Link ID	integer	No/No	any
2.0	Project ID	The project to which it is linked to	integer	No/Yes	any
3.0	Linked Object ID	The object ID the project is linked to	integer	No/No	any
4.0	Linked Object Type	The object type the project is linked to	string(255)	No/No	Contract, QuoteRequest, Recommendation, RecommendationAssociation, Supplier, AmendmentContract, MasterContract, CsoEvent, DutchAuction, JapaneseAuction, ExpenseCategoryRecommendation, ExpenseMerchantRecommendation, BenchmarkRecommendation, CategoryRecommendation, CommodityRecommendation, SupplierRecommendation, InternalSupplier
5.0	Created Date	The date the user created the project link	datetime	No/No	any
6.0	Last Updated Date	The date the project link was most recently updated	datetime	No/No	any

# Sheet: Login
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	User ID	User ID	integer(11)	Yes/No
2.0	Attempted at	Time attempted to login at	datetime	No/No
3.0	User Type	User Type	string(255)	No/No
4.0	User Login	User Login	string(255)	No/No
5.0	ID	ID	integer(11)	No/No
6.0	User Agent	User Agent header information when attempted to login	string(255)	No/No
7.0	Source	Source information when attempted to login	string(255)	No/No

# Sheet: Purchase Orders
Purchase Order Header Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
type	Indicates record type	0	0	string	Header
acknowledged-at	Has PO been acknowledged by Supplier?	0	0	datetime	any
created-at	Date record was created in Coupa.	0	0	datetime	any
id	Coupa's internal ID	0	0	int(11)	any
status	PO Status	0	0	string(50)	any
transmission-status	Transmission Status	0	0	string(50)	any
updated-at	Last Updated at Date	0	0	datetime	any
version	PO Supplier Version Number - Increase each time a PO is changed and triggers a resend to the supplier.	0	0	int(11)	any
internal-revision	Internal Revision Number - Increases each time a change is made to a PO whether that change is internal or causes the PO to be resent to the supplier.	0	0	integer(11)	any
exported	Has the PO successfully been sent to target system?	0	0	boolean	any
created-by-email	Email of User who created invoice	0	0	string(255)	any
accounting-total	Accounting total for the PO	0	0	decimal(32,4)	any
accounting-total-currency	Accounting total currency	0	0	string(6)	any
created-by-employee-number	Employee Number of User who created invoice	0	0	string(255)	any
created-by-firstname	First name of User who created invoice	0	0	string(40)	any
created-by-id	Coupa ID of User who created Invoice	0	0	int(11)	any
created-by-lastname	Last name of User who created invoice	0	0	string(40)	any
created-by-login	Login name of User who created invoice	0	0	string(255)	any
requisition-id	Coupa ID of originating requisition	0	0	int(11)	any
requester-email	Requesting account's email address	0	0	string(255)	any
requester-employee-number	Requesting account's employee number	0	0	string(255)	any
requester-firstname	Requesting account's First Name	0	0	string(40)	any
requester-id	Requesting Account's ID	0	0	integer(11)	any
requester-lastname	Requesting Account's Last Name	0	0	string(40)	any
requester-login	Requesting Account's Login	0	0	string(255)	any
ship-to-attention	Ship To Address Attention Line	0	0	string(255)	any
ship-to-address-city	Ship To Address City	0	0	string(50)	any
ship-to-address-id	Ship To Address Internal Coupa ID	0	0	int(11)	any
ship-to-address-name	Ship To Address Name	0	0	string(255)	any
ship-to-address-postal-code	Ship To Address Postal Code	0	0	string(50)	any
ship-to-address-state	Ship To Address State/Province	0	0	string(50)	any
ship-to-address-street1	Ship To Address Street Address	0	0	string(100)	any
ship-to-address-street2	Ship To Address Street Address Line 2	0	0	string(100)	any
ship-to-address-country	Country Code	0	0	string(4)	any
ship-to-user-email	Email of User Ship To User	0	0	string(255)	any
ship-to-user-employee-number	Employee Number of Ship To User	0	0	string(255)	any
ship-to-user-firstname	First name of Ship To User	0	0	string(40)	any
ship-to-user-id	Coupa ID of Ship To User	0	0	int(11)	any
ship-to-user-lastname	Last name of Ship To User	0	0	string(40)	any
ship-to-user-login	Login name of Ship To User	0	0	string(255)	any
supplier-id	Supplier Coupa internal ID number	1	0	int(11)	any
supplier-name	Supplier Name	0	0	string(100)	any
supplier-number	Supplier Number	0	0	string(255)	any
updated-by-email	Email of User last updated by	0	0	string(255)	any
updated-by-employee-number	Employee Number of User last updated by	0	0	string(255)	any
updated-by-firstname	First name of user last updated by	0	0	string(40)	any
updated-by-id	Coupa ID of User last updated by	0	0	int(11)	any
updated-by-lastname	Last name of User last updated by	0	0	string(40)	any
updated-by-login	Login name of User last updated by	0	0	string(255)	any
payment-terms-code	Payment Terms	0	0	string(255)	any
payment-terms-days-for-discount-payment	Number of days to pay to receive discount	0	0	integer(11)	any
payment-terms-days-for-net-payment	Net Days for Payment	0	0	integer(11)	any
payment-terms-discount-rate	Discount Rate for payment within Discount Terms	0	0	float(24)	any
Shipping-terms-code	Shipping Terms Code	0	0	string(255)	any
attachment-text-concat	Concatenation of Text Attachment Text (Header Level)	0	0		any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Purchase Order Line Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
type	Indicates record type	0	0	string	Line
accounting-total	Accounting Total for Line	0	0	decimal(32,4)	any
accounting-total-currency	Currency used for Accounting Total	0	0	string(6)	any
created-at	Line Created At Date	0	0	datetime	any
description	Line Item Description	1	0	string(255)	any
id	Coupa Internal Line ID	0	0	integer	any
invoiced	Amount Invoiced	0	0	decimal(30,6)	any
active-invoiced-amount	Active Invoiced Amount which includes Pending Approval and Approved Invoices	0	0	decimal(32,4)	any
line-number	Line Number	0	1	string(255)	any
need-by-date	Line Need By Date	0	0	datetime	any
order-header-id	PO Number / Coupa Internal ID	0	0	integer	any
price	Unit Price	1	0	decimal(30,6)	any
quantity	Quantity Ordered	0	0	decimal(30,6)	any
received	Quantity/Amount Received	0	0	decimal(32,4)	any
source-part-num	Part Number - Determined by: For Catalog Items: Supplier Item Number For Catalog Item w/o Supplier Item Number: Item Number Non-Catalog Item: User Entered Item Number	0	0	string(255)	any
status	Line Status	0	0	string(50)	any
sub-line-num	<Reserved for future use>	0	0	integer	any
supp-aux-part-num	Supplier Auxiliary Part Number (Punch Out)	0	0	decimal(32,4)	any
total	Total Amount	0	0	decimal(32,4)	any
currency	Currency used for PO	0	0	string(6)	any
line-type	Line Type	0	0	string(100)	any
updated-at	Date Line Last Updated	0	0	datetime	any
version	Line Version/Revision #	0	0	int(11)	any
account-code	Account Code (combined segments)	0	0	string(1024)	any
segment-1	Account Code Segment 1	0	0	string(100)	any
segment-2	Account Code Segment 2	0	0	string(100)	any
segment-3	Account Code Segment 3	0	0	string(100)	any
segment-4	Account Code Segment 4	0	0	string(100)	any
segment-5	Account Code Segment 5	0	0	string(100)	any
segment-6	Account Code Segment 6	0	0	string(100)	any
segment-7	Account Code Segment 7	0	0	string(100)	any
segment-8	Account Code Segment 8	0	0	string(100)	any
segment-9	Account Code Segment 9	0	0	string(100)	any
segment-10	Account Code Segment 10	0	0	string(100)	any
segment-11	Account Code Segment 11	0	0	string(100)	any
segment-12	Account Code Segment 12	0	0	string(100)	any
segment-13	Account Code Segment 13	0	0	string(100)	any
segment-14	Account Code Segment 14	0	0	string(100)	any
segment-15	Account Code Segment 15	0	0	string(100)	any
segment-16	Account Code Segment 16	0	0	string(100)	any
segment-17	Account Code Segment 17	0	0	string(100)	any
segment-18	Account Code Segment 18	0	0	string(100)	any
segment-19	Account Code Segment 19	0	0	string(100)	any
segment-20	Account Code Segment 20	0	0	string(100)	any
account-name	Account Name	0	0	string(1024)	any
account-type	Chart of Accounts	0	0	string(50)	any
contract-id	Coupa Contract Internal ID	0	0	integer	any
contract-name	Contract Name	0	0	string(100)	any
department	Department Name	0	0	string(255)	any
created-by-email	Email of User who created invoice	0	0	string(255)	any
created-by-employee-number	Employee Number of User who created invoice	0	0	string(255)	any
created-by-firstname	First name of User who created invoice	0	0	string(255)	any
created-by-id	Coupa ID of User who created Invoice	0	0	int(11)	any
created-by-lastname	Last name of User who created invoice	0	0	string(40)	any
created-by-login	Login name of User who created invoice	0	0	string(255)	any
supplier-id	Supplier Coupa internal ID number	0	0	integer	any
supplier-name	Supplier Name	0	0	string(100)	any
supplier-number	Supplier Number	0	0	string(255)	any
uom	Unit of Measure	0	0	string(6)	any
updated-by-email	Email of User last updated by	0	0	string(255)	any
updated-by-employee-number	Employee Number of User last updated by	0	0	string(255)	any
updated-by-firstname	First name of User last updated by	0	0	string(40)	any
updated-by-id	Coupa ID of User last updated by	0	0	Int(11)	any
updated-by-lastname	Last name of User last updated by	0	0	string(40)	any
updated-by-login	Login name of User last updated by	0	0	string(255)	any
commodity	commodity	0	0	string(255)	any
requisition-line	Requisition Line ID	0	0	RequisitionLine	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Purchase Order Line Allocation Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
type	Indicates record type	0	0		any
order-header-id	PO Number / Coupa Internal ID	0	0	integer(11)	any
order-line-id	Coupa Purchase Order Line ID	0	0	integer(11)	any
order-line-num	Coupa Purchase Order Line Number	0	0	string(255)	any
account-allocation-id	Unique allocation id (only used if split line accounting is in use for the given Line record)	0	0	integer(11)	any
account-allocation-sequence	Unique allocation sequential counter (only used if split line accounting is in use for the given Line record)	0	0	integer(11)	any
account-allocation-amount	Dollar amount for this allocation (only used if split line accounting is in use for the given Line record)	0	0	decimal(32,4)	any
account-allocation-percent	Amount allocation percent (only used if split line accounting is in use for the given Line record)	1	0	decimal(16,10)	any
account-code	Account code from Coupa (only used if split line accounting is in use for the given Line record)	0	0	string(1024)	any
account-active	Account active flag	0	0	integer(1)	any
segment-1	Account Segment-1	0	0	string(100)	any
segment-2	Account Segment-2	0	0	string(100)	any
segment-3	Account Segment-3	0	0	string(100)	any
segment-4	Account Segment-4	0	0	string(100)	any
segment-5	Account Segment-5	0	0	string(100)	any
segment-6	Account Segment-6	0	0	string(100)	any
segment-7	Account Segment-7	0	0	string(100)	any
segment-8	Account Ssegment-8	0	0	string(100)	any
segment-9	Account Segment-9	0	0	string(100)	any
segment-10	Account Segment-10	0	0	string(100)	any
segment-11	Account Segment-11	0	0	string(100)	any
segment-12	Account Segment-12	0	0	string(100)	any
segment-13	Account Segment-13	0	0	string(100)	any
segment-14	Account Segment-14	0	0	string(100)	any
segment-15	Account Ssegment-15	0	0	string(100)	any
segment-16	Account Segment-16	0	0	string(100)	any
segment-17	Account Segment-17	0	0	string(100)	any
segment-18	Account Segment-18	0	0	string(100)	any
segment-19	Account Segment-19	0	0	string(100)	any
segment-20	Account Segment-20	0	0	string(100)	any
account-name	Account name from Coupa	0	0	string(1024)	any
account-type	Chart of Accounts Name from Coupa	0	0	string(50)	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any















































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Remit To Addresses
Position	Column Name	Description	Type	Req/Unique	Allowable Values
1.0	Name	Nickname to help identify the address	string(255)	No/No	any
2.0	Id	Coupa Generated Unique Id	integer	No/No	any
3.0	Supplier Number	Supplier number for remit to address		No/No	any
4.0	Remit To Code	Unique identifying code per supplier	string(255)	Yes/Yes	any
5.0	Line 1	Street Line 1 of the address	string(100)	Yes/No	any
6.0	Line 2	Street Line 2 of the address	string(100)	No/No	any
7.0	City	City of the address	string(50)	Yes/No	any
8.0	State	State of the address	string(50)	No/No	any
9.0	Postal Code	Zip code or postal code	string(50)	Yes/No	any
10.0	Country Code	ISO standard Country Code		No/No	any
11.0	Attention	Attention	string(255)	No/No	any
12.0	Active	Active address?	boolean	No/No	any
13.0	VAT Number	VAT Number	string(255)	No/No	any
14.0	VAT Country Code	VAT Country Code		No/No	any
15.0	Local Tax Number	Local Tax Number	string(255)	Yes/No	any
16.0	custom-field-1	Integration Custom Field 1	string(255)	No/No	any
17.0	custom-field-2	Integration Custom Field 2	string(255)	No/No	any
18.0	custom-field-3	Integration Custom Field 3	string(255)	No/No	any
19.0	custom-field-4	Integration Custom Field 4	string(255)	No/No	any
20.0	custom-field-5	Integration Custom Field 5	string(255)	No/No	any
21.0	custom-field-6	Integration Custom Field 6	string(255)	No/No	any
22.0	custom-field-7	Integration Custom Field 7	string(255)	No/No	any
23.0	custom-field-8	Integration Custom Field 8	string(255)	No/No	any
24.0	custom-field-9	Integration Custom Field 9	string(255)	No/No	any
25.0	custom-field-10	Integration Custom Field 10	string(255)	No/No	any

# Sheet: Requisitions
Requisition Header Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
Record Type	Indicates record type	0	0	string(255)	Requisition Header
Requisition Id	Coupa Internal Requisition ID	0	0	integer(11)	any
Submitted At Date	Date the Requisition was Submitted	0	0	datetime	any
Status	Requisition Status	1	0	string(50)	any
Buyer Note	Buyer Note	0	0	text	any
Justification	Justification for requisition	0	0	text	any
Reject Reason	rejection reason	0	0	text	any
Total	Total Amount for Request	0	0	decimal	any
Currency Code	3 digit Currency Code for Total	0	0	string(6)	Any ISO 4217 three letter currency code
Requested By Employee Number	Employee Number of user who requisition is on behalf of cart/requisition	0	0	string(255)	any
Requested by Login	Login of user who requisition is on behalf of cart/requisition	0	0	string(255)	any
Requested by Email	Email of user who requisition is on behalf of cart/requisition	0	0	string(255)	Must be in the format of a valid email address.
Department	Name of the Department for the requisition	0	0	string(255)	any
Ship To Address Street 1	Ship To Address Street Line 1	0	0	string(100)	any
Ship To Address Street 2	Ship To Address Street Line 2	0	0	string(100)	any
Ship To Address City	Ship To Address City	0	0	string(50)	any
Ship To Address State	Ship To Address State/Provience	0	0	string(50)	any
Ship To Address Postal Code	Ship To Address Postal Code	0	0	string(50)	any
Ship To Address Country Code	Ship To Address Country Code	0	0	string(4)	any
Ship To Address Attention	Ship To Address Attention Field	0	0	string(255)	any
Ship To Address Id	Ship To Address Internal Address ID	0	0	integer(11)	any
Ship To Address Name	Ship To Address Name	0	0	string(255)	any
Ship To Address Location Code	Ship To Address Location Code	0	0	string(255)	any
Created At Date	Date the shopping cart/requisition was first created	0	0	datetime	any
Updated At Date	Date the requisition was last updated	0	0	datetime	any
Approved By Employee Number	Approved By Employee Numbers	0	0	string(255)	any
Approved by Login	Approved by Logins	0	0	string(255)	any
Approved by Email	Approved by Emails	0	0	string(255)	any
Created By Employee Number	Employee Number of user who created cart/requisition	0	0	string(255)	any
Created by Login	Login of user who created cart/requisition	0	0	string(255)	any
Created by Email	Email of user who created cart/requisition	0	0	string(255)	any
Updated By Employee Number	Employee Number of person who last updated the requisition	0	0	string(255)	any
Updated by Login	Login of person who last updated the requisition	0	0	string(255)	any
Updated by Email	Email of person who last updated the requisition	0	0	string(255)	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Requisition Line Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
Record Type	Indicates record type	0	0	string(255)	Requisition Lines, Line Split
Requisition Header Id	Requisition Header Id	0	0	integer(11)	any
Line Number	Line Number	0	0	integer(11)	any
Description	Line Description	1	0	string(255)	any
Item Name	Item Name	0	0	string(255)	any
Item Number	Item Number	0	0	string(255)	any
Supplier Auxiliary Part Number	Supplier Auxiliary Part Number	0	0	string(255)	any
Source Part Number	Source Part Number	0	0	string(255)	any
Need By Date	Need By Date	0	0	datetime	any
Price	Unit Price of Item	0	0	decimal	any
Total Quantity	Total Quantity Ordered	0	0	decimal(30,6)	any
Line Total	Line Total Amount	0	0	decimal(32,4)	any
Request Type	Request Type	0	0	string(100)	any
Currency Code	Currency Code	0	0	string(6)	Any ISO 4217 three letter currency code
Supplier Number	Supplier Number	0	0	string(255)	any
Supplier Name	Supplier Name	0	0	string(100)	any
Payment Terms	Payment Term Code	0	0	string(255)	Must match an existing payment term in Coupa
Shipping Terms	Shipping Term Code	0	0	string(255)	Must match an existing shipping term in Coupa
Unit of Measure	Unit of Measure	0	0	string(6)	any
Assets Tags	Assets Tags	0	0	string(255)	any
Commodity Name	Commodity Name	0	0	string(255)	any
Chart of Account Name	Chart of Account Name	0	0	string(50)	any
Account Code	Account Code	0	0	string(255)	any
Account Name	Account Name	0	0	string(255)	any
Segment 1	Account Segment 1	0	0	string(100)	any
Segment 2	Account Segment 2	0	0	string(100)	any
Segment 3	Account Segment 3	0	0	string(100)	any
Segment 4	Account Segment 4	0	0	string(100)	any
Segment 5	Account Segment 5	0	0	string(100)	any
Segment 6	Account Segment 6	0	0	string(100)	any
Segment 7	Account Segment 7	0	0	string(100)	any
Segment 8	Account Segment 8	0	0	string(100)	any
Segment 9	Account Segment 9	0	0	string(100)	any
Segment 10	Account Segment 10	0	0	string(100)	any
Segment 11	Account Segment 11	0	0	string(100)	any
Segment 12	Account Segment 12	0	0	string(100)	any
Segment 13	Account Segment 13	0	0	string(100)	any
Segment 14	Account Segment 14	0	0	string(100)	any
Segment 15	Account Segment 15	0	0	string(100)	any
Segment 16	Account Segment 16	0	0	string(100)	any
Segment 17	Account Segment 17	0	0	string(100)	any
Segment 18	Account Segment 18	0	0	string(100)	any
Segment 19	Account Segment 19	0	0	string(100)	any
Segment 20	Account Segment 20	0	0	string(100)	any
Created At	Date line was created	0	0	datetime	any
Updated At	Date line was last updated	0	0	datetime	any
Created By Employee Number	Employee Number of user who created line	0	0	string(255)	any
Created by Login	Login of user who created line	0	0	string(255)	any
Created by Email	Email of user who created line	0	0	string(255)	any
Updated By Employee Number	Employee Number of user who last updated line	0	0	string(255)	any
Updated by Login	Login of user who last updated line	0	0	string(255)	any
Updated by Email	email of user who last updated line	0	0	string(255)	any
Requisition Line Allocation Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Describes the type of row. Possible values are Header, Line, or Line Split.	0	0	string(255)	Line Split
Requisition Header ID	Coupa's Requisition Report ID	0	0	integer(11)	any
Requsition Line ID	Coupa's Requisition Report Line ID	0	0	integer(11)	any
Requisition Line Number	Requisition Line Number	0	0	integer(11)	any
Purchase Order Header Number	If a PO was created, Coupa's Order Header Number	0	0	integer(11)	any
Purchase Order Line ID	If a PO was created, Coupa's Order Line ID	0	0	integer(11)	any
Purchase Order Line Number	If a PO was created, Coupa's Order Line Number	0	0	integer(11)	any
Account Allocation ID	Account Allocation ID	0	0	integer(11)	any
Allocation Number	Position in the Account Allocation Sequence	0	0	integer(11)	any
Allocation Amount	Amount allocated to the account	0	0	decimal(30,6)	any
Allocation Percent	Percentage allocated to the account	0	0	decimal(8,2)	any
Account Code	The whole account code of the account	0	0	string(255)	any
Account Active	Flag indicating if the account is active. True or False.	0	0	string(4)	True/False
Account Segment 1	Account Segment 1	0	0	string(100)	any
Account Segment 2	Account Segment 2	0	0	string(100)	any
Account Segment 3	Account Segment 3	0	0	string(100)	any
Account Segment 4	Account Segment 4	0	0	string(100)	any
Account Segment 5	Account Segment 5	0	0	string(100)	any
Account Segment 6	Account Segment 6	0	0	string(100)	any
Account Segment 7	Account Segment 7	0	0	string(100)	any
Account Segment 8	Account Segment 8	0	0	string(100)	any
Account Segment 9	Account Segment 9	0	0	string(100)	any
Account Segment 10	Account Segment 10	0	0	string(100)	any
Account Segment 11	Account Segment 11	0	0	string(100)	any
Account Segment 12	Account Segment 12	0	0	string(100)	any
Account Segment 13	Account Segment 13	0	0	string(100)	any
Account Segment 14	Account Segment 14	0	0	string(100)	any
Account Segment 15	Account Segment 15	0	0	string(100)	any
Account Segment 16	Account Segment 16	0	0	string(100)	any
Account Segment 17	Account Segment 17	0	0	string(100)	any
Account Segment 18	Account Segment 18	0	0	string(100)	any
Account Segment 19	Account Segment 19	0	0	string(100)	any
Account Segment 20	Account Segment 20	0	0	string(100)	any
Account Name	Nickname for the account	0	0	string(255)	any
Currency Code	Currency Code	0	0	string(3)	Any ISO 4217 three letter currency code
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any






















































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Sourcing
Quote Award Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Award	Quote Award	0	0
2.0	Quote Award ID	Quote Award ID	0	0	integer	any
3.0	Created At Date	Created At Date	0	0	datetime	any
4.0	Updated At Date	Updated At Date	1	0	datetime	any
5.0	Event Awardable ID	Event Awardable ID	0	0	integer	any
6.0	Event Awardable Type	Event Awardable Type	0	0	string(255)	any
Quote Request Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Request	Quote Request	0	0
2.0	Quote Request Header ID	Quote Request Header ID	0	0	integer
3.0	Original ID	Original ID	0	0	integer
4.0	Revision	Revision	0	0	string(255)
5.0	Event Header Name	Event Header Name	0	0	text
6.0	Created At Date	Created At Date	0	0	datetime
7.0	Created by ID	Created by ID	0	0	integer
8.0	Updated At Date	Updated At Date	0	0	datetime
9.0	Updated by ID	Updated by ID	0	0	integer
10.0	Start Date	Start Date	0	0	datetime
11.0	End Date	End Date	0	0	datetime
12.0	State	State	0	0	string(255)
13.0	Event Type	Event Type	1	0	string(255)
14.0	Type	Type	0	0	string(255)
15.0	Start On Submit	Start On Submit	0	0	boolean
16.0	Bid On Start	Bid On Start	0	0	boolean
17.0	Time To Respond	Time To Respond	0	0	integer
18.0	Beaten Price Options - Total Event	Beaten Price Options - Total Event	0	0
19.0	Beaten Price Options - Any Lot	Beaten Price Options - Any Lot	0	0
20.0	Beaten Price Options - Individual Line	Beaten Price Options - Individual Line	0	0
21.0	Incremental Bidding Options - Any Lot Allow - Tie For First Place	Incremental Bidding Options - Any Lot Allow - Tie For First Place	0	0
22.0	Incremental Bidding Options - Any Lot - Require To Improve Size	Incremental Bidding Options - Any Lot - Require To Improve Size	0	0
23.0	Incremental Bidding Options - Any Lot - Size	Incremental Bidding Options - Any Lot - Size	0	0
24.0	Incremental Bidding Options - Any Lot - Size Total	Incremental Bidding Options - Any Lot - Size Total	0	0
25.0	Incremental Bidding Options - Individual Line Allow - Tie For First Place	Incremental Bidding Options - Individual Line Allow - Tie For First Place	0	0
26.0	Incremental Bidding Options - Individual Line - Require To Improve - Size	Incremental Bidding Options - Individual Line - Require To Improve - Size	0	0
27.0	Incremental Bidding Options - Individual Line - Size	Incremental Bidding Options - Individual Line - Size	0	0
28.0	Incremental Bidding Options - Individual Line - Size Total	Incremental Bidding Options - Individual Line - Size Total	0	0
29.0	Incremental Bidding Options - Total Event Allow - Tie For First Place	Incremental Bidding Options - Total Event Allow - Tie For First Place	0	0
30.0	Incremental Bidding Options - Total Event - Require To Improve - Size	Incremental Bidding Options - Total Event - Require To Improve - Size	0	0
31.0	Incremental Bidding Options - Total Event - Size	Incremental Bidding Options - Total Event - Size	0	0
32.0	Incremental Bidding Options - Total Event - Size Total	Incremental Bidding Options - Total Event - Size Total	0	0
33.0	Suppliers See	Suppliers See	0	0	string(255)
34.0	Automatic Bid Extensions	Automatic Bid Extensions	0	0	boolean
35.0	Competitive Bidding	Competitive Bidding	0	0	boolean
36.0	Currency Code	Currency Code	0	0
37.0	Banner Title	Banner Title	0	0	string(255)
38.0	Banner Text	Banner Text	0	0	text
39.0	Commodity Name	Commodity Name	0	0
40.0	Custom Field 1	Custom Field 1	0	0	string(255)
41.0	Custom Field 1	Custom Field 1	0	0	string(255)
42.0	Custom Field 3	Custom Field 3	0	0	string(255)
43.0	Custom Field 4	Custom Field 4	0	0	string(255)
44.0	Custom Field 5	Custom Field 5	0	0	string(255)
45.0	Custom Field 6	Custom Field 6	0	0	string(255)
46.0	Custom Field 7	Custom Field 7	0	0	string(255)
47.0	Custom Field 8	Custom Field 8	0	0	string(255)
48.0	Custom Field 9	Custom Field 9	0	0	string(255)
49.0	Custom Field 10	Custom Field 10	0	0	string(255)
50.0	Custom Field 11	Custom Field 11	0	0	string(255)
51.0	Custom Field 12	Custom Field 12	0	0	string(255)
52.0	Custom Field 13	Custom Field 13	0	0	string(255)
53.0	Custom Field 14	Custom Field 14	0	0	string(255)
54.0	Custom Field 15	Custom Field 15	0	0	string(255)
55.0	Custom Field 16	Custom Field 16	0	0	string(255)
56.0	Custom Field 17	Custom Field 17	0	0	string(255)
57.0	Custom Field 18	Custom Field 18	0	0	string(255)
58.0	Custom Field 19	Custom Field 19	0	0	string(255)
59.0	Custom Field 20	Custom Field 20	0	0	string(255)
60.0	Savings	Savings	0	0	decimal(32,4)
61.0	Weight Attachments Score	Weight Attachments Score (Points)	0	0	integer
62.0	Weight Questionnaires Score	Weight Questionnaires Score (Points)	0	0	integer
63.0	Weight Items Score	Weight Items Score (Points)	0	0	integer
64.0	Closed At State	Closed At State	0	0	string(255)
65.0	Allow Multiple Response	Allow Multiple Response	0	0	boolean
66.0	Sealed Bids	Sealed Bids	0	0	boolean
67.0	Item Required Fields	Item Required Fields	0	0	text
68.0	Pause Start Time	Pause Start Time	0	0	datetime
69.0	Paused At State	Paused At State	0	0	string(255)
70.0	Creatable From Object ID	Creatable From Object ID	0	0	integer
71.0	Creatable From Object Type	Creatable From Object Type	0	0	string(255)
72.0	Followed From Event #	Followed From Event #	0	0	integer
73.0	Reporting Savings	Reporting Savings	0	0	decimal(32,4)
74.0	Next Revision Event ID	Next Revision Event ID	0	0	integer
75.0	Allow Award Individual Line Items	Allow Award Individual Line Items	0	0	boolean
76.0	Event Timezone	Event Timezone	0	0	string(255)
77.0	End At Price	End At Price	0	0	decimal(30,6)
78.0	Max Number Of Steps	Max Number Of Steps	0	0	integer
79.0	Price Increase Interval	Price Increase Interval	0	0	integer
80.0	Planned Savings	Planned Savings	0	0	decimal(30,6)
81.0	Reporting Planned Savings	Reporting Planned Savings	0	0	decimal(30,6)
82.0	Allow Suppliers To Choose Currency	Allow Suppliers To Choose Currency	0	0	boolean
83.0	Sealing Type	Sealing Type	0	0	integer	one_step_unsealing, two_steps_unsealing
84.0	Sealing Stage	Sealing Stage	0	0	integer	all_envelopes_sealed, envelope1_unsealed, envelope2_unsealed
85.0	Base Price Calculation Method	Base Price Calculation Method	0	0	integer
86.0	Cost Avoidance	Cost Avoidance	0	0	decimal(30,4)
87.0	Public	Public	0	0	boolean
88.0	Allow Supplier To Send Attachments	Allow Supplier To Send Attachments	0	0	boolean
89.0	Allow Evaluators To View Event	Allow Evaluators To View Event	0	0	boolean
90.0	Related Requisitions	Related Requisitions	0	0
91.0	Related Contracts	Related Contracts	0	0
92.0	Related Orders	Related Orders	0	0
93.0	Related Invoices	Related Invoices
Quote Request Line Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Request Line	Quote Request Line	0	0
2.0	Quote Request Line ID	Quote Request Line ID	0	0	integer
3.0	Created At Date	Created At Date	0	0	datetime
4.0	Created by ID	Created by ID	0	0	integer
5.0	Updated At Date	Updated At Date	0	0	datetime
6.0	Updated by ID	Updated by ID	0	0	integer
7.0	Event #	Event #	0	0	integer
8.0	Type	Type	1	0	string(255)
9.0	Quantity	Quantity	0	0	decimal(30,6)
10.0	UOM	UOM	0	0	integer
11.0	Position	Position	0	0	integer
12.0	Price Amount	Price Amount	0	0	decimal(30,6)
13.0	Price Currency Code	Price Currency Code	0	0	integer
14.0	Item ID	Item ID	0	0	integer
15.0	Description	Description	0	0	string(255)
16.0	Ship To Address ID	Ship To Address ID	0	0	integer
17.0	Ship To Address Street Line 1	Ship To Address Street Line 1	0	0
18.0	Ship To Address Street Line 2	Ship To Address Street Line 2	0	0
19.0	Ship To Address City	Ship To Address City	0	0
20.0	Ship To Address State/Province	Ship To Address State/Province	0	0
21.0	Ship To Address Postal Code	Ship To Address Postal Code	0	0
22.0	Ship To Address Country Code	Ship To Address Country Code	0	0
23.0	Ship To Address Location Code	Ship To Address Location Code	0	0
24.0	Reporting Price Amount	Reporting Price Amount	0	0	decimal(30,6)
25.0	Lot ID	Lot ID	0	0	integer
26.0	Commodity Name	Commodity Name	0	0	integer
27.0	Weight	Weight	0	0	integer
28.0	Creatable From Object ID	Creatable From Object ID	0	0	integer
29.0	Creatable From Object Type	Creatable From Object Type	0	0	string(255)
30.0	Cost Formula ID	Cost Formula ID	0	0	integer
31.0	Initial Price	Initial Price	0	0	decimal(30,6)
32.0	Incremental Increase Unit	Incremental Increase Unit	0	0	string(255)
33.0	Incremental Increase	Incremental Increase	0	0	decimal(30,6)
34.0	Need By Date	Need By Date	0	0	datetime
35.0	Price Amount In Event Currency	Price Amount In Event Currency	0	0	decimal(30,6)
36.0	Form ID	Form ID	0	0	integer
37.0	Manually Entered Base Price	Manually Entered Base Price	0	0	boolean
38.0	Manufacturer Name	Manufacturer Name	0	0	string(255)
39.0	Manufacturer Part Number	Manufacturer Part Number	0	0	string(255)
Quote Request User Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Request User	Quote Request User	0	0
2.0	Quote Request User ID	Quote Request User ID	0	0	integer
3.0	Quote Request ID	Quote Request ID	0	0	integer
4.0	User ID	User ID	0	1	integer
5.0	Attitude	Attitude	0	1	string(255)	creator, owner, watcher, evaluator
6.0	Evaluation State	Evaluation State	0	0	string(255)
7.0	Evaluation File	Evaluation File	0	0	string(255)
8.0	Evaluation Sections	Evaluation Sections	0	0	integer
9.0	Created At Date	Created At Date	0	0	datetime
10.0	Updated At Date	Updated At Date	0	0	datetime
Quote Response Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Response	Quote Response	0	0
2.0	Quote Response Header ID	Quote Response Header ID	0	0	integer
3.0	Created At Date	Created At Date	0	0	datetime
4.0	Created by ID	Created by ID	0	0	integer
5.0	Updated At Date	Updated At Date	0	0	datetime
6.0	Updated by ID	Updated by ID	0	0	integer
7.0	Event #	Event #	0	0	integer
8.0	Comments	Comments	0	0	text
9.0	Submitted At	Submitted At	1	0	datetime
10.0	Quote Supplier ID	Quote Supplier ID	0	0	integer
11.0	State	State	0	0	string(255)
12.0	Position	Position	0	0	integer
13.0	Type	Type	0	0	string(255)
14.0	Name	Name	1	1	string(255)
15.0	Track ID	Track ID	0	0	integer
16.0	Quote Response Status	Quote Response Status	0	0	integer
17.0	Updated By Supplier	Updated By Supplier	0	0	boolean
18.0	Is Bargain	Is Bargain	0	0	boolean
19.0	Best Total	Best Total	0	0	decimal(30,6)
20.0	Nearby Best Total	Nearby Best Total	0	0	decimal(30,6)
21.0	Is Best	Whether this response has the same price as the best response. This field is only valid for the best response from each supplier	0	0	boolean
22.0	Rank	The rank of the response. This field is only valid for the best response from each supplier	0	0	integer
23.0	Bid Total	Bid Total	0	0	decimal(30,6)
24.0	All Responded	All Responded	0	0	boolean
25.0	Awarded Supplier ID	The ID of the awarded master supplier record	0	0	integer
26.0	Awarded	Awarded	0	0
27.0	Promoted	Promoted	0	0	boolean
Quote Response Line Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Response Line	Quote Response Line	0	0
2.0	Quote Response Line Id	Quote Response Line Id	0	0	integer
3.0	Created At Date	Created At Date	0	0	datetime
4.0	Created by ID	Created by ID	0	0	integer
5.0	Updated At Date	Updated At Date	0	0	datetime
6.0	Updated by ID	Updated by ID	0	0	integer
7.0	Event Response ID	Event Response ID	0	0	integer
8.0	Event Request Line ID	Event Request Line ID	0	0	integer
9.0	Type	Type	0	0	string(255)
10.0	Quantity	Quantity	0	0	decimal(30,6)
11.0	Position	Position	0	0	integer
12.0	Price Amount	Price Amount	1	0	decimal(30,6)
13.0	Lot ID	Lot ID	0	0	integer
14.0	Weight	Weight	0	0	integer
15.0	Supplier Item Name	Supplier Item Name	0	0	string(255)
16.0	Item Part Number	Item Part Number	0	0	string(255)
17.0	Item Description	Item Description	0	0	text
18.0	Price Currency Code	Price Currency Code	0	0	integer
19.0	UOM	UOM	0	0	integer
20.0	Reporting Price Amount	Reporting Price Amount	0	0	decimal(30,6)
21.0	Lead Time	Lead Time	0	0	integer
22.0	Price Amount In Event Currency	Price Amount In Event Currency	1	0	decimal(30,6)
23.0	Form Response ID	Form Response ID	0	0	integer
Quote Response Status Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Response Status	Quote Response Status	0	0
2.0	Quote Response Status ID	Quote Response Status ID	0	0	integer
2.0	Name	Name	1	1	string(255)
3.0	Active	Active	0	0	boolean
4.0	Created At Date	Created At Date	0	0	datetime
5.0	Updated At Date	Updated At Date	0	0	datetime
Quote Supplier Columns
Position	Column Name	Description	Req'd	Unique	Type	Allowable Values
1.0	Quote Supplier	Quote Supplier	0	0
2.0	Quote Supplier ID	Quote Supplier ID	0	0	integer
3.0	Created At Date	Created At Date	0	0	datetime
4.0	Created by ID	Created by ID	0	0	integer
5.0	Updated At Date	Updated At Date	0	0	datetime
6.0	Updated by ID	Updated by ID	0	0	integer
7.0	Type	Type	0	0	string(255)
8.0	Supplier ID	Supplier ID	1	0	integer
9.0	Supplier Name	Supplier Name	1	1	string(255)
10.0	Supplier Email	Supplier Email	1	0	string(255)
11.0	Supplier Contact Name	Supplier Contact Name	0	0	string(255)
12.0	Supplier Display Name	Supplier Display Name	0	0	string(255)
13.0	Event Request ID	Event Request ID	0	0	integer
14.0	Supplier Default locale	Supplier Default locale	0	0	string(255)
15.0	Emailed	Emailed	0	0	boolean
16.0	Changes Review Confirmed	Changes Review Confirmed	0	0	boolean
17.0	Revision Changes Reviewed	Revision Changes Reviewed	0	0	boolean
18.0	Terms Accepted	Terms Accepted	0	0	boolean































































































































































































































































































































































































































































































































































































































# Sheet: Supplier
Position	Column Name	Description	Required/Unique	Type	Allowable Values
1.0	Name	Name	Yes/Yes	string(100)	any
2.0	Status	Status	No/No	string(20)	any
3.0	Id	Id	No/No	integer(11)	any
4.0	Commodity	Commodity	No/No	integer	any
5.0	Supplier Number	Supplier Number	No/Yes	string(255)	any
6.0	Account Number	Account Number	No/No	string(255)	any
7.0	Tax ID	Tax ID	No/No	string(255)	any
8.0	DUNS	DUNS	No/No	string(255)	any
9.0	Online Store URL	Online Store URL	No/No	string(255)	any
10.0	Online Store Login	Online Store Login	No/No	string(255)	any
11.0	Primary Contact Email	Primary Contact Email	No/No	string(255)	any
12.0	Primary Contact Phone Work	Primary Contact Phone Work	No/No	integer(11)	any
13.0	Primary Contact Phone Mobile	Primary Contact Phone Mobile	No/No	integer(11)	any
14.0	Primary Contact Phone Fax	Primary Contact Phone Fax	No/No	integer(11)	any
15.0	Primary Contact Name Given	Primary Contact Name Given	No/No	string(40)	any
16.0	Primary Contact Name Family	Primary Contact Name Family	No/No	string(40)	any
17.0	Primary Address Street1	Primary Address Street1	No/No	string(255)	any
18.0	Primary Address Street2	Primary Address Street2	No/No	string(100)	any
19.0	Primary Address City	Primary Address City	No/No	string(100)	any
20.0	Primary Address State	Primary Address State	No/No	string(50)	any
21.0	Primary Address Postal Code	Primary Address Postal Code	No/No	string(50)	any
22.0	Primary Address Country Code	Primary Address Country Code	No/No	string(50)	any
23.0	Primary Address Tax Number	Primary Address Tax Number	No/No	string(255)	any
24.0	Primary Address Tax Country Code	Primary Address Tax Country Code	No/No	string(100)	any
25.0	Primary Address Local Tax Number	Primary Address Local Tax Number	No/No	string(255)	any
26.0	Invoice Matching Level	Invoice Matching Level	No/No	string(255)	2-way, 3-way, none
27.0	Po Method	Po Method	No/No	string(255)	cxml, xml, email, prompt, mark_as_sent, buy_online
28.0	PO Change Method'	PO Change Method'	No/No	string(255)	cxml, xml, email, prompt, mark_as_sent, buy_online
29.0	Buyer Hold	Buyer Hold	No/No	boolean	Yes/No, True/False
30.0	Default Locale	Will accept any valid locale short code i.e. en, en-GB, fr, fr-CA, etc.	No/No	string(255)
31.0	PO Email	PO Email	Yes/No	string(255)	any
32.0	Payment Method	Must be "Invoice", "P-Card", "Invoice Only", or "P-Card Only"	Yes/No	string(255)
33.0	Payment Method	Payment Method	Yes/No	string(255)	invoice, pcard, invoice_only, pcard_only, virtual_card
34.0	Virtual Card Email	Required when Payment Method = virtual_card; supplier email where Virtual Cards are sent	Yes/No	string(255)	any
35.0	Payment Terms	Payment Terms	No/No	integer(11)	any
36.0	Shipping Terms	Shipping Terms	No/No	integer(11)	any
37.0	PO cXML URL	PO cXML URL	Yes/No	string(255)	any
38.0	PO cXML Domain	PO cXML Domain	Yes/No	string(255)	any
39.0	PO cXML Identity	PO cXML Identity	Yes/No	string(255)	any
40.0	PO cXML Supplier Domain	PO cXML Supplier Domain	Yes/No	string(255)	any
41.0	PO cXML Supplier Identity	PO cXML Supplier Identity	Yes/No	string(255)	any
42.0	PO cXML Secret	PO cXML Secret	Yes/No	string(940)	any
43.0	PO cXML Protocol	PO cXML Protocol	Yes/No	string(255)	any
44.0	Savings (%)	Savings (%)	No/No	decimal(8,2)	any
45.0	On Hold	On Hold	No/No	boolean	Yes/No, True/False
46.0	Allow cXML Invoicing	Allow cXML Invoicing	No/No	boolean	Yes/No, True/False
47.0	cXML Invoicing - Supplier Domain	cXML Invoicing - Supplier Domain	Yes/No	string(255)	any
48.0	cXML Invoicing - Supplier Identity	cXML Invoicing - Supplier Identity	Yes/Yes	string(255)	any
49.0	cXML Invoicing - Buyer Domain	cXML Invoicing - Buyer Domain	Yes/No	string(255)	any
50.0	cXML Invoicing - Buyer Identity	cXML Invoicing - Buyer Identity	Yes/No	string(255)	any
51.0	cXML Invoicing Shared Key	cXML Invoicing Shared Key	Yes/No	string(255)	any
52.0	Invoice Emails	Invoice Emails	No/No	string(255)	any
53.0	Send Invoices To Approvals	Send Invoices To Approvals	No/No	boolean	Yes/No, True/False
54.0	Allow Invoicing From CSN	Allow Invoicing From CSN	No/No	boolean	Yes/No, True/False
55.0	Allow Invoicing No Backing Doc From CSN	Allow Invoicing No Backing Doc From CSN	No/No	boolean	Yes/No, True/False
56.0	custom-field-1	Integration Custom Field 1	No/No	string(255)	any
57.0	custom-field-2	Integration Custom Field 2	No/No	string(255)	any
58.0	custom-field-3	Integration Custom Field 3	No/No	string(255)	any
59.0	custom-field-4	Integration Custom Field 4	No/No	string(255)	any
60.0	custom-field-5	Integration Custom Field 5	No/No	string(255)	any
61.0	custom-field-6	Integration Custom Field 6	No/No	string(255)	any
62.0	custom-field-7	Integration Custom Field 7	No/No	string(255)	any
63.0	custom-field-8	Integration Custom Field 8	No/No	string(255)	any
64.0	custom-field-9	Integration Custom Field 9	No/No	string(255)	any
65.0	custom-field-10	Integration Custom Field 10	No/No	string(255)	any
66.0	Virtual Card Email	Email where Virtual Cards are sent when Payment Method is Virtual Card	Yes/No	string(255)	any
67.0	​PO cXML Secret	Required if PO method is cXML and wasn't previously configured.	Yes/No	string(940)	any
68.0	​PO cXML HTTP Basic Auth Password	Required if sending PO cXML requires HTTP Basic Auth.	Yes/No	string(255)	any









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Supplier Information
Supplier Information Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Specifies the header format for the row. Possible values include: Header, Address, Artifact, Attachment	0	0		Header
SIM ID	Coupa's unique identifier for the SIM record.	0	0	integer(11)	any
Supplier ID	Coupa's unique identifier for the supplier associated with the SIM record.	0	0	integer(12)	any
Buyer ID	Coupa's unique identifier for the buyer who created the SIM record.	0	0	integer(13)	any
SIM Status	The current approval status of the SIM record.	1	0	string(255)	Draft, Information Requested, Pending Approval, Approved, Declined by Supplier
Company Name	The name of the SIM record.	1	0	string(255)	any
Display Name	A user-friendly name for the suppler.	0	0	string(255)	any
Parent Company Name	Parent Supplier Company Name as it exists in Coupa. Must exist in Coupa.	0	0	string(255)	any
Industry	The default industry for the supplier.	0	0	string(255)	any
Preferred Currency	The currency the supplier would like to use to do business.	0	0		any
Preferred Language	The language the supplier would like to use to do business.	0	0		any
Inco Terms	Three letter Incoterm code for the supplier's commercial terms.	0	0	string(255)	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or 11
(1=EXW, 2=FCA, 3=CPT, 4=CIP, 5=DAT, 6=DAP, 7=DDP, 8=FAS, 9=FOB, 10=CFR, 11=CIF)
Commodity	The supplier's default commodity.	0	0		any
Minority Indicator	Indicates if the supplier is a minority supplier.	0	0	boolean	any
Minority Type	Three letter code for the minority type. Required if Minority Indicator is set to true.	0	0	integer	1, 2, 3, or 4
(1=HIS, 2=NAT, 3=AFR, 4=ASN)
Tax Region	The tax jurisdiction.	0	0	string(255)	US, International
Tax Classification	US tax categories.	0	0	string(255)	1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or 11
(1=1099, 2=C Corp, 3=Customer Refund, 4=Exempt 1099, 5=Tax Authority, 6=Tax & Gov, 7=Vendor, 8=Non-Profit, 9=Partner Referral, 10=S Corp, 11=Foreign Company)
Federal Tax ID	The supplier's Employer Identification Number (for US businesses).	0	0		any
DUNS	The supplier's Data Universal Numbering System number.	0	0	string(255)	any
Tax Exempt Explanation	If the supplier is tax exempt, they need to provide an explanation.	0	0	string(255)	any
Income Type	The type of income for the supplier.	0	0	string(255)	any
Federal Reportable	Indicates if the supplier is required to report federal taxes.	0	0	boolean	any
International Tax ID	The supplier's tax ID (for non-US businesses).	0	0	string(255)	any
International Tax Classification	Non-US tax categories.	0	0	string(255)	1, 2, 3, 4, 5, 6, 7, 8, 9, or 10
(1=Active NFFE, 2=Passive NFFE, 3=Exempt beneficial owner, 4=Deemed compliant FFI, 5=Canadian Financial Institution, 6=Other Partner Jurisdiction Financial Institution, 7=Participating Foreign Financial Institution, 8=Non Participating Financial Institution, 9=Specified U.S. Person, 10=Not a Specified U.S. Person)
International Explanation	If the supplier is tax exempt, they need to provide an explanation.	0	0		any
Backend System Invoicing	The type of ERP that Coupa integrates with for invoices.	0	0	string(255)	1 or 2
(1=SAP, 2=Oracle)
Backend System Catalog	The type of ERP that Coupa integrates with for catalogs.	0	0	string(255)	1, 2, 3, 4, 5, 6, 7, 8, 9, or 10
(1= CatBase, 2=Elastic, 3=iPartner Product Suite, 4=Claritum, 5=Contalog, 6=CatalognTime, 7=Advizia, 8=Aravo, 9=MatrixCMX, 10=SigmaCommerce)
Payment Term	The supplier's default payment terms. Must match an exisiting payment term in Coupa. Use the payment term code.	0	0		any
Supplier Region	The supplier's geographic region.	0	0	string(255)	1, 2, 3, or 4
(1=AMER, 2=EMEA, 3=APAC, 4=Japan)
Govt Agency Interaction Indicator	Govt agency interaction indicator for the ERP.	0	0	boolean	any
Govt Agency Interaction	Text for the govt agency interaction indicator that's fed to the ERP.	0	0		any
Organization Type	Describes the type of organization for the supplier.	0	0	string(255)	1, 2, 3, 4, 5, or 6
(1=Corporation, 2=Foreign Corporation, 3=Individual, 4=Foreign Individual, 5=Partnership, 6=Foreign Partnership)
Bribery Policy Indicator	Bribery policy indicator for the ERP.	0	0	boolean	any
Bribery Policy Text	Text for the bribery policy indicator that's fed to the ERP.	0	0		any
Govt Allegation Indicator	Govt allegation indicator for the ERP.	0	0	boolean	any
Govt Allegation Text	Text for the govt allegation indicator that's fed to the ERP.	0	0	string(255)	any
Third Party Interaction Indicator	Third party interaction indiciator for the ERP.	0	0	boolean	any
Third Party Interaction Text	Text for the third party interaction indicator that's fed to the ERP.	0	0		any
Country of Operation	The country where the supplier is based.	0	0		any
Goods or Services Provided	A short description of the what the supplier provides.	0	0	string(255)	any
Pay Group	A list of different ways the supplier can be paid.	0	0	string(255)	1, 2, 3, 4, 5, 6, 7, 8, 9, or 10
(1=Direct Debit, 2=Standard, 3=Customer Refund, 4=Employee, 5=Intercompany, 6=Lease, 7=Partner Referral, 8=Rent, 9=Tax, 10=Util/Telecom)
Invoice Amount Limit	A preset limit for the maximum value of an invoice submitted by the supplier.	0	0		any
Hold Payment Indicator	Prevent the supplier from being automatically paid through the ERP.	0	0	boolean	any
Hold Payment Text	Text for the hold payment indicator that's fed to the ERP.	0	0		any
Separate Remit To	Enable if the remit different than the primary address.	0	0	boolean	any
Comment Source	Field indicating who made the comment.	0	0	string(255)	any
Comment	Field for the actual comment.	0	0		any
Exported	Indicates if the SIM record has exported to the ERP.	0	0		any
Last Exported Date and Time	Shows the last time the SIM record was exported to the ERP.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Created Date and Time	Shows when the SIM record was created.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Created-By id	Coupa's unique identifier for the user.	0	0		any
Created-By Lastname, Firstname	The full name of the created-by user.	0	0		any
Created-By email	The email address of the created-by user.	0	0		any
Updated Date and Time	Shows when the SIM record was last updated.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Updated-By id	Coupa's unique identifier for the user.	0	0		any
Updated-By Lastname, Firstname	The full name of the updated-by user.	0	0		any
Updated-By email	The email address of the updated-by user.	0	0		any
Logo file name	The name of the supplier logo file, including file extension.	0	0	string(255)	any
Logo content type	The type of image file used by the supplier logo.	0	0	string(255)	any
Logo file size	The file size of the supplier logo.	0	0	integer	any
Logo updated at	Shows the last time the supplier logo was updated.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Website	The address of the supplier's website.	0	0	string(255)	any
Allow cXML Invoicing	Indicates if the supplier is allowed to send invoices via cXML.	0	0	boolean	any
Hold Invoices for AP Review	Indicates if invoices from this supplier should be reviewed by AP being approved to pay. Also known as AP Hold.	0	0	boolean	any
Send Invoices to Approvals	Indicates if the supplier's invoices will always be sent to approval, regardless of invoice tolerance settings.	0	0	boolean	any
Allow Invoicing with no Backing Doc from Connect	Indicates if the supplier can create an invoice via the supplier portal without a purchase order.	0	0	boolean	any
Allow Invoicing with Unbacked Lines from Connect	Indicates if the supplier can create an invoice lines via the supplier portal without a purchase order.	0	0	boolean	any
Invoice Matching Level	Selects the supplier's matching level: none, 2-way, or 3-way.	0	0	string(255)	none, 2-way, 3-way
Shipping Term	The default shipping term for the supplier.	0	0
Tax Code	The default tax code for the supplier.	0	0		the 'code' value
Savings Percentage	The savings percentage for using the supplier.	0	0	decimal(8,2)	any
Allow Invoicing from Connect	Indicates if the supplier is allowed to create an invoice via the supplier portal.	0	0	boolean	any
Allow Choosing Billing Account in Invoicing	Indicates if the supplier can choose a billing account when creating an invoice.	0	0	boolean	any
Invoice Inbound Emails	This field is for the invoice inbox. Specify specific email address for the supplier.	0	0		any
Default Invoice Email	This field is useful when you've whitelisted addresses. Replies to any supplier email will go to this preferred email instead of the invoice email address.	0	0	string(255)	any
Inbound Invoice Email Domain	This field is for the invoice inbox. Specifiy an email domain for the supplier.	0	0	string(255)	any
Duplicate Exists	There's already a supplier record that has similar fields: name, display name, DUNS, etc.	0	0	boolean	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Supplier Number	Supplier Number	0	0		any
Supplier Information Address Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Specifies the header format for the row. Possible values include: Header, Address, Artifact, Attachment	0	0		Address
Supplier Information ID	Coupa's unique identifier for the SIM record associated with this address.	0	0	integer	any
Address ID	Coupa's unique identifier for this address record.	0	0	integer	any
Address Type	The type of address of this record.	0	0	string(255)	1, 2, or 3
(1=RTA, 2=User, 3=Primary)
Location Code	A free field for storing info about the location from the ERP.	0	0	string(255)	any
Address Name	A user-friendly name to identify this address.	0	0	string(255)	any
Street Address	The first address line.	0	0	string(255)	any
Street Address 2	The second address line.	0	0	string(255)	any
Postal Code	The postal code of the address.	0	0	string(255)	any
City	The city of the address.	0	0	string(255)	any
State or Region	The state or region of the address	0	0	string(255)	any
Country	The country of the address.	0	0	string(255)	any
PO Box	The post office box of the address.	0	0	string(255)	any
PO Box Postal Code	The post office box postal code.	0	0	string(255)	any
Account Type	The type of account for the supplier.	0	0	string(255)	any
Intermediary Bank Name	The name of the intermediary bank name.	0	0	string(255)	any
Bank Address	The address line for the bank.	0	0	string(255)	any
Bank City	The city line for the bank.	0	0	string(255)	any
Bank State or Region	The state or region of the bank.	0	0	string(255)	any
Bank Postal Code	The postal code of the bank.	0	0	string(255)	any
Bank Country	The country of the bank.	0	0		any
Bank Work Phone	The telephone number of the bank.	0	0	string(255)	any
Bank Fax Phone	The fax number of the bank.	0	0	string(255)	any
Bank Account Name	The name on the bank account.	0	0	string(255)	any
Bank Account Number	The bank account number.	0	0	string(4 to 17 characters)	numeric characters
International Bank Account Number	The international bank account number	0	0	string(4 to 17 characters)
Bank Routing Number	The bank routing number.	0	0	string(9)	numeric characters
IBAN Number	The bank's International Bank Account Number.	0	0	string(5 to 34 characters)	5 to 34 characters
Sort Code	The bank's Sort Code.	0	0	string(6)	numeric characters
SWIFT Code	The bank's SWIFT code.	0	0	string(8 or 11 characters)	8 or 11 characters
BSB Number	The bank's BSB number.	0	0	string(6)	numeric characters
BIC	The bank's Bank Identifier Code.	0	0	string(255)	any
BIC Routing Code	The bank's BIC Routing Code.	0	0	string(255)	any
Created Date and Time	The date and time that the address record was created.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Updated Date and Time	The date and time that the address record was last updated.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Payment Method	The method of payment accepted by the supplier.	0	0	string(255)	1, 2, 3, or 4 (1=Bank transfer, 2=Cash, 3=Credit Card, 4=Pcard)
Account Currency	Account Currency	0	0		any
Bank Name	Bank Name.	0	0	string(255)	any
custom-field-1	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-2	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-3	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-4	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-5	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-6	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-7	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-8	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-9	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-10	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-11	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-12	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-13	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-14	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-15	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-16	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-17	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-18	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-19	Custom fields only available when kind=RTA	0	0	string(255)	any
custom-field-20	Custom fields only available when kind=RTA	0	0	string(255)	any
Bank Code	Bank Code	0	0	string(255)	any
IFSC	IFSC	0	0	string(255)	any
Transit Number And Institution Number	Transit Number And Institution Number	0	0	string(255)	any
Supplier Information Artifact Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Specifies the header format for the row. Possible values include: Header, Address, Artifact, Attachment	0	0		Artifact
Supplier Information ID	Coupa's unique identifier for the SIM record associated with this attachment record.	0	0	integer	any
Attachment ID	Coupa's unique identifier for this attachment record.	0	0	integer	any
Attachment Type	The type of document that's attached to the SIM record.	0	0	string(255)	any
Attachment Meta Type	More detailed information about the type of document attached to the SIM record, based on the attachment type.	0	0	string(255)	any
Supplier ID	Coupa's unique identifier for the supplier associated with the SIM record.	0	0	string(255)	any
Effective Date	The date when the document first becomes effective.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Expiry Date	The latest date when the document is effective.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Description	A brief description of the document that's attached to the SIM record.	0	0	string(255)	any
Created Date and Time	Shows when the SIM record was created.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Created-By id	Coupa's unique identifier for the user.	0	0	integer(11)	any
Created-By Lastname, Firstname	The full name of the created-by user.	0	0	string(255)	any
Created-By email	The email address of the created-by user.	0	0	string(255)	any
Updated Date and Time	Shows when the SIM record was last updated.	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Updated-By id	Coupa's unique identifier for the user.	0	0	integer(11)	any
Updated-By Lastname, Firstname	The full name of the updated-by user.	0	0	string(255)	any
Updated-By email	The email address of the updated-by user.	0	0	string(255)	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Supplier Information Contract Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
RecordType	Specifies the header format for the row.	0	0		any
Supplier Information ID	Coupa's unique identifier for the related SIM record associated with this contact.	0	0	integer	any
Contact ID	Coupa's unique identifier for this contact record.	0	0	integer	any
Contact Type	The job role of the supplier contact.	1	0	string(255)	1, 2, 3, or 4
(1=Primary, 2=Sales, 3=PO Delivery, 4=Account Receivable)
Prefix	The name prefix of the supplier contact.	0	0	string(255)	any
Suffix	The name suffix of the supplier contact.	0	0	string(255)	any
Additional Name Field	Any additional names of the supplier contact.	0	0	string(255)	any
First Name	The first name of the supplier contact.	0	0	string(255)	any
Last Name	The last name of the supplier contact.	0	0	string(255)	any
Full Name	The full name of the supplier contact.	0	0	string(255)	any
Email	The email address of the supplier contact.	0	0	string(255)	any
Work Phone	The work phone number of the supplier contact.	0	0	string(255)	any
Mobile Phone	The mobile phone number of the supplier contact.	0	0	string(255)	any
Fax Phone	The fax number of the supplier contact.	0	0	string(255)	any
Notes	A short note about the supplier contact.	0	0	string(255)	any
Created Date and Time	Shows when the SIM record was created	0	0	datetime	YYYY-MM-DDTHH:MM:SS+HH:MM
Created-By id	Coupa's unique identifier for the user.	0	0		any
Created-By Lastname, Firstname	The full name of the created-by user.	0	0		any
Created-By email	The email address of the created-by user.	0	0		any
Updated Date and Time	Shows when the SIM record was last updated.	0	0	datetime	any
Updated-By id	Coupa's unique identifier for the user.	0	0		any
Updated-By Lastname, Firstname	The full name of the updated-by user.	0	0		any
Updated-By email	The email address of the updated-by user.	0	0		any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any

































































































































































































































































































































































































































































































































































































































































































































































































































# Sheet: Supplier Items
Position	Column Name	Description	Type	Required/Unique	Allowable Values
1.0	Name	Item's Name	string(255)	No/No	any
2.0	Description	Item's Description	text	No/No	any
3.0	UOM Code	Item's Unit Of Measure Code	string(6)	No/No	Must be active in Coupa
4.0	Purchasable	Flag if item is purchasable	boolean	No/No	Yes/No
5.0	Item Number	Item Number	string(255)	No/No	any
6.0	Image Url	Item's Image Url	string(255)	No/No	URL
7.0	Commodity	Item's Commodity Name	string(255)	No/No	any
8.0	Tags	Item's Tags	(string300)	No/No	30 characters per tag; maximum of 10 tags
9.0	Require Inspection?	Does the item require an Inspection?	boolean	No/No	Yes/No
10.0	Require Asset Tag?	Does the item require an Asset Tag?	boolean	No/No	Yes/No
11.0	Require RFID?	Does the item require an RFID tag?	boolean	No/No	Yes/No
12.0	Supplier	Supplier's Name	string(100)	No/No	any
13.0	Preferred	Is the item a preferred item?	boolean	No/No	Yes/No
14.0	Contract Number	Contract Number	string(50)	No/No	any
15.0	Price	Price for item	decimal(30,6)	No/No	Numerical
16.0	Currency	Currency Code for item	string(6)	No/No	ISO 4217 three letter currency code
17.0	Supplier Part Num	Supplier Part Number	string(255)	Yes/No	any
18.0	Lead Time	Lead Time for item	integer(11)	No/No	any
19.0	Manufacturer	Manufacturer Name	string(255)	No/No	any
20.0	Savings %	Captured Savings % for this item	decimal(8,2)	No/No	Numerical
21.0	Created At	Date document was created	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
22.0	Updated At	Date document was last updated	datetime	No/No	YYYY-MM-DDTHH:MM:SS+HH:MM
23.0	Created By (Email)	Email of user who created the record	string(255)	No/No	Must be in valid email format: user@example.com
24.0	Created By (Employee Number)	Employee Number of user who created the record	string(255)	No/No	any
25.0	Created By (Login)	Login of user who created the record	string(255)	No/No	any
26.0	Updated By (Email)	Email of user who last updated the record	string(255)	No/No	Must be in valid email format: user@example.com
27.0	Updated By (Employee Number)	Employee Number of user who last updated the record	string(255)	No/No	any
28.0	Updated By (Login)	Login of user who last updated the record	string(255)	No/No	any
29.0	Supplier Minimum Order Quantity	Supplier Minimum Order Quantity	decimal(30,6)	No/No	any
30.0	Supplier Order Increment	Supplier Order Increment	decimal(30,6)	No/No	any

# Sheet: Tagging
Tagging Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
id	ID	0	0	integer	any
tag-id	Tag ID	0	0	integer	any
taggable-id	Taggable ID	0	0	integer	any
description	Description	0	0	text	any
active	Active	0	0	boolean	any
Tag Columns
Column Name	Description	Req'd	Unique	Type	Allowable Values
id	ID	0	0	integer	any
name	Name	1	1	string(30)	any
description	Description	0	0	text	any
system-tag	System Tag	0	0	boolean	any

# Sheet: Tax Registration
Position	Column Name	Description	Type	Required/Unique	Allowable Values
1.0	Number	The registered tax number	string(47)	Yes/No	any
2.0	Country Code	The country code of the tax registration		No/No	any
3.0	Active	Determines if the tax registration is enabled or disabled	boolean	No/No	any
4.0	Local	Set to true if this tax number cannot be used for cross-border invoices	boolean	No/No	any
5.0	Owner ID	Coupa ID of the entity to which the tax registration belongs.	integer	No/No	any
6.0	Owner Type	The type of the owning entity. Examples are Address and SupplierRemitTo	string(255)	No/No	any
7.0	custom-field-1	Integration Custom Field 1		No/No	any
8.0	custom-field-2	Integration Custom Field 2		No/No	any
9.0	custom-field-3	Integration Custom Field 3		No/No	any
10.0	custom-field-4	Integration Custom Field 4		No/No	any
11.0	custom-field-5	Integration Custom Field 5		No/No	any
12.0	custom-field-6	Integration Custom Field 6		No/No	any
13.0	custom-field-7	Integration Custom Field 7		No/No	any
14.0	custom-field-8	Integration Custom Field 8		No/No	any
15.0	custom-field-9	Integration Custom Field 9		No/No	any
16.0	custom-field-10	Integration Custom Field 10		No/No	any

# Sheet: TCS Tax Line
Position	Column Name	Description	Type	Required/Unique	Allowable Values
1.0	type	Describes the type of row. Possible values are Header, Line, Line Split, Tax Line, or Payment.	--	No/No	Header, Line, Line Split, Tax Line, or Payment
2.0	invoice-id	The unique identifier Coupa assigns to the invoice.		No/No	any
3.0	invoice-number	The user-created invoice number.		No/No	any
4.0	tax-line-number	The line number of the corresponding of the tax line.	integer	No/No	any
5.0	tax-line-id	The unique identifier Coupa assigns to the tax line.	integer	No/No	any
6.0	amount	The amount of tax calculated on the line.	decimal(32,4)	No/No	any
7.0	rate	The tax rate indicated on the invoice line.	float	No/No	any
8.0	code	The tax rate code for the invoice line tax rate. Must match an existing tax rate code within Coupa.	tax rate code	No/No	Must exist in Coupa
9.0	base	Base indicates the base amount of the invoice or line item to which tax was applied	decimal(30,4)	No/No	any
10.0	type	TcsTaxLine	string(255)	No/No	any
11.0	custom-field-1	Integration Custom Field 1		No/No	any
12.0	custom-field-2	Integration Custom Field 2		No/No	any
13.0	custom-field-3	Integration Custom Field 3		No/No	any
14.0	custom-field-4	Integration Custom Field 4		No/No	any
15.0	custom-field-5	Integration Custom Field 5		No/No	any
16.0	custom-field-6	Integration Custom Field 6		No/No	any
17.0	custom-field-7	Integration Custom Field 7		No/No	any
18.0	custom-field-8	Integration Custom Field 8		No/No	any
19.0	custom-field-9	Integration Custom Field 9		No/No	any
20.0	custom-field-10	Integration Custom Field 10		No/No	any

# Sheet: Users
Column Name	Description	Req'd	Unique	Type	Allowable Values
Login	Login	1	1	string(255)	any
Status	Status	0	0	string(255)	any
Id	Id	0	0	integer	any
Purchasing License	Purchasing License	0	0	boolean	any
Expense License	Expense License	0	0	boolean	any
Analytics License	Analytics License	0	0	boolean	any
AI Classification License	AI Classification License	0	0	boolean	any
Spend Guard License	Spend Guard License	0	0	boolean	any
Authentication Method	Authentication Method	0	0	string(255)	any
Single Sign-on ID	Single Sign-on ID	0	0	string(255)	any
Email	Email	1	1	string(255)	Must be in valid email format: user@example.com
Firstname	Firstname	1	0	string(40)	any
Lastname	Lastname	1	0	string(40)	any
Employee Number	Employee Number	0	1	string(255)	any
Department	Department	0	0	string(255)	any
Phone Work	Phone Work	0	0	string(255)	any
Phone Mobile	Phone Mobile	0	0	string(255)	any
Approval Limit Name	Approval Limit Name	0	0	string(255)	any
Approval Limit Amount	Approval Limit Amount	0	0	integer	any
Approval Limit Currency	Approval Limit Currency	0	0	string	any
Self-Approval Limit Name	Self-Approval Limit Name	0	0	string	any
Self-Approval Limit Amount	Self-Approval Limit Amount	0	0	integer	any
Self-Approval Limit Currency	Self-Approval Limit Currency	0	0	string	any
Approver Login	Approver Login	0	0	string	any
Default Chart Of Accounts Name	Default Chart Of Accounts Name	0	0	string	any
Default Chart Of Accounts Code	Default Chart Of Accounts Code	0	0	string	any
Default Account Code Segment-1	Default Account Code Segment-1	0	0	string(100)	any
Default Account Code Segment-2	Default Account Code Segment-2	0	0	string(100)	any
Default Account Code Segment-3	Default Account Code Segment-3	0	0	string(100)	any
Default Account Code Segment-4	Default Account Code Segment-4	0	0	string(100)	any
Default Account Code Segment-5	Default Account Code Segment-5	0	0	string(100)	any
Default Account Code Segment-6	Default Account Code Segment-6	0	0	string(100)	any
Default Account Code Segment-7	Default Account Code Segment-7	0	0	string(100)	any
Default Account Code Segment-8	Default Account Code Segment-8	0	0	string(100)	any
Default Account Code Segment-9	Default Account Code Segment-9	0	0	string(100)	any
Default Account Code Segment-10	Default Account Code Segment-10	0	0	string(100)	any
Default Account Code Segment-11	Default Account Code Segment-11	0	0	string(100)	any
Default Account Code Segment-12	Default Account Code Segment-12	0	0	string(100)	any
Default Account Code Segment-13	Default Account Code Segment-13	0	0	string(100)	any
Default Account Code Segment-14	Default Account Code Segment-14	0	0	string(100)	any
Default Account Code Segment-15	Default Account Code Segment-15	0	0	string(100)	any
Default Account Code Segment-16	Default Account Code Segment-16	0	0	string(100)	any
Default Account Code Segment-17	Default Account Code Segment-17	0	0	string(100)	any
Default Account Code Segment-18	Default Account Code Segment-18	0	0	string(100)	any
Default Account Code Segment-19	Default Account Code Segment-19	0	0	string(100)	any
Default Account Code Segment-20	Default Account Code Segment-20	0	0	string(100)	any
User Role Names	User Role Names	0	0	string	any
Default Currency	Default Currency	0	0	string	any
Default Locale	Default Locale	0	0	string(10)	See List of Default Locales: https://success.coupa.com/Integrate/Technical_Documentation/CSV/Export/Users#List_of_Default_Locales
Pcard Name	Pcard Name	0	0	string	any
Content Groups	Content Groups	0	0	string	any
Default Address Attention	Default Address Attention	0	0	string(255)	any
Default Address Street1	Default Address Street1	0	0	string(100)	any
Default Address Street2	Default Address Street2	0	0	string(100)	any
Default Address City	Default Address City	0	0	string(50)	any
Default Address State	Default Address State	0	0	string(50)	any
Default Address Postal Code	Default Address Postal Code	0	0	string(50)	any
Default Address Country Code	Default Address Country Code	0	0	string	any
Receive Coupa Emails	Receive Coupa Emails	0	0	boolean	any
Limited Data Table Viewing	Limited Data Table Viewing	0	0	boolean	any
Account Security Type	Account Security Type	0	0	integer	any
Account Group Names	Account Group Names	0	0	string	any
Approval Group Names	Approval Group Names	0	0	string	any
custom-field-1	Integration Custom Field 1	0	0	string(255)	any
custom-field-2	Integration Custom Field 2	0	0	string(255)	any
custom-field-3	Integration Custom Field 3	0	0	string(255)	any
custom-field-4	Integration Custom Field 4	0	0	string(255)	any
custom-field-5	Integration Custom Field 5	0	0	string(255)	any
custom-field-6	Integration Custom Field 6	0	0	string(255)	any
custom-field-7	Integration Custom Field 7	0	0	string(255)	any
custom-field-8	Integration Custom Field 8	0	0	string(255)	any
custom-field-9	Integration Custom Field 9	0	0	string(255)	any
custom-field-10	Integration Custom Field 10	0	0	string(255)	any
Country Of Residence Code	Country of Residence Code	0	0		any
Seniority Level
Business Function
Contingent Workforce License	Contingent Workforce License	0	0	boolean	any
Default Chart Of Accounts CCW Flag	Default Chart Of Accounts CCW Flag	0	0		any
Default Account Code Segment-1 Category	Default Account Code Segment-1 Category	0	0		any
Default Account Code Segment-2 Category	Default Account Code Segment-2 Category	0	0		any
Default Account Code Segment-3 Category	Default Account Code Segment-3 Category	0	0		any
Default Account Code Segment-4 Category	Default Account Code Segment-4 Category	0	0		any
Default Account Code Segment-5 Category	Default Account Code Segment-5 Category	0	0		any
Default Account Code Segment-6 Category	Default Account Code Segment-6 Category	0	0		any
Default Account Code Segment-7 Category	Default Account Code Segment-7 Category	0	0		any
Default Account Code Segment-8 Category	Default Account Code Segment-8 Category	0	0		any
Default Account Code Segment-9 Category	Default Account Code Segment-9 Category	0	0		any
Default Account Code Segment-10 Category	Default Account Code Segment-10 Category	0	0		any
Default Account Code Segment-11 Category	Default Account Code Segment-11 Category	0	0		any
Default Account Code Segment-12 Category	Default Account Code Segment-12 Category	0	0		any
Default Account Code Segment-13 Category	Default Account Code Segment-13 Category	0	0		any
Default Account Code Segment-14 Category	Default Account Code Segment-14 Category	0	0		any
Default Account Code Segment-15 Category	Default Account Code Segment-15 Category	0	0		any
Default Account Code Segment-16 Category	Default Account Code Segment-16 Category	0	0		any
Default Account Code Segment-17 Category	Default Account Code Segment-17 Category	0	0		any
Default Account Code Segment-18 Category	Default Account Code Segment-18 Category	0	0		any
Default Account Code Segment-19 Category	Default Account Code Segment-19 Category	0	0		any
Default Account Code Segment-20 Category	Default Account Code Segment-20 Category	0	0		any
Risk Assess User	Risk Assess License	0	0	boolean	any
Supply Chain License	Supply Chain License	0	0	boolean	any
Avatar Thumbnail URL	Avatar Thumbnail URL	0	0	UTL	any
```
