"""
E-Commerce Sales Analytics — Pandas Data Cleaning
Author: Sandeep Yadav

Place the raw Excel dataset at:
data/raw/Ecommerce_Sales_Analytics_Raw_Data.xlsx

Run:
python proper_project_pandas.py

Outputs:
- data/processed/Ecommerce_Sales_Analytics_Cleaned.xlsx
- reports/data_quality_report.txt
"""

from pathlib import Path
import pandas as pd


# Set project paths
PROJECT_DIR = Path(__file__).resolve().parent
RAW_FILE = PROJECT_DIR / "data" / "raw" / "Ecommerce_Sales_Analytics_Raw_Data.xlsx"
CLEAN_FILE = PROJECT_DIR / "data" / "processed" / "Ecommerce_Sales_Analytics_Cleaned.xlsx"
REPORT_FILE = PROJECT_DIR / "reports" / "data_quality_report.txt"


def main():
    # Create output folders when they do not exist
    CLEAN_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Check whether the raw dataset exists
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Raw dataset not found: {RAW_FILE}\n"
            "Place Ecommerce_Sales_Analytics_Raw_Data.xlsx in the data/raw folder."
        )

    # Load raw dataset
    data = pd.read_excel(RAW_FILE)

    # Collect a text report while also showing key checks in the terminal
    report_lines = [
        "E-COMMERCE SALES ANALYTICS — DATA QUALITY REPORT",
        "=" * 52,
        f"Input file: {RAW_FILE.name}",
        f"Initial shape: {data.shape}",
        "",
        "INITIAL PREVIEW",
        "-" * 20,
        data.head().to_string(),
        "",
        "COLUMN INFORMATION",
        "-" * 20,
        data.dtypes.to_string(),
        "",
        "MISSING VALUES BEFORE CLEANING",
        "-" * 32,
        data.isnull().sum().to_string(),
    ]

    # Check first few rows
    print(data.head())

    # Check number of rows and columns
    print("Dataset shape:", data.shape)

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
    missing_after_cleaning = data.isnull().sum()
    print(missing_after_cleaning)

    # Check for duplicate rows
    duplicate_count = int(data.duplicated().sum())
    print("Duplicate rows:", duplicate_count)

    # Check data types
    print(data.dtypes)

    # Check unique values in categorical columns
    categorical_columns = [
        "Customer_Segment",
        "Category",
        "Payment_Mode",
        "Sales_Channel",
        "Order_Status",
    ]
    for column in categorical_columns:
        print(f"Unique values in {column}:")
        print(data[column].unique())

    # Check statistical summaries
    numeric_columns = [
        "Quantity",
        "Unit_Price",
        "Sales",
        "Discount_Amount",
        "Net_Sales",
        "Profit",
    ]
    for column in numeric_columns:
        print(f"Statistical summary — {column}:")
        print(data[column].describe())

    # Validate Sales calculation
    data["Calculated_Sales"] = data["Quantity"] * data["Unit_Price"]
    sales_mismatches = int((data["Sales"] != data["Calculated_Sales"]).sum())
    print("Sales calculation mismatches:", sales_mismatches)

    # Identify rows where Discount Amount does not match the Discount rate
    mask = (
        data["Discount_Amount"].round(2)
        != (data["Sales"] * data["Discount"]).round(2)
    )

    # Correct Discount values for inconsistent rows, avoiding division by zero
    correctable_mask = mask & data["Sales"].ne(0)
    data.loc[correctable_mask, "Discount"] = (
        data.loc[correctable_mask, "Discount_Amount"]
        / data.loc[correctable_mask, "Sales"]
    ).round(2)

    # Validate Discount Amount after correction
    data["Calculated_Discount_Amount"] = data["Sales"] * data["Discount"]
    discount_mismatches = int(
        (
            data["Discount_Amount"].round(2)
            != data["Calculated_Discount_Amount"].round(2)
        ).sum()
    )
    print("Discount calculation mismatches after correction:", discount_mismatches)

    # Validate Net Sales calculation
    data["Calculated_Net_Sales"] = data["Sales"] - data["Discount_Amount"]
    net_sales_mismatches = int(
        (
            data["Net_Sales"].round(2)
            != data["Calculated_Net_Sales"].round(2)
        ).sum()
    )
    print("Net Sales calculation mismatches:", net_sales_mismatches)

    # Check for zero or negative profit
    non_positive_profit_count = int((data["Profit"] <= 0).sum())
    print("Rows with zero or negative profit:", non_positive_profit_count)

    # Remove temporary validation columns
    data.drop(
        columns=[
            "Calculated_Sales",
            "Calculated_Discount_Amount",
            "Calculated_Net_Sales",
        ],
        inplace=True,
    )

    # Save cleaned dataset
    data.to_excel(CLEAN_FILE, index=False)

    # Write final data quality report
    report_lines.extend(
        [
            "",
            "CLEANING SUMMARY",
            "-" * 20,
            "Customer_Name: filled missing values using the first known name for each Customer_ID.",
            "Discount: filled missing values with 0 and corrected rates where Discount_Amount disagreed.",
            "Payment_Mode: filled missing values with 'Unknown'.",
            f"Duplicate rows found (not automatically removed): {duplicate_count}",
            f"Sales calculation mismatches: {sales_mismatches}",
            f"Discount calculation mismatches after correction: {discount_mismatches}",
            f"Net Sales calculation mismatches: {net_sales_mismatches}",
            f"Rows with zero or negative profit: {non_positive_profit_count}",
            "",
            "MISSING VALUES AFTER CLEANING",
            "-" * 30,
            missing_after_cleaning.to_string(),
            "",
            f"Final shape: {data.shape}",
            f"Cleaned dataset saved to: {CLEAN_FILE.relative_to(PROJECT_DIR)}",
        ]
    )
    REPORT_FILE.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"\nCleaned dataset saved to: {CLEAN_FILE}")
    print(f"Data quality report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
