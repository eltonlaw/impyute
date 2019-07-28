"""test_fast_knn.py"""
import functools
import numpy as np
import impyute as impy
# pylint:disable=invalid-name

n = 100
data_c = np.random.normal(size=n*n).reshape((n, n))
data_m1 = data_c.copy()
for _ in range(int(n*0.3*n)):
    data_m1[np.random.randint(n)][np.random.randint(n)] = np.nan

def test_return_type():
    """ Check return type, should return an np.ndarray"""
    imputed = impy.fast_knn(data_m1)
    assert isinstance(imputed, np.ndarray)

def test_impute_missing_values():
    """ After imputation, no NaN's should exist"""
    imputed = impy.fast_knn(data_m1)
    assert not np.isnan(imputed).any()

data_m2 = np.array([[0., 1., np.nan, 3., 4.],
                    [5., 6., 7., 8., 9.],
                    [10., 11., 12., 13., 14.],
                    [15., 16., 17., 18., 19.],
                    [20., 21., 22., 23., 24.]])

def test_impute_value():
    "fast_knn using standard idw"
    imputed = impy.fast_knn(data_m2, k=2)
    assert np.isclose(imputed[0][2], 8.38888888888889)

def test_impute_value_custom_idw():
    "fast_knn using custom idw"
    idw = functools.partial(impy.util.inverse_distance_weighting.shepards, power=1)
    imputed = impy.fast_knn(data_m2, k=2, idw=idw)
    assert np.isclose(imputed[0][2], 8.913911092686593)
