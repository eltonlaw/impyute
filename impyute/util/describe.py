""" impyute.util.describe """
from impyute.util import find_null


def describe(data): # verbose=True):
    """ Print input/output multiple times

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
        null_xy: list of tuples
            Indices of all null points
        null_n: list
            Total number of null values for each column
        pmissing_n: float
            Percentage of missing values in dataset
        null_rows: list
            Indices of all rows that are completely null
        null_cols: list
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
    null_xy = find_null(data)
    null_n = len(null_xy)
    pmissing_n = float(null_n/len(data.flatten))
#    pmissing_rows = ""
#    pmissing_cols = ""
#    null_rows = ""
#    null_cols = ""
#    mean_rows = ""
#    mean_cols = ""
#    std_dev = ""
#                   "missingness": missingness,
    description = {"null_xy": null_xy,
                   "null_n": null_n,
                   "pmissing_n": pmissing_n}
#                   "pmissing_rows": pmissing_rows,
#                   "pmissing_cols": pmissing_cols,
#                   "null_rows": null_rows,
#                   "null_cols": null_cols,
#                   "mean_rows": mean_rows,
#                   "mean_cols": mean_cols,
#                   "std_dev": std_dev}
    return description
