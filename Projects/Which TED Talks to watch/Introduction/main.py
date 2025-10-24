import os
import zipfile

from kaggle.api.kaggle_api_extended import KaggleApi

# Instantiate the API class
api = KaggleApi()

# Authenticate the API
api.authenticate()

# Define the path where you want to download the dataset
path = './' # current directory

# Download the dataset
api.dataset_download_file('rounakbanik/ted-talks', 'ted_main.csv', path=path, force=True)

# Unzip the dataset file
with zipfile.ZipFile(os.path.join(path, "ted_main.csv.zip"), 'r') as zip_ref:
    zip_ref.extractall(path)
