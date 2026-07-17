# ==========================================================
# Project : Pandas Mastery Bootcamp
# Company : Zomato
# Day     : 01
# Module  : DataFrame
# File    : 03_dataframe.py
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
# DataFrame Information
# ==========================================================

print("=" * 80)
print("DATAFRAME INFORMATION")
print("=" * 80)

print(type(orders))

print()

print(f"Rows    : {orders.shape[0]:,}")
print(f"Columns : {orders.shape[1]}")

print()

# ==========================================================
# Entire DataFrame
# ==========================================================

print("=" * 80)
print("FIRST 5 ROWS")
print("=" * 80)

print(orders.head())

print()

# ==========================================================
# DataFrame Attributes
# ==========================================================

print("=" * 80)
print("DATAFRAME ATTRIBUTES")
print("=" * 80)

print("Shape")
print(orders.shape)

print()

print("Dimensions")
print(orders.ndim)

print()

print("Size")
print(orders.size)

print()

print("Columns")
print(orders.columns)

print()

print("Index")
print(orders.index)

print()

print("Data Types")
print(orders.dtypes)

print()

# ==========================================================
# Select Multiple Columns
# ==========================================================

print("=" * 80)
print("MULTIPLE COLUMNS")
print("=" * 80)

selected_columns = orders[
    [
        "order_id",
        "city",
        "order_value",
        "discount",
        "final_bill"
    ]
]

print(selected_columns.head())

print()

# ==========================================================
# Create New Column
# ==========================================================

orders["discount_percentage"] = round(
    (orders["discount"] / orders["order_value"]) * 100,
    2
)

print("=" * 80)
print("NEW COLUMN CREATED")
print("=" * 80)

print(
    orders[
        [
            "order_value",
            "discount",
            "discount_percentage"
        ]
    ].head()
)

print()

# ==========================================================
# Rename Column
# ==========================================================

orders.rename(
    columns={
        "final_bill": "net_bill"
    },
    inplace=True
)

print("=" * 80)
print("COLUMN RENAMED")
print("=" * 80)

print(orders.columns)

print()

# ==========================================================
# Drop Column
# ==========================================================

temp_df = orders.drop(
    columns=[
        "delivery_fee"
    ]
)

print("=" * 80)
print("COLUMN DROPPED (TEMP DATAFRAME)")
print("=" * 80)

print(temp_df.columns)

print()

# ==========================================================
# DataFrame Statistics
# ==========================================================

print("=" * 80)
print("NUMERIC SUMMARY")
print("=" * 80)

print(
    orders[
        [
            "order_value",
            "discount",
            "tip",
            "net_bill"
        ]
    ].describe()
)

print()

# ==========================================================
# Revenue Analysis
# ==========================================================

print("=" * 80)
print("BUSINESS SUMMARY")
print("=" * 80)

print("Total Orders        :", len(orders))
print("Total Revenue       :", orders["order_value"].sum())
print("Average Order Value :", round(orders["order_value"].mean(), 2))
print("Average Discount    :", round(orders["discount"].mean(), 2))
print("Average Net Bill    :", round(orders["net_bill"].mean(), 2))

print()

# ==========================================================
# Memory Usage
# ==========================================================

print("=" * 80)
print("MEMORY USAGE")
print("=" * 80)

print(orders.memory_usage(deep=True))

print()

# ==========================================================
# Module Completed
# ==========================================================

print("=" * 80)
print("DAY 01 - DATAFRAME MODULE COMPLETED SUCCESSFULLY")
print("=" * 80)