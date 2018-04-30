""" impyute.dataset.base

Load/generate data

"""
import numpy as np
from impyute.dataset.corrupt import Corruptor


def randu(bound=(0, 10), shape=(5, 5), missingness="mcar",
                   thr=0.2, dtype="int"):
    """ Return randomly generated dataset of numbers with uniformly
    distributed values between bound[0] and bound[1]

    Parameters
    ----------
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

    Returns
    -------
    numpy.ndarray
    """
    if dtype == "int":
        data = np.random.randint(bound[0], bound[1], size=shape).astype(float)
    elif dtype == "float":
        data = np.random.uniform(bound[0], bound[1], size=shape)
    corruptor = Corruptor(data, thr=thr)
    raw_data = getattr(corruptor, missingness)()
    return raw_data


def randn(theta=(0, 1), shape=(5, 5), missingness="mcar", thr=0.2,
                  dtype="float"):
    """ Return randomly generated dataset of numbers with normally
    distributed values with given and sigma.

    Parameters
    ----------
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

    Returns
    -------
    numpy.ndarray
    """
    mean, sigma = theta
    data = np.random.normal(mean, sigma, size=shape)
    if dtype == "int":
        data = np.round(data)
    elif dtype == "float":
        pass
    corruptor = Corruptor(data, thr=thr)
    raw_data = getattr(corruptor, missingness)()
    return raw_data


def test_data(mask=np.zeros((3, 3), dtype=bool)):
    """ Returns a dataset to use with tests (INTERNAL USE - FOR UNIT TESTING)

    mask: True/False array, same size as dataset
        Use True where missing values should occur and False everywhere else
    th: float between[0,1]
        Percentage of missing data in generated dataset
    """
    shape = np.shape(mask)
    data = np.reshape(np.arange(np.product(shape)), shape).astype("float")
    data[mask] = np.nan
    return data


def mnist(missingness="mcar", thr=0.2):
    """ Loads corrupted MNIST

    Parameters
    ----------
    missingness: ('mcar', 'mar', 'mnar')
        Type of missigness you want in your dataset
    th: float between [0,1]
        Percentage of missing data in generated data

    Returns
    -------
    numpy.ndarray
    """
    from sklearn.datasets import fetch_mldata
    dataset = fetch_mldata('MNIST original')
    corruptor = Corruptor(dataset.data, thr=thr)
    data = getattr(corruptor, missingness)()
    return {"X": data, "Y": dataset.target}
