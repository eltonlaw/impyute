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

    def test_return_type(self):
        """Check return type, should return an np.ndarray"""
        imputed = kalman(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_fill(self):
        """After filtering, no NaN's should exist"""
        imputed = kalman(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
