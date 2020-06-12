"""test_mice.py"""
import impyute as impy
from impyute.ops.testing import return_na_check

SHAPE = (5, 5)

def test_mice(test_data):
    imputed = impy.mice(test_data(SHAPE))
    return_na_check(imputed)
