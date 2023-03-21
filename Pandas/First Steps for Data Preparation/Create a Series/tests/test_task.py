import unittest

import pandas as pd
from task import create_series


class TestCase(unittest.TestCase):
    def test_simple(self):
        expected_series = pd.Series(5, index=['Alice'])
        pd.testing.assert_series_equal(create_series({'Alice' : 5}), expected_series)
