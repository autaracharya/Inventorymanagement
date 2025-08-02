# Author: Autar Acharya
# Student ID: 8906942
# Date: April 17, 2025

import psycopg2

# This connects to my Neon.Tech PostgreSQL DB
def connect_to_db():
    return psycopg2.connect(
        host="ep-long-base-a4sp1w3z-pooler.us-east-1.aws.neon.tech",
        dbname="neondb",
        user="neondb_owner",
        password="npg_Fpe4UGdgQq9K",  # my password from neon.tech
        sslmode="require"
    )

# This adds a new order to the database
def insert_order(customer_name, product, quantity, price):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO orders (customer_name, product, quantity, price)
        VALUES (%s, %s, %s, %s);
    """, (customer_name, product, quantity, price))
    conn.commit()
    cur.close()
    conn.close()

# This gets all orders so they can be shown in the app
def fetch_orders():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT customer_name, product, quantity, price, order_date FROM orders ORDER BY id DESC;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
