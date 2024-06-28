"""
File containing the `run` function, which is called to run the full experiment
"""
import numpy as np

class Fuse():
    """
    Class representing the fusion of the different models:
    grader + base + deferral
    """
    def __init__(self, base, deferral, grader):
        self.base = base
        self.deferral = deferral
        self.grader = grader

    def predict(self, data):
        preds = []
        count = 0
        for elmt in data:
            if (self.grader.predict([elmt])[0] == 1):
                count += 1
                preds.append(self.deferral.predict([elmt])[0])
            else:
                preds.append(self.base.predict([elmt])[0])
        # print("nb of hard:", count, "out of ", len(data))
        return np.array(preds)
    

def run(X, y, grader, base, deferral, resampling):
    # Training both grader and deferral
    base = base.fit(X, y)
    deferral = deferral.fit(X, y)
    base_preds = base.predict(X)

    # Train the grader
    # Get the dataset
    indexes = different(base_preds, y)
    X_grader = X
    y_grader = np.zeros((len(X_grader))) 
    y_grader[indexes] = 1 # Label 0: classified correctly / label 1: classified incorrectly
    # Data augmentation
    if len(np.unique(y_grader)) > 1: # Prevents case where the base classifier is too good
        X_grader, y_grader = resampling.fit_resample(X_grader, y_grader)

    # Train
    grader = grader.fit(X_grader, y_grader)

    # Fuse models
    model = Fuse(base, deferral, grader)

    return model, grader


# Different elements (returns indexes where elements of two arrays are different)
def different(arr1, arr2):
    return np.where(arr1 != arr2)[0]

# Return the accuracy of a model over a dataset
def accuracy(model, X, y):
    preds = model.predict(X)
    return np.sum(preds == y) / len(preds)
