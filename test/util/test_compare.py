"""test_compare.py"""
import unittest
import numpy as np
import impyute as impy

# pylint: disable=missing-docstring
class TestCompare(unittest.TestCase):
    """ Tests for `compare`"""
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        mask = np.zeros((5, 5), dtype=bool)
        mask[0][0] = True
        data_m = impy.dataset.test_data(mask=mask)
        labels = np.array([1, 0, 1, 1, 0])
        self.imputed_mode = []
        self.imputed_mode.append(["mode", (impy.mode(np.copy(data_m)), labels)])
        self.imputed_mode.append(["mean", (impy.mean(np.copy(data_m)), labels)])

    def test_output_file_exists(self):
        path = "./results.txt"
        impy.util.compare(self.imputed_mode, log_path=path)
