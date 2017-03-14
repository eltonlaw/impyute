"""test_random_imputation.py"""
import unittest
import numpy as np
from impy.imputations import random_imputation
from impy.datasets import random_uniform


class TestLOCF(unittest.TestCase):
    """ Tests for Random Imputation """
    def setUp(self):
        self.data = random_uniform(missingness="complete")

    def test_return_type(self):
        """Random Imputation: Check if it returns np's n-dimensional array"""
        self.assertEqual(str(type(random_imputation(self.data))),
                         "<class 'numpy.ndarray'>")

    def test_filled(self):
        """ Random Imputation: Fill Complete Data(nothing should happen)"""
        actual = random_imputation(self.data)
        self.assertTrue(np.array_equal(actual, self.data))


if __name__ == "__main__":
    unittest.main()
