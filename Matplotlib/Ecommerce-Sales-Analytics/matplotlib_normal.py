import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset (keep the Excel file in this script's working directory)
data = pd.read_excel("Ecommerce_Sales_Analytics_Cleaned.xlsx")


# Category-wise Sales

category_sales = data.groupby("Category")["Sales"].sum()

print("Category-wise Sales:")
print(category_sales)

plt.bar(category_sales.index, category_sales.values)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()


# Payment Mode-wise Sales

payment_sales = data.groupby("Payment_Mode")["Sales"].sum()

print("Payment Mode-wise Sales:")
print(payment_sales)

plt.bar(payment_sales.index, payment_sales.values)

plt.title("Payment Mode-wise Sales")
plt.xlabel("Payment Mode")
plt.ylabel("Sales")
plt.show()


# Unit Price vs Sales

print("Unit Price vs Sales:")
print(data[["Unit_Price", "Sales"]].describe())

plt.scatter(data["Unit_Price"], data["Sales"])

plt.title("Unit Price vs Sales")
plt.xlabel("Unit Price")
plt.ylabel("Sales")
plt.show()


# Profit Distribution

print("Profit Distribution:")
print(data["Profit"].describe())

plt.hist(data["Profit"], bins=20)

plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Number of Orders")
plt.show()


# Monthly Sales Trend

data["Order_Date"] = pd.to_datetime(data["Order_Date"])

monthly_sales = data.groupby(
    data["Order_Date"].dt.to_period("M")
)["Sales"].sum()

print("Monthly Sales Trend:")
print(monthly_sales)

plt.plot(monthly_sales.index.astype(str), monthly_sales.values, marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# Monthly Sales vs Profit

monthly_performance = data.groupby(
    data["Order_Date"].dt.to_period("M")
)[["Sales", "Profit"]].sum()

print("Monthly Sales vs Profit:")
print(monthly_performance)

plt.plot(monthly_performance.index.astype(str), monthly_performance["Sales"], marker="o", label="Sales")
plt.plot(monthly_performance.index.astype(str), monthly_performance["Profit"], marker="s", label="Profit")

plt.title("Monthly Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.legend()
plt.show()


# Top 10 Products by Sales

top_products = data.groupby("Product")["Sales"].sum().nlargest(10)

print("Top 10 Products by Sales:")
print(top_products)

plt.bar(top_products.index, top_products.values)

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# Category-wise Profit

category_profit = data.groupby("Category")["Profit"].sum()

print("Category-wise Profit:")
print(category_profit)

plt.bar(category_profit.index, category_profit.values)

plt.title("Category-wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()


# Category-wise Sales vs Profit

category_comparison = data.groupby("Category")[["Sales", "Profit"]].sum()

print("Category-wise Sales vs Profit:")
print(category_comparison)

category_comparison.plot(kind="bar")

plt.title("Category-wise Sales vs Profit")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()


# Category-wise Profit Margin

category_margin = (
    data.groupby("Category")["Profit"].sum()
    / data.groupby("Category")["Sales"].sum()
) * 100

print("Category-wise Profit Margin:")
print(category_margin.round(2))

plt.bar(category_margin.index, category_margin.values)

plt.title("Category-wise Profit Margin")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.show()


# Top 10 Cities by Sales

top_cities = data.groupby("City")["Sales"].sum().nlargest(10)

print("Top 10 Cities by Sales:")
print(top_cities)

plt.bar(top_cities.index, top_cities.values)

plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# Sales Channel-wise Sales

channel_sales = data.groupby("Sales_Channel")["Sales"].sum()

print("Sales Channel-wise Sales:")
print(channel_sales)

plt.bar(channel_sales.index, channel_sales.values)

plt.title("Sales Channel-wise Sales")
plt.xlabel("Sales Channel")
plt.ylabel("Sales")
plt.show()


# Customer Segment-wise Sales

segment_sales = data.groupby("Customer_Segment")["Sales"].sum()

print("Customer Segment-wise Sales:")
print(segment_sales)

plt.bar(segment_sales.index, segment_sales.values)

plt.title("Customer Segment-wise Sales")
plt.xlabel("Customer Segment")
plt.ylabel("Sales")
plt.show()


# Order Status Distribution

order_status = data["Order_Status"].value_counts()

print("Order Status Distribution:")
print(order_status)

plt.bar(order_status.index, order_status.values)

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")
plt.show()
