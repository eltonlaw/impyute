import numpy as np


class Mutator:
    """ Adds missingness to a complete dataset """
    def __init__(self, data, th=np.random.rand()):
        self.data = data
        self.th = th

    def mcar(self):
        """ Mutates a full dataset into a raw dataset that fulfills missingness
        completely at random

        PARAMETERS
        ---------
        th: float[0-1] (optional)
            The percentage of null values you want in your dataset

        RETURNS
        ------
        dict
        """
        for (x, y), _ in np.ndenumerate(self.data):
            if np.random.rand() > self.th:
                pass
            else:
                self.data[x][y] = np.nan
        output = {"data": self.data, "th": self.th}
        return output

    def mar(self):
        """ Mutates a full dataset into a raw dataset that fulfills missingness
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
        """ Mutates a full dataset into a raw dataset that fulfills missingness
        not at random
        """
        pass

    def complete(self):
        """ Do nothing to the data """
        output = {"data": self.data, "th": np.nan}
        return output
