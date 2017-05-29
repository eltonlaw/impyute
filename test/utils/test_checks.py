"""test_mcar_test.py"""
import unittest
import numpy as np
import sys
import os
from impyute.utils import checks
# from impyute import datasets


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
        redirect_stdout(True)
        output = checks(np.array([1, 2]))
        redirect_stdout(False)
        self.assertFalse(output)


def redirect_stdout(redirect):
    if redirect:
        sys.stdout = open(os.devnull, "w")
    else:
        sys.stdout.close()
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
