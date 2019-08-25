"""test_mice.py"""
import impyute as impy
from impyute.util.testing import return_na_check

SHAPE = (5, 5)


def test_mice(test_data):
    data = test_data(SHAPE)
    imputed = impy.em(data)
    return_na_check(imputed)
