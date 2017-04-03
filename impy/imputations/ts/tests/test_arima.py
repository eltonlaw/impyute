"""test_arima.py"""
import unittest
import numpy as np
from impy.imputations import arima
from impy.datasets import random_uniform


class TestArima(unittest.TestCase):
    """ Tests for Autoregressive Integrated Moving Average """
    def setUp(self):
        self.data_c = random_uniform(missingness="complete")
        self.data_m = random_uniform(missingness="mcar")

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
