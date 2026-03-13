-- Active: 1772655934942@@127.0.0.1@3306@mysql
--create database and use it
CREATE DATABASE sales_db; --Create a new database named 'sales_db'
USE sales_db; --Switch to the 'sales_db' database

--create table for products 
CREATE TABLE orders (
    order_id INT,  
    order_date DATE, 
    sku VARCHAR(50), 
    color VARCHAR(30), 
    size VARCHAR(10), 
    unit_price DECIMAL(10, 2), 
    quantity INT, 
    revenue DECIMAL(10, 2), 
    order_month VARCHAR(20), 
    PRIMARY KEY (order_id,sku)
); 

TRUNCATE TABLE orders; --Remove all existing data from the 'orders' table
LOAD DATA INFILE 'cleaned_women_clothing_ecommerce_sales.csv' 
INTO TABLE orders 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS; 

SELECT COUNT(*) AS total_records FROM orders; --Count the total number of records in the 'orders' table