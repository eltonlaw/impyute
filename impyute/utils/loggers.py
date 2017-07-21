""" impyute.utils.loggers """
from impyute.datasets import random_normal


def print_io(fn, loops=1, **kwargs):
    """ Prints out input data and output data

    Parameters
    ----------
    fn: Function
    loops: # of Loops
    **kwargs: Arguments for random_normal function

    Returns
    -------
    n/a

    """

    print("Function:{}".format(str(fn.__name__)))
    for i in range(loops):
        data = random_normal(**kwargs)
        print("\n")
        print("{} ========".format(i))
        print("{}  {}".format(data, fn(data)))
    print("============================")
