""" impyute.datasets.base
Artificial Dataset Generation
"""
import numpy as np
from impyute.datasets.corrupt import Corruptor


def random_uniform(bound=(0, 10), shape=(5, 5), missingness="mcar",
                   th=0.2, dtype="int"):
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
    th: float between [0,1]
        Percentage of missing data in generated data
    dtype: ('int','float')
        Type of data

    RETURNS
    ------
    numpy.ndarray
    """
    a = bound[0]
    b = bound[1]
    if dtype == "int":
        data = np.random.randint(a, b, size=shape).astype(float)
    elif dtype == "float":
        data = np.random.uniform(a, b, size=shape)
    corruptor = Corruptor(data, th=th)
    raw_data = getattr(corruptor, missingness)()
    return raw_data


def random_normal(theta=(0, 1), shape=(5, 5), missingness="mcar",
                  th=0.2, dtype="float"):
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
    th: float between [0,1]
        Percentage of missing data in generated data
    dtype: ('int','float')
        Type of data

    RETURNS
    ------
    numpy.ndarray
    """
    mu, sigma = theta
    data = np.random.normal(mu, sigma, size=shape)
    if dtype == "int":
        data = np.round(data)
    elif dtype == "float":
        pass
    corruptor = Corruptor(data, th=th)
    raw_data = getattr(corruptor, missingness)()
    return raw_data


def test_data(mask, th=0.2):
    """
    Returns a dataset to use with tests
    mask: True/False array, same size as dataset
        Use True where missing values should occur and False everywhere else
    th: float between[0,1]
        Percentage of missing data in generated dataset
    """
    shape = np.shape(mask)
    data = np.reshape(np.arange(shape[0] * shape[1]), shape).astype("float")
    data[mask] = np.nan
    return data


def mnist(missingness="mcar", th=0.2):
    """ Loads corrupted MNIST

    PARAMETERS
    ---------
    missingness: ('mcar', 'mar', 'mnar')
        Type of missigness you want in your dataset
    th: float between [0,1]
        Percentage of missing data in generated data

    RETURNS
    ------
    numpy.ndarray
    """
    from sklearn.datasets import fetch_mldata
    mnist = fetch_mldata('MNIST original')
    corruptor = Corruptor(mnist.data, th=th)
    data = getattr(corruptor, missingness)()
    return {"X": data, "Y": mnist.target}
