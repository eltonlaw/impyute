""" impyute.util.preprocess """
from functools import wraps

# Hacky way to handle python2 not having `ModuleNotFoundError`
# pylint: disable=redefined-builtin, missing-docstring
try:
    raise ModuleNotFoundError
except NameError:
    class ModuleNotFoundError(Exception):
        pass
except ModuleNotFoundError:
    pass
# pylint: enable=redefined-builtin, missing-docstring

def execute_fn_with_args_and_or_kwargs(fn, args, kwargs):
    """ If args + kwargs aren't accepted only args are passed in"""
    try:
        return fn(*args, **kwargs)
    except TypeError:
        return fn(*args)

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
        results = execute_fn_with_args_and_or_kwargs(fn, args, kwargs)

        # If Pandas exists, and the input data is a dataframe
        # then cast the input to an np.array and cast the output
        # back to a DataFrame.
        if pd_DataFrame and isinstance(args[0], pd_DataFrame):
            args[0] = args[0].values
            results = pd_DataFrame(results)

        return results
    return wrapper
