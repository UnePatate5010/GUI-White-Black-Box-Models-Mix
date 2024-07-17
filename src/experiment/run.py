"""
File containing the `run` function, which is called to run the full experiment
"""
import numpy as np

class Fuse():
    """
    Class representing the fusion of the different models:
    grader + base + deferral

    :param base: The base classifier
    :type base: class
    :param deferral: The deferral classifier
    :type deferral: class
    :param grader: The grader
    :type grader: class
    """

    def __init__(self, base, deferral, grader):
        """Constructor method
        """
        self.base = base
        self.deferral = deferral
        self.grader = grader

    def predict(self, data, hard=False):
        """Returns prediction and the number of 'hard' elements.

        :param data: Data to predict classes
        :type data: list
        :param hard: A boolean that specifies if the amount of data labeled as 'hard' should be return or not
        :type hard: boolean
        :return: A list of prediction (and the number of data labeled as 'hard')
        :rtype: numpy array (, int)
        """

        grader_preds = self.grader.predict(data)
        index_hard = np.where(grader_preds == 1)[0]
        index_easy = ~np.isin(np.arange(len(grader_preds)), index_hard)

        preds = np.empty((len(data)))
        if len(index_hard) != 0:
            hard_data = data[index_hard]
            pred_hard = self.deferral.predict(hard_data)
            preds[index_hard] = pred_hard
        if len(index_easy) != 0:
            easy_data = data[index_easy]
            pred_easy = self.base.predict(easy_data)
            preds[index_easy] = pred_easy

        count = len(index_hard)

        if hard:
            return preds, count
        return preds
    
    def predict_base(self, data):
        """Realize a prediction only using the base classifier

        :param data: Data to predict
        :type data: list
        :return: A list of prediction
        :rtype: list
        """
        return self.base.predict(data)
    
    def predict_deferral(self, data):
        """Realize a prediction only using the deferral classifier

        :param data: Data to predict
        :type data: list
        :return: A list of prediction
        :rtype: list
        """
        return self.deferral.predict(data)
    
    def accuracy(self, X, y):
        """Return the accuracy of the whole model over a provided dataset
        
        :param X: Dataset
        :type X: list
        :param y: labels
        :type y: list
        :return: The accuracy of the model
        :rtype: float
        """
        preds = self.predict(X)
        return np.sum(preds == y) / len(preds)
    
    def accuracy_base(self, X, y):
        """Return the accuracy of the base classifier over a provided dataset
        
        :param X: Dataset
        :type X: list
        :param y: labels
        :type y: list
        :return: The accuracy of the model
        :rtype: float
        """
        preds = self.base.predict(X)
        return np.sum(preds == y) / len(preds)
    
    def accuracy_deferral(self, X, y):
        """Return the accuracy of the deferral classifier over a provided dataset
        
        :param X: Dataset
        :type X: list
        :param y: labels
        :type y: list
        :return: The accuracy of the model
        :rtype: float
        """
        preds = self.deferral.predict(X)
        return np.sum(preds == y) / len(preds)
    
    def stats(self, X, y):
        """Returns statistics
        
        :param X: Dataset
        :type X: list
        :param y: labels
        :type y: list
        :return: Accuracy of the model, amount of data labeled as 'hard', accuracy of the base classifier, accuracy of the deferral classifier
        :rtype: float, int, float, float
        """
        preds, hard = self.predict(X, True)
        acc = calc_accuracy(preds, y)
        acc_base = self.accuracy_base(X, y)
        acc_deferral = self.accuracy_deferral(X, y)
        return acc, hard, acc_base, acc_deferral
    

def run(X, y, grader, base, deferral, resampling, percentage):
    """Run function that runs an experiment based on provided data.

    :param X: Dataset
    :type X: list
    :param y: labels
    :type y: list
    :param base: The base classifier
    :type base: class
    :param deferral: The deferral classifier
    :type deferral: class
    :param grader: The grader
    :type grader: class
    :param resampling: Resampling method
    :type resampling: class
    :param percentage: percentage of dataset used as validation set
    :type percentage: float
    :return: Trained model, trained grader, trained base classifier, trained deferral classifier, statistics, training_set, validation_set
    :rtype: class, class, class, class, tuple(float, int, float, float), tuple(list, list), tuple(list, list)
    """

    # Training and validation set
    training_size = round(percentage * len(X))
    indexes = np.arange(len(X))
    np.random.shuffle(indexes)

    # Shuffle
    X = X[indexes]
    y = y[indexes]

    X_val = X[:training_size]
    y_val = y[:training_size]

    X = X[training_size:]
    y = y[training_size:]

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
    if len(np.unique(y_grader)) > 1 and resampling != None: # Prevents cases where the base classifier is too good or there is no resampling method selected
        X_grader, y_grader = resampling.fit_resample(X_grader, y_grader)

    # Train
    grader = grader.fit(X_grader, y_grader)

    # Fuse models
    model = Fuse(base, deferral, grader)

    # Get some stats
    stats = model.stats(X_val, y_val) + model.stats(X, y)

    return model, grader, base, deferral, stats, (X, y), (X_val, y_val)


# Different elements (returns indexes where elements of two arrays are different)
def different(arr1, arr2):
    return np.where(arr1 != arr2)[0]

# Return the accuracy of a model over a dataset
def calc_accuracy(preds, y):
    return np.sum(preds == y) / len(preds)
