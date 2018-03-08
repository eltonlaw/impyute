""" impyute.imputations.cs.em"""
import random
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks

@checks
def em(data, loops=50, dtype="cont"):
    """ Imputes given data using expectation maximization.

    E-step: Calculates the expected complete data log likelihood ratio.
    M-step: Finds the parameters that maximize the log likelihood of the
    complete data.

    Parameters
    ----------
    data: numpy.nd.array
        Data to impute.
    loops: int
        Number of em iterations to run before breaking.
    dtype: ("cont","disc")
        Indicates whether the possible values will come from a continuous
        range or categorical range.

    Returns
    -------
    numpy.nd.array
        Imputed data.

    """
    if dtype == "cont":
        null_xy = find_null(data)
        for x_i, y_i in null_xy:
            col = data[:, int(y_i)]
            mu = col[~np.isnan(col)].mean()
            std = col[~np.isnan(col)].std()
            col[x_i] = random.gauss(mu, std)
            previous, i = 1, 1
            for i in range(loops):
                # Expectation
                mu = col[~np.isnan(col)].mean()
                std = col[~np.isnan(col)].std()
                # Maximization
                col[x_i] = random.gauss(mu, std)
                # Break out of loop if likelihood doesn't change at least 10%
                # and has run at least 5 times
                delta = (col[x_i]-previous)/previous
                if i > 5 and delta < 0.1:
                    data[x_i][y_i] = col[x_i]
                    break
                data[x_i][y_i] = col[x_i]
                previous = col[x_i]
        return data
    else:
        raise Exception("Other dtypes not supported yet.")
