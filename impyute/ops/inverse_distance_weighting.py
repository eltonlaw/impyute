""" Assign weights to distances in a way such that farther values are weighed less """
import numpy as np

def shepards(distances, power=2):
    """ Basic inverse distance weighting function

    Parameters
    ----------
    distances: list/numpy.ndarray
        1D list of numbers (ex. distance results from call to KDTree.query)

    power: int
        Default of 2 used since the referenced paper stated an exponent of 2 "gives seemingly
        satisfactory results"

    Returns
    -------
    numpy.ndarray
        1D list of numbers that sum to 1, represents weights of provided distances, in order.

    References
    ----------

    Shepard, Donald (1968). "A two-dimensional interpolation function for irregularly-spaced data".
    Proceedings of the 1968 ACM National Conference. pp. 517-524. doi:10.1145/800186.810616
    """
    return to_percentage(1/np.power(distances, power))

def to_percentage(vec):
    """ Converts list of real numbers into a list of percentages """
    return vec/np.sum(vec)
