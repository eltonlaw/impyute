"""Finds Null Values """
import numpy as np


def find_null(data):
    """Finds the indices of all missing values

    PARAMETERS
    ---------
    data: numpy.nd.array

    RETURNS
    ------
    List of tuples
    """
    null_xy = np.argwhere(np.isnan(data))
    return null_xy
