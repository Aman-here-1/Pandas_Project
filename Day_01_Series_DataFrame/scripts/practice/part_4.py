# Real Product Analyst Questions

from pathlib import Path

import pandas as pd

# ==========================================================
# Load Dataset
# ==========================================================

file_path = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "raw"
    / "orders.csv"
)

orders = pd.read_csv(file_path)

print(orders.head())

# q1. Which city contributes the highest number of orders?

print(orders["city"].value_counts())

# q.2 Most used payment method?

print(orders["payment_method"].value_counts())

# Q3. How many unique users placed orders?

print(orders["customer_id"].nunique())

# Q4. Top 20 highest bill orders?

print(orders.sort_values(by="final_bill", ascending=False).head(20))

# Q5. How many cuisines do we support?

print(orders["cuisine"].nunique())