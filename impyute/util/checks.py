""" impyute.util.check """
from functools import wraps
import numpy as np
from impyute.util import find_null
from impyute.util import BadInputError
# pylint:disable=invalid-name

def checks(fn):
    """ Main check function to ensure input is correctly formatted

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.

    Returns
    -------
    bool
        True if `data` is correctly formatted

    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """ Run input checks"""
        data = args[0]
        if len(np.shape(data)) != 2:
            raise BadInputError("No support for arrays that aren't 2D yet.")
        elif not _shape_2d(data):
            raise BadInputError("Not a 2D array.")
        elif not _is_ndarray(data):
            raise BadInputError("Not a np.ndarray.")
        elif not _dtype_float(data):
            raise BadInputError("Data is not float.")
        elif not _nan_exists(data):
            raise BadInputError("No NaN's in given data")
        return fn(*args, **kwargs)
    return wrapper

def _shape_2d(data):
    """ True if array is 2D"""
    return len(np.shape(data)) == 2

def _shape_3d(data):
    """ True if array is 3D"""
    return len(np.shape(data)) == 3

def _is_ndarray(data):
    """ True if the array is an instance of numpy's ndarray"""
    return isinstance(data, np.ndarray)

def _dtype_float(data):
    """ True if the values in the array are floating point"""
    return data.dtype == np.float

def _nan_exists(data):
    """ True if there is at least one np.nan in the array"""
    null_xy = find_null(data)
    return len(null_xy) > 0
