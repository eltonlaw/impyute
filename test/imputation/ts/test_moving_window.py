""" test/imputation/ts/test_moving_window.py """
import pytest
import numpy as np
import impyute as impy
#pylint:disable=missing-docstring, redefined-outer-name

@pytest.fixture
def data():
    return np.arange(0, 25).reshape(5, 5).astype(float)

def test_defaults_impute_leftmost_index(data):
    data[2][0] = np.nan
    imputed = impy.moving_window(data)
    assert not np.isnan(imputed).any()
    assert imputed[2][0] == 11.5

def test_defaults_impute_middle_index(data):
    data[2][2] = np.nan
    imputed = impy.moving_window(data)
    assert not np.isnan(imputed).any()
    assert imputed[2][2] == 12

def test_defaults_impute_rightmost_index(data):
    data[2][-1] = np.nan
    imputed = impy.moving_window(data)
    assert not np.isnan(imputed).any()
    assert imputed[2][-1] == 12.5

def test_custom_fn_impute_leftmost_index(data):
    data[2][0] = np.nan
    imputed = impy.moving_window(data, func=lambda l: max(l) * 2)
    assert not np.isnan(imputed).any()
    assert imputed[2][0] == 24

def test_custom_fn_impute_middle_index(data):
    data[2][2] = np.nan
    imputed = impy.moving_window(data, func=lambda l: max(l) * 2)
    assert not np.isnan(imputed).any()
    assert imputed[2][2] == 28

def test_custom_fn_impute_rightmost_index(data):
    data[2][-1] = np.nan
    imputed = impy.moving_window(data, func=lambda l: max(l) * 2)
    assert not np.isnan(imputed).any()
    assert imputed[2][-1] == 26

def test_custom_nindex_impute_leftmost_index_falls_off(data):
    data[2][0] = np.nan
    imputed = impy.moving_window(data, nindex=-1)
    assert not np.isnan(imputed).any()
    assert imputed[2][0] == 11.5

def test_custom_nindex_impute_rightmost_valid(data):
    data[2][0] = np.nan
    imputed = impy.moving_window(data, nindex=0)
    assert not np.isnan(imputed).any()
    assert imputed[2][0] == 12.5

def test_custom_nindex_impute_leftmost_falls_off(data):
    data[2][-1] = np.nan
    imputed = impy.moving_window(data, nindex=0)
    assert not np.isnan(imputed).any()
    assert imputed[2][-1] == 12.5

def test_custom_nindex_impute_rightmost_index_valid(data):
    data[2][-1] = np.nan
    imputed = impy.moving_window(data, nindex=-1)
    assert not np.isnan(imputed).any()
    assert imputed[2][-1] == 11.5
