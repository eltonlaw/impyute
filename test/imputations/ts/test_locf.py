"""test_locf.py"""
import unittest
import numpy as np
from impyute.imputations.ts import locf
from impyute.datasets import test_data


class TestLOCF(unittest.TestCase):
    """ Tests for Last Observation Carried Forward """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][0] = True
        self.data_m = test_data(mask)

    def test_impute_no_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = locf(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = locf(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = locf(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_na_at_i_start(self):
        """Check if null value at a row[i],column[0]=row[i],column[1]"""
        self.data_c[3][0] = np.nan
        actual = locf(self.data_c)
        self.data_c[3][0] = self.data_c[3][1]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_na_at_i(self):
        """Check if a null row[i],column[j]=row[i],column[j+1]"""
        self.data_c[3][3] = np.nan
        actual = locf(self.data_c)
        self.data_c[3][3] = self.data_c[3][4]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_na_at_i_end(self):
        """Check if at row[i],column[last_i]=row[i],column[last-1]"""
        last_i = len(self.data_c[0]) - 1
        self.data_c[3][last_i] = np.nan
        actual = locf(self.data_c)
        self.data_c[3][last_i] = self.data_c[3][last_i-1]
        self.assertTrue(np.array_equal(actual, self.data_c))


if __name__ == "__main__":
    unittest.main()
