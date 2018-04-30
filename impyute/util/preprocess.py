""" impyute.util.preprocess """
from functools import wraps
# pylint:disable=invalid-name

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
        if "inplace" in kwargs and kwargs['inplace']:
            data = args[0]
        else:
            data = args[0].copy()

        if len(args) == 1:
            return fn(data, **kwargs)
        return fn(data, *args[1:], **kwargs)
    return wrapper


