"""
File providing a function that returns an instance of an object that resample data with the ADASYN algorithm
"""
from imblearn.over_sampling import ADASYN
from resamplingMethods.resamplingMethod import resamplingMethod
import numpy as np


class adasyn(resamplingMethod):
    """Instantiate a ADASYN object with the provided parameters
    
    :param k_neighbors: The number of neighbors that are considered for each point to augment the dataset
    :type k_neighbors: int
    :return: A ADASYN resmapling method with the right parameters
    :rtype: class <ADASYN>
    """
    def __init__(self, k_neighbors):
        
        super().__init__()

        self.method = ADASYN(n_neighbors=k_neighbors)

    def fit_resample(self, X, y):
        unique, counts = np.unique(y, return_counts=True)
        if len(unique) > 1 and counts[1] > 1:
            if self.method.n_neighbors >= counts[1]:
                self.method.n_neighbors = counts[1] - 1 
            return self.method.fit_resample(X, y)
        return X, y
