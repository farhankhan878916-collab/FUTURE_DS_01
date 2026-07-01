import pandas as pd
import numpy as np

np.random.seed(42)

# ---- Setup dimensions ----
regions = ["North", "South", "East", "West"]
category_products = {
    "Furniture": ["Office Chair", "Executive Desk", "Bookshelf", "Filing Cabinet", "Sofa Set", "Study Table"],
    "Technology": ["Laptop", "Wireless Mouse", "Monitor 24in", "Bluetooth Speaker", "Printer", "Smartphone", "Tablet"],
    "Office Supplies": ["Notebook Pack", "Ballpoint Pens", "Sticky Notes", "Stapler", "Desk Organizer", "Whiteboard"],
    "Home Appliances": ["Air Fryer", "Mixer Grinder", "Electric Kettle", "Room Heater", "Vacuum Cleaner"]
}
segments = ["Consumer", "Corporate", "Small Business"]
ship_modes = ["Standard", "Express", "Same Day"]

base_price = {
    "Office Chair": 4200, "Executive Desk": 9800, "Bookshelf": 3200, "Filing Cabinet": 5400,
    "Sofa Set": 21000, "Study Table": 3600,
    "Laptop": 48000, "Wireless Mouse": 650, "Monitor 24in": 9200, "Bluetooth Speaker": 1800,
    "Printer": 7600, "Smartphone": 22000, "Tablet": 15500,
    "Notebook Pack": 220, "Ballpoint Pens": 90, "Sticky Notes": 60, "Stapler": 180,
    "Desk Organizer": 450, "Whiteboard": 1600,
    "Air Fryer": 6200, "Mixer Grinder": 3400, "Electric Kettle": 1400, "Room Heater": 2600,
    "Vacuum Cleaner": 8800
}
margin = {  # base profit margin per category
    "Furniture": 0.18, "Technology": 0.14, "Office Supplies": 0.32, "Home Appliances": 0.20
}

prod_to_cat = {p: c for c, plist in category_products.items() for p in plist}

# ---- Date range: 24 months ----
dates = pd.date_range("2024-01-01", "2025-12-31", freq="D")

rows = []
order_id_counter = 1000

for d in dates:
    # seasonality: more orders in Oct-Dec (festive/holiday), dip in Feb
    month = d.month
    season_factor = 1.0
    if month in [10, 11, 12]:
        season_factor = 1.6
    elif month in [1, 2]:
        season_factor = 0.75
    elif month in [6, 7]:
        season_factor = 1.15

    # slight year-over-year growth
    year_factor = 1.0 if d.year == 2024 else 1.22

    n_orders = np.random.poisson(6 * season_factor * year_factor)
    for _ in range(n_orders):
        product = np.random.choice(list(prod_to_cat.keys()))
        category = prod_to_cat[product]
        region = np.random.choice(regions, p=[0.28, 0.24, 0.26, 0.22])
        segment = np.random.choice(segments, p=[0.5, 0.32, 0.18])
        ship_mode = np.random.choice(ship_modes, p=[0.6, 0.3, 0.1])
        qty = np.random.choice([1, 1, 1, 2, 2, 3, 4], p=[0.35,0.2,0.15,0.15,0.08,0.05,0.02])
        unit_price = base_price[product] * np.random.uniform(0.92, 1.1)
        discount = np.random.choice([0, 0.05, 0.1, 0.15, 0.2], p=[0.45, 0.2, 0.2, 0.1, 0.05])
        sales = round(unit_price * qty * (1 - discount), 2)
        m = margin[category] + np.random.uniform(-0.05, 0.05)
        profit = round(sales * m, 2)

        rows.append({
            "Order_ID": f"ORD-{order_id_counter}",
            "Order_Date": d.strftime("%Y-%m-%d"),
            "Region": region,
            "Segment": segment,
            "Category": category,
            "Product": product,
            "Quantity": qty,
            "Unit_Price": round(unit_price, 2),
            "Discount": discount,
            "Sales": sales,
            "Profit": profit,
            "Ship_Mode": ship_mode
        })
        order_id_counter += 1

df = pd.DataFrame(rows)
df.to_csv("/home/claude/project/sales_data.csv", index=False)
print(df.shape)
print(df.head())
print(df["Order_Date"].min(), df["Order_Date"].max())
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
