"""test_mcar_test.py"""
import sys
import os
import unittest
import numpy as np
from impyute.utils import checks


class TestChecks(unittest.TestCase):
    """ Tests for checks"""
    def test_return_type(self):
        """ Check return type, should return a boolean"""
        _redirect_stdout(True)
        output = checks(np.array([[1., 2.], [3, 4]]))
        _redirect_stdout(False)
        self.assertEqual(type(output), type(False))

    def test_correct_input(self):
        """ Test that an array that satisfies all checks returns True"""
        # Integer np.ndarray (check: `_is_ndarray`, `_shape_2d`)
        arr = np.array([[1, 2], [3, 4]])
        # Cast integer array to float (check: `_dtype_float`)
        arr.dtype = np.float
        # Add a nan value to the array (check: `_nan_exists`)
        arr[0][0] = np.nan
        output = checks(arr)
        self.assertTrue(output)

    def test_1d(self):
        """ Check 1d array, should return false"""
        _redirect_stdout(True)
        arr = np.array([np.nan, 2])
        output = checks(arr)
        _redirect_stdout(False)
        self.assertFalse(output)

    def test_2d(self):
        """ Check 2d array, should return true"""
        arr = np.array([[1., 2.], [3, 4]])
        arr[0][0] = np.nan
        output = checks(arr)
        self.assertTrue(output)

    def test_3d_false(self):
        """ Check 3d array without setting allow_3d=True, should return false"""
        _redirect_stdout(True)
        arr = np.ones((5, 5, 3))
        arr[0][0][0] = np.nan
        output = checks(arr)
        _redirect_stdout(False)
        self.assertFalse(output)

    def test_3d_true(self):
        """ Check 3d array setting allow_3d=True, should return true"""
        arr = np.ones((5, 5, 3))
        arr[0][0][0] = np.nan
        output = checks(arr, allow_3d=True)
        self.assertTrue(output)

    def test_not_nparray(self):
        """ If not an np.array, should return false"""
        _redirect_stdout(True)
        output = checks([[np.nan, 2.], [3, 4]])
        _redirect_stdout(False)
        self.assertEqual(output, False)

    def test_nan_exists(self):
        """ If no NaN, should return false"""
        _redirect_stdout(True)
        output = checks(np.array([[1., 2.], [3, 4]]))
        _redirect_stdout(False)
        self.assertEqual(output, False)

def _redirect_stdout(redirect):
    """ Used to avoid printing error messages to screen while running tests"""
    if redirect:
        sys.stdout = open(os.devnull, "w")
    else:
        sys.stdout.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
