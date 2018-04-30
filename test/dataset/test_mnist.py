"""test_mnist.py"""
import unittest
import numpy as np
from impyute.dataset import mnist
from impyute.util import find_null


@unittest.skip("takes a long time, adds 30 sec for each test")
class TestMNIST(unittest.TestCase):
    """ Tests for base.py/mnist"""
    def setUp(self):
        self.data = mnist()["X"]

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        self.assertTrue(isinstance(self.data, np.ndarray))

    def test_missing_values_present(self):
        """ Check that the dataset is corrupted (missing values present)"""
        self.assertTrue(find_null(self.data).size != 0)


if __name__ == "__main__":
    unittest.main()
