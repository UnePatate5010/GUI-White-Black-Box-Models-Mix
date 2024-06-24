from enum import Enum
from widgets.modelFrames.decisionTreeFrame import DecisionTreeFrame
from widgets.modelFrames.randomForestFrame import RandomForestFrame

# Dictionnary associating models names to corresponding frame class (customtkinter)
MODEL_FRAMES = {"Decision tree": DecisionTreeFrame, "Random forest": RandomForestFrame}

class Models(Enum):
    CLASSIFIERS = ["Decision tree", "Random forest"] # List of available classifier
    GRADERS = ["Decision tree", "Random forest"] # List of available grader