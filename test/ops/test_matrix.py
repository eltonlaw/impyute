import numpy as np
from impyute.ops import matrix

def _is_gt_5(x):
    return x > 5

def test_map_nd_2d():
    arr = np.arange(10).reshape([5, 2])
    expected = np.array([
        [False, False],
        [False, False],
        [False, False],
        [True, True],
        [True, True],
    ])
    actual = map_nd(_is_gt_5, arr)
    assert matrix.every_nd(bool, expected == actual)
