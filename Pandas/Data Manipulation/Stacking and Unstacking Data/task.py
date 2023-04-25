import pandas as pd

# Sample DataFrame
data = {
    "Product": ["A", "A", "A", "B", "B", "B", "C", "C", "C"] * 2,
    "City": ["London", "New York", "Tokyo"] * 3 * 2,
    "Year": [2022] * 9 + [2023] * 9,
    "Sales": [100, 150, 200, 120, 170, 220, 140, 190, 240] * 2,
}


def create_multiindex_df(data):
    return pd.DataFrame(data).set_index(["Product", "City", "Year"])


df = create_multiindex_df(data)
print("Original DataFrame:")
print(df)


def unstack_year(df):
    return df.unstack(level="Year")


# unstacking the DataFrame
unstacked_df = unstack_year(df)

print("\nUnstacked DataFrame:")
print(unstacked_df)
