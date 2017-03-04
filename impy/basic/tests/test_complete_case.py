"""test_complete_case.py"""
import unittest
import numpy as np
from impy.basic import complete_case


class TestCC(unittest.TestCase):
    """ Test Complete Case """
    def setUp(self):
        """Setup"""
        self.data = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

    def tearDown(self):
        """Teardown"""
        pass

    def test_return_type(self):
        """CC Check if it returns numpy's ndarray"""
        output_type = str(type(complete_case(self.data)))
        self.assertEqual(output_type, "<class 'numpy.ndarray'>")

    def test_no_missing(self):
        """CC Check if nothing's missing nothing should change"""
        actual = complete_case(self.data)
        self.assertTrue(np.array_equal(actual, self.data))

    def test_missing(self):
        """CC Check if it drops the row if there's a missing data point"""
        self.data = np.array([[np.nan, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
        actual = complete_case(self.data)
        self.assertTrue(np.shape(actual) == (2, 3))


if __name__ == "__main__":
    unittest.main()
