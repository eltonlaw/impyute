""" impyute.deletions.complete_case """
import pandas as pd


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
    df = pd.DataFrame(data)
    df.dropna(axis=0, how="any", inplace=True)
    return df.as_matrix()
