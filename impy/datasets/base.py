" Dataset Generation "

import numpy as np
from impy.datasets import Mutator

def randomly_generate(range_i=7, data_shape=(5, 5), m_method="MCAR", m_th=0.3):
    """ Return randomly generated data

    PARAMETERS
    ---------
    range_i:int(optional)
        Determines the range of values in the matrix
    data_shape:tuple(optional)
        Size of the randomly generated data

    RETURNS
    ------
    numpy.ndarray

    """
    possible_points = np.append(np.arange(range_i), np.nan)
    generated_data = np.random.choice(possible_points, data_shape)
    mutator = Mutator()
    mutate = getattr(mutator, m_method)
    raw_data = mutate(generated_data, threshold=m_th).data
    return raw_data
