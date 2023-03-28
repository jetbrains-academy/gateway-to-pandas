import unittest
import pandas as pd
import numpy as np

from task import drop_duplicates_id, fillna, correct_inconsistency

class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        data = {
            'ID': [1, 2, 3, 3, 4, 5, 6, 7],
            'Name': ['Alice', 'Bob', 'Charlie', 'Charlie', 'Eve', 'Frank', None, 'Grace'],
            'Age': [25, 30, 22, 22, 28, None, 45, 32],
            'Height': [5.5, 6.1, 5.8, 5.8, None, 5.9, 6.2, '5.7'],
        }
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
