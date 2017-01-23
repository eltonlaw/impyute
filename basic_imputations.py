import numpy as np
import pandas as pd

def generate_data(range_i=7,data_shape=(5,5)):
    a = np.append(np.arange(range_i),None)
    sample_data = np.random.choice(a,data_shape)
    return sample_data

def drop_null(A):
    A_clean = []
    for a_i in A:
        if not(a_i == ([] or 0 or None)) and not np.isnan(a_i):
            A_clean.append(a_i)
    return A_clean

def test(fn,write=False,n_loops=10):
    for i in range(n_loops):
        print("== Test {} == \n".format(i))
        raw_data = generate_data()
        print("Raw:\n{}".format(raw_data))
        cleaned_data = fn(raw_data)
        print("Cleaned: \n{}\n".format(cleaned_data))
    if write:
        filename =fn.__name__+"_test_"+str(i)+".txt"
        np.savetxt(filename,test_data+new_data)

def init():
    #test(simple_random_imputation)
    test(locf)
    

#############
#data = generate_data()

def simple_random_imputation(data):
    """ Find the missing values in the dataset and fill them in with a randomly selected value from the same column"""
    df = pd.DataFrame(data)

    for col in df:
        df_null = pd.isnull(df[col])
        if (True in df_null.values):
            unique_values  = drop_null(df[col].unique()) # .unique method includes null values so we have to drop them afterward
            df[col][df_null] = np.random.choice(unique_values)
    filled_data = df.as_matrix()
    return filled_data

def complete_case(data):
    """ Return only data rows with complete data"""
    df = pd.DataFrame(data)
    df.dropna(axis=0,how="any",inplace=True)
    return df.as_matrix()

def locf(data):
    """ For missing values use the last observation carried forward """
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

if __name__ == "__main__":
    init()

    

