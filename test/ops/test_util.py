import numpy as np
from impyute.ops import matrix
from impyute.ops import util

def _add_one(x):
    """ """
    return x + 1

def _square(x):
    return x * x

def test_thread():
    assert 10 == util.thread(3, _square, _add_one)
    assert 100 == util.thread(3, _square, _add_one, _square) #4
    assert 82 == util.thread(3, _square, _square, _add_one) #4
    assert 10 == util.thread(3, lambda x: x*x, lambda x: x+1)
    assert 100 == util.thread(3, lambda x: x*x, lambda x: x+1, lambda x: x*x)
    assert 82 == util.thread(3, lambda x: x*x, lambda x: x*x, lambda x: x+1)

def test_identity():
    arr = np.array([[1., 2., 3.]])
    actual = arr
    expected = util.identity(arr)
    assert matrix.every_nd(bool, expected == actual)
