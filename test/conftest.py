import os
import shutil

import pytest
import numpy as np


@pytest.fixture(scope='function')
def test_data():
    def prepare_data(shape=(3, 3), pos1=0, pos2=0):
        data = np.reshape(np.arange(np.product(shape)), shape).astype("float")
        data[pos1, pos2] = np.nan
        return data
    return prepare_data


@pytest.fixture(scope='session')
def buck_test_data():
    data = np.asarray([[1, 2, 3, 4, 5, 6, 7, 8],
                   [1, 4, 6, 8, 10, 12, 14, 16],
                   [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
                   [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
                   [3, 6, 9, 12, 15, 18, 21, 24],
                   [4, 8, 9, 16, 20, 24, 28, 32]])
    data[0, 0] = np.nan
    return data


@pytest.fixture(scope='session')
def knn_test_data():
    n = 100
    data = np.random.normal(size=n * n).reshape((n, n))
    for _ in range(int(n * 0.3 * n)):
        data[np.random.randint(n), np.random.randint(n)] = np.nan
    return data


@pytest.fixture(scope='function')
def mw_data():
    return np.arange(0, 25).reshape(5, 5).astype(float)


@pytest.fixture(scope='session')
def results_path(tmpdir_factory):
    temp = tmpdir_factory.mktemp('logs')
    p = os.path.realpath(temp)
    log_path = os.path.join(p, 'results.txt')
    yield log_path
    if temp.exists():
        shutil.rmtree(str(temp))