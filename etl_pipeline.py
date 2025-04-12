import pandas as pd

# Extract: Load raw order data
df = pd.read_csv("sample_ecommerce_orders.csv")

# Display the first few rows
print(df.head())

# Step 1: Convert 'order_date' column to datetime format
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

# Step 2: Create a new column for total order value
df['order_value'] = df['quantity'] * df['price']

# Step 3: Clean column names (lowercase and replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 4: Drop rows where essential data is missing
df.dropna(subset=['order_id', 'customer_id', 'product_category', 'order_date'], inplace=True)

# Preview the cleaned and transformed data
print("\n--- Transformed Data ---")
print(df.head())