""" impyute.contrib.count_missing.py """
import numpy as np
from impyute.ops import matrix

def count_missing(data):
    """ Calculate the total percentage of missing values and also the
    percentage in each column.

    Parameters
    ----------
    data: np.array
        Data to impute.

    Returns
    -------
    dict
        Percentage of missing values in total and in each column.

    """
    size = len(data.flatten())
    nan_xy = matrix.nan_indices(data)
    np.unique(nan_xy)
    counter = {y: 0. for y in np.unique(nan_xy.T[1])}
    change_in_percentage = 1./size
    for _, y in nan_xy:
        counter[y] += change_in_percentage
    total_missing = len(nan_xy)/size
    counter["total"] = total_missing

    return counter
