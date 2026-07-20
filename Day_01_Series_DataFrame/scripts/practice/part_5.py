# Real Product Analyst Questions

from itertools import groupby
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
print(orders.groupby('city')['order_value'].sum().reset_index().sort_values(by="order_value",ascending=False))

print(orders.groupby('city')['order_value'].agg(['sum', 'mean', 'count']))

print(orders.groupby("city").agg(
    total_orders=("order_id", "count"),
    revenue=("final_bill", "sum"),
    average_order_value=("final_bill", "mean"),
    average_rating=("rating", "mean")
).reset_index().sort_values(by="revenue", ascending=False))


print(orders.groupby(['city', 'payment_method'])['order_value'].agg(['sum', 'mean', 'count']))
