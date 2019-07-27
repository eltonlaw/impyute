"""test_checks.py"""
import pytest
import numpy as np
from impyute.util import BadInputError
from impyute.util import checks

@checks
def some_fn(data):
    """Dummy fn that has form of np.array -> np.array"""
    return data

def test_correct_input():
    """ Test that an array that should satisfy all checks, no BadInputError should be raised"""
    # Integer np.ndarray (check: `_is_ndarray`, `_shape_2d`, `_nan_exists`)
    arr = np.array([[np.nan, 2], [3, 4]])
    # Cast integer array to float (check: `_dtype_float`)
    arr.dtype = np.float
    try:
        some_fn(arr)
    except BadInputError:
        assert False

def test_1d():
    """ Check 1d array, BadInputError raised"""
    arr = np.array([np.nan, 2])
    with pytest.raises(BadInputError) as excinfo:
        some_fn(arr)
    assert str(excinfo.value) == "No support for arrays that aren't 2D yet."

def test_not_nparray():
    """ If not an np.array, BadInputError raised"""
    with pytest.raises(BadInputError) as excinfo:
        some_fn([[np.nan, 2.], [3, 4]])
    assert str(excinfo.value) == "Not a np.ndarray."

def test_nan_exists():
    """ If no NaN, BadInputError raised"""
    with pytest.raises(BadInputError) as excinfo:
        some_fn(np.array([[1.]]))
    assert str(excinfo.value) == "No NaN's in given data"
