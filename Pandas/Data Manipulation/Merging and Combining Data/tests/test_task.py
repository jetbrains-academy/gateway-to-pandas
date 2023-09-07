import unittest
import pandas as pd

from task import merge_dataframes, filter_dataframe_by_license, count_imports


class TestFunctions(unittest.TestCase):
    def test_merge_dataframes(self):
        df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df2 = pd.DataFrame({"A": [1, 2], "C": [5, 6]})
        result = merge_dataframes(df1, df2, "A")
        expected = pd.DataFrame({"A": [1, 2], "B": [3, 4], "C": [5, 6]})
        pd.testing.assert_frame_equal(result, expected)

    def test_filter_dataframe_by_license(self):
        data = {"project_name": ["a", "b", "c"],
                "license": ["MIT License", "Apache License 2.0", "Other"]}
        df = pd.DataFrame(data)
        result = filter_dataframe_by_license(df, ["MIT License", "Apache License 2.0"])
        expected = pd.DataFrame({"project_name": ["a", "b"],
                                 "license": ["MIT License", "Apache License 2.0"]})
        pd.testing.assert_frame_equal(result, expected)

    def test_count_imports(self):
        data = {"import": ["a", "b", "a", "c", "b", "a"]}
        df = pd.DataFrame(data)
        result = count_imports(df, "import")
        print(result)
        expected = pd.Series({"a": 3, "b": 2, "c": 1},
                             index=pd.Index(['a', 'b', 'c'], dtype='object', name='import'),
                             name='count')
        print(expected)
        pd.testing.assert_series_equal(result, expected)
