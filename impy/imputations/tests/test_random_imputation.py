"""test_random_imputation.py"""
import unittest
import numpy as np
from impy.imputations import random_imputation
from impy.datasets import random_uniform


class TestRandomImputation(unittest.TestCase):
    """ Tests for Random Imputation """
    def setUp(self):
        self.data_c = random_uniform(missingness="complete")
        self.data_m = random_uniform(missingness="mcar")

    def test_return_type(self):
        """Random - Check if it returns np's n-dimensional array"""
        self.assertEqual(str(type(random_imputation(self.data_m))),
                         "<type 'numpy.ndarray'>")

    def test_do_nothing(self):
        """ Random - Fill Complete Data(nothing should happen)"""
        actual = random_imputation(self.data_c)
        self.assertTrue(np.array_equal(actual, self.data_c))

    def test_fill(self):
        """ Random - After imputation, no NaN's should exist"""
        imputed = random_imputation(self.data_m)
        self.assertFalse(np.isnan(imputed).any())


if __name__ == "__main__":
    unittest.main()
