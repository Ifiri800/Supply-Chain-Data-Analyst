import pandas as pd
import numpy as np
from pathlib import Path

# Reproducibility
np.random.seed(42)

# Project directories
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = BASE_DIR / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

print("Supply-chain data generator initialized.")
print(f"Raw data directory: {RAW_DATA_DIR}")


# -----------------------------
# SUPPLIERS
# -----------------------------

suppliers = pd.DataFrame({
    "supplier_id": ["SUP001", "SUP002", "SUP003", "SUP004", "SUP005"],
    "supplier_name": [
        "Alpha Industrial Supplies",
        "Beta Manufacturing Ltd",
        "Delta Distribution Co",
        "Prime Materials Nigeria",
        "Global Industrial Partners"
    ],
    "category": [
        "Packaging",
        "Raw Materials",
        "Components",
        "Chemicals",
        "Industrial Equipment"
    ],
    "payment_terms": [
        "Net 30",
        "Net 45",
        "Net 30",
        "Net 60",
        "Net 45"
    ]
})

suppliers.to_csv(
    RAW_DATA_DIR / "suppliers.csv",
    index=False
)

print(f"Suppliers created: {len(suppliers)}")

# -----------------------------
# PRODUCTS
# -----------------------------

products = pd.DataFrame({
    "product_id": [f"PROD{i:03d}" for i in range(1, 21)],

    "product_name": [
        "Industrial Pump",
        "Electric Motor",
        "Steel Pipe",
        "PVC Pipe",
        "Hydraulic Hose",
        "Control Valve",
        "Pressure Gauge",
        "Bearing",
        "Lubricant",
        "Safety Helmet",
        "Work Gloves",
        "Safety Boots",
        "Packaging Box",
        "Plastic Container",
        "Cleaning Chemical",
        "Water Treatment Chemical",
        "Filter Cartridge",
        "Electrical Cable",
        "Switch Gear",
        "Industrial Fan"
    ],

    "category": [
        "Equipment",
        "Equipment",
        "Piping",
        "Piping",
        "Components",
        "Components",
        "Instrumentation",
        "Components",
        "Chemicals",
        "Safety",
        "Safety",
        "Safety",
        "Packaging",
        "Packaging",
        "Chemicals",
        "Chemicals",
        "Components",
        "Electrical",
        "Electrical",
        "Equipment"
    ],

    "unit_cost": [
        185000, 320000, 95000, 42000, 28000,
        125000, 35000, 18000, 12000, 8500,
        3500, 22000, 1800, 2500, 15000,
        24000, 9500, 28000, 145000, 75000
    ],

    "selling_price": [
        240000, 410000, 125000, 58000, 40000,
        165000, 48000, 25000, 17000, 12000,
        5000, 30000, 2500, 3500, 21000,
        34000, 13500, 38000, 190000, 100000
    ],

    "supplier_id": [
        "SUP005", "SUP005", "SUP002", "SUP002", "SUP003",
        "SUP003", "SUP003", "SUP003", "SUP004", "SUP001",
        "SUP001", "SUP001", "SUP001", "SUP001", "SUP004",
        "SUP004", "SUP003", "SUP003", "SUP005", "SUP005"
    ],

    "warehouse_id": [
        "WH001", "WH001", "WH002", "WH002", "WH003",
        "WH003", "WH003", "WH003", "WH004", "WH001",
        "WH001", "WH001", "WH004", "WH004", "WH004",
        "WH004", "WH003", "WH003", "WH001", "WH001"
    ]
})

products.to_csv(
    RAW_DATA_DIR / "products.csv",
    index=False
)

print(f"Products created: {len(products)}")

# -----------------------------
# INVENTORY
# -----------------------------

# Generate one year of daily inventory data
dates = pd.date_range(
    start="2025-01-01",
    end="2025-12-31",
    freq="D"
)

inventory_records = []

# Base daily demand for each product
base_demand = {
    "PROD001": 8,
    "PROD002": 6,
    "PROD003": 15,
    "PROD004": 20,
    "PROD005": 25,
    "PROD006": 10,
    "PROD007": 18,
    "PROD008": 30,
    "PROD009": 35,
    "PROD010": 45,
    "PROD011": 70,
    "PROD012": 25,
    "PROD013": 100,
    "PROD014": 80,
    "PROD015": 30,
    "PROD016": 20,
    "PROD017": 40,
    "PROD018": 35,
    "PROD019": 8,
    "PROD020": 12
}

# Starting inventory for each product
current_stock = {
    product_id: np.random.randint(100, 500)
    for product_id in products["product_id"]
}

for date in dates:

    for _, product in products.iterrows():

        product_id = product["product_id"]
        warehouse_id = product["warehouse_id"]

        # Base demand
        demand = base_demand[product_id]

        # Add random demand variation
        daily_demand = max(
            0,
            int(np.random.normal(demand, demand * 0.25))
        )

        # Occasional higher demand
        if np.random.random() < 0.05:
            daily_demand = int(daily_demand * 1.5)

        # Replenishment
        receipts = 0

        if current_stock[product_id] < demand * 3:
            receipts = int(np.random.uniform(
                demand * 5,
                demand * 10
            ))

        opening_stock = current_stock[product_id]

        # Calculate available inventory
        available_stock = opening_stock + receipts

        # Occasional demand surge
        # This creates realistic stockout events
        if np.random.random() < 0.02:
            daily_demand = int(
                available_stock * np.random.uniform(1.2, 2.0)
            )

        # Calculate actual demand fulfilled
        fulfilled_demand = min(
            available_stock,
            daily_demand
        )

        # Calculate stockout
        stockout_units = max(
            0,
            daily_demand - available_stock
        )

        # Calculate closing stock
        closing_stock = max(
            0,
            available_stock - daily_demand
        )

        inventory_records.append({
            "date": date,
            "product_id": product_id,
            "warehouse_id": warehouse_id,
            "opening_stock": opening_stock,
            "receipts": receipts,
            "demand": daily_demand,
            "closing_stock": closing_stock,
            "stockout_units": stockout_units
        })

        # Update inventory for next day
        current_stock[product_id] = closing_stock

inventory = pd.DataFrame(inventory_records)

inventory.to_csv(
    RAW_DATA_DIR / "inventory.csv",
    index=False
)

print(f"Inventory records created: {len(inventory):,}")


# -----------------------------
# SALES
# -----------------------------

# Create sales transactions from inventory demand
sales_records = []

order_counter = 1

for _, row in inventory.iterrows():

    demand = int(row["demand"])
    stockout_units = int(row["stockout_units"])

    # Quantity ordered represents customer demand
    quantity_ordered = demand

    # Quantity fulfilled is demand minus unavailable inventory
    quantity_fulfilled = max(
        0,
        quantity_ordered - stockout_units
    )

    # Small variation in selling price
    product_id = row["product_id"]

    product_price = products.loc[
        products["product_id"] == product_id,
        "selling_price"
    ].iloc[0]

    unit_price = round(
        product_price * np.random.uniform(0.97, 1.03),
        2
    )

    sales_records.append({
        "order_id": f"ORD{order_counter:06d}",
        "order_date": row["date"],
        "product_id": product_id,
        "warehouse_id": row["warehouse_id"],
        "quantity_ordered": quantity_ordered,
        "quantity_fulfilled": quantity_fulfilled,
        "unit_price": unit_price
    })

    order_counter += 1

sales = pd.DataFrame(sales_records)

sales.to_csv(
    RAW_DATA_DIR / "sales.csv",
    index=False
)

print(f"Sales records created: {len(sales):,}")

# -----------------------------
# PURCHASE ORDERS
# -----------------------------

purchase_order_records = []

po_counter = 1

# Base lead times by supplier
supplier_lead_times = {
    "SUP001": 7,
    "SUP002": 14,
    "SUP003": 10,
    "SUP004": 21,
    "SUP005": 18
}

# Generate approximately 200 purchase orders
po_dates = pd.date_range(
    start="2025-01-05",
    end="2025-12-20",
    periods=200
)

for po_date in po_dates:

    # Select a random product
    product = products.sample(
        n=1,
        random_state=po_counter
    ).iloc[0]

    product_id = product["product_id"]
    supplier_id = product["supplier_id"]
    unit_cost = product["unit_cost"]

    # Supplier's normal lead time
    base_lead_time = supplier_lead_times[supplier_id]

    # Expected delivery
    expected_lead_time = max(
        3,
        int(np.random.normal(
            base_lead_time,
            2
        ))
    )

    expected_date = (
        po_date +
        pd.Timedelta(expected_lead_time, unit='D')
    )

    # Actual delivery has additional variability
    actual_delay = np.random.choice(
        [0, 0, 0, 1, 2, 3, 5, 7],
        p=[0.35, 0.20, 0.15, 0.10, 0.08, 0.05, 0.05, 0.02]
    )

    actual_date = (
        expected_date +
        pd.Timedelta(int(actual_delay), unit='D')
    )

    # Occasional early delivery
    if np.random.random() < 0.10:
        early_days = np.random.randint(1, 4)
        actual_date = expected_date - pd.Timedelta(
            early_days,
            unit="D"
        )

    # Purchase quantity
    quantity = int(
        np.random.uniform(100, 1000)
    )

    purchase_order_records.append({
        "po_id": f"PO{po_counter:05d}",
        "product_id": product_id,
        "supplier_id": supplier_id,
        "order_date": po_date,
        "expected_date": expected_date,
        "actual_date": actual_date,
        "quantity": quantity,
        "unit_cost": unit_cost
    })

    po_counter += 1

purchase_orders = pd.DataFrame(
    purchase_order_records
)

purchase_orders.to_csv(
    RAW_DATA_DIR / "purchase_orders.csv",
    index=False
)

print(
    f"Purchase orders created: "
    f"{len(purchase_orders):,}"
)


