""" impyute.utils.check """
import numpy as np
from impyute.utils import find_null


def checks(data, dims=2):
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
    if dims != 2:
        print("Error: No support for arrays that aren't 2D yet.")
    elif not _shape_2d(data):
        print("Error: Not a 2D array.")
    elif not _is_ndarray(data):
        print("Error: Not a np.ndarray.")
        return False
    elif not _dtype_float(data):
        print("Error: Data is not float.")
        return False
    elif not _nan_exists(data):
        print("Error: No NaN's in given data")
        return False
    else:
        return True

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
