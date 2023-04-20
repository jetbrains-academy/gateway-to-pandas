import pandas as pd

# Sample DataFrame
data = {
    "Product": ["A", "A", "A", "B", "B", "B", "C", "C", "C"] * 2,
    "City": ["London", "New York", "Tokyo"] * 3 * 2,
    "Year": [2022] * 9 + [2023] * 9,
    "Sales": [100, 150, 200, 120, 170, 220, 140, 190, 240] * 2,
}

df = pd.DataFrame(data).set_index(["Product", "City", "Year"])

print("Original DataFrame:")
print(df)

# Stacking the DataFrame
stacked_df = df.stack()

print("\nStacked DataFrame:")
print(stacked_df)
