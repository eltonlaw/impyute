"""
Simple Random Imputation
-----------------------
"""
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks


def random_imputation(data):
    """ Fill missing values in with a randomly selected value from the same column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    if not checks(data):
        raise Exception("Checks failed")
    null_xy = find_null(data)
    for x, y in null_xy:
        uniques = np.unique(data[:, y])
        uniques = uniques[~np.isnan(uniques)]
        data[x][y] = np.random.choice(uniques)
    return data
