""" Artificial Dataset Generation """
import numpy as np
from impy.datasets.mutate import Mutator


def random_uniform(bound=(0, 10), shape=(5, 5), missingness="mcar",
                   threshold=0.2, data_type="int"):
    """ Return randomly generated dataset of numbers with uniform values
    between 0 and range_i.

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
    mutator = Mutator()
    mutate = getattr(mutator, missingness)
    raw_data = mutate(generated_data, threshold=threshold)["data"]
    return raw_data


def random_normal(theta=(0, 1), shape=(5, 5), missingness="mcar",
                  threshold=0.2, data_type="int"):
    """ Return randomly generated dataset of numbers with uniform values
    between 0 and range_i.

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
    mutate = getattr(mutator, missingness)
    raw_data = mutate(generated_data, threshold=threshold)["data"]
    return raw_data
