"""test_locf.py"""
import unittest
import numpy as np
from impy.imputations import locf
from impy.datasets import random_int


class TestLOCF(unittest.TestCase):
    """ Tests for Last Observation Carried Forward """
    def setUp(self):
        self.data = random_int(missingness="complete")

    def test_return_type(self):
        """LOCF Check if it returns numpy's n-dimensional array"""
        self.assertEqual(str(type(locf(self.data))), "<class 'numpy.ndarray'>")

    def test_na_at_i_start(self):
        """LOCF Check if null value at a row[i],column[0]=row[i],column[1]"""
        self.data[3][0] = np.nan
        actual = locf(self.data)
        self.data[3][0] = self.data[3][1]
        self.assertTrue(np.array_equal(actual, self.data))

    def test_na_at_i(self):
        """LOCF Check if a null row[i],column[j]=row[i],column[j+1]"""
        self.data[3][3] = np.nan
        actual = locf(self.data)
        self.data[3][3] = self.data[3][4]
        self.assertTrue(np.array_equal(actual, self.data))

    def test_na_at_i_end(self):
        """LOCF Check nv at row[i],column[last_i]=row[i],column[last-1]"""
        last_i = len(self.data[0]) - 1
        self.data[3][last_i] = np.nan
        actual = locf(self.data)
        self.data[3][last_i] = self.data[3][last_i-1]
        self.assertTrue(np.array_equal(actual, self.data))


if __name__ == "__main__":
    unittest.main()
