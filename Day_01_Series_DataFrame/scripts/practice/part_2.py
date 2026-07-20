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

# print(orders.head())

# print(orders.columns)

# print(orders[["city", "area"]])

# print(orders[["city","area", "customer_segment"]].groupby(["city", "area"]).count())

# print(orders[orders["city"] == "Delhi"])

# print(orders[orders["city"].isin(["Delhi", "Mumbai"])])

print(orders[(orders["city"] == "Delhi") & (orders["customer_segment"] == "Consumer")])