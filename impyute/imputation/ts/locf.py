""" impyute.imputation.ts.locf """
import numpy as np
from impyute.util import find_null
from impyute.util import checks
from impyute.util import preprocess


@preprocess
@checks
def locf(data, axis=0):
    """ Last Observation Carried Forward

    For each set of missing indices, use the value of one row before(same
    column). In the case that the missing value is the first row, look one
    row ahead instead. If this next row is also NaN, look to the next row.
    Repeat until you find a row in this column that's not NaN. All the rows
    before will be filled with this value.

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.
    axis: boolean (optional)
        0 if time series is in row format (Ex. data[0][:] is 1st data point).
        1 if time series is in col format (Ex. data[:][0] is 1st data point).

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    if axis == 0:
        data = np.transpose(data)
    elif axis == 1:
        pass

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
                # pylint: disable=undefined-loop-variable
                for x_nan in range(i):
                    data[x_i+x_nan][y_i] = data[x_i+i][y_i]
            else:
                raise Exception("Error: Entire Column is NaN")
    return data
