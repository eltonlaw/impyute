"""test_locf.py"""
import unittest
import numpy as np
import impyute as impy


class TestLOCF(unittest.TestCase):
    """ Tests for Last Observation Carried Forward """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = impy.dataset.test_data(mask=mask)
        mask[0][0] = True
        self.data_m = impy.dataset.test_data(mask=mask)

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = impy.locf(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.locf(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_na_at_i_start(self):
        """Check if null value at a row[0],column[0]=row[1],column[0]"""
        self.data_c[0][0] = np.nan
        actual = impy.locf(self.data_c, axis=1)
        self.data_c[0][0] = self.data_c[1][0]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_na_at_i(self):
        """Check if a null row[i],column[j]=row[i-1],column[j]"""
        self.data_c[3][3] = np.nan
        actual = impy.locf(self.data_c, axis=1)
        self.data_c[3][3] = self.data_c[2][3]
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_na_at_i_end(self):
        """Check if at row[last_i],column[i]=row[last_i-1],column[i]"""
        last_i = np.shape(self.data_c)[0]-1
        self.data_c[last_i][3] = np.nan
        actual = impy.locf(self.data_c, axis=1)
        self.data_c[last_i][3] = self.data_c[last_i-1][3]
        self.assertTrue(np.array_equal(actual, self.data_c))


if __name__ == "__main__":
    unittest.main()
