""" impyute.dataset.corrupt """
import numpy as np


class Corruptor:
    """ Adds missing values to a complete dataset.

    Attributes
    ----------
    data: np.ndarray
        Matrix of values with no NaN's that you want to add NaN's to.
    thr: float (optional)
        The percentage of null values you want in your dataset, a number
        between 0 and 1.

    Methods
    -------
    mcar()
        Overwrite values with MCAR placed NaN's.
    mar()
        Overwrite values with MAR placed NaN's.
    mnar()
        Overwrite values with MNAR placed NaN's.

    """
    def __init__(self, data, thr=0.2, dtype=np.float):
        self.dtype = data.dtype
        self.shape = np.shape(data)
        self.data = data.astype(dtype)
        self.thr = thr

    def mcar(self):
        """ Overwrites values with MCAR placed NaN's """
        data_1d = self.data.flatten()
        n_total = len(data_1d)
        null_x = np.random.choice(range(n_total),
                                  size=int(self.thr*n_total),
                                  replace=False)
        for x_i in null_x:
            data_1d[x_i] = np.nan
        output = data_1d.reshape(self.shape)
        return output

    def mar(self):
        """ Overwrites values with MAR placed NaN's """
        output = self.data.copy()
        nrow, ncol = self.data.shape
        for i in range(0, nrow):
            for j in range(0, ncol - 1):
                cutoff = np.percentile(self.data[:, j], (1 - self.thr) * 100)
                if self.data[i, j] > cutoff:
                    output[i, j + 1] = np.nan
            # first columns
            cutoff = np.percentile(self.data[:, -1], (1 - self.thr) * 100)
            if self.data[i, -1] > cutoff:
                output[i, 0] = np.nan
        return output

    def mnar(self):
        """ Overwrites values with MNAR placed NaN's """
        pass

    def complete(self):
        """ Do nothing to the data """
        output = self.data
        return output
