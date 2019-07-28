"""test_mnist.py"""
import numpy as np
import pytest
from impyute.dataset import mnist
from impyute.util import find_null

pytest.skip("takes ~30 sec each test", allow_module_level=True)
data = mnist()["X"]

def test_return_type():
    """ Check return type, should return an np.ndarray"""
    assert isinstance(data, np.ndarray)

def test_missing_values_present():
    """ Check that the dataset is corrupted (missing values present)"""
    assert find_null(data).size != 0
