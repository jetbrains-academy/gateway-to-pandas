# Introduction
TED Talks are influential videos from expert speakers on a wide range of topics encompassing education, business, science, tech, creativity, and much more. The acronym TED stands for Technology, Entertainment, and Design, and it originated from a conference in 1984. These talks are known for their engaging and inspiring content, typically short in length — most talks are less than 18 minutes — allowing for the ideas to be easily consumed and shared.

TED Talks are globally recognized and have a large audience base due to their accessibility — they are free to watch online and are subtitled in numerous languages. The central principle of TED Talks is the dissemination of ideas to inspire and instigate change. 

With over thousands of talks to explore, finding the right TED Talk to watch can be a daunting task, making the use of data analysis an interesting approach to find a suitable talk to watch.

# Data downloading task
We will use [TED Talks dataset](https://www.kaggle.com/datasets/rounakbanik/ted-talks) from Kaggle. To download a dataset directly to your local machine using Python, you need to use the Kaggle API. Before we get started, you need to set up your Kaggle API credentials.

Here's how you can do it:
1. Go to your account page on Kaggle (https://www.kaggle.com/me/account), scroll down to the API section and click on "Create New API Token". This will download a `kaggle.json` file that contains your username and API key.
2. Move this file to the location `~/.kaggle/kaggle.json` (create the `.kaggle` directory if it does not exist).

Once your API credentials are set up, you can use Python code in `task.py` to download the dataset. This script will download and unzip the `ted-talks` dataset to the current directory.

This script uses the `kaggle` Python package, which you may need to install if it is not already installed. You can install it using pip:

```bash
pip install kaggle
```

**Important Note:** Be sure to keep your `kaggle.json` file secure as it contains your API credentials. You should also add it to your `.gitignore` file if you are using Git to prevent it from being committed to a public repository.

# Bonus task
Simply run all the cells in Jupyter Notebook [main.ipynb](`file://main.ipynb`) located here in the same folder and enjoy the results.
