"""
File providing a function that returns an instance of an object that resample data with the SMOTE algorithm
"""
from imblearn.over_sampling import SMOTE


def smote(k_neighbors):
    return SMOTE(k_neighbors=k_neighbors)