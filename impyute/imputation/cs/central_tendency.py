""" impyute.imputation.cs.central_tendency """
import numpy as np
from impyute.util import find_null
from impyute.util import checks
from impyute.util import preprocess
# pylint:disable=unused-argument
# pylint:disable=invalid-name

@preprocess
@checks
def mean(data, **kwargs):
    """ Substitute missing values with the mean of that column.

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
    for x_i, y_i in null_xy:
        row_wo_nan = data[:, [y_i]][~np.isnan(data[:, [y_i]])]
        new_value = np.mean(row_wo_nan)
        data[x_i][y_i] = new_value
    return data

@preprocess
@checks
def median(data, **kwargs):
    """ Substitute missing values with the median of that column(middle).

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
    cols_missing = set(null_xy.T[1])
    medians = {}
    for y_i in cols_missing:
        cols_wo_nan = data[:, [y_i]][~np.isnan(data[:, [y_i]])]
        median_y = np.median(cols_wo_nan)
        medians[str(y_i)] = median_y
    for x_i, y_i in null_xy:
        data[x_i][y_i] = medians[str(y_i)]
    return data

@preprocess
@checks
def mode(data, **kwargs):
    """ Substitute missing values with the mode of that column(most frequent).

    In the case that there is a tie (there are multiple, most frequent values)
    for a column randomly pick one of them.

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
    modes = []
    for y_i in range(np.shape(data)[1]):
        unique_counts = np.unique(data[:, [y_i]], return_counts=True)
        max_count = np.max(unique_counts[1])
        mode_y = [unique for unique, count in np.transpose(unique_counts)
                  if count == max_count and not np.isnan(unique)]
        modes.append(mode_y)  # Appends index of column and column modes
    for x_i, y_i in null_xy:
        data[x_i][y_i] = np.random.choice(modes[y_i])
    return data
