"""test_locf.py"""
import unittest
import numpy as np
from impy.imputations import locf
from impy.datasets import random_uniform


class TestLOCF(unittest.TestCase):
    """ Tests for Last Observation Carried Forward """
    def setUp(self):
        self.data_c = random_uniform(missingness="complete")
        self.data_m = random_uniform(missingness="mcar")

    def test_return_type(self):
        """LOCF Check if it returns numpy's n-dimensional array"""
        imputed = locf(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_na_at_i_start(self):
        """LOCF Check if null value at a row[i],column[0]=row[i],column[1]"""
        self.data_c[3][0] = np.nan
        actual = locf(self.data_c)
        self.data_c[3][0] = self.data_c[3][1]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_na_at_i(self):
        """LOCF Check if a null row[i],column[j]=row[i],column[j+1]"""
        self.data_c[3][3] = np.nan
        actual = locf(self.data_c)
        self.data_c[3][3] = self.data_c[3][4]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_na_at_i_end(self):
        """LOCF Check nv at row[i],column[last_i]=row[i],column[last-1]"""
        last_i = len(self.data_c[0]) - 1
        self.data_c[3][last_i] = np.nan
        actual = locf(self.data_c)
        self.data_c[3][last_i] = self.data_c[3][last_i-1]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_fill(self):
        """ LOCF - After imputation, no NaN's should exist"""
        imputed = locf(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
