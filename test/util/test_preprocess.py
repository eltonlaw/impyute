"""test_preprocess.py"""
import pytest
import numpy as np
from impyute.util import preprocess
from impyute.imputation.cs import mean

# pylint:disable=redefined-builtin
try:
    raise ModuleNotFoundError
except NameError:
    class ModuleNotFoundError(Exception):
        "placeholder required for python2.7"
        pass
except ModuleNotFoundError:
    pass

# pylint:disable=unused-argument
@preprocess
def mul(arr, **kwargs):
    """Some function that performs an inplace operation on the input. Accepts kwargs"""
    arr *= 25
    return arr


@preprocess
def mul_no_kwargs(arr):
    """Some function that performs an inplace operation on the input"""
    arr *= 25
    return arr


def test_inplace_false():
    """Input should be unchanged if inplace set to false"""
    A = np.ones((5, 5))
    A_copy = A.copy()
    mul(A, inplace=False)
    assert A[0, 0] == A_copy[0, 0]


def test_inplace_true():
    """Input may be changed if inplace set to true and operation is inplace"""
    A = np.ones((5, 5))
    A_copy = A.copy()
    mul(A, inplace=True)
    assert A[0, 0] != A_copy[0, 0]


def test_inplace_false_nokwargs():
    """Test that passed in function doesn't need to set kwargs as parameters
    Input should be unchanged if inplace set to false
    """
    A = np.ones((5, 5))
    A_copy = A.copy()
    # pylint: disable = unexpected-keyword-arg
    mul_no_kwargs(A, inplace=False)
    # pylint: enable = unexpected-keyword-arg
    assert A[0, 0] == A_copy[0, 0]


def test_inplace_true_nokwargs():
    """Test that passed in function doesn't need to set kwargs as parameters
    Input may be changed if inplace set to true and operation is inplace
    """
    A = np.ones((5, 5))
    A_copy = A.copy()
    # pylint: disable = unexpected-keyword-arg
    mul_no_kwargs(A, inplace=True)
    # pylint: enable = unexpected-keyword-arg
    assert A[0, 0] != A_copy[0, 0]


def test_pandas_input():
    """ Input: DataFrame, Output: DataFrame """
    # Skip this test if you don't have pandas
    pytest.importorskip('pandas')

    # Create a DataFrame with a NaN
    A = np.arange(25).reshape((5, 5)).astype(np.float)
    A[0, 0] = np.nan
    A = pd.DataFrame(A)

    # Assert that the output is a DataFrame
    assert isinstance(mean(A), pd.DataFrame)
