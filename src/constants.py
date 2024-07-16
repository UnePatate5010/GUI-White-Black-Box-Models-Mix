"""
This file contains diverse arrays and dictionnaries used to display scrollable menus and instantiate some frame frome strings.
"""
from enum import Enum
from widgets.modelFrames.decisionTreeFrame import DecisionTreeFrame
from widgets.modelFrames.randomForestFrame import RandomForestFrame
from widgets.modelFrames.svmFrame import SvmFrame

from widgets.resamplingFrames.smoteFrame import SMOTEFrame
from widgets.resamplingFrames.adasynFrame import ADASYNFrame

# Dictionnary associating models names to corresponding frame class (customtkinter)
MODEL_FRAMES = {"Decision tree": DecisionTreeFrame, "Random forest": RandomForestFrame, "Support Vector Machine": SvmFrame}

# Dictionnary associating resampling method names to corresponding frame class (customtkinter)
RESAMPLING_FRAMES = {"SMOTE": SMOTEFrame, "ADASYN": ADASYNFrame, "None": ()}


# Concatenation of MODEL_FRAMES and RESAMPLING_FRAMES
ALL = dict(MODEL_FRAMES, **RESAMPLING_FRAMES)
