"""Autoregressive Integrated Moving Average Imputation"""
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks

@checks
def arima(data, p, d, q):
    """Autoregressive Integrated Moving Average Imputation

    Stationary model

    PARAMETERS
    ----------
    data: numpy.ndarray
        The matrix with missing values that you want to impute
    p: int
        Number of autoregressive terms. Ex (p,d,q)=(1,0,0). 
    d: int
        Number of nonseasonal differences needed for stationarity
    q: int
        Number of lagged forecast errors in the prediction equation
    RETURNS
    -------
    numpy.ndarray
    """
    def _compute_nan_endpoints(x, y):
        pass

    try:
        p = int(p)
        d = int(d)
        q = int(q)
        data = isinstance(data, np.ndarray)
    except:
        raise Exception
    # ARIMA
    null_xy = find_null(data)
    for x, y in null_xy:
        print(x, y)
    return data



