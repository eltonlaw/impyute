"""test_averaging_imputations.py"""
import unittest
import numpy as np
from impy.imputations import mean_imputation
from impy.imputations import mode_imputation
from impy.imputations import median_imputation
from impy.datasets import random_uniform


class TestAveraging(unittest.TestCase):
    """ Tests for Averaging """
    def setUp(self):
        self.data = random_uniform(missingness="complete")

    def test_mean_return_type(self):
        """Mean Imputation Return Type"""
        self.assertEqual(str(type(mean_imputation(self.data))),
                         "<class 'numpy.ndarray'>")

    def test_mode_return_type(self):
        """Mode Imputation Return Type"""
        self.assertEqual(str(type(mode_imputation(self.data))),
                         "<class 'numpy.ndarray'>")

    def test_median_return_type(self):
        """Median Imputation Return Type"""
        self.assertEqual(str(type(median_imputation(self.data))),
                         "<class 'numpy.ndarray'>")

    def test_mean_fill(self):
        """ Mean Imputation Fill Complete Data(nothing should happen)"""
        actual = mean_imputation(self.data)
        self.assertTrue(np.array_equal(actual, self.data))

    def test_mode_fill(self):
        """ Mode Imputation Fill Complete Data(nothing should happen)"""
        actual = mode_imputation(self.data)
        self.assertTrue(np.array_equal(actual, self.data))

    def test_median_fill(self):
        """ Median Imputation Fill Complete Data(nothing should happen)"""
        actual = median_imputation(self.data)
        self.assertTrue(np.array_equal(actual, self.data))


if __name__ == "__main__":
    unittest.main()
