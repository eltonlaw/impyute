import pandas as pd
import numpy as np

def mean_imputation(data):
    """Multivariate Imputation by Chained Equations

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    
    """
    null_xy = np.argwhere(np.isnan(data))
    cols_missing = set([y  for x,y in null_xy])
    for x,y in null_xy: 
        col_wo_nan = data[:,[y]][~np.isnan(data[:,[y]])]
        new_value = np.mean(col_wo_nan)
        data[x][y] = new_value
    return data

