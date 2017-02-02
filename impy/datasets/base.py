import numpy as np

def randomly_generate(range_i=7,data_shape=(5,5)):
    a = np.append(np.arange(range_i),np.nan)
    sample_data = np.random.choice(a,data_shape)
    return sample_data
