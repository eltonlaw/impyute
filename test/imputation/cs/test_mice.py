"""test_mice.py"""
import unittest
import numpy as np
import impyute as impy

data=np.asarray([[1,2,3,4,5,6,7,8],
            [1,4,6,8,10,12,14,16],
            [0.5,1,1.5,2,2.5,3,3.5,4],
            [0.5,1,1.5,2,2.5,3,3.5,4],
            [3,6,9,12,15,18,21,24],
            [4,8,9,16,20,24,28,32]])


class TestEM(unittest.TestCase):
    """ Tests for Multivariate Imputation by Chained Equations"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((6, 8), dtype=bool)
        self.data_c = data[mask]
        data[0][0] = np.nan
        self.data_m = data

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.mice(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = impy.mice(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

if __name__ == "__main__":
    unittest.main()
