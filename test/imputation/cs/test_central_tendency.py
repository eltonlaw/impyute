"""test_averagings.py"""
import unittest
import numpy as np
import impyute as impy


class TestAveraging(unittest.TestCase):
    """ Tests for Averaging Imputations"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = impy.dataset.test_data(mask=mask)
        mask[0][0] = True
        self.data_m = impy.dataset.test_data(mask=mask)

    def test_mean_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.mode(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_mode_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.mode(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_median_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.mode(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_mean_impute_missing_values(self):
        """ After imputation, no Nan's should exist"""
        imputed = impy.mean(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_mode_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = impy.mode(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_median_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = impy.median(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
