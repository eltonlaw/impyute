""" impyute.util.preprocess """
from functools import wraps
# pylint:disable=invalid-name

# TODO:Some hacky ass code to handle python2 not having `ModuleNotFoundError`
try:
    raise ModuleNotFoundError
except NameError:
    class ModuleNotFoundError(Exception):
        pass
except ModuleNotFoundError:
    pass


def preprocess(fn):
    """ Base preprocess function for commonly used preprocessing

    PARAMETERS
    ----------
    data: numpy.ndarray
        Data to impute.

    RETURNS
    -------
    bool
        True if `data` is correctly formatted

    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """ Run input checks"""
        # convert tuple to list so args can be modified
        args = list(args)

        # Either make a copy or use a pointer to the original
        if "inplace" in kwargs and kwargs['inplace']:
            args[0] = args[0]
        else:
            args[0] = args[0].copy()

        # Check if Pandas exists
        try:
            import pandas as pd
            pd_DataFrame = pd.DataFrame
        except (ModuleNotFoundError, ImportError):
            pd_DataFrame = None

        # If Pandas exists, and the input data is a dataframe
        # then cast the input to an np.array and cast the output
        # back to a DataFrame.
        if pd_DataFrame and isinstance(args[0], pd_DataFrame):
            args[0] = args[0].as_matrix()
            return pd_DataFrame(fn(*args, **kwargs))
        else:
            return fn(*args, **kwargs)

    return wrapper
