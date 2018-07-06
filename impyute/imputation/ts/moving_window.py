""" impyute.imputation.ts.moving_window """
import numpy as np
from impyute.util import find_null
from impyute.util import checks
from impyute.util import preprocess
# pylint: disable=invalid-name
# pylint:disable=unused-argument

@preprocess
@checks
def moving_window(data, nindex=None, wsize=5, errors="coerce", func=np.mean,
        inplace=False, **kwargs):
    """ Interpolate the missing values based on nearby values.

    For example, with an array like this:

        array([[-1.24940, -1.38673, -0.03214945,  0.08255145, -0.007415],
               [ 2.14662,  0.32758 , -0.82601414,  1.78124027,  0.873998],
               [-0.41400, -0.977629,         nan, -1.39255344,  1.680435],
               [ 0.40975,  1.067599,  0.29152388, -1.70160145, -0.565226],
               [-0.54592, -1.126187,  2.04004377,  0.16664863, -0.010677]])

    Using a `k` or window size of 3. The one missing value would be set
    to -1.18509122. The window operates on the horizontal axis.

    Usage
    -----

    The parameters default the function to a moving mean. You may want to change
    the default window size:
        
        moving_window(data, wsize=10)

    To only look at past data (null value is at the rightmost index in the window):

        moving_window(data, nindex=-1)

    To use a custom function:
    
        moving_window(data, func=np.median)

    You can also do something like take 1.5x the max of previous values in the window:

        moving_window(data, func=lambda arr: max(arr) * 1.50, nindex=-1)
    

    Parameters
    ----------
    data: numpy.ndarray
        2D matrix to impute.
    nindex: int
        Null index. Index of the null value inside the moving average window.
        Use cases: Say you wanted to make value skewed toward the left or right
        side. 0 would only take the average of values from the right and -1
        would only take the average of values from the left
    wsize: int
        Window size. Size of the moving average window/area of values being used
        for each local imputation. This number includes the missing value.
    errors: {"raise", "coerce", "ignore"}
        Errors will occur with the indexing of the windows - for example if there
        is a nan at data[x][0] and `nindex` is set to -1 or there is a nan at
        data[x][-1] and `nindex` is set to 0. `"raise"` will raise an error,
        `"coerce"` will try again using an nindex set to the middle and `"ignore"`
        will just leave it as a nan.
    inplace: {True, False}
        Whether to return a copy or run on the passed-in array

    Returns
    -------
    numpy.ndarray
        Imputed data.

    """
    if errors == "ignore":
        raise Exception("`errors` value `ignore` not implemented yet. Sorry!")

    if not inplace:
        data = data.copy()

    wsize = 5
    nindex = None
    if nindex is None: # If using equal window side lengths
        assert wsize % 2 == 1, "The parameter `wsize` should not be even "\
        "if the value `nindex` is not set since it defaults to the midpoint "\
        "and an even `wsize` makes the midpoint ambiguous"
        wside_left = wsize // 2
        wside_right = wsize // 2
    else: # If using custom window side lengths
        assert nindex < wsize, "The null index must be smaller than the window size"
        if nindex == -1:
            wside_left = wsize - 1
            wside_right = 0
        else:
            wside_left = nindex
            wside_right = wsize - nindex - 1

    while True:
        null_xy = find_null(data)
        n_null_prev = len(null_xy)
        for x_i, y_i in null_xy:
            left_i = max(0, y_i-wside_left)
            right_i = min(wsize, y_i+wside_right+1)
            window = data[x_i, left_i: right_i]
            window_not_null = window[~np.isnan(window)]

            if len(window_not_null) > 0:
                try:
                    data[x_i][y_i] = func(window_not_null)
                    continue
                except Exception as e:
                    if errors == "raise":
                        raise e
                    else:
                        pass

            # Aggregate function didn't work for some reason
            if errors == "coerce":
                wside_left = wsize // 2
                wside_right = wsize_left
                window = data[x_i, y_i-wside_leftk: y_i + wside_right]
                window_not_null = window[~np.isnan(window)]
                try:
                    data[x_i][y_i] = func(window_not_null)
                except Exception:
                    pass
        if n_null_prev == len(find_null(data)):
            break

    return data
