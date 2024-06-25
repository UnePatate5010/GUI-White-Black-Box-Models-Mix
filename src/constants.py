from enum import Enum
from widgets.modelFrames.decisionTreeFrame import DecisionTreeFrame
from widgets.modelFrames.randomForestFrame import RandomForestFrame

from widgets.resamplingFrames.smoteFrame import SMOTEFrame

# Dictionnary associating models names to corresponding frame class (customtkinter)
MODEL_FRAMES = {"Decision tree": DecisionTreeFrame, "Random forest": RandomForestFrame}

# Dictionnary associating resampling method names to corresponding frame class (customtkinter)
RESAMPLING_FRAMES = {"SMOTE": SMOTEFrame}

# Concatenation of MODEL_FRAMES and RESAMPLING_FRAMES
BOTH = dict(MODEL_FRAMES, **RESAMPLING_FRAMES)

class Models(Enum):
    CLASSIFIERS = ["Decision tree", "Random forest"] # List of available classifier
    GRADERS = ["Decision tree", "Random forest"] # List of available grader
    RESAMPLING = ["SMOTE"]