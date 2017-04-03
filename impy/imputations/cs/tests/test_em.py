"""test_em.py"""
import unittest
import numpy as np
from impy.datasets import random_uniform
from impy.imputations import em


class TestEM(unittest.TestCase):
    """ Tests for Expectation Maximization"""
    def setUp(self):
        self.data_c = random_uniform(missingness="complete")
        self.data_m = random_uniform(missingness="mcar")

    def test_return_type(self):
        """Check return type, should return an np.ndarray"""
        imputed = em(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_fill(self):
        """After imputation, no NaN's should exist"""
        imputed = em(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
