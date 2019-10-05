import numpy as np
from impyute.ops import matrix
from impyute.ops import wrapper

@wrapper.wrappers
@wrapper.checks
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
    nan_xy = matrix.nan_indices(data)
    for x, y in nan_xy:
        uniques = np.unique(data[:, y])
        uniques = uniques[~np.isnan(uniques)]
        data[x][y] = np.random.choice(uniques)
    return data
