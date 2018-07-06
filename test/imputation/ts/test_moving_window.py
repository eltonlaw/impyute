""" test/imputation/ts/test_moving_window.py """
import unittest
import numpy as np
import impyute as impy


class TestMovingWindowDefaults(unittest.TestCase):
    """ Tests for moving_window default parameters """
    def setUp(self):
        self.data = np.arange(0, 25).reshape(5, 5).astype(float)

    def test_impute_leftmost_index(self):
        self.data[2][0] = np.nan 
        imputed = impy.moving_window(self.data)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][0], 11.5)

    def test_impute_middle_index(self):
        self.data[2][2] = np.nan 
        imputed = impy.moving_window(self.data)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][2], 12)

    def test_impute_rightmost_index(self):
        self.data[2][-1] = np.nan 
        imputed = impy.moving_window(self.data)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][-1], 12.5)

class TestMovingWindowCustomFunction(unittest.TestCase):
    """ Tests for passing a custom function """
    def setUp(self):
        self.data = np.arange(0, 25).reshape(5, 5).astype(float)

    def test_impute_leftmost_index(self):
        self.data[2][0] = np.nan 
        imputed = impy.moving_window(self.data, func=lambda l: max(l) * 2)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][0], 24)

    def test_impute_middle_index(self):
        self.data[2][2] = np.nan
        imputed = impy.moving_window(self.data, func=lambda l: max(l) * 2)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][2], 28)

    def test_impute_rightmost_index(self):
        self.data[2][-1] = np.nan 
        imputed = impy.moving_window(self.data, func=lambda l: max(l) * 2)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][-1], 26)

class TestMovingWindowCustomNindex(unittest.TestCase):
    """ Test for edge cases of nindex when the window completely falls off the array """
    def setUp(self):
        self.data = np.arange(0, 25).reshape(5, 5).astype(float)

    def test_impute_leftmost_index(self):
        self.data[2][0] = np.nan 
        imputed = impy.moving_window(self.data, nindex=-1)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][0], 11.5)

    def test_impute_rightmost_index(self):
        self.data[2][-1] = np.nan 
        imputed = impy.moving_window(self.data, nindex=0)
        self.assertFalse(np.isnan(imputed).any())
        self.assertEqual(imputed[2][-1], 12.5)

if __name__ == "__main__":
    unittest.main()
