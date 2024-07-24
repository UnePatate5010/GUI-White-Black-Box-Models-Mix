"""
This file contains diverse arrays and dictionnaries used to display scrollable menus and instantiate some frame frome strings.
"""
from enum import Enum
from widgets.modelFrames.decisionTreeFrame import DecisionTreeFrame
from widgets.modelFrames.randomForestFrame import RandomForestFrame
from widgets.modelFrames.svmFrame import SvmFrame

from widgets.resamplingFrames.smoteFrame import SMOTEFrame
from widgets.resamplingFrames.adasynFrame import ADASYNFrame

from widgets.datasets.dimReduction.tsneFrame import TSNEFrame
from widgets.datasets.dimReduction.isomapFrame import IsomapFrame
from widgets.datasets.dimReduction.pcaFrame import PCAFrame
from widgets.datasets.dimReduction.umapFrame import UMAPFrame

# Dictionnary associating models names to corresponding frame class (customtkinter)
MODEL_FRAMES = {"Decision tree": DecisionTreeFrame, "Random forest": RandomForestFrame, "Support Vector Machine": SvmFrame}

# Dictionnary associating resampling method names to corresponding frame class (customtkinter)
RESAMPLING_FRAMES = {"SMOTE": SMOTEFrame, "ADASYN": ADASYNFrame, "None": ()}

# Dictionnary associating dimensionality reduction method names to corresponding frame class (customtkinter)
DIM_REDUCTION = {"TSNE": TSNEFrame, "Isomap": IsomapFrame, "PCA": PCAFrame, "UMAP": UMAPFrame, "None": ()}


# Concatenation of MODEL_FRAMES and RESAMPLING_FRAMES
ALL = dict(dict(MODEL_FRAMES, **RESAMPLING_FRAMES), **DIM_REDUCTION)
