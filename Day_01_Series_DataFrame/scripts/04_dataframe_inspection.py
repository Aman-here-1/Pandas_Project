# ==========================================================
# Project : Pandas Mastery Bootcamp
# Company : Zomato
# Day     : 01
# Module  : DataFrame Inspection
# File    : 04_dataframe_inspection.py
# Author  : Aman Chouhan
# ==========================================================

from pathlib import Path

import pandas as pd

# ==========================================================
# Load Dataset
# ==========================================================

file_path = (
    Path(__file__).parent.parent
    / "data"
    / "raw"
    / "orders.csv"
)

orders = pd.read_csv(file_path)

# ==========================================================
# DATASET OVERVIEW
# ==========================================================

print("=" * 100)
print("DATASET OVERVIEW")
print("=" * 100)

print("Shape :", orders.shape)
print("Rows  :", orders.shape[0])
print("Cols  :", orders.shape[1])

print()

# ==========================================================
# HEAD
# ==========================================================

print("=" * 100)
print("HEAD()")
print("=" * 100)

print(orders.head())

print()

print("=" * 100)
print("HEAD(10)")
print("=" * 100)

print(orders.head(10))

print()

# ==========================================================
# TAIL
# ==========================================================

print("=" * 100)
print("TAIL()")
print("=" * 100)

print(orders.tail())

print()

print("=" * 100)
print("TAIL(10)")
print("=" * 100)

print(orders.tail(10))

print()

# ==========================================================
# RANDOM SAMPLE
# ==========================================================

print("=" * 100)
print("SAMPLE(5)")
print("=" * 100)

print(orders.sample(5, random_state=42))

print()

print("=" * 100)
print("SAMPLE(10)")
print("=" * 100)

print(orders.sample(10, random_state=10))

print()

# ==========================================================
# INFO
# ==========================================================

print("=" * 100)
print("INFO()")
print("=" * 100)

orders.info()

print()

# ==========================================================
# DTYPES
# ==========================================================

print("=" * 100)
print("DTYPES")
print("=" * 100)

print(orders.dtypes)

print()

# ==========================================================
# COLUMNS
# ==========================================================

print("=" * 100)
print("COLUMNS")
print("=" * 100)

for i, column in enumerate(orders.columns, start=1):
    print(f"{i:02d}. {column}")

print()

# ==========================================================
# INDEX
# ==========================================================

print("=" * 100)
print("INDEX")
print("=" * 100)

print(orders.index)

print()

# ==========================================================
# DESCRIBE NUMERIC
# ==========================================================

print("=" * 100)
print("DESCRIBE() - NUMERIC")
print("=" * 100)

print(orders.describe())

print()

# ==========================================================
# DESCRIBE OBJECT
# ==========================================================

print("=" * 100)
print("DESCRIBE() - OBJECT")
print("=" * 100)

print(orders.describe(include="object"))

print()

# ==========================================================
# MISSING VALUES
# ==========================================================

print("=" * 100)
print("MISSING VALUES")
print("=" * 100)

print(orders.isnull().sum())

print()

# ==========================================================
# DUPLICATES
# ==========================================================

print("=" * 100)
print("DUPLICATES")
print("=" * 100)

print("Duplicate Rows :", orders.duplicated().sum())

print()

# ==========================================================
# MEMORY USAGE
# ==========================================================

print("=" * 100)
print("MEMORY USAGE")
print("=" * 100)

memory_mb = orders.memory_usage(deep=True).sum() / 1024 / 1024

print(f"Memory Usage : {memory_mb:.2f} MB")

print()

# ==========================================================
# BUSINESS SUMMARY
# ==========================================================

print("=" * 100)
print("BUSINESS SUMMARY")
print("=" * 100)

print(f"Total Orders             : {len(orders):,}")
print(f"Unique Customers         : {orders['customer_id'].nunique():,}")
print(f"Unique Restaurants       : {orders['restaurant_id'].nunique():,}")
print(f"Cities Covered           : {orders['city'].nunique()}")
print(f"Average Order Value      : ₹{orders['order_value'].mean():.2f}")
print(f"Maximum Order Value      : ₹{orders['order_value'].max()}")
print(f"Minimum Order Value      : ₹{orders['order_value'].min()}")
print(f"Total Revenue            : ₹{orders['order_value'].sum():,.2f}")
print(f"Average Delivery Minutes : {orders['delivery_minutes'].mean():.2f}")
print(f"Average Rating           : {orders['rating'].mean():.2f}")

print()

# ==========================================================
# MODULE COMPLETED
# ==========================================================

print("=" * 100)
print("DAY 01 - DATAFRAME INSPECTION COMPLETED")
print("=" * 100)