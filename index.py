import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

print(df)
print(df.head(2))
print(df.describe(include='all'))
print(df["Name"])
