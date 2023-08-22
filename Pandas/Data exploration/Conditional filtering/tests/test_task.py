import unittest
import pandas as pd

from task import filter


class TestFunctions(unittest.TestCase):
    def test_sort(self):
        df = pd.DataFrame({'name': ['Adam', 'Brian', 'Christos', 'Dolly', 'Elena', 'Demetra', 'Brian'],
                           'surname': ['Brown', 'Smith', 'Andreou', 'Kuang', 'Blake', 'Andreou', 'Smith'],
                           'age': [23, 45, 12, 22, 73, 34, 45],
                           'favourite_colour': pd.Categorical(
                               ['blue', 'red', 'green', 'yellow', 'pink', 'yellow', 'red'])})
        result = filter(df)
        filtered = df[df.age <= 60]
        filtered = filtered[(filtered.name.str.startswith('A')) | (filtered.name.str.startswith('D'))]
        expected = filtered[~(filtered.surname == 'Brown')]
        pd.testing.assert_frame_equal(result, expected)
