"""Autoregressive Integrated Moving Average Imputation"""
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks
# pylint: disable=invalid-name

@checks
def arima(data, p, d, q, axis=0):
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
    axis: boolean (optional)
        0 if time series is in row format (Ex. data[0][:] is 1st data point).
        1 if time series is in col format (Ex. data[:][0] is 1st data point).

    RETURNS
    -------
    numpy.ndarray
    """
    assert isinstance(p, int), "Parameter `p` must be an integer"
    assert isinstance(d, int), "Parameter `d` must be an integer"
    assert isinstance(q, int), "Parameter `q` must be an integer"

    null_xy = find_null(data)
    for x, y in null_xy:
        print(x, y)
    return data
