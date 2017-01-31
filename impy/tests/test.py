import numpy as np
import pandas as pd
from basic_imputations import *
#from mice import mice

def generate_data(range_i=7,data_shape=(5,5)):
    a = np.append(np.arange(range_i),np.nan)
    sample_data = np.random.choice(a,data_shape)
    return sample_data

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
    #test(mice)
    test(mean_imputation)
    pass

if __name__ == "__main__":
    run()
