""" impyute: Data imputations library to preprocess datasets with missing dat

impyute.imputations.cs:   Imputations on cross sectional data
impyute.imputations.ts:   Imputations on time series data
impyute.deletion:         Deletion type missing data handling
impyute.contrib:          Volatile and experimental code
"""
# pylint: disable=wrong-import-position

__title__ = 'impyute'
__version__ = '0.0.8'
__build__ = 0x021300
__author__ = 'Elton Law'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 Elton law'


### Top Level Modules

from impyute import dataset
from impyute import deletion
from impyute import ops
from impyute import contrib

__all__ = ["contrib", "dataset", "deletion", "ops"]

### Cross Sectional Imputations

from impyute.imputation.cs import mean
from impyute.imputation.cs import median
from impyute.imputation.cs import mode
from impyute.imputation.cs import em
from impyute.imputation.cs import fast_knn
from impyute.imputation.cs import buck_iterative
from impyute.imputation.cs import random

__all__.extend([
    "mean",
    "median",
    "mode",
    "em",
    "fast_knn",
    "buck_iterative",
    "random"
])

### Time Series Imputations

from impyute.imputation.ts import locf
from impyute.imputation.ts import moving_window

__all__.extend([
    "locf",
    "moving_window"
])

### Deletions
from impyute.deletion import complete_case

__all__.extend([
    "complete_case"
])
