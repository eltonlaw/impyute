"""test_averaging_imputations.py"""
import unittest
import numpy as np
from impy.imputations.cs import mean_imputation
from impy.imputations.cs import mode_imputation
from impy.imputations.cs import median_imputation
from impy.datasets import test_data


class TestAveraging(unittest.TestCase):
    """ Tests for Averaging Imputations"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][0] = True
        self.data_m = test_data(mask)

    def test_mean_return_type(self):
        """ Mean - Check if return type is a numpy array"""
        imputed = mode_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_mode_return_type(self):
        """ Mode - Check if return type is a numpy array"""
        imputed = mode_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_median_return_type(self):
        """ Median - Check if return type is a numpy array"""
        imputed = mode_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_mean_do_nothing(self):
        """ Mean - After imputation, no change should occur"""
        imputed = mean_imputation(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_mode_do_nothing(self):
        """ Mode - After imputation, no change should occur"""
        imputed = mode_imputation(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_median_do_nothing(self):
        """ Median - After imputation, no change should occur"""
        imputed = median_imputation(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_mean_fill(self):
        """ Mean - After imputation, no Nan's should exist"""
        imputed = mean_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_mode_fill(self):
        """ Mode - After imputation, no NaN's should exist"""
        imputed = mode_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_median_fill(self):
        """ Median - After imputation, no NaN's should exist"""
        imputed = median_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
