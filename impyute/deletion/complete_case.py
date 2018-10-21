""" impyute.deletion.complete_case """
import numpy as np
from impyute.util import checks
from impyute.util import preprocess

@preprocess
@checks
def complete_case(data):
    """ Return only data rows with all columns

    Parameters
    ----------
    data: numpy.ndarray
        Data to impute.

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    return data[~np.isnan(data).any(axis=1)]
