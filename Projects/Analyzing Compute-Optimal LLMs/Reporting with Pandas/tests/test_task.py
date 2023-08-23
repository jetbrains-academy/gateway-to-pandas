import unittest
import pandas as pd

from task import year_stats_styler


class YearStatsStylerTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Model name': ['A', 'B', 'C', 'D', 'E'],
            'Year': [2020, 2021, 2021, 2022, 2022],
            'Parameters': [1.0, 1.5, 2.0, 2.5, 3.0],
            'Training tokens': [10, 20, 30, 40, 50]
        })

    def test_year_stats_styler(self):
        styler = year_stats_styler(self.df)
        self.assertIsInstance(styler, pd.io.formats.style.Styler)

        # Test the underlying DataFrame of the Styler object
        styler_df = styler.data
        self.assertEqual(styler_df.index.name, 'Year')
        self.assertEqual(styler_df.iloc[0, 0], 1)
        self.assertEqual(styler_df.iloc[1, 0], 2)
        self.assertEqual(styler_df.iloc[2, 0], 2)


if __name__ == '__main__':
    unittest.main()
