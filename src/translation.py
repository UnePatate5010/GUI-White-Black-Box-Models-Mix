"""
This file allows to translate human readable arguments to function arguments names
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
    mapping, func = mappings[mapping_key]
    converted_dict = {mapping[k]: v for k, v in human_readable_dict.items()}
    return converted_dict, func


def translateAndInstantiate(input):
    X, y = loadDataset(mappings[input["dataset"]])
    
    grader = aux(input, "grader")

    base = aux(input, "base")

    deferral = aux(input, "deferral")

    resampling = aux(input, "resampling")

    return (X, y), grader, base, deferral, resampling


def aux(input, key):
    model = input[key]
    modelDict, modelFunc = translate(*model)
    model = modelFunc(**modelDict)
    return model