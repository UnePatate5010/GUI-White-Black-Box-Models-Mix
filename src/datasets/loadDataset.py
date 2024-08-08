"""
File deidcated to load datasets from a csv file (via its path) and convert it to an array of data and an array of labels
"""

import csv
import numpy as np

def loadDataset(path):
    """Function that imports/loads a dataset from a csv file
    
    :param path: Path to the csv file. Either a absolute path or a relative path from the directory where the GUI was launched
    :type path: str
    :return: A List representing the dataset, a list of labels
    :rtype: list, list
    """
    X = []
    y = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", lineterminator = '\n')
        for row in reader:
            X.append(row[:-1])
            y.append(row[-1])
    X = np.array(X).astype(np.float32)
    y = np.array(y).astype(np.int16)
    return X, y
