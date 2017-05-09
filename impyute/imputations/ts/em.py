"""
Expectation Maximization Imputation on Time Series Data
-------------------------------------------------------
"""

import numpy as np
from impyute.utils import find_null
from impyute.filter import Kalman

from impyute.datasets import random_uniform
data = random_uniform()


def em(data, loops=10):
    """ Imputes given time series data using expectation maximization and the
    kalman filter

    E-step: Runs the Kalman Filter to predict each missing values
    M-step: Finds the parameters that maximize the log likelihood of the
    complete data

    PARAMETERS
    ---------
    data: numpy.nd.array
        data with missing values
    loops: int
        Number of em iterations to run before breaking
    dtype: ("cont","disc")
        Indicates whether the possible values will come from a continuous
        range or categorical range
    RETURNS
    ---------
    numpy.nd.array
    """
    null_xy = find_null(data)
    for x_i, y_i in null_xy:
        row = data[x_i, :][~np.isnan(data[x_i, :])]
        for i in range(loops):
            # E-step
            X_k0 = [row.mean(), row.var()]
            P_k0 = np.identity(len(X_k0))
            kf = Kalman(1, 1, X_k0, P_k0)
            for x in row:
                kf.filter(np.transpose([[x, 0]]))
            data[x_i][y_i] = kf.predict_next()[0][0]
            print(data[x_i][y_i])
            row = data[x_i]
            # M-step
            # Update params such that expected log-le is maximized

    return data
