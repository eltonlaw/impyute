"""test_config.py"""
import unittest
from impyute.utils import config
from impyute.datasets import random_normal


class TestConfig(unittest.TestCase):
    """ Tests for config"""
    def setUp(self):
        self.c = config(random_normal())

    def test_n_layers(self):
        self.assertEqual(len(self.c["layers"]), 2)

    def test_decreasing_layer_size(self):
        self.assertTrue(self.c["layers"][0] > self.c["layers"][1])
