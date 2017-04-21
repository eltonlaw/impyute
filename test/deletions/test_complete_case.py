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
        """ Check return type, should return an np.ndarray"""
        imputed = complete_case(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_impute_no_missing_values(self):
        """ After imputation, no change should occur"""
        imputed = complete_case(self.data_c)
        self.assertTrue(np.array_equal(imputed, self.data_c))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = complete_case(self.data_m)
        self.assertTrue(np.shape(imputed) == (4, 5))


if __name__ == "__main__":
    unittest.main()
