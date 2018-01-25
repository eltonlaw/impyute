"""test_checks.py"""
import sys
import os
import unittest
import numpy as np
from impyute.utils import checks
from impyute.utils import BadInputError

class TestChecks(unittest.TestCase):
    """ Tests for checks"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        @checks
        def foo(data):
            return data
        self.foo = foo

    def test_correct_input(self):
        """ Test that an array that should satisfy all checks, no BadInputError should be raised"""
        # Integer np.ndarray (check: `_is_ndarray`, `_shape_2d`, `_nan_exists`)
        arr = np.array([[np.nan, 2], [3, 4]])
        # Cast integer array to float (check: `_dtype_float`)
        arr.dtype = np.float
        try:
            out = self.foo(arr)
        except BadInputError:
            self.fail(e)

    def test_1d(self):
        """ Check 1d array, BadInputError raised"""
        arr = np.array([np.nan, 2])
        with self.assertRaises(BadInputError):
            output = self.foo(arr)

    def test_not_nparray(self):
        """ If not an np.array, BadInputError raised"""
        with self.assertRaises(BadInputError):
            output = self.foo([[np.nan, 2.], [3, 4]])

    def test_nan_exists(self):
        """ If no NaN, BadInputError raised"""
        with self.assertRaises(BadInputError):
            output = self.foo(np.array([[1.]]))

# def _redirect_stdout(redirect):
#     """ Used to avoid printing error messages to screen while running tests"""
#     if redirect:
#         sys.stdout = open(os.devnull, "w")
#     else:
#         sys.stdout.close()
#         sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
