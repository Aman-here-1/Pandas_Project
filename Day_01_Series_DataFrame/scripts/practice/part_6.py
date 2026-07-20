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


orders["customer_total_spend"] = (
    orders
    .groupby("customer_id")["final_bill"]
    .transform("sum")
)

print(orders["customer_total_spend"].head())

# q.1: Mujhe sirf wahi cities chahiye jahan 5000 se zyada orders aaye.

a = orders.groupby("city").filter(lambda x: len(x)> 5000)
print(a)

orders.groupby("restaurant_id").filter(
    lambda x:
    x["final_bill"].sum() > 1000000
)



orders["discount_pct"] = orders.apply(
    lambda row:
    row["discount"] / row["order_value"]
    if row["order_value"] > 0
    else 0,
    axis=1
)


city_region = {
    "Delhi": "North",
    "Jaipur": "North",
    "Indore": "Central",
    "Pune": "West",
    "Mumbai": "West"
}

b = orders["region"] = (
    orders["city"]
    .map(city_region)
)

rating_map = {
    5: "Excellent",
    4: "Good",
    3: "Average",
    2: "Poor",
    1: "Bad"
}

c = orders["rating_label"] = (
    orders["rating"]
    .map(rating_map)
)
print(a)
print(b)
print(c)