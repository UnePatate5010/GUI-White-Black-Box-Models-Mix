"""
File deidcated to load datasets from a csv file (via its path) and convert it to an array of data and an array of labels
"""

import csv
import numpy as np

def loadDataset(path):
    X = []
    y = []
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", lineterminator = '\n')
        for row in reader:
            X.append(row[:-1])
            y.append(row[-1])
    X = np.array(X).astype(np.float16)
    y = np.array(y).astype(np.int16)
    return X, y
