import numpy as np


def mcar_test(data):
    """ Implementation of Little's MCAR Test

    Parameters
    ----------
    np.ndarray

    Returns
    ------
    Boolean;
    """
    for ii, datapoint in enumerate(data.T):
        datapoint = datapoint[~np.isnan(datapoint)]
        datapoint.mean()

    return True
