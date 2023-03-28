import unittest
import pandas as pd
from task import create_dataframe, add_month_cost, add_annual_cost_in_thousands

class TestEmployeeData(unittest.TestCase):

    def test_add_month_cost(self):
        df = create_dataframe()
        add_month_cost(df, [50000, 800000, 200000, 500000])
        expected_month_costs = pd.Series([50000, 800000, 200000, 500000], name='Month cost')
        pd.testing.assert_series_equal(df['Month cost'], expected_month_costs)

    def test_add_annual_salary_in_thousands(self):
        df = create_dataframe()
        add_month_cost(df, [50000, 800000, 200000, 500000])
        add_annual_cost_in_thousands(df)
        expected_annual_costs = pd.Series([600, 9600, 2400, 6000], name='Annual cost in thousands')
        pd.testing.assert_series_equal(df['Annual cost in thousands'], expected_annual_costs)

if __name__ == '__main__':
    unittest.main()
