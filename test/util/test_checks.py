"""test_checks.py"""
import unittest
import numpy as np
from impyute.util import BadInputError
from impyute.util import checks

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
            self.foo(arr)
        except BadInputError as e:
            self.fail(e)

    def test_1d(self):
        """ Check 1d array, BadInputError raised"""
        arr = np.array([np.nan, 2])
        with self.assertRaises(BadInputError):
            self.foo(arr)

    def test_not_nparray(self):
        """ If not an np.array, BadInputError raised"""
        with self.assertRaises(BadInputError):
            self.foo([[np.nan, 2.], [3, 4]])

    def test_nan_exists(self):
        """ If no NaN, BadInputError raised"""
        with self.assertRaises(BadInputError):
            self.foo(np.array([[1.]]))

if __name__ == "__main__":
    unittest.main()
