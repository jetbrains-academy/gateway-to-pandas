import unittest

from task import download_csv_with_retries


class TestCase(unittest.TestCase):
    def setUp(self):
        # Set up the environment before testing
        self.url = 'https://raw.githubusercontent.com/jetbrains-academy/pandas-tutorial/main/import_stats.csv'
        self.df = download_csv_with_retries(self.url)
        self.expected_columns = ['fq_name', 'count']

    def test_dataframe_shape(self):
        self.assertEqual(self.df.shape, (134891, 2), "The DataFrame shape is incorrect.")

    def test_dataframe_columns(self):
        self.assertEqual(list(self.df.columns), self.expected_columns, "The DataFrame columns are incorrect.")
