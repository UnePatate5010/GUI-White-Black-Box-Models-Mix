"""
File providing a function that returns an instance of an object that represents a random forest classifier.
"""
from sklearn.ensemble import RandomForestClassifier


def randomForest(n_trees, criterion, maximumDepth, min_samples_split, min_samples_leaf, max_features, bootstrap, n_samples_boot):
    """Instantiate a Random Forest with the provided parameters
    
    :param n_trees: The number of decision trees in the forest.
    :type n_trees: int
    :param criterion: The criterion used to evaluate the auqlity of a split
    :type criterion: str
    :param maximumDepth:The maximum depth of the tree
    :type maximumDepth: int or None
    :param min_samples_split: The minimum amount of elements to consider to split.
    :type min_samples_split: int
    :param min_samples_leaf: The minimum amout of elements to consider a subset as a leaf in the tree
    :type min_samples_leaf: int
    :param max_features: The maximum number of features to consider when splitting
    :type max_features: int or None
    :param bootstrap: Whether bootstrap samples are used when building trees. If False, the whole dataset is used to build each tree
    :type bootstrap: boolean
    :param n_samples_boot: If bootstrap is True, the number of samples to draw from X to train each base estimator.
    :type n_samples_boot: int or float
    :return: A RandomForestClassifier classifier with the right parameters
    :rtype: class <RandomForestClassifier>
    """
    return RandomForestClassifier(n_estimators=n_trees, criterion=criterion, max_depth=maximumDepth,
                                  min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf,
                                  max_features=max_features, bootstrap=bootstrap, max_samples=n_samples_boot)