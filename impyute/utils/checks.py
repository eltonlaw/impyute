""" Checks inputted data format"""
import numpy as np


def checks(data):
    if not shape_2d(data):
        print("Error: Not a 2D Tensor")
        return False
    if not is_ndarray(data):
        print("Error: Not a np.ndarray")
        return False
    if not dtype_float(data):
        print("Error: Data is not continuous")
        return False
    return True


def shape_2d(data):
    return len(np.shape(data)) == 2


def is_ndarray(data):
    return isinstance(data, np.ndarray)


def dtype_float(data):
    return np.array(list(data)).dtype == np.float64
