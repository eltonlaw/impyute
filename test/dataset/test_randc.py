import numpy as np
import pytest
from impyute.dataset.base import randc
from impyute.util import BadInputError

def test_raise_error_nlevel_exceed_shape():
    with pytest.raises(BadInputError) as e:
        randc(shape=(2, 2))
    expected = "nlevel exceeds the size of desired dataset. Please decrease the nlevel or increase the shape"
    assert str(e.value) == expected

@pytest.mark.parametrize("nlevels, shape", [(5, (5,5)), (9, (3,4)), (100, (20, 20))])
def test_nlevel_categories(nlevels, shape):
    """ideally the returned matrix should have nlevel+1 different categories, +1 because the Corrupt class introduce np.nan
       however, if the missing value introduced by Corrupt class happens to replace a group of categories, the unique
       category number would be < nlevel + 1
    """
    dataframe = randc(nlevels, shape)
    assert len(np.unique(dataframe)) <= nlevels + 1


@pytest.mark.parametrize("nlevels, shape", [(5, (5,5)), (9, (3, 4)), (100, (20, 20))])
def test_dataframe_shape(nlevels, shape):
    """test if the returned data frame has desired shape"""
    dataframe = randc(nlevels, shape)
    assert dataframe.shape == shape
