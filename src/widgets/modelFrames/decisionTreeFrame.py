"""
This frame is displayed when a Decision Tree classifier is selected, providing fields to input/select
hyperparameters.
"""

import tkinter as tk
import customtkinter as ctk
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from widgets.modelFrames.model import Model

class DecisionTreeFrame(ctk.CTkFrame, Model):
    """
    Frame containing all entry fields for Decision Tree Clasifier.

    :param master: the master frame/window of this frame
    """

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        Model.__init__(self)

        self.grid_columnconfigure((1), weight=1)


        # Criterion entry: Scrollable menu
        self.labels.append(ctk.CTkLabel(self, text="Criterion"))
        self.labels[-1].grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.scrollValues = ["gini", "entropy", "log_loss"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["gini"]))
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Maximum depth of trees
        self.labels.append(ctk.CTkLabel(self, text="Maximum depth"))
        self.labels[-1].grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(Spinbox(self))
        self.entries[-1].set(None) # Default value
        self.entries[-1].grid(row=2, column=1, padx=20, pady=20, sticky="we")

        # Splitter entry: Scrollable menu
        self.labels.append(ctk.CTkLabel(self, text="Splitter"))
        self.labels[-1].grid(row=3, column=0, padx=20, pady=20, sticky="w")

        self.scrollValues = ["best", "random"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["best"]))
        self.entries[-1].grid(row=3, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)