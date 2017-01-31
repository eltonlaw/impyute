import numpy as np
import pandas as pd

def simple_random_imputation(data):
    """ Find the missing values in the dataset and fill them in with a randomly selected value from the same column
    
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
        if (True in df_null.values):
            unique_values  = [a_i for a_i in df[col].unique() if not(a_i == ([] or 0 or None)) and not np.isnan(a_i)]  # .unique method includes null values so we have to drop them afterward
            df[col][df_null] = np.random.choice(unique_values)
    filled_data = df.as_matrix()
    return filled_data


