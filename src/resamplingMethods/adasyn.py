"""
File providing a function that returns an instance of an object that resample data with the ADASYN algorithm
"""
from imblearn.over_sampling import ADASYN


def adasyn(k_neighbors):
    """Instantiate a ADASYN object with the provided parameters
    
    :param k_neighbors: The number of neighbors that are considered for each point to augment the dataset
    :type k_neighbors: int
    :return: A ADASYN resmapling method with the right parameters
    :rtype: class <ADASYN>
    """
    return ADASYN(n_neighbors=k_neighbors)