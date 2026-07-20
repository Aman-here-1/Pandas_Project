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

print(file_path)
print(orders.head())

orders = pd.read_csv(file_path)

print(orders.head())

print(orders.duplicated().sum())

print(orders.shape)

print(orders.info())
print(orders.describe(include='all'))
print(orders.sample(10))

print(orders.nunique())

print(orders.isnull().sum())

print(orders.duplicated().sum())

print(orders.dtypes)