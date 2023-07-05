Exploring data is an important first step in any data analysis project. 
Pandas provides a variety of tools for exploring and summarizing data, 
including `describe()`, `info()`, and `shape`.
These functions allow you to 
quickly understand the size and structure of your dataset, as well as basic 
statistics, like mean, standard deviation, and quartiles.

### `describe()`

The `describe()` function in pandas provides a comprehensive summary of numerical and 
categorical data. It calculates statistics, like count, mean, standard deviation, 
minimum, maximum, quartiles, and more. It helps understand data distribution, 
identify outliers, and check for missing values.

`describe()` works with different data types and has different statistics for each data type.

Basic syntax:
```python
data_frame.describe(percentiles=None, include='all')
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })
df.describe()  # By default only numeric columns are included
df.describe(include='all')  # include all columns
df.describe(include=[object])  # include only object columns
```

### `info()`
It returns the description of every column (its type, non-null counts, and memory usage).

Basic syntax:
```python
data_frame.info(verbose=True, memory_usage=True)
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'categorical': pd.Categorical(['d','e','f']),
                   'numeric': [1, 2, 3],
                   'object': ['a', 'b', 'c']
                  })
df.info(verbose=True, memory_usage=True)
```



### `value_count()`
It return the counts of unique rows in the DataFrame. If you specify the row, 
it will return the counts of unique values in that row.

Basic syntax:
```python
data_frame.value_counts(subset=None)
```

Example:
```python
import pandas as pd

df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith']
                  })
df.value_counts()  # get unique row count 
df.value_counts(subset='surname')  # get unique value counts for row 'surname'
```


### Computing basic statistics

Pandas has a bunch of built-in functions to compute different statistics, which will help you explore your data.
- `df.shape()` — returns the shape of the DataFrame.
- `df.mean(axis=None, skip_na=True)` – returns the mean over the specified axis (defaut axis – columns).
- `df.mode(axis=None)` – returns the mode over the specified axis.
- `df.min(axis=None, skip_na=True)` – returns the min over the specified axis.
- `df.max(axis=None, skip_na=True)` – returns the max over the specified axis.
- `df.sum(axis=None)` – returns the sum of all values over the specified axis.
- `df.std(axis=None)` – returns the standard deviation over the specified axis.
- `df.var(axis=None)` – returns the variance over the specified axis.
- `df.cov()` – returns the covariance table for each pair of columns.
- `df.quantile(q=[0.1, 0.5])` – returns the specified quantiles.
