"""
This file allows to translate human readable arguments to function arguments names.
"""
from datasets.loadDataset import loadDataset
from models.decisionTree import decisionTree
from models.randomForest import randomForest
from models.svm import svm
from resamplingMethods.smote import smote

# Link a method name (human readable) to a tuple of a dicitonnary that translate human readable arguments
# to real arguments names and the corresponding function that instanciate such model
mappings = {
    # ========== Datasets ========== #
    "Corner": "./datasets/corner.csv",
    "Moons": "./datasets/moons.csv",

    # ========== Models ========== #
    "Decision tree": ({
        "Criterion": "criterion",
        "Maximum depth": "maximumDepth",
        "Splitter": "splitter",
        "Minimum split samples": "min_samples_split",
        "Minimum leaf samples": "min_samples_leaf",
        "Maximum number\n of features": "max_features"
    }, decisionTree),

    "Random forest": ({
        "Number of trees": "n_trees",
        "Criterion": "criterion",
        "Maximum depth": "maximumDepth",
        "Minimum split samples": "min_samples_split",
        "Minimum leaf samples": "min_samples_leaf",
        "Maximum number\n of features": "max_features",
        "Bootstrap": "bootstrap",
        "Maximum number of\n samples per tree": "n_samples_boot"
    }, randomForest),

    "Support Vector Machine": ({
        "Regularization parameter": "C",
        "Kernel": "kernel",
        "Degree": "degree",
        "Kernel coefficient": "gamma",
        "Maximum iteration": "max_iter"
    }, svm),

    # ========== Resampling ========== #
    "SMOTE": ({
        "K-neighbors": "k_neighbors"
    }, smote)
}


def translate(mapping_key, human_readable_dict):
    """Returns a translated dictionnary and the corresponding function. This function is used to
    retrieve the right parameters names and function for each models/resampling method.

    :param mapping_key: Name of the method or the resampling method
    :type mapping_key: str
    :param human_readable_dict: A human readable dictionnary to translate
    :type human_readable_dict: dict
    :return: The translated dictionnary, the corresponding function
    :rtype: dict, function
    """
    mapping, func = mappings[mapping_key]
    converted_dict = {mapping[k]: v for k, v in human_readable_dict.items()}
    return converted_dict, func


def translateAndInstantiate(input):
    """Translates the user data and returns the corresponding dataset, models and resampling method.

    :param input: A dictionnary of all input data
    :type input: dict
    :return: A tuple of the dataset and the labels, the grader, the base classifier, the deferral classifier, the resampling method
    :rtype: tuple(list, list), class, class, class, class
    """
    X, y = loadDataset(mappings[input["dataset"]])
    
    grader = aux(input, "grader")

    base = aux(input, "base")

    deferral = aux(input, "deferral")

    resampling = aux(input, "resampling")

    return (X, y), grader, base, deferral, resampling


def aux(input, key):
    """Auxiliary function used in 'translateAndInstantiate'. Returns an instantiated model.

    :param input: The dictionnary containing all data selected by the user
    :type input: dict
    :param key: Name of the model to instantiate
    :type key: str
    :return: the instantiated model
    :rtype: class
    """
    model = input[key]
    modelDict, modelFunc = translate(*model)
    model = modelFunc(**modelDict)
    return model