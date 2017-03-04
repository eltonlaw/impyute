import numpy as np


class Mutator:
    """ Adds missingness to a complete dataset """

    def mcar(self, data, threshold=np.random.rand()):
        """ Mutates a full dataset into a raw dataset that fulfills missingness
        completely at random

        PARAMETERS
        ---------
        threshold: float[0-1] (optional)
            The percentage of null values you want in your dataset

        RETURNS
        ------
        dict
        """
        for (x, y), _ in np.ndenumerate(data):
            if np.random.rand() > threshold:
                pass
            else:
                data[x][y] = np.nan
        output = {"data": data, "threshold": threshold}
        return output

    def mar(self, data, threshold):
        """ Mutates a full dataset into a raw dataset that fulfills missingness
        at random

        PARAMETERS
        ---------
        threshold: (optional)
            The percentage of null values you want in your dataset

        RETURNS
        ------
        numpy.ndarray
        """
        pass

    def mnar(self, data):
        """ Mutates a full dataset into a raw dataset that fulfills missingness
        not at random
        """
        pass
