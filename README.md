# Supply-Chain-Data-Analyst
End-to-end supply chain data analysis projects using Python, SQL, Excel, and Power BI, covering inventory optimization, demand planning, procurement, logistics, forecasting, and supply chain performance KPIs.
# Supply Chain Data Analysis

A portfolio of **data-driven supply chain analysis projects** focused on using analytics to improve inventory management, demand planning, procurement, logistics, and overall supply chain performance.

This repository demonstrates practical application of **Python, SQL, Excel, and data visualization** to solve supply chain problems and support data-driven decision-making.

---

## 📌 Objectives

The main objectives of this portfolio are to:

* Analyze supply chain performance using real-world and simulated datasets.
* Identify inventory inefficiencies and stockout risks.
* Support demand planning and forecasting.
* Analyze procurement and supplier performance.
* Optimize inventory levels and replenishment decisions.
* Measure logistics and fulfillment performance.
* Build reusable analytical models and Python functions.
* Transform raw supply chain data into actionable insights.
* Develop dashboards and visualizations for decision-making.

---

## 🧰 Tools & Technologies

| Tool                 | Application                                      |
| -------------------- | ------------------------------------------------ |
| **Python**           | Data cleaning, analysis, modeling and automation |
| **Pandas**           | Data manipulation and analysis                   |
| **NumPy**            | Numerical analysis                               |
| **Matplotlib**       | Data visualization                               |
| **Seaborn**          | Exploratory data analysis                        |
| **SQL**              | Data extraction, transformation and analysis     |
| **Excel**            | Supply chain calculations and analysis           |
| **Power BI**         | Interactive dashboards and reporting             |
| **Jupyter Notebook** | Analysis and documentation                       |
| **VS Code**          | Development environment                          |
| **Git & GitHub**     | Version control and portfolio management         |

---

## 📊 Supply Chain Analysis Areas

### 1. Inventory Analysis

Projects will examine:

* Economic Order Quantity (EOQ)
* Safety Stock
* Reorder Point (ROP)
* Reorder Quantity
* ABC Analysis
* Inventory Turnover
* Days Inventory Outstanding
* Stockout Analysis
* Excess and Obsolete Inventory
* Service Level
* Fill Rate
* Inventory Carrying Cost
* Lead-Time Analysis

### 2. Demand Planning & Forecasting

Analysis may include:

* Historical demand analysis
* Demand variability
* Moving averages
* Weighted moving averages
* Exponential smoothing
* Demand forecasting
* Forecast accuracy
* Forecast bias
* Mean Absolute Error (MAE)
* Mean Absolute Percentage Error (MAPE)
* Root Mean Squared Error (RMSE)

### 3. Procurement Analytics

Analysis of:

* Supplier performance
* Purchase orders
* Supplier lead time
* Purchase price variance
* Procurement cycle time
* On-time delivery
* Supplier quality
* Supplier reliability
* Spend analysis
* Procurement trends

### 4. Logistics & Distribution

Analysis of:

* Order fulfillment
* On-time delivery
* In-full delivery
* OTIF
* Transportation performance
* Delivery lead time
* Warehouse performance
* Shipment volumes
* Distribution efficiency
* Logistics cost

### 5. Supply Chain KPIs

Key performance indicators include:

* Inventory Turnover
* Fill Rate
* Service Level
* Stockout Rate
* OTIF
* On-Time Delivery
* Order Fulfillment Rate
* Forecast Accuracy
* Forecast Bias
* Supplier Lead Time
* Purchase Price Variance
* Carrying Cost
* Days of Inventory
* Perfect Order Rate
---

## 📈 Example Projects

### Inventory Optimization

Analyze SKU-level inventory data to determine:

* ABC classification
* EOQ
* Safety stock
* Reorder point
* Inventory turnover
* Stockout risk
* Recommended replenishment strategy

### Demand Planning

Analyze historical demand to:

* Identify demand patterns
* Calculate demand variability
* Build forecasts
* Measure forecast accuracy
* Identify forecast bias
* Support inventory planning

### Supplier Performance

Evaluate suppliers based on:

* On-time delivery
* Lead time
* Quality performance
* Order fulfillment
* Purchase price
* Reliability

### Logistics Performance

Analyze delivery data to determine:

* On-time delivery rate
* OTIF
* Average delivery lead time
* Order fulfillment rate
* Transportation performance
* Distribution bottlenecks

---

## 🔬 Analytical Methods

The portfolio will apply practical supply chain models such as:

### Economic Order Quantity

$$
EOQ = \sqrt{\frac{2DS}{H}}
$$

Where:

* **D** = Annual demand
* **S** = Ordering cost per order
* **H** = Annual holding cost per unit

### Reorder Point

$$
ROP = (Average\ Demand \times Lead\ Time) + Safety\ Stock
$$

### Inventory Turnover

$$
Inventory\ Turnover =
\frac{Cost\ of\ Goods\ Sold}{Average\ Inventory}
$$

### Fill Rate

$$
Fill\ Rate =
\frac{Units\ Supplied}{Units\ Ordered} \times 100
$$

### On-Time Delivery

$$
OTD =
\frac{Orders\ Delivered\ On\ Time}
{Total\ Orders} \times 100
$$

---

## 📊 Analysis Workflow

Each project generally follows this workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
KPI Calculation
   ↓
Supply Chain Modeling
   ↓
Visualization
   ↓
Insights
   ↓
Recommendations

---

## 🐍 Python Approach

Python will be used to develop reusable analytical functions rather than repeating calculations manually.

Example:

```python
def calculate_inventory_turnover(cogs, average_inventory):
    return cogs / average_inventory
```

Reusable functions will be developed for metrics such as:

* EOQ
* Safety Stock
* Reorder Point
* Inventory Turnover
* Fill Rate
* Stockout Rate
* Service Level
* Forecast Accuracy
* OTIF
* Lead Time

---

## 🗄️ SQL Analysis

SQL projects will focus on extracting and transforming supply chain data from relational databases.

Example analytical questions:

```sql
-- Which products have the highest inventory value?

SELECT
    product_id,
    SUM(quantity * unit_cost) AS inventory_value
FROM inventory
GROUP BY product_id
ORDER BY inventory_value DESC;
```

Other SQL analysis will include:

* SKU performance
* Supplier performance
* Purchase orders
* Inventory movements
* Stockouts
* Customer orders
* Delivery performance
* Monthly trends

---

## 📊 Dashboards

Tableau dashboards will be developed to communicate supply chain performance to decision-makers.

Potential dashboard pages include:

**Executive Overview**

* Total inventory value
* Inventory turnover
* Service level
* Fill rate
* OTIF
* Stockout rate

**Inventory**

* ABC analysis
* Inventory by SKU
* Slow-moving inventory
* Excess inventory
* Reorder alerts

**Procurement**

* Supplier performance
* Spend
* Lead time
* Purchase price variance

**Logistics**

* Delivery performance
* OTIF
* Transportation trends
* Order fulfillment

---

## 💡 Business Questions

The projects will focus on questions such as:

1. Which products contribute most to inventory value?
2. Which SKUs are at risk of stockout?
3. Which products are overstocked?
4. What is the optimal reorder quantity?
5. How much safety stock is required?
6. Which suppliers consistently deliver late?
7. What is the average supplier lead time?
8. How accurate is the demand forecast?
9. What factors are driving inventory growth?
10. Where are the major supply chain bottlenecks?
11. How can service levels be improved?
12. How can inventory carrying costs be reduced?

---

## 🎯 Portfolio Goal

This repository is being developed as a practical **Supply Chain Data Analytics portfolio** demonstrating the ability to:

> **Collect → Clean → Analyze → Model → Visualize → Interpret → Recommend**

---

## 🚀 Future Development

Planned additions include:

* Advanced demand forecasting
* Machine learning for demand prediction
* Supplier risk scoring
* Inventory optimization
* ABC-XYZ analysis
* Network optimization
* Predictive stockout modeling
* Scenario analysis
* Automated reporting
* Interactive Power BI dashboards
* SQL-based supply chain data warehouse projects

## 📜 License

This repository is intended for educational, portfolio, and professional development purposes.
