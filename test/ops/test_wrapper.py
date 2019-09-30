import pytest
import numpy as np
from impyute.imputation.cs import mean
from impyute.ops import preprocess
from impyute.ops import BadInputError
from impyute.ops import BadOutputError
from impyute.ops import checks
from impyute.ops import wrapper

# pylint:disable=redefined-builtin
try:
    raise ModuleNotFoundError
except NameError:
    class ModuleNotFoundError(Exception):
        "placeholder required for python2.7"
        pass
except ModuleNotFoundError:
    pass

@preprocess
def preprocess_mul(arr, **kwargs):
    """Some function that performs an inplace operation on the input. Accepts kwargs"""
    arr *= 25
    return arr

@preprocess
def preprocess_mul_no_kwargs(arr):
    """Some function that performs an inplace operation on the input"""
    arr *= 25
    return arr

def test_inplace_false():
    """Input should be unchanged if inplace set to false"""
    A = np.ones((5, 5))
    A_copy = A.copy()
    preprocess_mul(A, inplace=False)
    assert A[0, 0] == A_copy[0, 0]

def test_inplace_true():
    """Input may be changed if inplace set to true and operation is inplace"""
    A = np.ones((5, 5))
    A_copy = A.copy()
    preprocess_mul(A, inplace=True)
    assert A[0, 0] != A_copy[0, 0]

def test_inplace_false_nokwargs():
    """Test that passed in function doesn't need to set kwargs as parameters
    Input should be unchanged if inplace set to false
    """
    A = np.ones((5, 5))
    A_copy = A.copy()
    preprocess_mul_no_kwargs(A, inplace=False)
    assert A[0, 0] == A_copy[0, 0]

def test_inplace_true_nokwargs():
    """Test that passed in function doesn't need to set kwargs as parameters
    Input may be changed if inplace set to true and operation is inplace
    """
    A = np.ones((5, 5))
    A_copy = A.copy()
    preprocess_mul_no_kwargs(A, inplace=True)
    assert A[0, 0] != A_copy[0, 0]

def test_pandas_input():
    """ Input: DataFrame, Output: DataFrame """
    # Skip this test if you don't have pandas
    pytest.importorskip('pandas')
    import pandas as pd
    # Create a DataFrame with a NaN
    A = np.arange(25).reshape((5, 5)).astype(np.float)
    A[0, 0] = np.nan
    A = pd.DataFrame(A)
    # Assert that the output is a DataFrame
    assert isinstance(mean(A), pd.DataFrame)

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

@wrapper.conform_output
def conform_output_dummy(x):
    return x

def is_between_0_1(x):
    return 0 <= x <= 1

def coerce_between_0_1(arr, x_i, y_i):
    val = arr[x_i, y_i]
    if val < 0:
        return 0
    elif val > 1:
        return 1
    else:
        return x

def test_conform_output_not_used():
    """ If neither args passed, don't do anything"""
    assert "some input" == conform_output_dummy("some input")

def test_conform_output_valid_coerce():
    """ Check value valid and coerce invalid values"""
    arr = np.array([[1.1, 0.5], [0.2, -1]])
    actual = conform_output_dummy(
            arr,
            valid_fn=is_between_0_1,
            coerce_fn=coerce_between_0_1,
            )
    expected = np.array([[1.0, 0.5], [0.2, 0.0]])
    assert np.array_equal(expected, actual)

def test_conform_output_coerce():
    """ Coerce function doesn't run if no valid_fn passed  """
    arr = np.array([[1.1, 0.5], [0.2, -1]])
    actual = conform_output_dummy(
            arr,
            coerce_fn=coerce_between_0_1,
            )
    expected = np.array([[1.1, 0.5], [0.2, -1]])
    assert np.array_equal(expected, actual)

def test_conform_output_valid():
    """ No coerce_fn with valid_fn will raise BadOutputeError if invalid values
    encountered. First invalid value is 1.1
    """
    arr = np.array([[1.1, 0.5], [0.2, -1]])
    with pytest.raises(BadOutputError) as excinfo:
        conform_output_dummy(arr, valid_fn=is_between_0_1)
    assert str(excinfo.value) == "1.1 does not conform"
