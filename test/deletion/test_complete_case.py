"""test_complete_case.py"""
import numpy as np
from impyute.deletion import complete_case
from impyute.util.testing import return_na_check

SHAPE = (5, 5)


def test_complete_case_(test_data):
    data = test_data(SHAPE)
    imputed = complete_case(data)
    return_na_check(imputed)


def test_impute_missing_values(test_data):
    data = test_data(SHAPE)
    imputed = complete_case(data)
    assert np.shape(imputed) == (4, 5)


def test_imputed_values(test_data):
    data = test_data(SHAPE)
    imputed = complete_case(data)
    expected = np.arange(5, 25, dtype=float).reshape(4, 5)
    assert np.equal(imputed, expected).all()
