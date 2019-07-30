"""test_em.py"""
import impyute as impy
from impyute.util.testing import return_na_check

SHAPE = (5, 5)


def test_em_(test_data):
    data = test_data(SHAPE)
    imputed = impy.em(data)
    return_na_check(imputed)