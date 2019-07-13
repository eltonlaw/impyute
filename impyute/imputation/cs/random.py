""" impyute.imputation.cs.random """
import numpy as np
from impyute.util import find_null
from impyute.util import preprocess
from impyute.util import checks

@preprocess
@checks
def random(data):
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
    null_xy = find_null(data)
    for x, y in null_xy:
        uniques = np.unique(data[:, y])
        uniques = uniques[~np.isnan(uniques)]
        data[x][y] = np.random.choice(uniques)
    return data
