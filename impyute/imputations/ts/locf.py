"""
Last Observation Carried Forward Algorithm
------------------------------------------
"""

from impyute.utils import find_null
import numpy as np
from impyute.utils import checks


def locf(data):
    """ For missing values use the last observation carried forward

    For each set of missing indices, use the value of one row before(same
    column). In the case that the missing value is the first row, look one
    row ahead instead. If this next row is also NaN, look to the next row.
    Repeat until you find a row in this column that's not NaN. All the rows
    before will be filled with this value.

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    if not checks(data):
        raise Exception("Checks failed")
    null_xy = find_null(data)
    for x_i, y_i in null_xy:
        # Simplest scenario, look one row back
        if x_i-1 > -1:
            data[x_i][y_i] = data[x_i-1][y_i]
        # Look n rows forward
        else:
            x_residuals = np.shape(data)[0]-x_i-1  # n datapoints left
            val_found = False
            for i in range(1, x_residuals):
                if not np.isnan(data[x_i+i][y_i]):
                    val_found = True
                    break
            if val_found:
                for x_nan in range(i):
                    data[x_i+x_nan][y_i] = data[x_i+i][y_i]
            else:
                print("Error: Entire Column is NaN")
                raise Exception
    return data
