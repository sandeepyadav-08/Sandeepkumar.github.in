# E-Commerce Sales Analytics — SQL Project

## Project overview
This project analyzes a cleaned e-commerce orders dataset with 3,000 records using MySQL. The queries examine overall performance, category and city sales, monthly trends, customer segments, payment methods, order status, discounts, profit margins, customer ranking, repeat customers, and product rankings.

## Dataset
- Rows: 3,000
- Main fields: Order date, customer, category, product, quantity, sales, discount, net sales, profit, payment mode, sales channel, and order status.
- Database: `ecommerce_analytics`
- Table: `ecommerce_sales_analytics_cleaned`

## How to run
1. Import the cleaned dataset into MySQL Workbench.
2. Select the `ecommerce_analytics` schema.
3. Open `queries_1_to_31.sql`.
4. Run the queries individually and review the Result Grid.

## SQL concepts covered
- Aggregations: `COUNT`, `SUM`, `AVG`
- Grouping and sorting: `GROUP BY`, `ORDER BY`
- Filters: `HAVING`
- Conditional logic: `CASE WHEN`
- Subqueries
- Window functions: `RANK`, `DENSE_RANK`, `PARTITION BY`, `LAG`, `LEAD`
- Running totals and month-over-month growth
- Repeat-customer rate and customer lifetime value

## Important schema note
The imported first column currently has the header `ï»¿Order_ID` due to a UTF-8 BOM in the CSV. The SQL script references it using backticks. If you rename the column to `Order_ID` in MySQL, update the queries accordingly.

## Files
- `queries_1_to_31.sql` — SQL analysis queries.
- Result outputs should be captured from MySQL Workbench after running the queries and can be saved separately for submission.
