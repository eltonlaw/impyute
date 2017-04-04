""" impy.datasets.base
Artificial Dataset Generation
"""
import numpy as np
from impy.datasets.mutate import Mutator


def random_uniform(bound=(0, 10), shape=(5, 5), missingness="mcar",
                   threshold=0.2, data_type="int"):
    """ Return randomly generated dataset of numbers with uniformly
    distributed values between bound[0] and bound[1]

    PARAMETERS
    ---------
    bound:tuple (start,stop)
        Determines the range of values in the matrix. Index 0 for start
        value and index 1 for stop value. Start is inclusive, stop is
        exclusive.
    shape:tuple(optional)
        Size of the randomly generated data
    missingness: ('mcar', 'mar', 'mnar')
        Type of missigness you want in your dataset
    threshold: float between [0,1]
        Percentage of missing data in generated data
    data_type: ('int','float')
        Type of data

    RETURNS
    ------
    numpy.ndarray
    """
    a = bound[0]
    b = bound[1]
    if data_type == "int":
        generated_data = np.random.randint(a, b, size=shape).astype(float)
    elif data_type == "float":
        generated_data = np.random.uniform(a, b, size=shape)
    mutator = Mutator(generated_data)
    raw_data = getattr(mutator, missingness)()["data"]
    return raw_data


def random_normal(theta=(0, 1), shape=(5, 5), missingness="mcar",
                  threshold=0.2, data_type="int"):
    """ Return randomly generated dataset of numbers with normally
    distributed values with given and sigma.

    PARAMETERS
    ---------
    theta: tuple (mu, sigma)
        Determines the range of values in the matrix
    shape:tuple(optional)
        Size of the randomly generated data
    missingness: ('mcar', 'mar', 'mnar')
        Type of missigness you want in your dataset
    threshold: float between [0,1]
        Percentage of missing data in generated data
    data_type: ('int','float')
        Type of data

    RETURNS
    ------
    numpy.ndarray
    """
    mu, sigma = theta
    generated_data = np.random.normal(mu, sigma, size=shape)
    if data_type == "int":
        generated_data = np.round(generated_data)
    elif data_type == "float":
        pass
    mutator = Mutator()
    raw_data = getattr(mutator, missingness)()["data"]
    return raw_data
