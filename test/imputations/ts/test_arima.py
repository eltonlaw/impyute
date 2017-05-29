"""test_arima.py"""
import unittest
import numpy as np
from impyute.imputations.ts import arima
from impyute.datasets import test_data


class TestArima(unittest.TestCase):
    """ Tests for Autoregressive Integrated Moving Average """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incomplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][0] = True
        self.data_m = test_data(mask)

    @unittest.skip("function unfinished")
    def test_return_type(self):
        """Check return type, should return an np.ndarray"""
        imputed = arima(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    @unittest.skip("function unfinished")
    def test_impute_no_missing_values(self):
        """ After imputation, no change should occur"""
        imputed = arima(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    @unittest.skip("function unfinished")
    def test_impute_missing_values(self):
        """After imputation, no NaN's should exist"""
        imputed = arima(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
