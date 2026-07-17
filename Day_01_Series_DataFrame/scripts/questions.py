from pathlib import Path
import pandas as pd

file_path = (
    Path(__file__).parent.parent
    / "data"
    / "raw"
    / "orders.csv"
)

orders = pd.read_csv(file_path)

print(orders.head(10))

