"""Print input/output multiple times"""


def print_io(fn, loops=1, **kwargs):
    """ Prints out input data and output data
    PARAMETERS
    ---------
    fn: Function
    loops: # of Loops
    **kwargs: Arguments for random_int function

    RETURNS
    ------
    n/a

    """
    from impy.datasets import random_int

    print("Function:{}".format(str(fn.__name__)))
    for i in range(loops):
        data = random_int(**kwargs)
        print("\n")
        print("{} ========".format(i))
        print("{}  {}".format(data, fn(data)))
    print("============================")
