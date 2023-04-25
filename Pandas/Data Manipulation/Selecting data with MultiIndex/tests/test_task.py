import unittest
import pandas as pd
import pandas.testing as pdt

from task import df, select_2022_columns


class TestMultiIndex(unittest.TestCase):

    def test_xs_2022(self):
        actual = select_2022_columns(df)

        expected_data = {
            "Sales": [7000, 2000, 7000, 4000, 5000, 5000, 1000],
            "Offers": [70, 20, 10, 70, 40, 50, 50],
        }
        expected = pd.DataFrame(expected_data, index=actual.index, columns=actual.columns)

        pdt.assert_frame_equal(actual, expected)


if __name__ == '__main__':
    unittest.main()
