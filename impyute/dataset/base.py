""" Shared functions to load/generate data """
import itertools
import math
import random
import string
import numpy as np
from impyute.dataset.corrupt import Corruptor
from impyute.ops import error

def randu(bound=(0, 10), shape=(5, 5), missingness="mcar", thr=0.2, dtype="int"):
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
        Type of missingness you want in your dataset
    thr: float between [0,1]
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


def randn(theta=(0, 1), shape=(5, 5), missingness="mcar", thr=0.2, dtype="float"):
    """ Return randomly generated dataset of numbers with normally
    distributed values with given and sigma.

    Parameters
    ----------
    theta: tuple (mu, sigma)
        Determines the range of values in the matrix
    shape:tuple(optional)
        Size of the randomly generated data
    missingness: ('mcar', 'mar', 'mnar')
        Type of missingness you want in your dataset
    thr: float between [0,1]
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

def randc(nlevels=5, shape=(5, 5), missingness="mcar", thr=0.2):
    """ Return randomly generated dataset with uniformly distributed categorical data (alphabetic character)

    Parameters
    ----------
    nlevels: int
        Specify the number of different categories in the dataset
    shape: tuple(optional)
        Size of the randomly generated data
    missingness: string in ('mcar', 'mar', 'mnar')
        Type of missingness you want in your dataset
    thr: float between [0,1]
        Percentage of missing data in generated data

    Returns
    -------
    numpy.ndarray
    """
    if shape[0]*shape[1] < nlevels:
        raise error.BadInputError("nlevel exceeds the size of desired dataset. Please decrease the nlevel or increase the shape")

    length = len(string.ascii_lowercase)
    n_fold = int(math.floor(math.log(nlevels, length)))
    cat_pool = list(string.ascii_lowercase)

    # when nlevel > 26, the alphabetical character is used up, need to generate extra strings as categorical data
    if n_fold > 0:
        for i in range(2, n_fold+2):
            pool_candidate = list(itertools.product(string.ascii_lowercase, repeat=i))
            cat_pool.extend([''.join(w) for w in pool_candidate])
            if len(cat_pool) > nlevels:
                break

    cat = random.sample(cat_pool, nlevels)
    data = np.random.choice(cat, shape, replace=True)

    # make sure the data frame has nlevel different categories
    while len(np.unique(data)) != nlevels:
        data = np.random.choice(cat, shape, replace=True)

    corruptor = Corruptor(data, thr=thr, dtype=np.str)
    raw_data = getattr(corruptor, missingness)()
    return raw_data



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
