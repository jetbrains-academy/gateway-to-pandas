import unittest
import pandas as pd
from task import create_dataframe, add_month_salary, add_annual_salary_in_thousands

class TestEmployeeData(unittest.TestCase):

    def test_add_month_salary(self):
        df = create_dataframe()
        add_month_salary(df, [50000, 500000, 700000, 1000000])
        expected_month_salaries = pd.Series([50000, 500000, 700000, 1000000], name='Month salary')
        pd.testing.assert_series_equal(df['Month salary'], expected_month_salaries)

    def test_add_annual_salary_in_thousands(self):
        df = create_dataframe()
        add_month_salary(df, [50000, 500000, 700000, 1000000])
        add_annual_salary_in_thousands(df)
        expected_annual_salaries = pd.Series([600, 6000, 8400, 12000], name='Annual salary in thousands')
        pd.testing.assert_series_equal(df['Annual salary in thousands'], expected_annual_salaries)

if __name__ == '__main__':
    unittest.main()
