import numpy as np
import pandas as pd
from basic_imputations import *
from mice import *

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

def run():
    #test(simple_random_imputation)
    #test(complete_case)
    #test(locf)

if __name__ == "__main__":
    run()
