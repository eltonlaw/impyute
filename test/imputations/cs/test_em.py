"""test_em.py"""
import unittest
import numpy as np
from impyute.datasets import test_data
from impyute.imputations.cs import em


class TestEM(unittest.TestCase):
    """ Tests for Expectation Maximization"""
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
        """ Check return type, should return an np.ndarray"""
        imputed = em(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_impute_no_missing_values(self):
        """ After imputation, no change should occur"""
        imputed = em(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = em(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
