# 📊 Business Sales Performance Analytics
**Future Interns — Data Science & Analytics Task 1 (2026)**

An end-to-end sales analytics project: data cleaning, KPI analysis, trend/category/region performance, an interactive client-ready dashboard, and a formal analysis report with business recommendations.

---

## 🧩 Problem Statement
A retail business (**Meridian Retail Group** — simulated, anonymized data representing a realistic multi-category e-commerce/retail operation) needed to understand:
- Which products generate the most revenue
- How sales change over time (seasonality, growth)
- Which categories/regions are most profitable
- Where the business should focus to grow faster

## 🗂️ Dataset
- **File:** [`Sales_Data.xlsx`](./Sales_Data.xlsx) / [`sales_data.csv`](./sales_data.csv)
- **Size:** 5,610 transactions | Jan 2024 – Dec 2025 (24 months)
- **Fields:** Order ID, Order Date, Region, Segment, Category, Product, Quantity, Unit Price, Discount, Sales, Profit, Ship Mode
- Simulated data built to mirror a real multi-category retail business (Furniture, Technology, Office Supplies, Home Appliances) across 4 regions and 3 customer segments, with realistic seasonality (festive-season spike) and year-over-year growth baked in.

## 🛠️ Tools Used
- **Python (pandas)** — data generation, cleaning, and aggregation
- **HTML / CSS / JavaScript (Chart.js)** — interactive dashboard
- **Microsoft Word (docx)** — client-ready analysis report

## 📈 What Was Analyzed
- Monthly revenue & profit trend, YoY growth
- Top-selling products by revenue, profit, and units sold
- Category performance (revenue vs. profit margin)
- Regional performance (revenue, profit, margin)
- Customer segment mix (Consumer / Corporate / Small Business)
- Fulfilment mix (Standard / Express / Same Day)
- Region × Category revenue heatmap

## 🔑 Key Insights
1. Revenue grew **~9% year-over-year**, with a strong seasonal spike every **Oct–Dec** (~60% above the Jan–Feb baseline).
2. **Technology** drives 58% of revenue but has the thinnest margin (14%); **Office Supplies** is under 2% of revenue but the most profitable category (32% margin).
3. A single product — **Laptop** — generates ~27% of total company revenue, a notable concentration risk.
4. **North & East** regions contribute 55% of sales; **West** underperforms despite similar order volume.
5. **60% of orders** ship Standard, indicating room to test premium shipping upsells.

## ✅ Recommendations
- Cross-sell high-margin categories (Office Supplies, Home Appliances) alongside Technology purchases.
- Build inventory & marketing spend ahead of the Q4 seasonal peak; extend light promotions into the slow Jan–Feb period.
- Bundle the Laptop with accessories to reduce single-SKU dependency and raise attach-rate revenue.
- Audit pricing, marketing, and delivery speed in the West region to close the revenue gap.
- Test a paid Express-shipping upgrade to shift fulfilment mix and improve margins.

## 📁 Repository Contents
| File | Description |
|---|---|
| `sales_data.csv` / `Sales_Data.xlsx` | Cleaned raw dataset |
| `dashboard.html` | Interactive client-ready sales dashboard |
| `Sales_Performance_Report.docx` | Full analysis report with insights & recommendations |
| `generate_data.py` | Script used to simulate the sales dataset |
| `analyze.py` | Python script for KPI, trend, category, region, and segment analysis |

## 🖥️ View the Dashboard
Open `dashboard.html` in any browser — no installation needed. It includes:
- KPI summary cards (revenue, profit, orders, AOV, top category)
- Monthly revenue & profit trend chart
- Top-selling products ranked list
- Category and region breakdowns
- Region × Category revenue heatmap
- Fulfilment mix chart
- Insights & recommendations panel

## 🎓 About This Task
Completed as part of the **Future Interns – Data Science & Analytics Task 1 (2026)**: *Business Sales Performance Analytics.*
[Task details](https://futureinterns.com/author/sujanshetty263gmail-com/) | [Future Interns on LinkedIn](https://www.linkedin.com/company/future-interns/)
