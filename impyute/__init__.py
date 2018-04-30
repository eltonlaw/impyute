"""
Library of missing data imputations
"""
# pylint: disable=wrong-import-position

__title__ = 'impyute'
__version__ = '0.0.6'
__build__ = 0x021300
__author__ = 'Elton Law'
__license__ = 'GPL-3.0'
__copyright__ = 'Copyright 2017 Elton law'


### Top Level Modules

__all__ = ["dataset", "util", "deletion", "filter"]

### Cross Sectional Imputations

from impyute.imputation.cs import mean
from impyute.imputation.cs import median
from impyute.imputation.cs import mode
from impyute.imputation.cs import em
from impyute.imputation.cs import fast_knn
from impyute.imputation.cs import mice
from impyute.imputation.cs import random

__all__.extend([
    "mean",
    "median",
    "mode",
    "em",
    "fast_knn",
    "mice",
    "random"
])

### Time Series Imputations

from impyute.imputation.ts import locf
from impyute.imputation.ts import arima

__all__.extend([
    "locf",
    "arima"
])

### Deletions
from impyute.deletion import complete_case

__all__.extend([
    "complete_case"
])
