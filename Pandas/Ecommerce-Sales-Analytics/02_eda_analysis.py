import pandas as pd

# Load cleaned dataset
data = pd.read_excel("Ecommerce_Sales_Analytics_Cleaned.xlsx")

# Check the data
print(data.head())

# Calculate total number of orders
total_orders = data["Order_ID"].nunique()

print("Total Orders:", total_orders)

# Calculate total unique customers
total_customers = data["Customer_ID"].nunique()

print("Total Unique Customers:", total_customers)

# Calculate total sales
total_sales = data["Sales"].sum()

print("Total Sales:", total_sales)

# Calculate total net sales
total_net_sales = data["Net_Sales"].sum()

print("Total Net Sales:", total_net_sales)

# Calculate total profit
total_profit = data["Profit"].sum()

print("Total Profit:", total_profit)

# Calculate Average Order Value
average_order_value = data["Net_Sales"].sum() / data["Order_ID"].nunique()

print("Average Order Value:", round(average_order_value, 2))

# Calculate sales by category
category_sales = data.groupby("Category")["Sales"].sum()

print(category_sales)

# Calculate profit by category
category_profit = data.groupby("Category")["Profit"].sum()

print(category_profit)

# Calculate sales by city
city_sales = data.groupby("City")["Sales"].sum()

print(city_sales)

# Calculate sales by sales channel
channel_sales = data.groupby("Sales_Channel")["Sales"].sum()

print(channel_sales)

# Calculate sales by payment mode
payment_sales = data.groupby("Payment_Mode")["Sales"].sum()

print(payment_sales)

# Calculate sales by customer segment
segment_sales = data.groupby("Customer_Segment")["Sales"].sum()

print(segment_sales)

# Calculate sales by order status
status_sales = data.groupby("Order_Status")["Sales"].sum()

print(status_sales)

# Extract month and year from Order_Date
data["Month"] = data["Order_Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = data.groupby("Month")["Sales"].sum()

print(monthly_sales)

# Calculate monthly profit
monthly_profit = data.groupby("Month")["Profit"].sum()

print(monthly_profit)

# Calculate top 10 customers by net sales
top_customers = (
    data.groupby("Customer_ID")["Net_Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)

# Calculate overall profit margin
profit_margin = (
    data["Profit"].sum() / data["Net_Sales"].sum()
) * 100

print("Profit Margin:", round(profit_margin, 2), "%")

# Calculate total quantity sold
total_quantity = data["Quantity"].sum()

print("Total Quantity Sold:", total_quantity)

# Calculate total delivered orders
delivered_orders = (data["Order_Status"] == "Delivered").sum()

print("Delivered Orders:", delivered_orders)

# Calculate total cancelled orders
cancelled_orders = (data["Order_Status"] == "Cancelled").sum()

print("Cancelled Orders:", cancelled_orders)

# Calculate total returned orders
returned_orders = (data["Order_Status"] == "Returned").sum()

print("Returned Orders:", returned_orders)

# Calculate cancellation rate
cancellation_rate = (
    cancelled_orders / total_orders
) * 100

print("Cancellation Rate:", round(cancellation_rate, 2), "%")

# Calculate return rate
return_rate = (
    returned_orders / total_orders
) * 100

print("Return Rate:", round(return_rate, 2), "%")

# Calculate delivery rate
delivery_rate = (
    delivered_orders / total_orders
) * 100

print("Delivery Rate:", round(delivery_rate, 2), "%")

# Calculate profit margin by category
category_analysis = data.groupby("Category")[["Net_Sales", "Profit"]].sum()

category_analysis["Profit_Margin"] = (
    category_analysis["Profit"]
    / category_analysis["Net_Sales"]
) * 100

print(category_analysis)

# ==========================================
# STEP 26: Category-wise Profit Margin
# ==========================================

# Calculate total Net Sales and Profit for each category
category_analysis = data.groupby("Category")[["Net_Sales", "Profit"]].sum()

# Calculate profit margin for each category
category_analysis["Profit_Margin"] = (
    category_analysis["Profit"] /
    category_analysis["Net_Sales"]
) * 100

# Display category-wise profit margin
print(category_analysis)

# STEP 27: Customer Segment-wise Profit
segment_profit = data.groupby("Customer_Segment")["Profit"].sum()

print(segment_profit)

# STEP 28: City-wise Profit
city_profit = data.groupby("City")["Profit"].sum()

print(city_profit)

# ==========================================
# STEP 29: Sales Channel-wise Profit
# ==========================================

channel_profit = data.groupby("Sales_Channel")["Profit"].sum()

print(channel_profit)

# STEP 30: Payment Mode-wise Profit
payment_profit = data.groupby("Payment_Mode")["Profit"].sum()

print(payment_profit)

# ==========================================
# STEP 31: Monthly Order Trend
# ==========================================

monthly_orders = data.groupby("Month")["Order_ID"].nunique()

print(monthly_orders)

# ==========================================
# STEP 32: Monthly Customer Trend
# ==========================================

monthly_customers = data.groupby("Month")["Customer_ID"].nunique()

print(monthly_customers)

# ==========================================
# STEP 33: Average Discount by Category
# ==========================================

avg_discount_category = data.groupby("Category")["Discount"].mean() * 100

print(avg_discount_category.round(2))

# ==========================================
# STEP 34: Top 10 Products by Profit
# ==========================================

product_profit = data.groupby("Product")["Profit"].sum()
top_products_profit = product_profit.sort_values(ascending=False).head(10)
print(top_products_profit)

# ==========================================
# STEP 35: Top 10 Cities by Sales
# ==========================================

city_sales_total = data.groupby("City")["Sales"].sum()
top_cities_sales = city_sales_total.sort_values(ascending=False).head(10)
print(top_cities_sales)

# ==========================================
# STEP 36: Correlation Analysis
# ==========================================

numeric_data = data[
    [
        "Quantity",
        "Unit_Price",
        "Discount",
        "Sales",
        "Discount_Amount",
        "Net_Sales",
        "Profit"
    ]
]
correlation = numeric_data.corr()
print(correlation.round(2))

# ==========================================
# STEP 37: Basic Statistical Analysis
# ==========================================

statistical_data = data[
    [
        "Quantity",
        "Unit_Price",
        "Sales",
        "Discount_Amount",
        "Net_Sales",
        "Profit"
    ]
]
statistical_summary = statistical_data.describe()
print(statistical_summary.round(2))

# ==========================================
# STEP 38: Final EDA Summary
# ==========================================

print("Total Orders:", total_orders)
print("Unique Customers:", total_customers)
print("Total Sales:", total_sales)
print("Total Net Sales:", round(total_net_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Average Order Value:", round(average_order_value, 2))
print("Profit Margin:", round(profit_margin, 2), "%")
print("Total Quantity Sold:", total_quantity)
print("Delivered Orders:", delivered_orders)
print("Cancelled Orders:", cancelled_orders)
print("Returned Orders:", returned_orders)
print("Delivery Rate:", round(delivery_rate, 2), "%")
print("Cancellation Rate:", round(cancellation_rate, 2), "%")
print("Return Rate:", round(return_rate, 2), "%")

# ==========================================
# STEP 39: Outlier Analysis using IQR Method
# ==========================================

outlier_columns = [
    "Quantity",
    "Unit_Price",
    "Sales",
    "Discount_Amount",
    "Net_Sales",
    "Profit"
]

print("\n========== OUTLIER ANALYSIS (IQR METHOD) ==========")

for column in outlier_columns:
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    outlier_mask = (data[column] < lower_bound) | (data[column] > upper_bound)
    outlier_count = int(outlier_mask.sum())

    print(f"\nColumn: {column}")
    print("Lower Bound:", round(lower_bound, 2))
    print("Upper Bound:", round(upper_bound, 2))
    print("Outlier Count:", outlier_count)

# Note: Outliers are identified only; they are not removed automatically.

# ==========================================
# STEP 40: Business Insights
# ==========================================

print("\n========== BUSINESS INSIGHTS ==========")

category_sales_insights = data.groupby("Category")["Sales"].sum()
if not category_sales_insights.empty:
    best_sales_category = category_sales_insights.idxmax()
    print("Highest Sales Category:", best_sales_category,
          "| Sales:", round(category_sales_insights.max(), 2))

category_profit_insights = data.groupby("Category")["Profit"].sum()
if not category_profit_insights.empty:
    best_profit_category = category_profit_insights.idxmax()
    print("Highest Profit Category:", best_profit_category,
          "| Profit:", round(category_profit_insights.max(), 2))

city_sales_insights = data.groupby("City")["Sales"].sum()
if not city_sales_insights.empty:
    best_sales_city = city_sales_insights.idxmax()
    print("Highest Sales City:", best_sales_city,
          "| Sales:", round(city_sales_insights.max(), 2))

channel_sales_insights = data.groupby("Sales_Channel")["Sales"].sum()
if not channel_sales_insights.empty:
    best_sales_channel = channel_sales_insights.idxmax()
    print("Highest Sales Channel:", best_sales_channel,
          "| Sales:", round(channel_sales_insights.max(), 2))

product_profit_insights = data.groupby("Product")["Profit"].sum()
if not product_profit_insights.empty:
    best_profit_product = product_profit_insights.idxmax()
    print("Highest Profit Product:", best_profit_product,
          "| Profit:", round(product_profit_insights.max(), 2))

segment_sales_insights = data.groupby("Customer_Segment")["Sales"].sum()
if not segment_sales_insights.empty:
    best_sales_segment = segment_sales_insights.idxmax()
    print("Highest Sales Customer Segment:", best_sales_segment,
          "| Sales:", round(segment_sales_insights.max(), 2))

payment_sales_insights = data.groupby("Payment_Mode")["Sales"].sum()
if not payment_sales_insights.empty:
    best_payment_mode = payment_sales_insights.idxmax()
    print("Highest Sales Payment Mode:", best_payment_mode,
          "| Sales:", round(payment_sales_insights.max(), 2))

monthly_sales_insights = data.groupby("Month")["Sales"].sum()
if not monthly_sales_insights.empty:
    best_sales_month = monthly_sales_insights.idxmax()
    print("Highest Sales Month:", best_sales_month,
          "| Sales:", round(monthly_sales_insights.max(), 2))

monthly_profit_insights = data.groupby("Month")["Profit"].sum()
if not monthly_profit_insights.empty:
    best_profit_month = monthly_profit_insights.idxmax()
    print("Highest Profit Month:", best_profit_month,
          "| Profit:", round(monthly_profit_insights.max(), 2))

print("\nTop 5 Products by Profit:")
print(product_profit_insights.sort_values(ascending=False).head(5))

print("\nTop 5 Cities by Sales:")
print(city_sales_insights.sort_values(ascending=False).head(5))
