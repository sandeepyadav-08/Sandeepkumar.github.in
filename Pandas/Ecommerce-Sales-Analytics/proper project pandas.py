# Import pandas library
import pandas as pd


# Load raw dataset
data = pd.read_excel("C:/Users/PC/Downloads/Ecommerce_Sales_Analytics_Raw_Data.xlsx")


# Check first few rows
print(data.head())


# Check number of rows and columns
print(data.shape)


# Check column names, data types and non-null values
data.info()


# Check missing values in each column
print(data.isnull().sum())


# Fill missing Customer_Name using the customer's existing name
data["Customer_Name"] = data["Customer_Name"].fillna(
    data.groupby("Customer_ID")["Customer_Name"].transform("first")
)


# Check missing values in Discount
print(data["Discount"].value_counts(dropna=False).sort_index())


# Fill missing Discount with 0
data["Discount"] = data["Discount"].fillna(0)


# Check missing values in Payment_Mode
print(data["Payment_Mode"].value_counts(dropna=False))


# Fill missing Payment_Mode with 'Unknown'
data["Payment_Mode"] = data["Payment_Mode"].fillna("Unknown")


# Check missing values after cleaning
print(data.isnull().sum())


# Check for duplicate rows
print(data.duplicated().sum())


# Check data types
print(data.dtypes)


# Check unique values in categorical columns
print(data["Customer_Segment"].unique())
print(data["Category"].unique())
print(data["Payment_Mode"].unique())
print(data["Sales_Channel"].unique())
print(data["Order_Status"].unique())


# Check statistical summary of Quantity
print(data["Quantity"].describe())


# Check statistical summary of Unit Price
print(data["Unit_Price"].describe())


# Check statistical summary of Sales
print(data["Sales"].describe())


# Check statistical summary of Discount Amount
print(data["Discount_Amount"].describe())


# Check statistical summary of Net Sales
print(data["Net_Sales"].describe())


# Check statistical summary of Profit
print(data["Profit"].describe())


# Validate Sales calculation
data["Calculated_Sales"] = data["Quantity"] * data["Unit_Price"]

print((data["Sales"] != data["Calculated_Sales"]).sum())


# Identify rows where Discount Amount does not match the Discount rate
mask = (
    data["Discount_Amount"].round(2)
    !=
    (data["Sales"] * data["Discount"]).round(2)
)


# Correct Discount values for inconsistent rows
data.loc[mask, "Discount"] = (
    data.loc[mask, "Discount_Amount"]
    /
    data.loc[mask, "Sales"]
).round(2)


# Validate Discount Amount after correction
data["Calculated_Discount_Amount"] = (
    data["Sales"] * data["Discount"]
)

print(
    (
        data["Discount_Amount"].round(2)
        != data["Calculated_Discount_Amount"].round(2)
    ).sum()
)


# Validate Net Sales calculation
data["Calculated_Net_Sales"] = (
    data["Sales"] - data["Discount_Amount"]
)

print(
    (
        data["Net_Sales"].round(2)
        != data["Calculated_Net_Sales"].round(2)
    ).sum()
)


# Check for zero or negative profit
print((data["Profit"] <= 0).sum())


# Remove temporary validation columns
data.drop(
    columns=[
        "Calculated_Sales",
        "Calculated_Discount_Amount",
        "Calculated_Net_Sales"
    ],
    inplace=True
)


# Save cleaned dataset
data.to_excel(
    "Ecommerce_Sales_Analytics_Cleaned.xlsx",
    index=False
)
