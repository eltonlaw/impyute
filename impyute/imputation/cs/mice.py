""" impyute.imputation.cs.mice """
import numpy as np
from impyute.util import checks, find_null, preprocess

@preprocess
@checks
def mice(data):
    """ Multivariate Imputation By Chained Equations

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
    return data
