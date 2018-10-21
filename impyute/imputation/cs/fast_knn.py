""" impyute.imputation.cs.knn """
import numpy as np
from impyute.util import find_null
from impyute.util import checks
from impyute.util import preprocess
from impyute.imputation.cs import mean
from scipy.spatial import KDTree
# pylint: disable=invalid-name
# pylint:disable=unused-argument

@preprocess
@checks
def fast_knn(data, k=3, eps=0, p=2, distance_upper_bound=np.inf, leafsize=10, **kwargs):
    """ Impute using a variant of the nearest neighbours approach

    Basic idea: Impute array with a basic mean impute and then use the resulting complete
    array to construct a KDTree. Use this KDTree to compute nearest neighbours.
    After finding `k` nearest neighbours, take the weighted average of them. Basically,
    find the nearest row in terms of distance

    This approach is much, much faster than the other implementation (fit+transform
    for each subset) which is almost prohibitively expensive.

    Usage
    -----

        >>> data = np.arange(25).reshape((5, 5)).astype(np.float)
        >>> data[0][2] =  np.nan
        >>> data
        array([[ 0.,  1., nan,  3.,  4.],
               [ 5.,  6.,  7.,  8.,  9.],
               [10., 11., 12., 13., 14.],
               [15., 16., 17., 18., 19.],
               [20., 21., 22., 23., 24.]])
        >> fast_knn(data, k=1) # Weighted average (by distance) of nearest 1 neighbour
        array([[ 0.,  1.,  7.,  3.,  4.],
               [ 5.,  6.,  7.,  8.,  9.],
               [10., 11., 12., 13., 14.],
               [15., 16., 17., 18., 19.],
               [20., 21., 22., 23., 24.]])
        >> fast_knn(data, k=2) # Weighted average of nearest 2 neighbours
        array([[ 0.        ,  1.        , 10.08608891,  3.        ,  4.        ],
               [ 5.        ,  6.        ,  7.        ,  8.        ,  9.        ],
               [10.        , 11.        , 12.        , 13.        , 14.        ],
               [15.        , 16.        , 17.        , 18.        , 19.        ],
               [20.        , 21.        , 22.        , 23.        , 24.        ]])
        >> fast_knn(data, k=3)
        array([[ 0.        ,  1.        , 13.40249283,  3.        ,  4.        ],
               [ 5.        ,  6.        ,  7.        ,  8.        ,  9.        ],
               [10.        , 11.        , 12.        , 13.        , 14.        ],
               [15.        , 16.        , 17.        , 18.        , 19.        ],
               [20.        , 21.        , 22.        , 23.        , 24.        ]])
        >> fast_knn(data, k=5) # There are at most only 4 neighbours. Raises error
        ...
        IndexError: index 5 is out of bounds for axis 0 with size 5


    Parameters
    ----------
    data: numpy.ndarray
        2D matrix to impute.

    k: int, optional
        Parameter used for method querying the KDTree class object. Number of
        neighbours used in the KNN query. Refer to the docs for
        [`scipy.spatial.KDTree.query`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html).

    eps: nonnegative float, optional
        Parameter used for method querying the KDTree class object. From the
        SciPy docs: "Return approximate nearest neighbors; the kth returned
        value is guaranteed to be no further than (1+eps) times the distance to
        the real kth nearest neighbor". Refer to the docs for
        [`scipy.spatial.KDTree.query`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html).

    p : float, 1<=p<=infinity, optional
        Parameter used for method querying the KDTree class object. Straight from the
        SciPy docs: "Which Minkowski p-norm to use. 1 is the
        sum-of-absolute-values Manhattan distance 2 is the usual Euclidean
        distance infinity is the maximum-coordinate-difference distance". Refer to
        the docs for
        [`scipy.spatial.KDTree.query`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html).

    distance_upper_bound : nonnegative float, optional
        Parameter used for method querying the KDTree class object. Straight
        from the SciPy docs: "Return only neighbors within this distance. This
        is used to prune tree searches, so if you are doing a series of
        nearest-neighbor queries, it may help to supply the distance to the
        nearest neighbor of the most recent point." Refer to the docs for
        [`scipy.spatial.KDTree.query`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html).

    leafsize: int, optional
        Parameter used for construction of the `KDTree` class object. Straight from
        the SciPy docs: "The number of points at which the algorithm switches
        over to brute-force. Has to be positive". Refer to the docs for
        [`scipy.spatial.KDTree`](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.html)
        for more information.

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    null_xy = find_null(data)
    data_c = mean(data)
    kdtree = KDTree(data_c, leafsize=leafsize)

    for x_i, y_i in null_xy:
        distances, indices = kdtree.query(data_c[x_i], k=k+1, eps=eps,
                                          p=p, distance_upper_bound=distance_upper_bound)
        # Will always return itself in the first index. Delete it.
        distances, indices = distances[1:], indices[1:]
        weights = distances/np.sum(distances)
        # Assign missing value the weighted average of `k` nearest neighbours
        data[x_i][y_i] = np.dot(weights, [data_c[ind][y_i] for ind in indices])
    return data
