import numpy as np
from impyute.ops import matrix
from impyute.ops import wrapper

@wrapper.wrappers
@wrapper.checks
def em(data, eps=0.1):
    """ Imputes given data using expectation maximization.

    E-step: Calculates the expected complete data log likelihood ratio.
    M-step: Finds the parameters that maximize the log likelihood of the
    complete data.

    Parameters
    ----------
    data: numpy.nd.array
        Data to impute.
    eps: float
        The amount of minimum change between iterations to break, if relative change < eps, converge.
        relative change = abs(current - previous) / previous
    inplace: boolean
        If True, operate on the numpy array reference

    Returns
    -------
    numpy.nd.array
        Imputed data.

    """
    nan_xy = matrix.nan_indices(data)
    for x_i, y_i in nan_xy:
        col = data[:, int(y_i)]
        mu = col[~np.isnan(col)].mean()
        std = col[~np.isnan(col)].std()
        col[x_i] = np.random.normal(loc=mu, scale=std)
        previous, i = 1, 1
        while True:
            i += 1
            # Expectation
            mu = col[~np.isnan(col)].mean()
            std = col[~np.isnan(col)].std()
            # Maximization
            col[x_i] = np.random.normal(loc=mu, scale=std)
            # Break out of loop if likelihood doesn't change at least 10%
            # and has run at least 5 times
            delta = np.abs(col[x_i]-previous)/previous
            if i > 5 and delta < eps:
                data[x_i][y_i] = col[x_i]
                break
            data[x_i][y_i] = col[x_i]
            previous = col[x_i]
    return data
