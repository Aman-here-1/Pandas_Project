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

