import numpy as np


class Corruptor:
    """ Adds missingness to a complete dataset """
    def __init__(self, data, th=np.random.rand()):
        self.dtype = data.dtype
        self.shape = np.shape(data)
        self.data = data.astype(np.float)
        self.th = th

    def mcar(self):
        """ Corrupts a full dataset into a raw dataset that fulfills missingness
        completely at random

        PARAMETERS
        ---------
        th: float[0-1] (optional)
            The percentage of null values you want in your dataset

        RETURNS
        ------
        dict
        """
        data_1d = self.data.flatten()
        n_total = len(data_1d)
        null_x = np.random.choice(range(n_total),
                                  size=int(self.th*n_total),
                                  replace=False)
        for x in null_x:
            data_1d[x] = np.nan
        output = data_1d.reshape(self.shape).astype(self.dtype)
        return output

    def mar(self):
        """ Corrupts a full dataset into a raw dataset that fulfills missingness
        at random

        PARAMETERS
        ---------
        th: (optional)
            The percentage of null values you want in your dataset

        RETURNS
        ------
        numpy.ndarray
        """
        pass

    def mnar(self):
        """ Corrupts a full dataset into a raw dataset that fulfills missingness
        not at random
        """
        pass

    def complete(self):
        """ Do nothing to the data """
        output = self.data.astype(self.dtype)
        return output
