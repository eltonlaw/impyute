"""test_fast_knn.py"""
import unittest
import numpy as np
import impyute as impy
# pylint:disable=invalid-name


class TestFastKNN(unittest.TestCase):
    """ Tests for Fast KNN """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        n = 100
        self.data_c = np.random.normal(size=n*n).reshape((n, n))
        self.data_m = self.data_c.copy()
        for _ in range(int(n*0.3*n)):
            self.data_m[np.random.randint(n)][np.random.randint(n)] = np.nan

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.fast_knn(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = impy.fast_knn(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
