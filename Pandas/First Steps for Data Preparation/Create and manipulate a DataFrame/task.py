import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['Saint Petersburg', 'New York', 'Prague', 'Paphos']
    }

    return pd.DataFrame(data)

def add_month_salary(df, month_salaries):
    df['Month salary'] = month_salaries

def add_annual_salary_in_thousands(df):
    df['Annual salary in thousands'] = 12 * df['Month salary'] // 1000

if __name__ == "__main__":
    df = create_dataframe()
    add_month_salary(df, [50000, 500000, 700000, 1000000])
    add_annual_salary_in_thousands(df)
    print(df)
