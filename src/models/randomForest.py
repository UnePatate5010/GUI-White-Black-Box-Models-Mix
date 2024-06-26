"""
File providing a function that returns an instance of an object that represents a random forest classifier
"""
from sklearn.ensemble import RandomForestClassifier


def randomForest(n_trees, criterion, maximumDepth, min_samples_split, min_samples_leaf, max_features, bootstrap, n_samples_boot):
    return RandomForestClassifier(n_estimators=n_trees, criterion=criterion, max_depth=maximumDepth,
                                  min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                                  max_features=max_features, bootstrap=bootstrap, max_samples=n_samples_boot)