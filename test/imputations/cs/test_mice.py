"""test_mice.py"""
import unittest
import numpy as np
from impyute.datasets import test_data
from impyute.imputations.cs import mice


class TestEM(unittest.TestCase):
    """ Tests for Multivariate Imputation by Chained Equations"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask=mask)
        mask[0][0] = True
        self.data_m = test_data(mask=mask)

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = mice(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = mice(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

if __name__ == "__main__":
    unittest.main()
