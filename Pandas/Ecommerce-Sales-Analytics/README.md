# E-Commerce Sales Analytics — Pandas Data Cleaning

**Author:** Sandeep Yadav  
**Tools:** Python, Pandas, Excel

## Project overview

This project cleans and validates an e-commerce sales dataset using Pandas. It checks data quality, handles selected missing values, validates sales calculations, checks discount consistency, and exports a cleaned Excel file.

## Project structure

```text
Pandas/Ecommerce-Sales-Analytics/
├── data/
│   ├── raw/
│   │   └── Ecommerce_Sales_Analytics_Raw_Data.xlsx  (add locally)
│   └── processed/
│       └── Ecommerce_Sales_Analytics_Cleaned.xlsx   (generated)
├── reports/
│   └── data_quality_report.txt                      (generated)
├── proper_project_pandas.py
├── requirements.txt
└── README.md
```

## Data-cleaning steps

1. Load the raw Excel dataset and inspect the first rows, dimensions, data types, and missing values.
2. Fill missing `Customer_Name` values from the first known name associated with the same `Customer_ID`.
3. Fill missing `Discount` values with `0`.
4. Fill missing `Payment_Mode` values with `Unknown`.
5. Check duplicate rows and categorical values.
6. Review descriptive statistics for quantity, unit price, sales, discount amount, net sales, and profit.
7. Validate `Sales = Quantity × Unit_Price`.
8. Compare `Discount_Amount` with `Sales × Discount`, and correct inconsistent discount rates where sales is non-zero.
9. Validate `Net_Sales = Sales − Discount_Amount`.
10. Check for zero or negative profit and remove temporary validation columns.
11. Export the cleaned dataset and a text data-quality report.

**Note:** Duplicate rows are reported but not automatically deleted. This avoids removing records without confirming whether they are genuine duplicates.

## Run the project

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Add the raw dataset

Place your source Excel file at:

```text
data/raw/Ecommerce_Sales_Analytics_Raw_Data.xlsx
```

The raw dataset is not included in this repository; add your own authorized copy locally.

### 3. Run the script

From this project folder, run:

```bash
python proper_project_pandas.py
```

### 4. Check the outputs

- Cleaned Excel file: `data/processed/Ecommerce_Sales_Analytics_Cleaned.xlsx`
- Data quality report: `reports/data_quality_report.txt`

## Important notes

- The script uses project-relative paths instead of a computer-specific Windows path.
- It expects the source file to contain the columns used in the script, including `Customer_ID`, `Customer_Name`, `Discount`, `Payment_Mode`, `Quantity`, `Unit_Price`, `Sales`, `Discount_Amount`, `Net_Sales`, and `Profit`.
- Review the report after running the script. A validation mismatch is reported rather than silently hidden.
