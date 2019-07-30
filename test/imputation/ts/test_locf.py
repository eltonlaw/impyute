"""test_locf.py"""
import numpy as np
import impyute as impy
from impyute.util.testing import return_na_check

SHAPE = (5, 5)


def test_locf_(test_data):
    data = test_data(SHAPE)
    imputed = impy.locf(data)
    return_na_check(imputed)


def test_na_at_i_start(test_data):
    data = test_data(SHAPE)
    actual = impy.locf(data, axis=1)
    data[0, 0] = data[1, 0]
    assert np.array_equal(actual, data)


def test_na_at_i(test_data):
    data = test_data(SHAPE, 3, 3)
    actual = impy.locf(data, axis=1)
    data[3, 3] = data[2, 3]
    assert np.array_equal(actual, data)


def test_na_at_i_end(test_data):
    data = test_data(SHAPE)
    last_i = np.shape(data)[0] - 1
    data = test_data(SHAPE, last_i, 3)
    actual = impy.locf(data, axis=1)
    data[last_i, 3] = data[last_i - 1, 3]
    assert np.array_equal(actual, data)