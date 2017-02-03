import numpy as np

def mean_imputation(data):
    """ Substitute missing values with the mean of that column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    
    """
    #temp = data
    data = temp
    null_xy = np.argwhere(np.isnan(data))
    cols_missing = set([y  for x,y in null_xy])
    for x,y in null_xy: 
        row_wo_nan= data[:,[y]][~np.isnan(data[:,[y]])]
        new_value = np.mean(row_wo_nan)
        data[x][y] = new_value
    return data
