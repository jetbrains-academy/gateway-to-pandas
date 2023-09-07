import unittest

from task import download_csv_with_retries


class TestCase(unittest.TestCase):
    def setUp(self):
        # Set up the environment before testing
        self.url = 'https://raw.githubusercontent.com/jetbrains-academy/gateway-to-pandas/main/Pandas/import_stats.csv'
        self.df = download_csv_with_retries(self.url)
        self.expected_columns = ['import_name', 'count']

    def test_dataframe_shape(self):
        self.assertEqual((105024, 2), self.df.shape, "The DataFrame shape is incorrect.")

    def test_dataframe_columns(self):
        self.assertEqual(self.expected_columns, list(self.df.columns), "The DataFrame columns are incorrect.")
