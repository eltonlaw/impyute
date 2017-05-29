"""Autoregressive Integrated Moving Average Imputation"""
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks


def arima(data, p, d, q):
    """Autoregressive Integrated Moving Average Imputation

    PARAMETERS
    ----------
    data: numpy.ndarray
        The matrix with missing values that you want to impute
    p: int
        Number of autoregressive terms
    d: int
        Number of nonseasonal differences needed for stationarity
    q: int
        Number of lagged forecast errors in the prediction equation
    RETURNS
    -------
    numpy.ndarray
    """
    # Verify inputs
    if not checks(data):
        raise Exception("Checks failed")
    try:
        p = int(p)
        d = int(d)
        q = int(q)
        data = isinstance(data, np.array)
    except:
        raise Exception
    # Arima
    null_xy = find_null(data)
    for x, y in null_xy:
        print(x, y)
    return data
