import pandas as pd
import numpy as np

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

def mean_imputation(data):
    """Multivariate Imputation by Chained Equations

    PARAMETERS
    ---------
    data: numpy.ndarray

    RETURNS
    ------
    numpy.ndarray
    
    """
    null_xy = np.argwhere(np.isnan(data))
    cols_missing = set([y  for x,y in null_xy])
    for x,y in null_xy: 
        col_wo_nan = data[:,[y]][~np.isnan(data[:,[y]])]
        new_value = np.mean(col_wo_nan)
        data[x][y] = new_value
    return data

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
    df.dropna(axis=0,how="any",inplace=True)
    return df.as_matrix()

def locf(data):
    """ For missing values use the last observation carried forward 

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
        #print("col:{},missing_col_i:{}".format(col,missing_col_i))
        if len(missing_col_i) > 0:
            for i in missing_col_i:
               missing_i.append((col,i))
    #print("missing_i:{}".format(missing_i))
    for col,row in missing_i:
        #print("df[{}][{}]:{}".format(col,row,df[col][row]))
        try:
            df.set_value(row,col,df[col-1][row])
        except:
            df.set_value(row,col,df[col+1][row])
    return df.as_matrix()

