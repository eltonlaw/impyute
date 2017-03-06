"""
The :mod: impy.imputations module implements baseline imputation algorithms
"""

from .locf import locf
from .random_imputation import random_imputation
from .averaging_imputations import mean_imputation
from .averaging_imputations import mode_imputation
from .averaging_imputations import median_imputation

__all__ = ["locf", "random_imputation",
           "mean_imputation", "mode_imputation", "median_imputation"]
