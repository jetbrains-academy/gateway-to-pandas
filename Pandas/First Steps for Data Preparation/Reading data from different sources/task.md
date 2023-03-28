## Reading data from different sources

Pandas provides extensive support for reading data from various sources. One of the most popular method [pandas.read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv) allows you to read a comma-separated values (csv) file into DataFrame. It also supports optionally iterating or breaking of the file into chunks.

```python
import pandas as pd

filepath_or_buffer = 'somedata.csv'
df = pd.read_csv(filepath_or_buffer)
```

Any valid string path is acceptable as value of `filepath_or_buffer`. The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. A local file could be: file://localhost/path/to/table.csv.

If you want to pass in a path object, pandas accepts any `os.PathLike`. By file-like object, we refer to objects with a `read()` method, such as a file handle (e.g. via builtin `open` function) or `StringIO`.

Some interesting examples of reading data from different sources:

1. Reading from a compressed file
```python
import pandas as pd

filename = 'somedata.csv.gz'  # gzipped CSV file
df = pd.read_csv(filename, compression='gzip')
```
2. Reading directly from cloud storages: Amazon S3 example is below, and also Google Cloud Storage (GCS) is possible.
```python
import pandas as pd
# you need to `pip install boto3`
import boto3
from io import StringIO

# Set up S3 client
s3 = boto3.client('s3', aws_access_key_id='YOUR_ACCESS_KEY', aws_secret_access_key='YOUR_SECRET_KEY')

# Define bucket and object key
bucket_name = 'your-bucket-name'
file_key = 'path/to/data.csv'

# Read object from S3 and decode
obj = s3.get_object(Bucket=bucket_name, Key=file_key)
file_content = obj['Body'].read().decode('utf-8')

# Load data into DataFrame
csv_data = StringIO(file_content)
df = pd.read_csv(csv_data)
```

### Task
* Implement reading data from CSV file to pandas DataFrame.
