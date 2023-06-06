import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'height': [178, 183, 150, 163, 158, 178, 167],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})

if __name__ == "__main__":
    # Create a bar plot of sales by product category
    df.plot(x='favourite_colour', y='age', kind='bar')

    # Create a scatter plot of sales against advertising spend
    df.plot(x='age', y='height', kind='scatter')

    # Create a histogram of the distribution of ages
    df['age'].plot(kind='hist')

    # Create a Kernel Density Estimate plot of height
    df['height'].plot(kind='kde')
