import pandas as pd

def read_csv_with_header(filepath_or_buffer, header=0):
    df = pd.read_csv(filepath_or_buffer, header=header)
    return df

if __name__ == '__main__':
    filepath_or_buffer = 'somedata.csv'
    df = pd.read_csv(filepath_or_buffer, header=2)
    print(df.head())
