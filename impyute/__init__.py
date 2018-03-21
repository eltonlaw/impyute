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

__all__ = ["datasets", "utils", "deletions", "filters"]

### Cross Sectional Imputations

from impyute.imputations.cs import mean_imputation as mean
from impyute.imputations.cs import median_imputation as median
from impyute.imputations.cs import mode_imputation as mode
from impyute.imputations.cs import em
from impyute.imputations.cs import fast_knn
from impyute.imputations.cs import mice
from impyute.imputations.cs import random_imputation as random

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

from impyute.imputations.ts import locf
from impyute.imputations.ts import arima

__all__.extend([
    "locf",
    "arima"
])

### Deletions
from impyute.deletions import complete_case

__all__.extend([
    "complete_case"
])
