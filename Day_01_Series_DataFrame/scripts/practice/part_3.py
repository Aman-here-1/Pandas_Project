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
# print(orders.iloc[0:5, 0:3])
# print(orders.loc[21445, "city"])

# print(orders.sort_values(by="discount", ascending=False).head(15))


# print(orders.sort_values(by=["city", "discount"], ascending=[True, False]))

print(orders["city"].value_counts().head()) 
print(orders["city"].value_counts().tail(3))