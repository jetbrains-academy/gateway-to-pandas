import unittest

from task import load_data, compute_cosine_similarities, get_recommendations

class TestTEDRecommendations(unittest.TestCase):
    filename = '../Intro and data downloading/ted_main.csv'

    def test_load_data(self):
        df = load_data(self.filename)
        self.assertTrue(df.shape[0] > 0)
        self.assertTrue('content' in df.columns)

    def test_compute_cosine_similarities(self):
        df = load_data(self.filename)
        cosine_similarities = compute_cosine_similarities(df)
        self.assertTrue(cosine_similarities.shape[0] > 0)

    def test_get_recommendations(self):
        df = load_data(self.filename)
        cosine_similarities = compute_cosine_similarities(df)
        recs = get_recommendations('The power of vulnerability', df, cosine_similarities)
        self.assertTrue(len(recs) == 10)

if __name__ == '__main__':
    unittest.main()
