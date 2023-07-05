### Conditional filtering
One common approach is to use conditional statements to create boolean masks that
 indicate which rows satisfy the given conditions. For instance, you can use comparison 
operators, such as greater than (>), less than (<), equal to (==), and logical operators, 
like and, or, and not, to define the conditions. Applying these conditions to the DataFrame 
using square brackets allows you to filter the data and obtain a subset that meets the 
specified criteria.

- Filtering with one or multiple conditions:

```python
# Filtering based on multiple conditions
filtered_data = df[(df['column1'] > 10) & (df['column2'] == 'A')]
```
This filters the DataFrame df to include only the rows where the values in the column 'column1' 
are greater than 10 and the values in the column 'column2' are equal to 'A'. 
The & operator is used for the logical 'and' operation.

- Filtering with string methods:
You can use built-in string methods, such as `starts_with`, `contains`, `ends_with`, and so on, to filter strings.
```python
# Filtering based on string values
filtered_data = df[df['column'].str.contains('apple', case=False)]
```
This filters the DataFrame to include only the rows where the values in the column 'column' 
contain the substring 'apple'. The str.contains() method performs a case-insensitive search.

- Filtering with negation:
```python
# Filtering with negation
filtered_data = df[~(df['column'] == 'A')]
```
This filters the DataFrame to exclude the rows where the values in the 'column' 
column are equal to 'A'. The ~ operator is used to negate the condition.

- Filtering with `isin()`:
```python
# Filtering based on multiple values
values_to_filter = ['A', 'B', 'C']
filtered_data = df[df['column_name'].isin(values_to_filter)]
```
This filters the DataFrame to include only the rows where the values in the column 
'column_name' are present in the values_to_filter list.

## Task
In the DataFrame, leave only the data that meets the following criteria:
1. Age is less than or equal to 60.
2. Name starts with A or D.
3. Surname is not "Brown".
