### Reading data from different sources

Pandas provides extensive support for reading data from various sources. One of the most popular method [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv) allows you to read a comma-separated values (csv) file into DataFrame. It also supports optionally iterating or breaking of the file into chunks.

```python
import pandas as pd

filepath_or_buffer = 'somedata.csv'
df = pd.read_csv(filepath_or_buffer)
```

Any valid string path is acceptable as value of `filepath_or_buffer`. The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. A local file could be: file://localhost/path/to/table.csv.

If you want to pass in a path object, pandas accepts any `os.PathLike`. By file-like object, we refer to objects with a `read()` method, such as a file handle (e.g. via builtin `open` function) or `StringIO`.

### Task
* Implement reading data from CSV-file to pandas DataFrame.
