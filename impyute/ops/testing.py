""" Utilities used for unit tests """
import numpy as np


def return_na_check(data):
    """Helper function for tests to check if the data returned is a
       numpy array and that the imputed data has no NaN's.

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.
    
    Returns
    -------
    None

    """
    assert isinstance(data, np.ndarray)
    assert not np.isnan(data).any()
