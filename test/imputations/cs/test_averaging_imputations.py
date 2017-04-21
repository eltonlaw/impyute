"""test_averaging_imputations.py"""
import unittest
import numpy as np
from impyute.imputations.cs import mean_imputation
from impyute.imputations.cs import mode_imputation
from impyute.imputations.cs import median_imputation
from impyute.datasets import test_data


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
        """ Check return type, should return an np.ndarray"""
        imputed = mode_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_mode_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = mode_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_median_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = mode_imputation(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_mean_impute_no_missing_values(self):
        """ After imputation, no change should occur"""
        imputed = mean_imputation(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_mode_impute_no_missing_values(self):
        """ After imputation, no change should occur"""
        imputed = mode_imputation(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_median_impute_no_missing_values(self):
        """ After imputation, no change should occur"""
        imputed = median_imputation(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_mean_impute_missing_values(self):
        """ After imputation, no Nan's should exist"""
        imputed = mean_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_mode_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = mode_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_median_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = median_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
