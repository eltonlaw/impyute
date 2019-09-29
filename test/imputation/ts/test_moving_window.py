""" test/imputation/ts/test_moving_window.py """
import pytest
import numpy as np
import impyute as impy
from impyute.ops.testing import return_na_check
#pylint:disable=missing-docstring, redefined-outer-name


@pytest.mark.parametrize(
    'pos1,pos2,expected',
    [
        (2, 0, 11.5),
        (2, 2, 12),
        (2, -1, 12.5)]
    )
def test_defaults_impute(pos1, pos2, expected, mw_data):
    mw_data[pos1, pos2] = np.nan
    imputed = impy.moving_window(mw_data)
    return_na_check(imputed)
    assert imputed[pos1, pos2] == expected


@pytest.mark.parametrize(
    'pos1,pos2,expected',
    [
        (2, 0, 24),
        (2, 2, 28),
        (2, -1, 26)]
    )
def test_custom_fn_impute(pos1, pos2, expected, mw_data):
    mw_data[pos1, pos2] = np.nan
    imputed = impy.moving_window(mw_data, func=lambda l: max(l) * 2)
    return_na_check(imputed)
    assert imputed[pos1, pos2] == expected


@pytest.mark.parametrize(
    'pos1,pos2,expected',
    [
        (2, 0, 12.5),
        (2, -1, 12.5)]
    )
def test_custom_nindex_impute_0(pos1, pos2, expected, mw_data):
    mw_data[pos1, pos2] = np.nan
    imputed = impy.moving_window(mw_data, nindex=0)
    return_na_check(imputed)
    assert imputed[pos1, pos2] == expected


@pytest.mark.parametrize(
    'pos1,pos2,expected',
    [
        (2, 0, 11.5),
        (2, -1, 11.5)]
    )
def test_custom_nindex_impute_1(pos1, pos2, expected, mw_data):
    mw_data[pos1, pos2] = np.nan
    imputed = impy.moving_window(mw_data, nindex=-1)
    return_na_check(imputed)
    assert imputed[pos1, pos2] == expected
