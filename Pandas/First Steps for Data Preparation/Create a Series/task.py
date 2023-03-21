import pandas as pd


def create_series(dict_: dict):
    return pd.Series(dict_)


if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie", "David"]
    name_lengths = {name : len(name) for name in students}
    series = create_series(name_lengths)
    print(series)
