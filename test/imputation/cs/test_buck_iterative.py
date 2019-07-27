"""test_buck_iterative.py"""
import numpy as np
import impyute as impy

data = np.asarray([[1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 4, 6, 8, 10, 12, 14, 16],
                   [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
                   [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
                   [3, 6, 9, 12, 15, 18, 21, 24],
                   [4, 8, 9, 16, 20, 24, 28, 32]])
mask = np.zeros((6, 8), dtype=bool)
data_c = data[mask]
data[0][0] = np.nan
data_m = data

def test_return_type():
    """ Check return type, should return an np.ndarray"""
    imputed = impy.buck_iterative(data_m)
    assert isinstance(imputed, np.ndarray)

def test_impute_missing_values():
    """ After imputation, no NaN's should exist"""
    imputed = impy.buck_iterative(data_m)
    assert not np.isnan(imputed).any()
