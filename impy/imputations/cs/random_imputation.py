"""
Simple Random Imputation
-----------------------
"""
import numpy as np
from impy.diagnostics import find_null


def random_imputation(data):
    """ Fill missing values in with a randomly selected value from the same column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    null_xy = find_null(data)
    for x, y in null_xy:
        uniques = np.unique(data[:, y])
        uniques = uniques[~np.isnan(uniques)]
        data[x][y] = np.random.choice(uniques)
    return data
