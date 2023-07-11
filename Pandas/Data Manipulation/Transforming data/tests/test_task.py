import unittest
import pandas as pd

from task import total_sales_per_city, average_sales_per_category


class TestSalesFunctions(unittest.TestCase):

    def setUp(self):
        data = {
            "City": ["London", "London", "New York", "New York", "New York", "Tokyo", "Tokyo"],
            "Category": ["Electronics", "Clothing", "Electronics", "Electronics", "Clothing", "Electronics", "Clothing"],
            "Sales": [7000, 2000, 7000, 4000, 5000, 5000, 1000],
            "Offers": [70, 20, 10, 70, 40, 50, 50],
        }
        self.df = pd.DataFrame(data)

    def test_total_sales_per_city(self):
        expected_result = pd.Series({"London": 9000, "New York": 16000, "Tokyo": 6000}, name="Sales")
        expected_result.index.name = "City"
        actual_result = total_sales_per_city(self.df)
        pd.testing.assert_series_equal(actual_result, expected_result)

    def test_average_sales_per_category(self):
        expected_result = pd.Series({"Clothing": 2666.666667, "Electronics": 5750.000000}, name="Sales")
        expected_result.index.name = "Category"
        actual_result = average_sales_per_category(self.df) #.reset_index()
        pd.testing.assert_series_equal(actual_result.round(6), expected_result)


if __name__ == "__main__":
    unittest.main()
