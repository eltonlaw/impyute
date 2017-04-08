"""
Complete Case Algorithm
----------------------
"""
import pandas as pd


def complete_case(data):
    """ Return only data rows with complete data

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """

    df = pd.DataFrame(data)
    df.dropna(axis=0, how="any", inplace=True)
    return df.as_matrix()
