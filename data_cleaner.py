import pandas as pd
import numpy as np

data = {
    "sku": ["A100", "A101", "A102", "A102", "A103", "A104"],
    "product_name": ["Blue Shirt", "Red Hat", "Black Shoes", "Black Shoes", None, "Green Jacket"],
    "price": [19.99, 9.99, "49.99", "49.99", 29.99, np.nan],
    "category": ["Clothing", "Accessories", "Footwear", "Footwear", "clothing", "CLOTHING"]
}
df = pd.DataFrame(data)

# Step 1: Remove duplicate SKUs
df = df.drop_duplicates(subset=['sku'], keep='first')

# Step 2: Fix price data type
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Step 3: Standardize category text
df['category'] = df['category'].str.strip().str.title()

# Step 4: Drop rows with missing product names
df = df.dropna(subset=['product_name'])

# Step 5: Flag missing prices instead of guessing
df['needs_price_review'] = df['price'].isnull()

print(df)