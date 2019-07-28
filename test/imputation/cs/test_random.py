"""test_random_imputation.py"""
import numpy as np
import impyute as impy

mask = np.zeros((3, 3), dtype=bool)
data_c = impy.dataset.test_data(mask=mask)
mask[0][0] = True
data_m = impy.dataset.test_data(mask=mask)

def test_return_type():
    """Check return type, should return an np.ndarray"""
    imputed = impy.random(data_m)
    assert isinstance(imputed, np.ndarray)

def test_impute_missing_values():
    """After imputation, no NaN's should exist"""
    imputed = impy.random(data_m)
    assert not np.isnan(imputed).any()
