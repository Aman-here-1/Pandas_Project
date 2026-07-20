# ==========================================================
# Project : Pandas Mastery Bootcamp
# Day     : 01
# Topic   : Data Generator
# ==========================================================

import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from faker import Faker

# ----------------------------------------------------------
# Configuration
# ----------------------------------------------------------

fake = Faker("en_IN")
random.seed(42)
Faker.seed(42)

TOTAL_ORDERS = 50000

START_DATE = datetime(2026, 1, 1)
END_DATE = datetime(2026, 6, 30)

# ----------------------------------------------------------
# Master Data
# ----------------------------------------------------------

CITIES = {
    "Lucknow": ["Gomti Nagar", "Hazratganj", "Indira Nagar", "Alambagh", "Mahanagar"],
    "Delhi": ["Saket", "Dwarka", "Rohini", "Karol Bagh", "Lajpat Nagar"],
    "Mumbai": ["Andheri", "Bandra", "Powai", "Borivali", "Malad"],
    "Bangalore": ["Koramangala", "Whitefield", "HSR Layout", "BTM Layout", "Indiranagar"],
    "Hyderabad": ["Madhapur", "Gachibowli", "Kondapur", "Hitech City", "Kukatpally"],
    "Pune": ["Hinjewadi", "Baner", "Viman Nagar", "Kothrud", "Wakad"],
    "Jaipur": ["Malviya Nagar", "Vaishali Nagar", "Mansarovar", "C Scheme", "Jagatpura"],
    "Indore": ["Vijay Nagar", "Palasia", "Rajendra Nagar", "Bhawarkua", "Sudama Nagar"]
}

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Wallet"
]

ORDER_STATUS = [
    "Delivered",
    "Cancelled",
    "Rejected"
]

CUSTOMER_SEGMENTS = [
    "New",
    "Regular",
    "Gold",
    "Platinum"
]


# ----------------------------------------------------------
# Generate One Order
# ----------------------------------------------------------

def generate_order(order_number: int):

    city = random.choice(list(CITIES.keys()))
    area = random.choice(CITIES[city])

    order_time = fake.date_time_between(
        start_date=START_DATE,
        end_date=END_DATE
    )

    delivery_minutes = random.randint(20, 70)

    delivery_time = order_time + timedelta(minutes=delivery_minutes)

    order_value = random.randint(150, 1500)

    discount = random.randint(0, int(order_value * 0.30))

    delivery_fee = random.randint(20, 60)

    tip = random.randint(0, 100)

    rating = random.randint(1, 5)

    status = random.choices(
        ORDER_STATUS,
        weights=[90, 7, 3]
    )[0]

    return {
        "order_id": f"ZO{100000 + order_number}",
        "customer_id": f"CU{random.randint(10000,99999)}",
        "restaurant_id": f"RS{random.randint(1000,1999)}",
        "city": city,
        "area": area,
        "order_time": order_time,
        "delivery_time": delivery_time,
        "delivery_minutes": delivery_minutes,
        "order_status": status,
        "payment_method": random.choice(PAYMENT_METHODS),
        "customer_segment": random.choice(CUSTOMER_SEGMENTS),
        "order_value": order_value,
        "discount": discount,
        "delivery_fee": delivery_fee,
        "tip": tip,
        "final_bill": order_value - discount + delivery_fee + tip,
        "rating": rating
    }


# ----------------------------------------------------------
# Generate Dataset
# ----------------------------------------------------------

orders = []

for i in range(1, TOTAL_ORDERS + 1):
    orders.append(generate_order(i))

df = pd.DataFrame(orders)

# ----------------------------------------------------------
# Save CSV
# ----------------------------------------------------------

output_path = Path(__file__).parent.parent / "data" / "raw"
output_path.mkdir(parents=True, exist_ok=True)

df.to_csv(
    output_path / "orders.csv",
    index=False
)
print("=" * 60)
print("Dataset Generated Successfully")
print("=" * 60)
print(f"Rows    : {len(df):,}")
print(f"Columns : {len(df.columns)}")
print(f"Saved   : {output_path / 'orders.csv'}")
print("=" * 60)

print(df.head())