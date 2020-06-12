import numpy as np
from impyute.ops import matrix
from impyute.ops import wrapper
# pylint: disable=too-many-locals

@wrapper.wrappers
@wrapper.checks
def mice(data):
    """ Multivariate Imputation by Chained Equations

    ...otherwise known as fully conditional specification (FCS).

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
    return data
