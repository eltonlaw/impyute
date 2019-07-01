"""test_fast_knn.py"""
import unittest
import numpy as np
import impyute as impy
# pylint:disable=invalid-name

class TestFastKNN(unittest.TestCase):
    """ Tests for Fast KNN """
    def setUp(self):
        """
        self.data_c: Complete dataset/No missing values
        self.data_m: Incommplete dataset/Has missing values
        """
        n = 100
        self.data_c = np.random.normal(size=n*n).reshape((n, n))
        self.data_m = self.data_c.copy()
        for _ in range(int(n*0.3*n)):
            self.data_m[np.random.randint(n)][np.random.randint(n)] = np.nan

    def test_return_type(self):
        """ Check return type, should return an np.ndarray"""
        imputed = impy.fast_knn(self.data_m)
        self.assertTrue(isinstance(imputed, np.ndarray))

    def test_impute_missing_values(self):
        """ After imputation, no NaN's should exist"""
        imputed = impy.fast_knn(self.data_m)
        self.assertFalse(np.isnan(imputed).any())

    def test_impute_value(self):
        data = np.array([[ 0. , 1. , np.nan, 3. , 4. ],
                         [ 5. , 6. , 7. , 8. , 9. ],
                         [10. , 11. , 12. , 13. , 14. ],
                         [15. , 16. , 17. , 18. , 19. ],
                         [20. , 21. , 22. , 23. , 24. ]])
        imputed = impy.fast_knn(data, k=2) # Weighted average of nearest 2 neighbours
        self.assertTrue(np.isclose(imputed[0][2], 8.913911092686593))

if __name__ == "__main__":
    unittest.main()
