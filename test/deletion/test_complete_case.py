"""test_complete_case.py"""
import numpy as np
from impyute.dataset import test_data
from impyute.deletion import complete_case

mask = np.zeros((5, 5), dtype=bool)
data_c = test_data(mask)
mask[0][0] = True
data_m = test_data(mask)

def test_return_type():
    """ Check return type, should return an np.ndarray"""
    imputed = complete_case(data_m)
    assert isinstance(imputed, np.ndarray)

def test_impute_no_missing_values():
    """ After imputation, no change should occur"""
    imputed = complete_case(data_m)
    assert not np.isnan(imputed).any()

def test_impute_missing_values():
    """ After imputation, no NaN's should exist"""
    imputed = complete_case(data_m)
    assert np.shape(imputed) == (4, 5)

def test_imputed_values():
    """ Assert values are as expected"""
    imputed = complete_case(data_m)
    expected = np.array([
        [5., 6., 7., 8., 9.],
        [10., 11., 12., 13., 14.],
        [15., 16., 17., 18., 19.],
        [20., 21., 22., 23., 24.]
    ])
    assert np.equal(imputed, expected).all()
