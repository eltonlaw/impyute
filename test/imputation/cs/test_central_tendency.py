"""test_averagings.py"""
import numpy as np
import impyute as impy

mask = np.zeros((5, 5), dtype=bool)
data_c = impy.dataset.test_data(mask=mask)
mask[0][0] = True
data_m = impy.dataset.test_data(mask=mask)

def test_mean_return_type():
    """ Check return type, should return an np.ndarray"""
    imputed = impy.mode(data_m)
    assert isinstance(imputed, np.ndarray)

def test_mode_return_type():
    """ Check return type, should return an np.ndarray"""
    imputed = impy.mode(data_m)
    assert isinstance(imputed, np.ndarray)

def test_median_return_type():
    """ Check return type, should return an np.ndarray"""
    imputed = impy.mode(data_m)
    assert isinstance(imputed, np.ndarray)

def test_mean_impute_missing_values():
    """ After imputation, no Nan's should exist"""
    imputed = impy.mean(data_m)
    assert not np.isnan(imputed).any()

def test_mode_impute_missing_values():
    """ After imputation, no NaN's should exist"""
    imputed = impy.mode(data_m)
    assert not np.isnan(imputed).any()

def test_median_impute_missing_values():
    """ After imputation, no NaN's should exist"""
    imputed = impy.median(data_m)
    assert not np.isnan(imputed).any()
