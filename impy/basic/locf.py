"""
Last Observation Carried Forward Algorithm
------------------------------------------
"""

import pandas as pd


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
    df = pd.DataFrame(data)
    missing_i = []
    for col in df:
        missing_col_i = pd.isnull(df[col].values).nonzero()[0]
        if len(missing_col_i) > 0:
            for i in missing_col_i:
                missing_i.append((col, i))
    for col, row in missing_i:
        try:
            df.set_value(row, col, df[col-1][row])
        except LookupError as _:
            df.set_value(row, col, df[col+1][row])
    return df.as_matrix()
