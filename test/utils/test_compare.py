"""test_averaging_imputations.py"""
import unittest
import numpy as np
from impyute.utils import compare
from impyute.imputations.cs import mode_imputation
from impyute.imputations.cs import mean_imputation
from impyute.datasets import test_data

# pylint: disable=missing-docstring
class TestCompare(unittest.TestCase):
    """ Tests for Averaging Imputations"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        mask[0][0] = True
        data_m = test_data(mask=mask)
        labels = np.array([1, 0, 1, 1, 0])
        self.imputed_mode = []
        self.imputed_mode.append(["mode", (mode_imputation(np.copy(data_m)), labels)])
        self.imputed_mode.append(["mean", (mean_imputation(np.copy(data_m)), labels)])

    def test_output_file_exists(self):
        path = "./results.txt"
        compare(self.imputed_mode, log_path=path)
