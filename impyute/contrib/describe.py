""" impyute.contrib.describe """
from impyute.ops import matrix

def describe(data): # verbose=True):
    """ Print input/output multiple times

    Eventually will be used instead of matrix.nan_indices everywhere

    Parameters
    ----------
    data: numpy.nd.array
        The data you want to get a description from
    verbose: boolean(optional)
        Decides whether the description is short or long form

    Returns
    -------
    dict
        missingness: list
            Confidence interval of data being MCAR, MAR or MNAR - in that order
        nan_xy: list of tuples
            Indices of all null points
        nan_n: list
            Total number of null values for each column
        pmissing_n: float
            Percentage of missing values in dataset
        nan_rows: list
            Indices of all rows that are completely null
        nan_cols: list
            Indices of all columns that are completely null
        mean_rows: list
            Mean value of each row
        mean_cols: list
            Mean value of each column
        std_dev: list
            std dev for each row/column
        min_max: list
            Finds the minimum and maximum for each row

    """
#    missingness = [0.33, 0.33, 0.33]  # find_missingness(data)
    nan_xy = matrix.nan_indices(data)
    nan_n = len(nan_xy)
    pmissing_n = float(nan_n/len(data.flatten))
#    pmissing_rows = ""
#    pmissing_cols = ""
#    nan_rows = ""
#    nan_cols = ""
#    mean_rows = ""
#    mean_cols = ""
#    std_dev = ""
#                   "missingness": missingness,
    description = {"nan_xy": nan_xy,
                   "nan_n": nan_n,
                   "pmissing_n": pmissing_n}
#                   "pmissing_rows": pmissing_rows,
#                   "pmissing_cols": pmissing_cols,
#                   "nan_rows": nan_rows,
#                   "nan_cols": nan_cols,
#                   "mean_rows": mean_rows,
#                   "mean_cols": mean_cols,
#                   "std_dev": std_dev}
    return description
