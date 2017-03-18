"""Find Distribution Parameters for different distributions """
import numpy as np


def gaussian(data, dist):
    """Finds the normal distribution thetas for continuous data

    PARAMETERS
    ---------
    data: numpy.nd.array

    RETURNS
    ------
    dictionary
    """
    all_dists = ["gaussian"]
    try:
        all_dists.index(dist)
    except:
        raise Exception("Value of 'dist' {} is not valid".format(dist))
    thetas = {}
    data = data[~np.isnan(data)]
    if dist == "gaussian":
        mu = np.mean(data)
        var = np.var(data)
        thetas["mu"] = mu
        thetas["var"] = var
        return thetas
