"""
This frame is displayed when a Decision Tree classifier is selected, providing fields to input/select
hyperparameters.
"""

import customtkinter as ctk
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox

class DecisionTreeFrame(ctk.CTkFrame):
    """
    Frame containing all entry fields for Decision Tree Clasifier.

    :param master: the master frame/window of this frame
    """

    def __init__(self, master):
        super().__init__(master)

        self.labels = [] # List of labels (for entries)
        self.entries = [] # List of entry fields

        # Criterion entry: Scrollable menu
        self.labels.append(ctk.CTkLabel(self, text="Criterion"))
        self.labels[-1].grid(row=0, column=0, padx=20, pady=20, sticky="w")

        self.scrollValues = ["gini", "entropy", "log_loss"]
        self.entries.append(ctk.CTkOptionMenu(self, width=200, values=["gini"]))
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
        self.entries.append(ctk.CTkOptionMenu(self, width=200, values=["best"]))
        self.entries[-1].grid(row=3, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)



    def get(self):
        dic = {}
        for i in range(len(self.entries)):
            dic.update({self.labels[i].cget("text"): self.entries[i].get()})
        return dic

