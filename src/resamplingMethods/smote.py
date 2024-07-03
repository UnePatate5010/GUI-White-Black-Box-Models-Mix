"""
File providing a function that returns an instance of an object that resample data with the SMOTE algorithm
"""
from imblearn.over_sampling import SMOTE


def smote(k_neighbors):
    """Instantiate a SMOTE object with the provided parameters
    
    :param k_neighbors: The number of neighbors that are considered for each point to augment the dataset
    :type k_neighbors: int
    :return: A SMOTE resmapling method with the right parameters
    :rtype: class <SMOTE>
    """
    return SMOTE(k_neighbors=k_neighbors)