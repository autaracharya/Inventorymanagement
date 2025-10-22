# Customer Orders Management System

# Author: Autar Acharya  

## Project Description

This is a basic desktop application built using Python and Tkinter that connects to a Neon.Tech PostgreSQL database. It allows users to:
- Add new customer orders
- View all customer orders in a table
- Automatically record order date and time


## Features

- Form to enter:
  - Customer Name
  - Product
  - Quantity (default is 1, must be non-negative)
  - Price (must be non-negative)
- Orders are displayed in a table with:
  - Customer Name
  - Product
  - Quantity
  - Price
  - Order Date (auto-generated)

---

## Database Setup (Neon.Tech)
  My Database Connection String: postgresql://neondb_owner:npg_Fpe4UGdgQq9K@ep-long-base-a4sp1w3z-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require 

1. Create your PostgreSQL database on [https://neon.tech]
2. Use the following SQL to create the orders table:

sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    product VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
