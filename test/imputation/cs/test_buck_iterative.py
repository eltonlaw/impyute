"""test_buck_iterative.py"""
import impyute as impy
from impyute.ops.testing import return_na_check


def test_buck_iter(buck_test_data):
    imputed = impy.buck_iterative(buck_test_data)
    return_na_check(imputed)
