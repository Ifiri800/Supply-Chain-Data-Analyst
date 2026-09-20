# Project 1 — Supply Chain Inventory & Demand Planning Analytics

## Client Case Study: Nexora Industrial Supply & Services Ltd.

> **Note:** Nexora Industrial Supply & Services Ltd. (NISSL) is a fictitious company created for this portfolio project. The dataset is synthetic and is intended to demonstrate supply-chain analytics methods and business decision-making.

---

## 1. Company Context

### About Nexora Industrial Supply & Services Ltd.

Nexora Industrial Supply & Services Ltd. (NISSL) is a fictitious industrial supply and distribution company serving customers that require a broad range of operational materials and industrial products.

Its portfolio includes:

* Industrial equipment
* Mechanical components
* Electrical materials
* Piping materials
* Chemicals
* Safety equipment
* Packaging materials
* Instrumentation products

NISSL operates **four warehouses** and works with **five suppliers** to meet customer demand.

As the company expands its operations, management has identified challenges involving inventory availability, customer fulfillment, supplier reliability, procurement concentration, and demand planning.

The management team has commissioned a supply-chain analytics project to provide evidence-based insights that can support inventory, procurement, and demand-planning decisions.

---

# 2. Business Problem

NISSL is experiencing a gap between **customer demand, inventory availability, supplier performance, and replenishment planning**.

During the analysis period, customers ordered **281,903 units**, but only **263,663 units were fulfilled**, leaving **18,240 units of unfulfilled demand** and an overall fill rate of **93.53%**.

At the same time, the company faces several interconnected supply-chain challenges:

### Inventory availability

The company recorded **146 stockout records**, indicating recurring inventory availability issues.

### Demand concentration

Demand is concentrated among a relatively small number of products:

* Top 3 products: **40.10% of total demand**
* Top 5 products: **53.70%**
* Top 10 products: **78.39%**

A disruption affecting high-volume products can therefore have a disproportionate effect on customer fulfillment.

### Inventory investment

High-value products create substantial inventory investment. Equipment represents approximately **33.6% of total inventory value**, creating a need to balance product availability with working-capital efficiency.

### Demand variability

Demand variability differs substantially across products. Products with high demand variability require more careful safety-stock and replenishment planning than products with relatively stable demand.

### Supplier performance

Supplier performance varies considerably:

* On-time delivery: approximately **53.8%–84.1%**
* Average lead time: approximately **6.9–21.0 days**

Longer or less predictable supplier lead times increase replenishment uncertainty.

### Procurement concentration

One supplier accounts for approximately **57.1% of procurement spend**, creating a significant concentration that management should monitor as part of procurement-risk planning.

### Forecasting and replenishment

Historical demand fluctuations make simple demand assumptions insufficient for planning future inventory requirements. NISSL needs a structured approach that connects:

**Demand Forecast → Safety Stock → Reorder Point → Supplier Lead Time → Replenishment Decision**

---

# 3. Business Impact

If these issues are not effectively managed, NISSL may experience:

* Lost or delayed customer orders
* Lower service levels
* Increased stockout frequency
* Emergency procurement
* Higher logistics and expedited-delivery costs
* Excess inventory
* Increased working-capital requirements
* Greater exposure to supplier disruptions
* Inefficient replenishment decisions
* Poor alignment between procurement and actual demand

The analytical objective is therefore not simply to measure inventory performance, but to help management understand **where supply-chain performance is deteriorating, why it may be occurring, and where intervention should be prioritized.**

---

# 4. Project Objectives

The project aims to:

### Objective 1 — Establish Data Reliability

Validate the quality, completeness, consistency, and integrity of the supply-chain datasets before conducting business analysis.

### Objective 2 — Understand Demand and Fulfillment

Analyze demand patterns across products, categories, warehouses, and time periods and measure customer fulfillment performance.

### Objective 3 — Evaluate Inventory Performance

Assess inventory value, turnover, days of inventory, demand variability, stockout exposure, and inventory concentration.

### Objective 4 — Optimize Replenishment

Apply inventory-management techniques including:

* ABC analysis
* Safety stock
* Reorder point
* Economic Order Quantity
* Inventory-position analysis

to support more structured replenishment decisions.

### Objective 5 — Evaluate Supplier Performance

Measure supplier spend, delivery reliability, lead time, lead-time variability, and stockout exposure.

### Objective 6 — Develop Demand Forecasts

Compare statistical forecasting techniques and evaluate their ability to predict future demand.

### Objective 7 — Translate Analytics into Decisions

Convert analytical results into practical recommendations for inventory management, procurement, supplier management, and demand planning.

---

# 5. Business Questions

The analysis is designed to answer five groups of management questions.

## A. Demand & Customer Fulfillment

1. What products generate the highest customer demand?
2. Which product categories contribute most to total demand?
3. How concentrated is demand across the portfolio?
4. What is the company's overall fill rate?
5. Which products have the highest unfulfilled demand?
6. Which warehouses experience the greatest demand and fulfillment pressure?
7. Which months show unusually high demand or weaker fulfillment?

## B. Inventory Management

8. Which products and categories represent the greatest inventory investment?
9. Which products have the highest and lowest inventory turnover?
10. Which products exhibit the greatest demand variability?
11. Which products require greater safety-stock protection?
12. What are the modeled reorder points for each product?
13. Which products require replenishment monitoring?
14. What order quantities are suggested by the EOQ model?
15. Which inventory items represent the greatest combined demand, value, and replenishment risk?

## C. Supplier & Procurement

16. Which suppliers account for the largest procurement spend?
17. How concentrated is procurement spending?
18. Which suppliers have the longest lead times?
19. Which suppliers have the greatest lead-time variability?
20. Which suppliers have the lowest on-time delivery performance?
21. What level of stockout exposure is associated with each supplier's products?
22. Where should procurement teams increase supplier-performance monitoring?

## D. Demand Forecasting

23. What patterns are visible in historical demand?
24. How accurately can future demand be predicted?
25. How do moving average, weighted moving average, exponential smoothing, and ARIMA compare?
26. Which model produces the lowest forecast error on the selected test period?
27. What demand should the company plan for over the next three months?
28. How can forecasts be incorporated into inventory and replenishment decisions?

## E. Management Decision Support

29. Which products require greater replenishment attention?
30. Which supply-chain areas require closer monitoring?
31. Where are the major procurement and supplier dependencies?
32. How can demand, inventory, procurement, and supplier data be integrated into a management dashboard?
33. What analytical framework can NISSL use to continuously monitor supply-chain performance?

---

# 6. Data & Scope

The project uses a synthetic operational dataset representing NISSL's supply-chain activities.

| Dataset         | Records | Purpose                           |
| --------------- | ------: | --------------------------------- |
| Suppliers       |       5 | Supplier and procurement analysis |
| Products        |      20 | Product master data               |
| Inventory       |   7,300 | Inventory and stockout analysis   |
| Sales           |   7,300 | Demand and fulfillment analysis   |
| Purchase Orders |     200 | Supplier and lead-time analysis   |

### Analytical Scope

The analysis covers:

* **20 products**
* **8 product categories**
* **4 warehouses**
* **5 suppliers**
* **200 purchase orders**
* **12 months of demand/inventory activity**

---

# 7. Analytical Framework

The project follows an end-to-end supply-chain analytics workflow:

```text
                    BUSINESS PROBLEM
                          │
                          ▼
                   DATA VALIDATION
                          │
                          ▼
               EXPLORATORY DATA ANALYSIS
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
       DEMAND         INVENTORY       SUPPLIERS
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                 DEMAND FORECASTING
                          │
                          ▼
              REPLENISHMENT PLANNING
                          │
                          ▼
                 BUSINESS INSIGHTS
                          │
                          ▼
                  RECOMMENDATIONS
```

---

# 8. Analytical Methods

## Data Quality & Validation

* Missing-value analysis
* Duplicate detection
* Primary-key validation
* Inventory reconciliation
* Quantity validation
* Date validation
* Lead-time validation
* Stockout consistency checks

## Demand Analytics

* Descriptive statistics
* Product demand analysis
* Category analysis
* Warehouse analysis
* Monthly demand trends
* Demand concentration
* Fill rate
* Unfulfilled demand

## Inventory Analytics

* Inventory valuation
* ABC classification
* Inventory turnover
* Days Inventory
* Demand variability
* Coefficient of variation
* Safety stock
* Reorder point
* EOQ
* Inventory position
* Replenishment monitoring
* Inventory risk screening

## Supplier Analytics

* Procurement spend
* Spend concentration
* Average lead time
* Lead-time variability
* On-time delivery
* Late delivery
* Supplier stockout exposure
* Supplier risk indicators

## Forecasting

* Three-month moving average
* Weighted moving average
* Simple exponential smoothing
* ARIMA
* MAE
* RMSE
* MAPE
* Chronological train/test validation

---

# 9. Key Performance Indicators

| KPI                     |            Result |
| ----------------------- | ----------------: |
| Total ordered demand    | **281,903 units** |
| Total fulfilled demand  | **263,663 units** |
| Unfulfilled demand      |  **18,240 units** |
| Overall fill rate       |        **93.53%** |
| Unfulfilled demand rate |         **6.47%** |
| Stockout records        |           **146** |
| Products                |            **20** |
| Suppliers               |             **5** |
| Warehouses              |             **4** |
| Purchase orders         |           **200** |

---

# 10. Key Analytical Findings

## Demand Concentration

Demand is highly concentrated:

* Top 3 products = **40.10%**
* Top 5 products = **53.70%**
* Top 10 products = **78.39%**

This indicates that inventory availability for high-volume products deserves particular management attention.

## Customer Fulfillment

The overall fill rate is **93.53%**, with **18,240 units** of demand unfulfilled.

Packaging Box recorded the highest unfulfilled quantity at **3,977 units**.

Electric Motor recorded the lowest product-level fill rate at **88.61%**.

## Inventory

Equipment represents approximately **33.6% of inventory value**.

ABC analysis classified the portfolio as:

| Class | Products | Consumption Value Share |
| ----- | -------: | ----------------------: |
| A     |       11 |                  77.62% |
| B     |        5 |                  15.54% |
| C     |        4 |                   6.84% |

The analysis demonstrates that high physical demand does not necessarily mean high financial importance.

## Supplier Performance

Procurement spend is concentrated with SUP005 at approximately **57.1%**.

Supplier on-time delivery varies from approximately **53.8% to 84.1%**, while average lead times range from approximately **6.9 to 21.0 days**.

## Forecasting

The three-month moving average produced the lowest error on the selected test period:

* **MAE:** 3,111 units
* **RMSE:** 3,464 units
* **MAPE:** 12.25%

The selected model forecasts approximately **24,708 units per month** for January–March 2026.

---

# 11. Management Recommendations

Based on the analysis, NISSL should consider:

### Inventory

* Prioritize high-demand and high-value products.
* Establish differentiated inventory policies using ABC classification.
* Monitor products with low inventory coverage.
* Incorporate demand variability into safety-stock decisions.
* Review products whose inventory positions fall below modeled reorder points.

### Procurement

* Monitor procurement concentration.
* Evaluate supplier dependency and alternative sourcing options where appropriate.
* Incorporate supplier lead time into replenishment planning.

### Supplier Management

* Establish supplier-performance monitoring.
* Track on-time delivery and lead-time variability.
* Investigate recurring late deliveries.
* Monitor supplier-associated stockout exposure while recognizing that association does not establish causation.

### Demand Planning

* Use forecasting as an input to replenishment planning.
* Continuously monitor forecast accuracy.
* Progress from portfolio-level forecasting toward product- and warehouse-level forecasts.
* Incorporate seasonality and demand uncertainty as additional historical data becomes available.

### Decision Support

Develop a supply-chain management dashboard combining:

**Demand + Inventory + Suppliers + Procurement + Forecasts + Fulfillment**

---

# 12. Limitations & Assumptions

This project uses a synthetic dataset and is intended to demonstrate analytical capability rather than represent an actual company's operational performance.

Key assumptions include:

* 95% service-level assumption for safety-stock calculations.
* ₦10,000 assumed ordering cost for EOQ.
* 20% annual holding-rate assumption for EOQ.
* Simplified safety-stock methodology.
* Limited forecasting history and a three-month test period.
* Open purchase-order commitments are not fully incorporated into the inventory-gap assessment.
* Negative inventory gaps are treated as **replenishment-monitoring signals**, not definitive evidence of understocking.
* Supplier-associated stockouts do not establish supplier causation.

---

# 13. Project Deliverables

The project is organized into five analytical notebooks:

| Notebook                             | Analysis                                  |
| ------------------------------------ | ----------------------------------------- |
| `01_data_quality_check.ipynb`        | Data validation and reconciliation        |
| `02_exploratory_data_analysis.ipynb` | Demand, fulfillment and stockout analysis |
| `03_inventory_analysis.ipynb`        | Inventory optimization and replenishment  |
| `04_supplier_analysis.ipynb`         | Supplier and procurement analytics        |
| `05_Demand_Forecasting.ipynb`        | Forecasting and demand planning           |

---

# 14. Tools & Technologies

### Programming & Data Analysis

Python · Pandas · NumPy · SciPy · Statsmodels · Scikit-learn

### Visualization

Matplotlib · Seaborn · Plotly

### Supply Chain Analytics

ABC Analysis · EOQ · Safety Stock · Reorder Point · Inventory Turnover · Demand Variability · Fill Rate · Stockout Analysis · Supplier Performance · Demand Forecasting

### Development & Version Control

VS Code · Jupyter Notebook · Git · GitHub

### Planned Extensions

SQL · Power BI · Tableau · Machine Learning · Optimization

---

# 15. Project Outcome

This project demonstrates an end-to-end approach to **supply-chain data analytics**, moving from raw operational data through validation, exploratory analysis, inventory modeling, supplier evaluation, forecasting, and management recommendations.

The primary analytical objective is to help management balance four competing priorities:

**Customer Service**
↕
**Inventory Availability**
↕
**Working Capital**
↕
**Supply Risk**

The project demonstrates how a Supply Chain Data Analyst can transform operational data into **measurable KPIs, analytical insights, forecasting outputs, and decision-support recommendations**.
