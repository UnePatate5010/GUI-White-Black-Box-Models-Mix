"""
File providing a function that returns an instance of an object that represents a decision tree classifier.
"""
from sklearn.tree import DecisionTreeClassifier


def decisionTree(criterion, maximumDepth, splitter, min_samples_split, min_samples_leaf, max_features):
    """Instantiate a Decision Tree with the provided parameters
    
    :param criterion: The criterion used to evaluate the auqlity of a split
    :type criterion: str
    :param maximumDepth: The maximum depth of the tree
    :type maximumDepth: int or None
    :param splitter: The strategy used to find the best split
    :type splitter: str
    :param min_samples_split: The minimum amount of elements to consider to split.
    :type min_samples_split: int
    :param min_samples_leaf: The minimum amout of elements to consider a subset as a leaf in the tree
    :type min_samples_leaf: int
    :param max_features: The maximum number of features to consider when splitting
    :type max_features: int or None
    :return: A DecisionTreeClassifier classifier with the right parameters
    :rtype: class <DecisionTreeClassifiers>
    """
    return DecisionTreeClassifier(criterion=criterion, max_depth=maximumDepth, splitter=splitter,
                                  min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                                  max_features=max_features)
