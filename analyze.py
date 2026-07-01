import pandas as pd
import json

df = pd.read_csv("/home/claude/project/sales_data.csv", parse_dates=["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)
df["Year"] = df["Order_Date"].dt.year

# ---- KPIs ----
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
avg_order_value = total_sales / total_orders
profit_margin = total_profit / total_sales * 100

# ---- Monthly trend ----
monthly = df.groupby("Month").agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order_ID","count")).reset_index()

# YoY growth
y2024 = df[df.Year==2024]["Sales"].sum()
y2025 = df[df.Year==2025]["Sales"].sum()
yoy_growth = (y2025 - y2024) / y2024 * 100

# ---- Top products ----
top_products = df.groupby("Product").agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Qty=("Quantity","sum")).reset_index().sort_values("Sales", ascending=False)

# ---- Category performance ----
cat_perf = df.groupby("Category").agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order_ID","count")).reset_index()
cat_perf["Margin_%"] = cat_perf["Profit"]/cat_perf["Sales"]*100
cat_perf = cat_perf.sort_values("Sales", ascending=False)

# ---- Region performance ----
region_perf = df.groupby("Region").agg(Sales=("Sales","sum"), Profit=("Profit","sum"), Orders=("Order_ID","count")).reset_index()
region_perf["Margin_%"] = region_perf["Profit"]/region_perf["Sales"]*100
region_perf = region_perf.sort_values("Sales", ascending=False)

# ---- Segment performance ----
seg_perf = df.groupby("Segment").agg(Sales=("Sales","sum"), Profit=("Profit","sum")).reset_index().sort_values("Sales", ascending=False)

# ---- Ship mode ----
ship_perf = df.groupby("Ship_Mode").agg(Sales=("Sales","sum"), Orders=("Order_ID","count")).reset_index()

# ---- Region x Category cross for heatmap ----
cross = df.pivot_table(index="Region", columns="Category", values="Sales", aggfunc="sum").fillna(0)

print("=== KPIs ===")
print(f"Total Sales: {total_sales:,.0f}")
print(f"Total Profit: {total_profit:,.0f}")
print(f"Total Orders: {total_orders:,}")
print(f"Avg Order Value: {avg_order_value:,.0f}")
print(f"Overall Profit Margin: {profit_margin:.1f}%")
print(f"YoY Sales Growth (2024->2025): {yoy_growth:.1f}%")

print("\n=== Top 10 Products by Sales ===")
print(top_products.head(10).to_string(index=False))

print("\n=== Category Performance ===")
print(cat_perf.to_string(index=False))

print("\n=== Region Performance ===")
print(region_perf.to_string(index=False))

print("\n=== Segment Performance ===")
print(seg_perf.to_string(index=False))

print("\n=== Ship Mode ===")
print(ship_perf.to_string(index=False))

print("\n=== Region x Category cross ===")
print(cross.to_string())

# Save all outputs for dashboard building
export = {
    "kpis": {
        "total_sales": round(total_sales,2),
        "total_profit": round(total_profit,2),
        "total_orders": int(total_orders),
        "avg_order_value": round(avg_order_value,2),
        "profit_margin": round(profit_margin,2),
        "yoy_growth": round(yoy_growth,2)
    },
    "monthly": monthly.to_dict(orient="records"),
    "top_products": top_products.to_dict(orient="records"),
    "categories": cat_perf.to_dict(orient="records"),
    "regions": region_perf.to_dict(orient="records"),
    "segments": seg_perf.to_dict(orient="records"),
    "ship_modes": ship_perf.to_dict(orient="records"),
    "cross": cross.reset_index().to_dict(orient="records")
}
with open("/home/claude/project/dashboard_data.json","w") as f:
    json.dump(export, f, indent=2)
print("\nSaved dashboard_data.json")
