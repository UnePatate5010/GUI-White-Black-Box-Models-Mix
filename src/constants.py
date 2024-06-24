from enum import Enum
from widgets.modelFrames.decisionTreeFrame import DecisionTreeFrame
from widgets.modelFrames.randomForestFrame import RandomForestFrame

MODEL_FRAMES = {"Decision tree": DecisionTreeFrame, "Random forest": RandomForestFrame}

class Models(Enum):
    CLASSIFIERS = ["Decision tree", "Random forest"]
    GRADERS = ["Decision tree", "Random forest"]