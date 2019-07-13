"""test_preprocess.py"""
import unittest
import numpy as np
from impyute.util import preprocess
from impyute.imputation.cs import mean

# TODO:Some hacky ass code to handle python2 not having `ModuleNotFoundError`
try:
    raise ModuleNotFoundError
except NameError:
    class ModuleNotFoundError(Exception):
        pass
except ModuleNotFoundError:
    pass

class TestPreprocess(unittest.TestCase):
    """ Tests for checks"""
    def setUp(self):
        @preprocess
        def mul(arr, **kwargs):
            arr *= 25
            return arr
        self.mul = mul

        @preprocess
        def mul_no_kwargs(arr):
            arr *= 25
            return arr
        self.mul_no_kwargs = mul_no_kwargs

    def test_inplace_false(self):
        A = np.ones((5, 5))
        A_copy = A.copy()
        self.mul(A, inplace=False)
        assert A[0][0] == A_copy[0][0]

    def test_inplace_true(self):
        A = np.ones((5, 5))
        A_copy = A.copy()
        self.mul(A, inplace=True)
        assert A[0][0] != A_copy[0][0]

    def test_inplace_false_nokwargs(self):
        A = np.ones((5, 5))
        A_copy = A.copy()
        # pylint: disable = unexpected-keyword-arg
        self.mul_no_kwargs(A, inplace=False)
        # pylint: enable = unexpected-keyword-arg
        assert A[0][0] == A_copy[0][0]

    def test_inplace_true_nokwargs(self):
        A = np.ones((5, 5))
        A_copy = A.copy()
        # pylint: disable = unexpected-keyword-arg
        self.mul_no_kwargs(A, inplace=True)
        # pylint: enable = unexpected-keyword-arg
        assert A[0][0] != A_copy[0][0]

    def test_pandas_input(self):
        """ Input: DataFrame, Output: DataFrame """
        # Skip this test if you don't have pandas
        try:
            import pandas as pd
        except (ModuleNotFoundError, ImportError):
            return True

        # Create a DataFrame with a NaN
        A = np.arange(25).reshape((5,5)).astype(np.float)
        A[0][0] = np.nan
        A = pd.DataFrame(A)

        # Assert that the output is a DataFrame
        assert isinstance(mean(A), pd.DataFrame)

if __name__ == "__main__":
    unittest.main()

