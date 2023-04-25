import unittest
import pandas as pd
import pandas.testing as pdt

from task import data, create_multiindex_df, unstack_year


class TestDataManipulation(unittest.TestCase):
    def test_create_multiindex_df(self):
        df = create_multiindex_df(data)

        # Check the index and columns of the DataFrame
        expected_index = pd.MultiIndex.from_product(
            [["A", "B", "C"], ["London", "New York", "Tokyo"], [2022, 2023]],
            names=["Product", "City", "Year"],
        )
        expected_columns = ["Sales"]

        self.assertTrue(set(df.index) == set(expected_index))
        self.assertListEqual(df.columns.tolist(), expected_columns)

    def test_unstack_year(self):
        df = create_multiindex_df(data)
        unstacked_df = unstack_year(df)

        # Check the index and columns of the unstacked DataFrame
        expected_index = pd.MultiIndex.from_product(
            [["A", "B", "C"], ["London", "New York", "Tokyo"]],
            names=["Product", "City"],
        )
        expected_columns = pd.MultiIndex.from_product(
            [["Sales"], [2022, 2023]], names=[None, "Year"]
        )

        self.assertTrue(unstacked_df.index.equals(expected_index))
        self.assertTrue(unstacked_df.columns.equals(expected_columns))


if __name__ == "__main__":
    unittest.main()
