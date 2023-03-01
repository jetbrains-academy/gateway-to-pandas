import pandas as pd  # Importing the Pandas module

ages = pd.Series([7, 22, 35, 58, 97], name="Age") # Creating a Series object from scratch

# Creating DataFrame, using a Series and Python list and dictionary objects
df = pd.DataFrame(
    {
        "Age": ages,
        "Sex": ["female", "male", "male", "female", "female"],
    }
)

if __name__ == "__main__":
    print(ages)
    print(df)
