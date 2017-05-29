"""test_mcar_test.py"""
import unittest
import numpy as np
# from impyute import datasets
from impyute.utils import checks


class TestChecks(unittest.TestCase):
    """ Tests for checks"""
    def test_return_type(self):
        """ Check return type, should return a boolean"""
        output = checks(np.array([[1., 2.], [3, 4]]))
        self.assertEqual(type(output), type(True))

    def test_2d(self):
        """ Check 2d array, should return true"""
        output = checks(np.array([[1., 2.], [3, 4]]))
        self.assertTrue(output)

    def test_not_2d(self):
        """ Check 1d array, should return false"""
        output = checks(np.array([1, 2]))
        self.assertFalse(output)


if __name__ == "__main__":
    unittest.main()
