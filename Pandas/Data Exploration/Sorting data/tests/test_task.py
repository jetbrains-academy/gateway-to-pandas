import unittest
import pandas as pd

from task import sort


class TestFunctions(unittest.TestCase):
    def test_sort(self):
        df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Dolly', 'Brian'],
                   'surname': ['Brown', 'Smith', 'Andreou', 'Brown', 'Blake', 'Andreou', 'Smith'],
                   'age': [23, 45, 12, 22, 73, 34, 45],
                   'favourite_colour': pd.Categorical(['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})
        result = sort(df)
        expected = df.sort_values(by=['surname', 'age'], ascending=False)
        pd.testing.assert_frame_equal(result, expected)
