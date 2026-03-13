# Sales-Analytics-For-Ecommerce-business
Sales Data Analytics Dashboard Project Report
Project Overview
This project focuses on building a complete data analytics pipeline to analyze sales performance. The workflow involved transforming raw sales data stored in a CSV file into a structured database and developing an interactive business intelligence dashboard using Power BI.
The objective of the project was to demonstrate practical skills in data management, SQL querying, and data visualization while generating meaningful insights from transactional sales data.
________________________________________
Data Source
The dataset used for this project contained sales transaction records with the following fields:
•	Order ID
•	Order Date
•	SKU (Product Identifier)
•	Product Color
•	Product Size
•	Unit Price
•	Quantity
•	Revenue
•	Order Month
The dataset was initially stored as a CSV file and required cleaning and transformation before analysis.
________________________________________
Data Preparation
The raw dataset was first reviewed and cleaned to ensure data quality and consistency. Key preparation steps included:
•	Standardizing column formats
•	Verifying revenue calculations
•	Removing potential duplicates
•	Ensuring correct data types for numerical and date fields
After cleaning, the dataset was prepared for database storage.
________________________________________
Database Implementation
A MySQL relational database was created to store the structured dataset.
A table named orders was created with fields corresponding to the dataset attributes. The cleaned CSV data was then imported into the database.
SQL queries were used to validate and explore the dataset, including:
•	Counting total orders
•	Summing total revenue
•	Identifying top-selling products
•	Reviewing order distributions by month
This step ensured the dataset was correctly structured before visualization.
________________________________________
Business Intelligence Dashboard
The MySQL database was connected to Power BI Desktop using an ODBC connection. The data was then used to develop an interactive sales dashboard.
Key dashboard components included:
Key Performance Indicators (KPIs)
•	Total Revenue
•	Total Orders
•	Total Units Sold
•	Average Order Value
Visualizations
•	Monthly Revenue Trend (Line Chart)
•	Top Products by Revenue (Clustered Bar Chart)
•	Revenue Distribution by Product Attributes (Donut Chart)
Interactive Features
To improve usability, interactive slicers were added allowing users to filter data by:
•	Product color
•	Product size
•	Order month
These filters allow decision-makers to dynamically explore the dataset and identify trends.
________________________________________
Key Insights
The dashboard enables several useful business insights, including:
•	Identification of top-performing products by revenue
•	Analysis of seasonal sales trends
•	Comparison of product variations such as color and size
•	Monitoring of overall business performance through KPI metrics
These insights can help organizations make data-driven decisions regarding inventory, marketing strategies, and product offerings.
________________________________________
Technologies Used
•	MySQL
•	SQL
•	Power BI Desktop
•	ODBC Driver
•	Microsoft Excel / CSV data processing
________________________________________
Conclusion
This project demonstrates the ability to build a complete analytics workflow from raw data ingestion to visualization. By integrating SQL-based data management with Power BI dashboards, the project provides a scalable framework for analyzing sales data and generating business insights.
The techniques used in this project can be applied to real-world business intelligence scenarios involving transactional data analysis and reporting.


