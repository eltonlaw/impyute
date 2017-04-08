"""
Last Observation Carried Forward Algorithm
------------------------------------------
"""

from impyute.diagnostics import find_null


def locf(data):
    """ For missing values use the last observation carried forward

    For each set of missing indices, use the value of one column before(same
    row). In the case that the missing value is the first column, we take one
    column ahead instead (same row still).

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    null_xy = find_null(data)
    for x_i, y_i in null_xy:
        try:
            data[x_i][y_i] = data[x_i][y_i-1]
        except:
            data[x_i][y_i] = data[x_i][y_i+1]
    return data
