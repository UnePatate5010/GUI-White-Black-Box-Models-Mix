"""
This file allows to translate human readable arguments to function arguments names
"""
from models.decisionTree import decisionTree
from models.randomForest import randomForest
from resamplingMethods.smote import smote

# Link a method name (human readable) to a tuple of a dicitonnary that translate human readable arguments
# to real arguments names and the corresponding function that instanciate such model
mappings = {
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

    # ========== Resampling ========== #
    "SMOTE": ({
        "K-neighbors": "k_neighbors"
    }, smote)
}


def translate(mapping_key, human_readable_dict):
    mapping, func = mappings[mapping_key]
    converted_dict = {mapping[k]: v for k, v in human_readable_dict.items()}
    return converted_dict, func