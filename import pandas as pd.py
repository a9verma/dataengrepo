import pandas as pd

# Load the CSV
df = pd.read_csv('sample_ecommerce_orders.csv')

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])

# Extract date features
df['order_year'] = df['order_date'].dt.year
df['order_month'] = df['order_date'].dt.month
df['order_day'] = df['order_date'].dt.day

# Ensure customer_id and product_id are strings
df['customer_id'] = df['customer_id'].astype(str)
df['product_id'] = df['product_id'].astype(str)

# Clean product category: capitalize and strip spaces
df['product_category'] = df['product_category'].str.strip().str.title()

# Fill any missing total_price with calculated value
df['order_value'] = df['quantity'] * df['price']
df['total_price'] = df['order_value']  # or any other calculation you intend

# Preview the cleaned data
print(df.head())

from sqlalchemy import create_engine

# Create a SQLite database named 'ecommerce.db'
engine = create_engine('sqlite:///ecommerce.db')

# Load the cleaned DataFrame into a table named 'orders'
df.to_sql('orders', con=engine, if_exists='replace', index=False)

print("✅ Data successfully loaded into 'ecommerce.db' (table: orders).")
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine('sqlite:///ecommerce.db')

# SQL query to select total sales by category
query = """
SELECT product_category, SUM(order_value) AS total_sales
FROM orders
GROUP BY product_category
ORDER BY total_sales DESC;
"""

# Load the query result into a pandas DataFrame
df_sales = pd.read_sql(query, con=engine)

# Display the result
print("Total Sales by Category:")
print(df_sales)

import matplotlib.pyplot as plt

# Sample code for plotting
df['total_sales'] = df['total_price'] * df['quantity']

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(df['customer_id'], df['total_sales'], color='blue')

plt.title('Total Spend per Customer')
plt.xlabel('Customer ID')
plt.ylabel('total sales')

# Show the plot
plt.show()