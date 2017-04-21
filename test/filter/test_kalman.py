"""test_kalman.py"""
import unittest
import numpy as np
from impyute.filter import kalman
from impyute.datasets import random_uniform


class TestArima(unittest.TestCase):
    """ Tests for Kalman Filter """
    def setUp(self):
        self.data_c = random_uniform(missingness="complete")
        self.data_m = random_uniform(missingness="mcar")

    @unittest.skip("function unfinished")
    def test_return_type(self):
        """Check return type, should return an np.ndarray"""
        imputed = kalman(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    @unittest.skip("function unfinished")
    def test_impute_no_missing_values(self):
        """After fitering, no change should occur"""
        filtered = kalman(self.data_m)
        self.assertTrue(np.array_equal(filtered, self.data_c))

    @unittest.skip("function unfinished")
    def test_impute_missing_values(self):
        """After filtering, no NaN's should exist"""
        filtered = kalman(self.data_m)
        self.assertFalse(np.isnan(filtered).any())


if __name__ == "__main__":
    unittest.main()
