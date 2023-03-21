import unittest
import pandas as pd
import os
from io import StringIO
from task import read_csv_with_header


class TestReadCSVWithHeader(unittest.TestCase):

    def test_read_csv_from_file(self):
        csv_data = 'col1,col2,col3\n1,2,3\n4,5,6\n7,8,9\n10,11,12'
        file_buffer = StringIO(csv_data)
        filename = 'test_data.csv'

        with open(filename, 'w') as f:
            f.write(file_buffer.getvalue())

        df = read_csv_with_header(filename)

        # Cleanup: remove the temporary test file
        os.remove(filename)

        expected_columns = ['col1', 'col2', 'col3']
        self.assertListEqual(df.columns.tolist(), expected_columns)
        self.assertEqual(df.shape, (4, 3))
        self.assertEqual(df.iloc[0, 0], 1)
        self.assertEqual(df.iloc[1, 2], 6)


if __name__ == '__main__':
    unittest.main()
