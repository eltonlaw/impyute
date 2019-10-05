""" Common operations on matrices

*Look into whether it's worth writing these in raw c*
"""
import numpy as np

def nan_indices(data):
    """ Finds the indices of all missing values.

    Parameters
    ----------
    data: numpy.ndarray

    Returns
    -------
    List of tuples
        Indices of all missing values in tuple format; (i, j)
    """
    return np.argwhere(np.isnan(data))

def map_nd(fn, arr):
    """ Map fn that takes a value over entire n-dim array

    Parameters
    ----------
    arr: numpy.ndarray

    Returns
    -------
    numpy.ndarray

    """
    return np.vectorize(fn)(arr)

def every_nd(fn, arr):
    """ Returns bool, true if fn is true for all elements of arr

    Parameters
    ----------
    arr: numpy.ndarray

    Returns
    -------
    bool

    """
    return all(map(fn, arr.flatten()))
