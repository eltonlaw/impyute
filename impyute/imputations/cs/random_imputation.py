""" impyute.imputations.cs.random_imputation"""
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks

def random_imputation(data):
    """ Fill missing values in with a randomly selected value from the same
    column.

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    if not checks(data):
        raise Exception("Checks failed")
    null_xy = find_null(data)
    for x, y in null_xy:
        uniques = np.unique(data[:, y])
        uniques = uniques[~np.isnan(uniques)]
        data[x][y] = np.random.choice(uniques)
    return data
