import numpy as np

def median_imputation(data):
    """ Substitute missing values with the mode of that column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    
    """
    null_xy = np.argwhere(np.isnan(data))
    cols_missing = set(null_xy.T[1])
    medians = {}
    for y in cols_missing: 
        cols_wo_nan = data[:,[y]][~np.isnan(data[:,[y]])]
        median_y = np.median(cols_wo_nan)
        medians[str(y)] = median_y
    for x,y in null_xy:
        data[x][y] = medians[str(y)]


