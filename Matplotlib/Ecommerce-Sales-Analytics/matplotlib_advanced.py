import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset (keep the Excel file in this script's working directory)
data = pd.read_excel("Ecommerce_Sales_Analytics_Cleaned.xlsx")


# Category-wise Sales

category_sales = data.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("Category-wise Sales:")
print(category_sales)

bars = plt.bar(category_sales.index, category_sales.values, color="purple", edgecolor="black")

plt.title("Category-wise Sales Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Product Category")
plt.ylabel("Total Sales (₹)")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in category_sales.values], padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Payment Mode-wise Sales

payment_sales = data.groupby("Payment_Mode")["Sales"].sum().sort_values(ascending=False)

print("Payment Mode-wise Sales:")
print(payment_sales)

bars = plt.bar(payment_sales.index, payment_sales.values, color="teal", edgecolor="black")

plt.title("Payment Mode-wise Sales Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Payment Mode")
plt.ylabel("Total Sales (₹)")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in payment_sales.values], padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Unit Price vs Sales

print("Unit Price vs Sales:")
print(data[["Unit_Price", "Sales"]].describe())

plt.scatter(data["Unit_Price"], data["Sales"], color="royalblue", alpha=0.5)

plt.title("Unit Price vs Sales Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Unit Price (₹)")
plt.ylabel("Sales (₹)")
plt.grid(linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Profit Distribution

print("Profit Distribution:")
print(data["Profit"].describe())

plt.hist(data["Profit"], bins=30, color="darkorange", edgecolor="black", alpha=0.8)

plt.title("Profit Distribution Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Profit (₹)")
plt.ylabel("Number of Orders")
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Monthly Sales Trend

data["Order_Date"] = pd.to_datetime(data["Order_Date"])

monthly_sales = data.groupby(
    data["Order_Date"].dt.to_period("M")
)["Sales"].sum()

print("Monthly Sales Trend:")
print(monthly_sales)

plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o", linewidth=2.5, color="royalblue")

plt.title("Monthly Sales Trend Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.grid(linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Monthly Sales vs Profit

monthly_performance = data.groupby(
    data["Order_Date"].dt.to_period("M")
)[["Sales", "Profit"]].sum()

print("Monthly Sales vs Profit:")
print(monthly_performance)

plt.plot(monthly_performance.index.astype(str), monthly_performance["Sales"], marker="o", linewidth=2, label="Sales")
plt.plot(monthly_performance.index.astype(str), monthly_performance["Profit"], marker="s", linewidth=2, label="Profit")

plt.title("Monthly Sales vs Profit Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Top 10 Products by Sales

top_products = data.groupby("Product")["Sales"].sum().nlargest(10).sort_values()

print("Top 10 Products by Sales:")
print(top_products.sort_values(ascending=False))

bars = plt.barh(top_products.index, top_products.values, color="seagreen", edgecolor="black")

plt.title("Top 10 Products by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Total Sales (₹)")
plt.ylabel("Product")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in top_products.values], padding=3)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Category-wise Profit

category_profit = data.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print("Category-wise Profit:")
print(category_profit)

bars = plt.bar(category_profit.index, category_profit.values, color="darkgreen", edgecolor="black")

plt.title("Category-wise Profit Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Product Category")
plt.ylabel("Total Profit (₹)")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in category_profit.values], padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Category-wise Sales vs Profit

category_comparison = data.groupby("Category")[["Sales", "Profit"]].sum()

print("Category-wise Sales vs Profit:")
print(category_comparison)

ax = category_comparison.plot(kind="bar", figsize=(10, 6), color=["royalblue", "darkorange"], edgecolor="black")

ax.set_title("Category-wise Sales vs Profit Analysis", fontsize=16, fontweight="bold")
ax.set_xlabel("Product Category")
ax.set_ylabel("Amount (₹)")
ax.legend(["Sales", "Profit"])
ax.grid(axis="y", linestyle="--", alpha=0.3)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()


# Category-wise Profit Margin

category_margin = (
    data.groupby("Category")["Profit"].sum()
    / data.groupby("Category")["Sales"].sum()
) * 100

category_margin = category_margin.sort_values(ascending=False)

print("Category-wise Profit Margin:")
print(category_margin.round(2))

bars = plt.bar(category_margin.index, category_margin.values, color="mediumseagreen", edgecolor="black")

plt.title("Category-wise Profit Margin Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Product Category")
plt.ylabel("Profit Margin (%)")
plt.bar_label(bars, labels=[f"{v:.2f}%" for v in category_margin.values], padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Top 10 Cities by Sales

top_cities = data.groupby("City")["Sales"].sum().nlargest(10).sort_values()

print("Top 10 Cities by Sales:")
print(top_cities.sort_values(ascending=False))

bars = plt.barh(top_cities.index, top_cities.values, color="slateblue", edgecolor="black")

plt.title("Top 10 Cities by Sales", fontsize=16, fontweight="bold")
plt.xlabel("Total Sales (₹)")
plt.ylabel("City")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in top_cities.values], padding=3)
plt.grid(axis="x", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Sales Channel-wise Sales

channel_sales = data.groupby("Sales_Channel")["Sales"].sum().sort_values(ascending=False)

print("Sales Channel-wise Sales:")
print(channel_sales)

bars = plt.bar(channel_sales.index, channel_sales.values, color="cornflowerblue", edgecolor="black")

plt.title("Sales Channel-wise Sales Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Sales Channel")
plt.ylabel("Total Sales (₹)")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in channel_sales.values], padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Customer Segment-wise Sales

segment_sales = data.groupby("Customer_Segment")["Sales"].sum().sort_values(ascending=False)

print("Customer Segment-wise Sales:")
print(segment_sales)

bars = plt.bar(segment_sales.index, segment_sales.values, color="coral", edgecolor="black")

plt.title("Customer Segment-wise Sales Analysis", fontsize=16, fontweight="bold")
plt.xlabel("Customer Segment")
plt.ylabel("Total Sales (₹)")
plt.bar_label(bars, labels=[f"₹{v/100000:.2f}L" for v in segment_sales.values], padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()


# Order Status Distribution

order_status = data["Order_Status"].value_counts()

print("Order Status Distribution:")
print(order_status)

bars = plt.bar(order_status.index, order_status.values, color="mediumpurple", edgecolor="black")

plt.title("Order Status Distribution", fontsize=16, fontweight="bold")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.bar_label(bars, padding=3)
plt.xticks(rotation=15)
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()
