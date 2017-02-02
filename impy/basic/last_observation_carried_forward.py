import pandas as pd
import numpy as np

def last_observation_carried_forward(data):
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

