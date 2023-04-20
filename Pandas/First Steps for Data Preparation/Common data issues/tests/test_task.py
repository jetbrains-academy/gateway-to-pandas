import unittest
import pandas as pd
import numpy as np

from task import drop_duplicates_id, fillna, correct_inconsistency, data


class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(data)

        self.df_no_duplicates = drop_duplicates_id(self.df)
        self.df_fillna = fillna(self.df_no_duplicates)
        self.df_final = correct_inconsistency(self.df_fillna)

    def test_duplicates_removal(self):
        self.assertEqual(len(self.df_no_duplicates), len(self.df['ID'].unique()), "Duplicates removal failed")

    def test_missing_values(self):
        self.assertFalse(self.df_fillna['Age'].isnull().any(), "Missing values in 'Age' not handled properly")

    def test_inconsistencies(self):
        self.assertTrue(np.issubdtype(self.df_final['Height'].dtype, np.number),
                        "Inconsistencies in 'Height' not corrected")


if __name__ == '__main__':
    unittest.main()
