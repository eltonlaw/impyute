import numpy as np

class Mutator:
    """ 
    Data Mutator    
    """
    def MCAR(self, data, threshold=np.random.rand()):
        """ Mutates a full dataset into a raw dataset that fulfills missingness completely at random
        
        PARAMETERS
        ---------
        threshold: float[0-1] (optional)
            The percentage of null values you want in your dataset
            
        RETURNS
        ------
        dict
        """
        for (x,y),_ in np.ndenumerate(data):
            if np.random.rand() > threshold:
                pass
            else:
                data[x][y] = np.nan
        return {"data":data, "threshold:"threshold}
    def MAR(self, data, threshold):
        """ Mutates a full dataset into a raw dataset that fulfills missingness at random
        
        PARAMETERS
        ---------
        threshold: (optional)
            The percentage of null values you want in your dataset
            
        RETURNS
        ------
        numpy.ndarray
        """
        pass
    def MNAR(self, data):
        pass

