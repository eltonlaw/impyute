"""
Expectation Maximization Imputation
------------
"""
import numpy as np
from impy.diagnostics import find_null


def expectation_maximization(data, loops=50):
    """ Imputes given data using expectation maximization

    E-step: Calculates the expected complete data log likelihood ratio
    M-step: Maximizes the

    Parameters
    ---------
    data: numpy.nd.array
        data with missing values
    Returns
    ---------
    numpy.nd.array
    """
    null_xy = find_null(data)

    for x_i, y_i in null_xy:
        col_max = max(data[:, 0])
        col_min = min(data[:, 0])
        # mu_0; initial mean random value between max and min column values
        mu = (col_max-col_min)*np.random.rand()+col_min
        # var_0; initial variance random value between 0 and 1
        sigma = np.random.rand()
        pr = 0
        for ii in range(50):
            pr_prev = pr
            # Expectation
            pr = sigma * np.random.randn() + mu
            # Maximization
            sigma, mu = np.log(pr)
            delta = pr_prev
            if delta < 0.1:
                break
    return data
