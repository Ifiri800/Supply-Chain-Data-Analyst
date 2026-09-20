# Project Supply Chain Inventory & Demand Planning Analytics

## Client Case Study: Nexora Industrial Supply & Services Ltd.

> **Case-study note:** Nexora Industrial Supply & Services Ltd. (NISSL) is a fictional company created for portfolio purposes. The dataset is synthetic and designed to demonstrate supply-chain analytics methods.

---

## 1. Business Context

Nexora Industrial Supply & Services Ltd. manages the procurement, inventory, and distribution of industrial materials and equipment across multiple warehouses.

Management identified a need to improve the alignment between customer demand, inventory availability, supplier performance, and replenishment planning.

The objective of this project was to transform operational supply-chain data into actionable insights for inventory planning, procurement management, and demand forecasting.

---

## 2. Business Problem

The analysis focused on five interconnected supply-chain challenges:

* Unfulfilled customer demand and stockout exposure
* Inventory concentration and replenishment requirements
* Demand variability across products
* Supplier lead-time and delivery-performance variability
* Limited forward-looking demand planning

These issues can increase working-capital requirements, create service-level problems, and make procurement decisions less predictable.

---

## 3. Project Objectives

The project was designed to:

1. Validate the quality and consistency of supply-chain data.
2. Analyze demand, fulfillment, and stockout patterns.
3. Evaluate inventory value and efficiency.
4. Develop ABC inventory classification.
5. Calculate inventory turnover, safety stock, reorder points, and EOQ.
6. Evaluate supplier delivery and lead-time performance.
7. Develop and compare demand forecasting models.
8. Translate analytical findings into management recommendations.

---

## 4. Data Scope

The analysis used five interconnected datasets:

| Dataset         | Records | Purpose                                            |
| --------------- | ------: | -------------------------------------------------- |
| Suppliers       |       5 | Supplier and commercial information                |
| Products        |      20 | Product, category, cost, and warehouse information |
| Inventory       |   7,300 | Daily inventory movements and stockouts            |
| Sales           |   7,300 | Customer demand and fulfillment                    |
| Purchase Orders |     200 | Procurement and supplier delivery performance      |

The dataset represents one year of operational activity.

---

## 5. Key Supply-Chain KPIs

| KPI                          |  Result |
| ---------------------------- | ------: |
| Total units ordered          | 281,903 |
| Total units fulfilled        | 263,663 |
| Unfulfilled demand           |  18,240 |
| Overall fill rate            |  93.53% |
| Unfulfilled demand rate      |   6.47% |
| Stockout records             |     146 |
| Top 3 product demand share   |  40.10% |
| Top 10 product demand share  |  78.39% |
| Largest supplier spend share |  57.06% |

These indicators provide the baseline for evaluating customer service, inventory concentration, procurement exposure, and replenishment requirements.

---

## 6. Demand & Fulfillment Findings

Demand was concentrated across a relatively small number of products.

The top three products accounted for **40.10%** of total ordered demand, while the top ten accounted for **78.39%**.

Packaging Box recorded the highest demand at **47,865 units** and also had the largest unfulfilled quantity at **3,977 units**.

The overall fill rate was **93.53%**, meaning that **18,240 units** of ordered demand were not fulfilled.

Monthly performance also varied considerably. November recorded the lowest monthly fill rate at **88.90%**, while May recorded the highest at **97.37%**.

### Management implication

High-demand products require closer monitoring because relatively small availability problems can create significant customer-service impacts.

---

## 7. Inventory Analysis

Inventory analysis examined:

* Inventory value
* ABC classification
* Inventory turnover
* Days inventory outstanding
* Demand variability
* Safety stock
* Reorder point
* Economic Order Quantity
* Inventory risk indicators

### Inventory value

Equipment represented approximately **33.56%** of total inventory value, making it the largest inventory-value category.

Electric Motor had the highest individual inventory value at approximately **₦6.50 billion**.

### ABC analysis

| Class | Products | Consumption Value Share |
| ----- | -------: | ----------------------: |
| A     |       11 |                  77.62% |
| B     |        5 |                  15.54% |
| C     |        4 |                   6.84% |

The analysis demonstrates why inventory management should consider both **demand volume and monetary value**.

For example, Electric Motor was classified as an A item because of its high monetary value despite relatively low unit demand, while Packaging Box was classified as C because of its low unit cost despite having the highest demand.

### Management implication

A-items require tighter inventory controls, monitoring, and replenishment planning because inventory decisions involving these products have a greater financial impact.

---

## 8. Replenishment Analysis

Safety stock and reorder-point calculations were developed using historical demand variability and supplier lead-time information.

The model used a 95% service-level assumption with a Z-value of 1.645.

The resulting reorder-point analysis identified products whose latest inventory position was below the modeled reorder point.

These were treated as **replenishment-monitoring signals**, rather than automatic purchase recommendations.

The largest modeled inventory gaps included:

* Cleaning Chemical
* Work Gloves
* Packaging Box
* Lubricant
* Plastic Container
* Filter Cartridge
* Water Treatment Chemical
* Bearing

The analysis also calculated EOQ to estimate economically appropriate order quantities under the stated assumptions.

### Management implication

Replenishment decisions should combine:

**Forecast demand + inventory position + safety stock + reorder point + supplier lead time + open purchase orders**

rather than relying on a single inventory metric.

---

## 9. Supplier Performance

Supplier performance was evaluated using:

* Procurement spend
* Purchase-order volume
* Average lead time
* Lead-time variability
* On-time delivery
* Late delivery
* Stockout exposure

Supplier average lead times ranged from approximately **6.9 to 21.0 days**.

On-time delivery performance ranged from approximately **53.8% to 84.1%**.

One supplier represented approximately **57.1% of total procurement spend**, creating significant procurement concentration.

### Management implication

Supplier management should consider both service performance and financial exposure.

Potential actions include:

* Supplier performance monitoring
* Lead-time tracking
* Supplier development
* Procurement diversification
* Safety-stock adjustments for long-lead-time items
* Regular supplier scorecards

Supplier-associated stockouts were treated as **exposure indicators**, not proof of supplier causation.

---

## 10. Demand Forecasting

Historical monthly demand was analyzed using:

* 3-month moving average
* Weighted moving average
* Simple exponential smoothing
* ARIMA

The models were evaluated using:

* MAE
* RMSE
* MAPE

The **3-month moving average** produced the lowest error on the three-month test period:

| Model                        |      MAE |     RMSE |   MAPE |
| ---------------------------- | -------: | -------: | -----: |
| 3-Month Moving Average       | 3,111.00 | 3,463.96 | 12.25% |
| ARIMA(1,1,1)                 | 3,248.90 | 3,586.74 | 12.81% |
| Weighted Moving Average      | 3,259.00 | 3,597.46 | 12.85% |
| Simple Exponential Smoothing | 3,284.67 | 3,620.73 | 12.95% |

Because the test set contained only three observations, the result should be interpreted as a portfolio case-study finding rather than evidence that the moving-average method will always outperform other models.

The selected model produced an average monthly forecast of approximately **24,708 units** for the following three-month planning horizon.

---

## 11. Inventory Coverage

The latest inventory position contained approximately **2,841 units** across the portfolio.

Against the forecast monthly demand, this represented approximately **0.11 months of aggregate inventory coverage**, or about **3.5 days**.

This is a high-level planning indicator because products have different demand rates, unit costs, and lead times.

At product level, several products had very low or zero latest closing inventory.

For example:

* Electric Motor: 0 units
* Bearing: 0 units
* Cleaning Chemical: 83 units
* Electrical Cable: 100 units
* Water Treatment Chemical: 60 units

These observations should trigger replenishment review and confirmation against open purchase orders and planned receipts.

---

## 12. Analytical Framework

The project combined descriptive, diagnostic, and predictive analytics.

### Descriptive Analytics

* Demand analysis
* Fulfillment analysis
* Inventory value
* Supplier performance
* Warehouse analysis

### Diagnostic Analytics

* Stockout analysis
* Demand variability
* ABC classification
* Inventory turnover
* Supplier lead-time variability
* Replenishment gaps

### Predictive Analytics

* Moving-average forecasting
* Weighted moving average
* Exponential smoothing
* ARIMA forecasting

### Decision-Support Analytics

* Safety stock
* Reorder point
* EOQ
* Inventory risk screening
* Forecast-based replenishment planning

---

## 13. Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **SciPy**
* **Matplotlib**
* **Seaborn**
* **Statsmodels**
* **Scikit-learn**
* **Jupyter Notebook**
* **Excel / OpenPyXL**
* **Git & GitHub**

The portfolio is designed for future extension into SQL, Power BI/Tableau dashboards, machine-learning forecasting, and optimization models.

---

## 14. Management Recommendations

Based on the analysis, management should:

1. Prioritize high-demand products for closer availability monitoring.
2. Apply differentiated inventory policies using ABC classification.
3. Monitor products approaching or below modeled reorder points.
4. Incorporate supplier lead time into replenishment planning.
5. Review supplier concentration where procurement spend is highly concentrated.
6. Track supplier delivery performance through regular scorecards.
7. Combine forecasts with current inventory, open purchase orders, and expected receipts.
8. Monitor forecast accuracy continuously and update models as new demand data becomes available.
9. Develop product-level and warehouse-level forecasting models.
10. Integrate inventory, procurement, supplier, and demand data into a management dashboard.

---

## 15. Limitations & Assumptions

This portfolio case study uses synthetic data.

Important assumptions include:

* The dataset represents a controlled business scenario rather than a real company's operational records.
* The EOQ model assumes a fixed ordering cost and annual holding-cost rate.
* The safety-stock model primarily reflects demand variability and average lead time.
* Lead-time variability and demand/lead-time covariance were not fully modeled in the simplified safety-stock calculation.
* Forecast evaluation used a relatively short three-month test period.
* Supplier-associated stockouts do not establish supplier causation.
* Replenishment gaps are monitoring signals and should be validated against open POs, planned receipts, demand changes, and operational constraints.

---

## 16. Project Deliverables

The project includes:

* Data quality assessment
* Exploratory data analysis
* Inventory optimization analysis
* Supplier performance analysis
* Demand forecasting analysis
* Replenishment analysis
* KPI visualizations
* Business recommendations
* Reproducible Python/Jupyter workflows

### Notebook sequence

```text
01_data_quality_check.ipynb
02_exploratory_data_analysis.ipynb
03_inventory_analysis.ipynb
04_supplier_analysis.ipynb
05_Demand_Forecasting.ipynb
```

---

## 17. Portfolio Skills Demonstrated

This project demonstrates practical capability in:

**Supply Chain Analytics**

* Inventory management
* Demand analysis
* Replenishment planning
* Procurement analytics
* Supplier performance
* Stockout analysis

**Inventory Optimization**

* ABC analysis
* Safety stock
* Reorder point
* EOQ
* Inventory turnover
* Inventory coverage

**Data Analytics**

* Data cleaning
* Data validation
* Exploratory data analysis
* KPI development
* Statistical analysis
* Forecast evaluation

**Forecasting**

* Moving averages
* Exponential smoothing
* ARIMA
* MAE
* RMSE
* MAPE

**Technical**

* Python
* Pandas
* NumPy
* Statistical modeling
* Data visualization
* Jupyter
* Git/GitHub

---

## 18. Project Outcome

The analysis provides an end-to-end framework for connecting **customer demand, inventory availability, supplier performance, and demand forecasting**.

The project demonstrates how supply-chain data can be transformed from operational records into measurable KPIs, analytical models, and management decision-support insights.

The next stage of the portfolio will extend this framework into **SQL analytics, interactive dashboards, advanced forecasting, and supply-chain optimization models**.
