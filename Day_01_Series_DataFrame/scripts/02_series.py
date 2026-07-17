# ==========================================================
# Project : Pandas Mastery Bootcamp
# Company : Zomato
# Day     : 01
# Module  : Series
# File    : 02_series.py
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
# Dataset Information
# ==========================================================

print("=" * 80)
print("DATASET INFORMATION")
print("=" * 80)

print(f"Rows    : {orders.shape[0]:,}")
print(f"Columns : {orders.shape[1]}")

print()

# ==========================================================
# What is a Series?
# ==========================================================

city_series = orders["city"]

print("=" * 80)
print("CITY SERIES")
print("=" * 80)

print(city_series.head())

print()

print("Type :", type(city_series))

print()

# ==========================================================
# Another Series
# ==========================================================

order_value_series = orders["order_value"]

print("=" * 80)
print("ORDER VALUE SERIES")
print("=" * 80)

print(order_value_series.head())

print()

print("Type :", type(order_value_series))

print()

# ==========================================================
# Series Attributes
# ==========================================================

print("=" * 80)
print("SERIES ATTRIBUTES")
print("=" * 80)

print("Series Name      :", city_series.name)
print("Data Type        :", city_series.dtype)
print("Length           :", len(city_series))
print("Shape            :", city_series.shape)
print("Memory Usage     :", city_series.memory_usage(deep=True), "bytes")

print()

# ==========================================================
# Unique Cities
# ==========================================================

print("=" * 80)
print("UNIQUE CITIES")
print("=" * 80)

print(city_series.unique())

print()

print("Total Unique Cities :", city_series.nunique())

print()

# ==========================================================
# Value Counts
# ==========================================================

print("=" * 80)
print("CITY DISTRIBUTION")
print("=" * 80)

print(city_series.value_counts())

print()

# ==========================================================
# Numeric Series Operations
# ==========================================================

print("=" * 80)
print("ORDER VALUE ANALYSIS")
print("=" * 80)

print("Minimum Order Value :", order_value_series.min())
print("Maximum Order Value :", order_value_series.max())
print("Average Order Value :", round(order_value_series.mean(), 2))
print("Median Order Value  :", order_value_series.median())
print("Total Revenue       :", order_value_series.sum())

print()

# ==========================================================
# Top 10 Order Values
# ==========================================================

print("=" * 80)
print("TOP 10 ORDER VALUES")
print("=" * 80)

print(order_value_series.nlargest(10))

print()

# ==========================================================
# Bottom 10 Order Values
# ==========================================================

print("=" * 80)
print("LOWEST 10 ORDER VALUES")
print("=" * 80)

print(order_value_series.nsmallest(10))

print()

# ==========================================================
# Business Example
# ==========================================================

print("=" * 80)
print("FIRST 10 CITIES")
print("=" * 80)

for index, city in city_series.head(10).items():
    print(f"Row {index:>5} --> {city}")

print()

# ==========================================================
# Module Completed
# ==========================================================

print("=" * 80)
print("DAY 01 - SERIES MODULE COMPLETED SUCCESSFULLY")
print("=" * 80)