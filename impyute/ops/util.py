""" Random utility functions """
from functools import wraps

__all__ = [
    "constantly", "complement", "identity", "thread",
    "execute_fn_with_args_and_or_kwargs"
    ]

def thread(arg, *fns):
    if len(fns) > 0:
        return thread(fns[0](arg), *fns[1:])
    else:
        return arg

def identity(x):
    return x

def constantly(x):
    """ Returns a function that takes any args and returns x """
    def func(*args, **kwargs):
        return x
    return func

def complement(fn):
    """ Return fn that outputs the opposite truth values of the
    input function
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return not fn(*args, **kwargs)
    return wrapper

def execute_fn_with_args_and_or_kwargs(fn, args, kwargs):
    """ If args + kwargs aren't accepted only args are passed in"""
    try:
        return fn(*args, **kwargs)
    except TypeError:
        return fn(*args)
