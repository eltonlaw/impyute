"""test_gaussian.py"""
import unittest
from impy.tools.theta import gaussian
from impy.datasets import random_uniform


class TestGaussian(unittest.TestCase):
    """ Tests for finding distribution paramers"""
    def setUp(self):
        self.data = random_uniform(missingness="complete")
        self.valid_dist = "gaussian"
        self.invalid_dist = "qw"

    def test_return_type(self):
        """gaussian: Tests if it returns a dictionary"""
        self.assertTrue(isinstance(gaussian(self.data, self.valid_dist), dict))

    def test_invalid_dist(self):
        """gaussian: Tests if invalid "dist" raises an exception"""
        with self.assertRaises(Exception) as context:
            gaussian(self.data, self.invalid_dist)
            self.assertTrue("Value of 'dist' qw is not valid"
                            in context.exception)


if __name__ == "__main__":
    unittest.main()
