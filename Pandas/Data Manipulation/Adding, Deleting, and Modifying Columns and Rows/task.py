import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(data)
df["City"] = ["London", "New York", "Tokyo", "Berlin"]


def modify(df_):
    df_["Country"] = ["UK", "USA", "Japan", "Germany"]
    df_ = df_.drop("City", axis=1)
    df_["Age"] = df_["Age"] + 1
    new_row = {"Name": "Eva", "Age": 45, "Country": "Germany"}
    df_ = df_.append(new_row, ignore_index=True)
    df_ = df_.drop(2)
    df_.loc[1, ["Name", "Age"]] = ["Robert", 32]
    return df_


df_modified = modify(df)
print(df_modified)
