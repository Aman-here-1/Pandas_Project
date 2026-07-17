# ==========================================================
# Project : Pandas Mastery Bootcamp
# Company : Zomato
# Day     : 01
# Module  : Assignment Solution
# File    : 05_assignment_solution.py
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

print("=" * 100)
print("DAY 01 ASSIGNMENT SOLUTION")
print("=" * 100)

# ==========================================================
# Q1 Total Rows & Columns
# ==========================================================

print("\nQ1. Total Rows & Columns")
print("-" * 60)

print(f"Rows    : {orders.shape[0]:,}")
print(f"Columns : {orders.shape[1]}")

# ==========================================================
# Q2 Column Names
# ==========================================================

print("\nQ2. Column Names")
print("-" * 60)

for i, column in enumerate(orders.columns, start=1):
    print(f"{i:02d}. {column}")

# ==========================================================
# Q3 Data Types
# ==========================================================

print("\nQ3. Data Types")
print("-" * 60)

print(orders.dtypes)

# ==========================================================
# Q4 Numeric Columns
# ==========================================================

print("\nQ4. Numeric Columns")
print("-" * 60)

numeric_columns = orders.select_dtypes(include="number").columns

print(list(numeric_columns))

# ==========================================================
# Q5 Categorical Columns
# ==========================================================

print("\nQ5. Categorical Columns")
print("-" * 60)

categorical_columns = orders.select_dtypes(include="object").columns

print(list(categorical_columns))

# ==========================================================
# Q6 Missing Values
# ==========================================================

print("\nQ6. Missing Values")
print("-" * 60)

print(orders.isnull().sum())

# ==========================================================
# Q7 Duplicate Rows
# ==========================================================

print("\nQ7. Duplicate Rows")
print("-" * 60)

print(orders.duplicated().sum())

# ==========================================================
# Q8 First 20 Orders
# ==========================================================

print("\nQ8. First 20 Orders")
print("-" * 60)

print(orders.head(20))

# ==========================================================
# Q9 Last 20 Orders
# ==========================================================

print("\nQ9. Last 20 Orders")
print("-" * 60)

print(orders.tail(20))

# ==========================================================
# Q10 Random 20 Orders
# ==========================================================

print("\nQ10. Random 20 Orders")
print("-" * 60)

print(orders.sample(20, random_state=42))

# ==========================================================
# Q11 Unique Cities
# ==========================================================

print("\nQ11. Unique Cities")
print("-" * 60)

print(orders["city"].unique())

# ==========================================================
# Q12 Orders Per City
# ==========================================================

print("\nQ12. Orders Per City")
print("-" * 60)

print(orders["city"].value_counts())

# ==========================================================
# Q13 Payment Method Distribution
# ==========================================================

print("\nQ13. Payment Method Distribution")
print("-" * 60)

print(orders["payment_method"].value_counts())

# ==========================================================
# Q14 Order Status Distribution
# ==========================================================

print("\nQ14. Order Status Distribution")
print("-" * 60)

print(orders["order_status"].value_counts())

# ==========================================================
# Q15 Rating Distribution
# ==========================================================

print("\nQ15. Rating Distribution")
print("-" * 60)

print(orders["rating"].value_counts().sort_index())

# ==========================================================
# Q16 Revenue Summary
# ==========================================================

print("\nQ16. Revenue Summary")
print("-" * 60)

print(f"Total Revenue        : ₹{orders['order_value'].sum():,.2f}")
print(f"Average Order Value  : ₹{orders['order_value'].mean():.2f}")
print(f"Highest Order Value  : ₹{orders['order_value'].max()}")
print(f"Lowest Order Value   : ₹{orders['order_value'].min()}")

# ==========================================================
# Q17 Discount Summary
# ==========================================================

print("\nQ17. Discount Summary")
print("-" * 60)

print(f"Total Discount : ₹{orders['discount'].sum():,.2f}")
print(f"Average        : ₹{orders['discount'].mean():.2f}")
print(f"Maximum        : ₹{orders['discount'].max()}")

# ==========================================================
# Q18 Delivery Analysis
# ==========================================================

print("\nQ18. Delivery Analysis")
print("-" * 60)

print(f"Average Delivery Time : {orders['delivery_minutes'].mean():.2f} Minutes")
print(f"Fastest Delivery      : {orders['delivery_minutes'].min()} Minutes")
print(f"Slowest Delivery      : {orders['delivery_minutes'].max()} Minutes")

# ==========================================================
# Q19 Top 10 Highest Orders
# ==========================================================

print("\nQ19. Top 10 Highest Orders")
print("-" * 60)

print(
    orders.nlargest(
        10,
        "order_value"
    )[
        [
            "order_id",
            "city",
            "order_value"
        ]
    ]
)

# ==========================================================
# Q20 Lowest 10 Orders
# ==========================================================

print("\nQ20. Lowest 10 Orders")
print("-" * 60)

print(
    orders.nsmallest(
        10,
        "order_value"
    )[
        [
            "order_id",
            "city",
            "order_value"
        ]
    ]
)

# ==========================================================
# Completion
# ==========================================================

print()
print("=" * 100)
print("DAY 01 COMPLETED SUCCESSFULLY")
print("=" * 100)

print("""
Topics Covered
--------------
✓ Data Generator
✓ Read CSV
✓ DataFrame
✓ Series
✓ head()
✓ tail()
✓ sample()
✓ shape
✓ columns
✓ dtypes
✓ info()
✓ describe()
✓ unique()
✓ nunique()
✓ value_counts()
✓ isnull()
✓ duplicated()
✓ select_dtypes()
✓ nlargest()
✓ nsmallest()
""")