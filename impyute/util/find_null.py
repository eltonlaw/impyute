""" impyute.util.find_null """
import numpy as np


def find_null(data):
    """ Finds the indices of all missing values.

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.

    Returns
    -------
    List of tuples
        Indices of all missing values in tuple format; (i, j)

    """
    null_xy = np.argwhere(np.isnan(data))
    return null_xy
