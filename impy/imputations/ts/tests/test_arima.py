"""test_arima.py"""
import unittest
import numpy as np
from impy.imputations.ts import arima
from impy.datasets import test_data


class TestArima(unittest.TestCase):
    """ Tests for Autoregressive Integrated Moving Average """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][0] = True
        self.data_m = test_data(mask)

    def test_return_type(self):
        """Check return type, should return an np.ndarray"""
        imputed = arima(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_fill(self):
        """After imputation, no NaN's should exist"""
        imputed = arima(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
