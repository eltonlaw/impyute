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
        cleaned_data = fn(cleaned_data)
        print("Cleaned: \n{}\n".format(cleaned_data))
    if write:
        filename =fn.__name__+"_test_"+str(i)+".txt"
        np.savetxt(filename,test_data+new_data)
    

#############

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

def complete_case_analysis(data):
    """ Return only data rows with complete data"""
    df = pd.DataFrame(data)
    
    return df.as_matrix()

test(simple_random_imputation)

    

