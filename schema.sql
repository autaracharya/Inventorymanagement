-- Author: Autar Acharya
-- Student ID: 8906942
-- Date: April 17, 2025

-- This script creates the orders table in the Neon.Tech database

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,                         -- Auto-generated unique ID for each order
    customer_name VARCHAR(100) NOT NULL,           -- Customer's name (required)
    product VARCHAR(100) NOT NULL,                 -- Product name (required)
    quantity INTEGER NOT NULL CHECK (quantity >= 0), -- Quantity (non-negative, required)
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price (non-negative, required)
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Automatically sets the order date
);
