"""test_fast_knn.py"""
import functools
import numpy as np
import impyute as impy
from impyute.ops.testing import return_na_check
# pylint:disable=invalid-name

SHAPE = (5, 5)


def test_return_type(knn_test_data):
    imputed = impy.fast_knn(knn_test_data)
    return_na_check(imputed)


def test_impute_value(test_data):
    """fast_knn using standard idw"""
    data = test_data(SHAPE, 0, 2)
    imputed = impy.fast_knn(data, k=2)
    assert np.isclose(imputed[0, 2], 8.38888888888889)


def test_impute_value_custom_idw(test_data):
    """fast_knn using custom idw"""
    data = test_data(SHAPE, 0, 2)
    idw_fn = functools.partial(impy.ops.inverse_distance_weighting.shepards, power=1)
    imputed = impy.fast_knn(data, k=2, idw_fn=idw_fn)
    assert np.isclose(imputed[0, 2], 8.913911092686593)
