import unittest
import pandas as pd

from task import data, modify


class TestModifyFunction (unittest.TestCase):
    def test_modify(self):
        df = pd.DataFrame(data)
        df["City"] = ["London", "New York", "Tokyo", "Berlin"]

        df_modified = modify(df)

        expected_data = {
            "Name": ["Alice", "Robert", "David", "Eva"],
            "Age": [26, 32, 41, 45],
            "Country": ["UK", "USA", "Germany", "Germany"]
        }
        expected_df = pd.DataFrame(expected_data)

        pd.testing.assert_frame_equal (df_modified.reset_index(drop=True), expected_df.reset_index(drop=True))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
