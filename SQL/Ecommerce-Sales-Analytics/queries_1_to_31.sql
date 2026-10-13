USE ecommerce_analytics;

-- QUERY 1
SELECT COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned;


-- QUERY 2
SELECT Category AS Category_Name, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Category ORDER BY Total_Sales DESC;


-- QUERY 3
SELECT City, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY City ORDER BY Total_Sales DESC;


-- QUERY 4
SELECT YEAR(Order_Date) AS Order_Year, MONTH(Order_Date) AS Order_Month, MONTHNAME(Order_Date) AS Month_Name, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY YEAR(Order_Date), MONTH(Order_Date), MONTHNAME(Order_Date) ORDER BY Order_Year, Order_Month;


-- QUERY 5
SELECT Customer_Segment, COUNT(`ï»¿Order_ID`) AS Total_Orders, COUNT(DISTINCT Customer_ID) AS Unique_Customers, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_Segment ORDER BY Total_Sales DESC;


-- QUERY 6
SELECT Payment_Mode, COUNT(`ï»¿Order_ID`) AS Total_Orders, COUNT(DISTINCT Customer_ID) AS Unique_Customers, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Payment_Mode ORDER BY Total_Sales DESC;


-- QUERY 7
SELECT Order_Status, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Order_Status ORDER BY Total_Orders DESC;


-- QUERY 8
SELECT Product, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Product ORDER BY Total_Sales DESC LIMIT 10;


-- QUERY 9
SELECT Customer_ID, Customer_Name, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name ORDER BY Total_Net_Sales DESC LIMIT 10;


-- QUERY 10
SELECT SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit, ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Percent FROM ecommerce_sales_analytics_cleaned;


-- QUERY 11
SELECT Sales_Channel, COUNT(`ï»¿Order_ID`) AS Total_Orders, COUNT(DISTINCT Customer_ID) AS Unique_Customers, SUM(Quantity) AS Total_Quantity, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Sales_Channel ORDER BY Total_Sales DESC;


-- QUERY 12
SELECT Discount, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Sales) AS Total_Sales, SUM(Discount_Amount) AS Total_Discount, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Discount ORDER BY Discount;


-- QUERY 13
SELECT Category, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Category HAVING SUM(Sales) > 2500000 ORDER BY Total_Sales DESC;


-- QUERY 14
SELECT Category, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit, CASE WHEN SUM(Profit) >= 500000 THEN 'High Profit' WHEN SUM(Profit) >= 300000 THEN 'Medium Profit' ELSE 'Low Profit' END AS Profit_Performance FROM ecommerce_sales_analytics_cleaned GROUP BY Category ORDER BY Total_Profit DESC;


-- QUERY 15
SELECT Customer_ID, Customer_Name, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name HAVING SUM(Net_Sales) > (SELECT AVG(Customer_Total) FROM (SELECT Customer_ID, SUM(Net_Sales) AS Customer_Total FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID) AS Customer_Sales) ORDER BY Total_Net_Sales DESC;


-- QUERY 16
SELECT Order_Status, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Sales) AS Total_Sales, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, CASE WHEN Order_Status = 'Delivered' THEN 'Successful' WHEN Order_Status = 'Cancelled' THEN 'Cancelled' WHEN Order_Status = 'Returned' THEN 'Returned' ELSE 'Other' END AS Order_Performance FROM ecommerce_sales_analytics_cleaned GROUP BY Order_Status ORDER BY Total_Orders DESC;


-- QUERY 17
SELECT Customer_ID, Customer_Name, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name ORDER BY Total_Profit DESC LIMIT 10;


-- QUERY 18
SELECT Category, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit, ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Percent FROM ecommerce_sales_analytics_cleaned GROUP BY Category ORDER BY Profit_Margin_Percent DESC;


-- QUERY 19
SELECT Customer_ID, Customer_Name, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, RANK() OVER (ORDER BY SUM(Profit) DESC) AS Profit_Rank FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name ORDER BY Profit_Rank LIMIT 10;


-- QUERY 20
SELECT Customer_ID, Customer_Name, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, DENSE_RANK() OVER (ORDER BY SUM(Profit) DESC) AS Profit_Rank FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name ORDER BY Profit_Rank LIMIT 10;


-- QUERY 21
SELECT Customer_Segment, Customer_ID, Customer_Name, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, RANK() OVER (PARTITION BY Customer_Segment ORDER BY SUM(Profit) DESC) AS Profit_Rank FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_Segment, Customer_ID, Customer_Name ORDER BY Customer_Segment, Profit_Rank;


-- QUERY 22
SELECT YEAR(Order_Date) AS Order_Year, MONTH(Order_Date) AS Order_Month, MONTHNAME(Order_Date) AS Month_Name, SUM(Net_Sales) AS Monthly_Net_Sales, SUM(SUM(Net_Sales)) OVER (PARTITION BY YEAR(Order_Date) ORDER BY MONTH(Order_Date)) AS Running_Net_Sales FROM ecommerce_sales_analytics_cleaned GROUP BY YEAR(Order_Date), MONTH(Order_Date), MONTHNAME(Order_Date) ORDER BY Order_Year, Order_Month;


-- QUERY 23
SELECT YEAR(Order_Date) AS Order_Year, MONTH(Order_Date) AS Order_Month, MONTHNAME(Order_Date) AS Month_Name, SUM(Net_Sales) AS Monthly_Net_Sales, LAG(SUM(Net_Sales)) OVER (PARTITION BY YEAR(Order_Date) ORDER BY MONTH(Order_Date)) AS Previous_Month_Sales FROM ecommerce_sales_analytics_cleaned GROUP BY YEAR(Order_Date), MONTH(Order_Date), MONTHNAME(Order_Date) ORDER BY Order_Year, Order_Month;


-- QUERY 24
SELECT YEAR(Order_Date) AS Order_Year, MONTH(Order_Date) AS Order_Month, MONTHNAME(Order_Date) AS Month_Name, SUM(Net_Sales) AS Monthly_Net_Sales, LAG(SUM(Net_Sales)) OVER (PARTITION BY YEAR(Order_Date) ORDER BY MONTH(Order_Date)) AS Previous_Month_Sales, ROUND((SUM(Net_Sales) - LAG(SUM(Net_Sales)) OVER (PARTITION BY YEAR(Order_Date) ORDER BY MONTH(Order_Date))) / LAG(SUM(Net_Sales)) OVER (PARTITION BY YEAR(Order_Date) ORDER BY MONTH(Order_Date)) * 100, 2) AS MoM_Growth_Percent FROM ecommerce_sales_analytics_cleaned GROUP BY YEAR(Order_Date), MONTH(Order_Date), MONTHNAME(Order_Date) ORDER BY Order_Year, Order_Month;


-- QUERY 25
SELECT YEAR(Order_Date) AS Order_Year, MONTH(Order_Date) AS Order_Month, MONTHNAME(Order_Date) AS Month_Name, SUM(Net_Sales) AS Monthly_Net_Sales, LEAD(SUM(Net_Sales)) OVER (PARTITION BY YEAR(Order_Date) ORDER BY MONTH(Order_Date)) AS Next_Month_Sales FROM ecommerce_sales_analytics_cleaned GROUP BY YEAR(Order_Date), MONTH(Order_Date), MONTHNAME(Order_Date) ORDER BY Order_Year, Order_Month;


-- QUERY 26
SELECT Category, Product, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, RANK() OVER (PARTITION BY Category ORDER BY SUM(Profit) DESC) AS Product_Rank FROM ecommerce_sales_analytics_cleaned GROUP BY Category, Product ORDER BY Category, Product_Rank;


-- QUERY 27
SELECT Category, Product, Total_Net_Sales, Total_Profit, Product_Rank FROM (SELECT Category, Product, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, RANK() OVER (PARTITION BY Category ORDER BY SUM(Profit) DESC) AS Product_Rank FROM ecommerce_sales_analytics_cleaned GROUP BY Category, Product) AS Ranked_Products WHERE Product_Rank <= 3 ORDER BY Category, Product_Rank;


-- QUERY 28
SELECT Customer_ID, Customer_Name, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name HAVING COUNT(`ï»¿Order_ID`) > 1 ORDER BY Total_Orders DESC;


-- QUERY 29
SELECT COUNT(*) AS Total_Customers, SUM(CASE WHEN Total_Orders > 1 THEN 1 ELSE 0 END) AS Repeat_Customers, ROUND(SUM(CASE WHEN Total_Orders > 1 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS Repeat_Customer_Rate_Percent FROM (SELECT Customer_ID, COUNT(`ï»¿Order_ID`) AS Total_Orders FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID) AS Customer_Order_Count;


-- QUERY 30
SELECT Customer_ID, Customer_Name, COUNT(`ï»¿Order_ID`) AS Total_Orders, SUM(Net_Sales) AS Customer_Lifetime_Sales, SUM(Profit) AS Customer_Lifetime_Profit FROM ecommerce_sales_analytics_cleaned GROUP BY Customer_ID, Customer_Name ORDER BY Customer_Lifetime_Profit DESC LIMIT 10;


-- QUERY 31
SELECT Category, Product, Total_Net_Sales, Total_Profit FROM (SELECT Category, Product, SUM(Net_Sales) AS Total_Net_Sales, SUM(Profit) AS Total_Profit, RANK() OVER (PARTITION BY Category ORDER BY SUM(Profit) DESC) AS Product_Rank FROM ecommerce_sales_analytics_cleaned GROUP BY Category, Product) AS Ranked_Products WHERE Product_Rank = 1 ORDER BY Total_Profit DESC;
