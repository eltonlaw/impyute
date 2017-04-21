"""test_complete_case.py"""
import unittest
import numpy as np
from impyute.datasets import test_data
from impyute.deletions import complete_case


class TestCC(unittest.TestCase):
    """ Test Complete Case """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        self.data_c = test_data(mask)
        mask[0][0] = True
        self.data_m = test_data(mask)

    def tearDown(self):
        """Teardown"""
        pass

    def test_return_type(self):
        """Return type = np array"""
        output_type = str(type(complete_case(self.data_c)))
        self.assertEqual(output_type, "<class 'numpy.ndarray'>")

    def test_no_missing(self):
        """If nothing's missing nothing should change"""
        actual = complete_case(self.data_c)
        self.assertTrue(np.array_equal(actual, self.data))

    def test_missing(self):
        """CC Check if it drops the row if there's a missing data point"""
        actual = complete_case(self.data_m)
        self.assertTrue(np.shape(actual) == (2, 3))


if __name__ == "__main__":
    unittest.main()
