"""
Simple Random Imputation
-----------------------
"""
import numpy as np
import pandas as pd


def random_imputation(data):
    """ Fill missing values in with a randomly selected value from the same column

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    """
    df = pd.DataFrame(data)

    for col in df:
        df_null = pd.isnull(df[col])
        if True in df_null.values:
            # .unique method includes null values so we have to drop it
            unique_values = [a_i for a_i in df[col].unique()
                             if not(a_i == ([] or 0 or None)) and
                             not np.isnan(a_i)]
            df[col][df_null] = np.random.choice(unique_values)
    filled_data = df.as_matrix()
    return filled_data
