""" impyute.imputations.cs.knn"""
import numpy as np
from impyute.utils import find_null
from impyute.utils import checks
from impyute.imputations.cs import mean_imputation
from scipy.spatial import KDTree
# pylint: disable=invalid-name

@checks
def fast_knn(data, k=5):
    """ Impute using a variant of the nearest neighbours approach

    Basic idea: Impute array and then use the resulting complete
    array to construct a KDTree. Use this KDTree to compute nearest neighbours.
    After finding `k` nearest neighbours, take the weighted average of them.

    This approach is much, much faster than the other implementation (fit+transform
    for each subset) which is almost prohibitively expensive.

    Parameters
    ----------
    data: numpy.ndarray
        2D matrix to impute.

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    null_xy = find_null(data)
    data_c = mean_imputation(data)
    kdtree = KDTree(data_c)

    for x_i, y_i in null_xy:
        distances, indices = kdtree.query(data[x_i], k=k+1)
        # Will always return itself in the first index. Delete it.
        distances, indices = distances[1:], indices[1:]
        weights = (np.sum(distances)-distances)/np.sum(distances)
        # Make weights sum to 1
        weights_unit = weights/np.sum(weights)
        # Assign missing value the weighted average of `k` nearest neighbours
        data[x_i][y_i] = np.dot(weights_unit, [data[y_i][ind] for ind in indices])
    return data
