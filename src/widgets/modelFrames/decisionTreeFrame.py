"""
This frame is displayed when a Decision Tree classifier is selected, providing fields to input/select
hyperparameters.
"""

import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from widgets.modelFrames.model import Model

class DecisionTreeFrame(ctk.CTkScrollableFrame, Model):
    """
    Frame containing all entry fields for Decision Tree Clasifier.

    :param master: the master frame/window of this frame
    :type master: class
    """

    def __init__(self, master):
        ctk.CTkScrollableFrame.__init__(self, master)
        Model.__init__(self)

        self.grid_columnconfigure((1), weight=1)
        # self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)


        # Criterion entry: Scrollable menu
        self.labels.append(ctk.CTkLabel(self, text="Criterion"))
        self.labels[-1].grid(row=0, column=0, padx=20, pady=20, sticky="w")
        CTkToolTip(self.labels[-1], "Function used to measure the quality of a split.")
        self.scrollValues = ["gini", "entropy", "log_loss"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["gini"]))
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Maximum depth of trees
        self.labels.append(ctk.CTkLabel(self, text="Maximum depth"))
        CTkToolTip(self.labels[-1], "The maximum depth of the tree. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.")
        self.labels[-1].grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(Spinbox(self, minimum_value=1))
        self.entries[-1].set(None) # Default value
        self.entries[-1].grid(row=1, column=1, padx=20, pady=20, sticky="we")

        # Splitter entry: Scrollable menu
        self.labels.append(ctk.CTkLabel(self, text="Splitter"))
        self.labels[-1].grid(row=2, column=0, padx=20, pady=20, sticky="w")
        CTkToolTip(self.labels[-1], "Strategy used to choose the split at each node. \"best\" for the best split and \"random\" for the best random split.")
        self.scrollValues = ["best", "random"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["best"]))
        self.entries[-1].grid(row=2, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Minimum number of elements for splits
        self.labels.append(ctk.CTkLabel(self, text="Minimum split samples"))
        self.labels[-1].grid(row=3, column=0, padx=20, pady=20, sticky="w")
        CTkToolTip(self.labels[-1], "The minimum number of samples required to split an internal node.")
        self.entries.append(Spinbox(self, minimum_value=2, none_enable=False))
        self.entries[-1].set(2) # Default value
        self.entries[-1].grid(row=3, column=1, padx=20, pady=20, sticky="we")

        # Minimum number of elements at leafs
        self.labels.append(ctk.CTkLabel(self, text="Minimum leaf samples"))
        self.labels[-1].grid(row=4, column=0, padx=20, pady=20, sticky="w")
        CTkToolTip(self.labels[-1], "The minimum number of samples required to be at a leaf node.")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(1) # Default value
        self.entries[-1].grid(row=4, column=1, padx=20, pady=20, sticky="we")

        # Maximum number of features considered when splitting
        self.labels.append(ctk.CTkLabel(self, text="Maximum number\n of features"))
        self.labels[-1].grid(row=5, column=0, padx=20, pady=20, sticky="w")
        CTkToolTip(self.labels[-1], "The number of features to consider when looking for the best split. If None, then max_features=n_features.")
        self.entries.append(Spinbox(self, minimum_value=1))
        self.entries[-1].set(None) # Default value
        self.entries[-1].grid(row=5, column=1, padx=20, pady=20, sticky="we")