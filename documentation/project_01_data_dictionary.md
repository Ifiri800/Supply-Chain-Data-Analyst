# Project 01: Data Dictionary

## 1. Products

| Column | Description | Data Type |
|---|---|---|
| product_id | Unique product identifier | String |
| product_name | Product name | String |
| category | Product category | String |
| unit_cost | Cost of purchasing one unit | Float |
| selling_price | Selling price per unit | Float |
| supplier_id | Primary supplier identifier | String |
| warehouse_id | Primary warehouse identifier | String |

## 2. Sales

| Column | Description | Data Type |
|---|---|---|
| order_id | Unique customer order identifier | String |
| order_date | Date of customer order | Date |
| product_id | Product identifier | String |
| warehouse_id | Warehouse fulfilling the order | String |
| quantity_ordered | Quantity requested by customer | Integer |
| quantity_fulfilled | Quantity actually supplied | Integer |
| unit_price | Selling price per unit | Float |

## 3. Inventory

| Column | Description | Data Type |
|---|---|---|
| date | Inventory observation date | Date |
| product_id | Product identifier | String |
| warehouse_id | Warehouse identifier | String |
| opening_stock | Stock available at beginning of day | Integer |
| receipts | Units received during the day | Integer |
| demand | Units demanded during the day | Integer |
| closing_stock | Stock available at end of day | Integer |
| stockout_units | Unfulfilled demand caused by stock shortage | Integer |

## 4. Purchase Orders

| Column | Description | Data Type |
|---|---|---|
| po_id | Purchase order identifier | String |
| product_id | Product identifier | String |
| supplier_id | Supplier identifier | String |
| order_date | Date purchase order was placed | Date |
| expected_date | Expected delivery date | Date |
| actual_date | Actual delivery date | Date |
| quantity | Quantity ordered | Integer |
| unit_cost | Purchase cost per unit | Float |

## 5. Suppliers

| Column | Description | Data Type |
|---|---|---|
| supplier_id | Unique supplier identifier | String |
| supplier_name | Supplier name | String |
| category | Supplier category | String |
| payment_terms | Supplier payment terms | String |