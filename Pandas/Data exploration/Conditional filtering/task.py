import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Demetra', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Kuang', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})


def filter(df):  # return filtered df
    filtered = df[df.age <= 60]
    filtered = filtered[(filtered.name.str.startswith('A')) | (filtered.name.str.startswith('D'))]
    filtered = filtered[~(filtered.surname == 'Brown')]
    return filtered


if __name__ == '__main__':
    print(filter(df))
