"""test_averagings.py"""
import impyute as impy
from impyute.util.testing import return_na_check

SHAPE = (5, 5)


def test_mean(test_data):
    data = test_data(SHAPE)
    imputed = impy.mean(data)
    return_na_check(imputed)


def test_mode(test_data):
    data = test_data(SHAPE)
    imputed = impy.mode(data)
    return_na_check(imputed)


def test_median(test_data):
    data = test_data(SHAPE)
    imputed = impy.median(data)
    return_na_check(imputed)