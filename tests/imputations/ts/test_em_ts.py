"""test_em.py"""
import unittest
import numpy as np
from impyute.imputations.ts import em
from impyute.datasets import test_data


class TestEM_ts(unittest.TestCase):
    """ Tests for EM with Kalman Filter """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][4] = True
        self.data_m = test_data(mask)

    @unittest.skip("function unfinished")
    def test_return_type(self):
        """Check return type, should return an np.ndarray"""
        imputed = em(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    @unittest.skip("function unfinished")
    def test_fill(self):
        """After imputation, no NaN's should exist"""
        imputed = em(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
