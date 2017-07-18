""" Checks format of input data """
import numpy as np
from impyute.utils import find_null


def checks(data, allow_3d=False):
    """ Main check function to ensure input is correctly formatted"""
    if not _shape_2d(data):
        if not allow_3d or not _shape_3d:
            print("Error: Not a 2D/3D Tensor")
            return False
    if not _is_ndarray(data):
        print("Error: Not a np.ndarray")
        return False
    if not _dtype_float(data):
        print("Error: Data is not continuous")
        return False
    if not _nan_exists(data):
        print("Error: No NaN's in given data")
        return False
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
    return np.array(list(data)).dtype == np.float64

def _nan_exists(data):
    """ True if there is at least one np.nan in the array"""
    null_xy = find_null(data)
    return len(null_xy)
