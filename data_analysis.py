import pandas as pd
import matplotlib.pyplot as plt
import os

# Load raw data
df = pd.read_csv("data/raw_data.csv")

# Display raw info
print("Before Cleaning:\n", df.info())

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Convert purchase_date to datetime
df["purchase_date"] = pd.to_datetime(df["purchase_date"], errors="coerce")

# Drop duplicate rows
df = df.drop_duplicates()

# Drop rows missing customer_id or revenue
df = df.dropna(subset=["customer_id", "revenue_($)"])

# Convert revenue to numeric
df["revenue_($)"] = pd.to_numeric(df["revenue_($)"], errors="coerce")

# Handle missing name/email
df["name"] = df["name"].fillna("Unknown")
df["email"] = df["email"].fillna("unknown@example.com")

# Create cleaned_data folder if it doesn't exist
os.makedirs("cleaned_data", exist_ok=True)
df.to_csv("cleaned_data/cleaned_data.csv", index=False)

# Group revenue by product
revenue_by_product = df.groupby("product")["revenue_($)"].sum()

# Create visuals folder if it doesn't exist
os.makedirs("visuals", exist_ok=True)

# Plot revenue by product
revenue_by_product.plot(kind="bar", title="Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()
plt.savefig("visuals/revenue_by_product.png")
plt.show()
