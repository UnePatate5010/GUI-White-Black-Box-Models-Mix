"""
File providing a function that returns an instance of an object that represents a decision tree classifier
"""
from sklearn.tree import DecisionTreeClassifier


def decisionTree(criterion, maximumDepth, splitter, min_samples_split, min_samples_leaf, max_features):
    return DecisionTreeClassifier(criterion=criterion, max_depth=maximumDepth, splitter=splitter,
                                  min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                                  max_features=max_features)
