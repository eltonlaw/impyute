""" impyute.util.count_missing.py """
import numpy as np
from impyute.util import find_null


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
    null_xy = find_null(data)
    np.unique(null_xy)
    counter = {y: 0. for y in np.unique(null_xy.T[1])}
    change_in_percentage = 1./size
    for _, y in null_xy:
        counter[y] += change_in_percentage
    total_missing = len(null_xy)/size
    counter["total"] = total_missing

    return counter
