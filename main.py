# Author: Autar Acharya
# Student ID: 8906942
# Date: April 17, 2025

import tkinter as tk
from tkinter import ttk, messagebox
from db import insert_order, fetch_orders

# This function is for adding a new order when button is clicked
def submit_order():
    try:
        name = name_entry.get()
        product = product_entry.get()
        quantity = int(quantity_entry.get())
        price = float(price_entry.get())

        # Don't allow negative values
        if quantity < 0 or price < 0:
            raise ValueError

        insert_order(name, product, quantity, price)
        messagebox.showinfo("Success", "Order added successfully!")
        refresh_orders()
    except:
        messagebox.showerror("Error", "Please enter valid data.")

# This updates the table with the latest data
def refresh_orders():
    # Clear old rows
    for row in order_table.get_children():
        order_table.delete(row)

    # Get fresh data from DB
    for order in fetch_orders():
        order_table.insert("", tk.END, values=order)

# Main window setup
root = tk.Tk()
root.title("Autar Acharya Customer Orders Management System")

# Input field for customer name
tk.Label(root, text="Customer Name").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Input field for product
tk.Label(root, text="Product").grid(row=1, column=0)
product_entry = tk.Entry(root)
product_entry.grid(row=1, column=1)

# Input for quantity
tk.Label(root, text="Quantity").grid(row=2, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.insert(0, "1")
quantity_entry.grid(row=2, column=1)

# Input for price
tk.Label(root, text="Price").grid(row=3, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=3, column=1)

# Button to submit the order
submit_btn = tk.Button(root, text="Add Order", command=submit_order)
submit_btn.grid(row=4, column=0, columnspan=2)

# Table to show orders
columns = ("Customer Name", "Product", "Quantity", "Price", "Order Date")
order_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    order_table.heading(col, text=col)

order_table.grid(row=5, column=0, columnspan=2, pady=10)

# Load orders when app starts
refresh_orders()

# Start the GUI app
root.mainloop()
