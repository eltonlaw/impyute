import numpy as np

def mode_imputation(data):
    """ Substitute missing values with the mode of that column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    
    """
    null_xy = np.argwhere(np.isnan(data))
    cols_missing = set([y  for x,y in null_xy])
    modes = []
    for y in range(np.shape(data)[1]):
        unique_counts = np.unique(data[:,[y]],return_counts=True)
        max_count = np.max(unique_counts[1])
        mode_y = [u for u,c in np.transpose(unique_counts) if c == max_count and not np.isnan(u)] 
        modes.append(mode_y)  # Appends index of column and column modes
    for x,y in null_xy:
        data[x][y] = np.random.choice(modes[y])
    return data
