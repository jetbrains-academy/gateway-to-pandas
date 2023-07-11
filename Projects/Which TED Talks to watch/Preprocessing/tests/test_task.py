import unittest
from scipy.sparse import issparse

from task import process_ted_talks

class TestTedTalkProcessing(unittest.TestCase):
    def test_process_ted_talks(self):
        filename = '../Intro and data downloading/ted_main.csv'
        X = process_ted_talks(filename)

        # test if the returned object is a sparse matrix (as returned by TfidfVectorizer)
        self.assertTrue(issparse(X))

        # test if the shape of the matrix is as expected
        # note that the exact numbers would depend on your data
        self.assertEqual((2550, 15984), X.shape)

if __name__ == '__main__':
    unittest.main()
