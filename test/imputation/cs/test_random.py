"""test_random_imputation.py"""
import impyute as impy
from impyute.util.testing import return_na_check

SHAPE = (3, 3)


def test_random_(test_data):
    data = test_data(SHAPE)
    imputed = impy.random(data)
    return_na_check(imputed)