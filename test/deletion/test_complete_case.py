"""test_complete_case.py"""
import unittest
import numpy as np
from impyute.dataset import test_data
from impyute.deletion import complete_case
from impyute.util import checks

@checks
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

    def test_imputed_values(self):
        """ Assert values are as expected"""
        imputed = complete_case(self.data_m)
        expected = np.array([
            [5., 6., 7., 8., 9.],
            [10., 11., 12., 13., 14.],
            [15., 16., 17., 18., 19.],
            [20., 21., 22., 23., 24.]
        ])
        self.assertTrue(np.equal(imputed, expected).all())


if __name__ == "__main__":
    unittest.main()
