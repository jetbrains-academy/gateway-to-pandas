import unittest
import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

from task import lin_reg_fit


class TestLinRegFit(unittest.TestCase):
    def setUp(self):
        # Set up some data that will be used across tests
        self.df = pd.DataFrame({
            'Training tokens': np.array([1.5, 3.2, 4.8, 2.9]),
            'Parameters': np.array([3.4, 1.2, 3.5, 2.4])
        })
        self.model = LinearRegression()
        self.model.fit(np.log(self.df['Training tokens'].values.reshape(-1, 1)),
                       np.log(self.df['Parameters'].values.reshape(-1, 1)))

    def test_lin_reg_fit(self):
        expected_coefs = self.model.coef_
        expected_intercepts = self.model.intercept_
        actual_model = lin_reg_fit(self.df)
        np.testing.assert_array_almost_equal(actual_model.coef_, expected_coefs, decimal=2)
        np.testing.assert_almost_equal(actual_model.intercept_, expected_intercepts, decimal=2)


if __name__ == '__main__':
    unittest.main()
