"""
This frame is displayed when a Random forest classifier is selected, providing fields to input/select
hyperparameters.
"""

import customtkinter as ctk
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox

class RandomForestFrame(ctk.CTkFrame):
    """
    Frame containing all entry fields for Random Forest Clasifier.

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
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues, hover_color="red")

        # Number of trees: 
        self.labels.append(ctk.CTkLabel(self, text="Number of trees"))
        self.labels[-1].grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(Spinbox(self))
        self.entries[-1].set(100) # Default value
        self.entries[-1].grid(row=1, column=1, padx=20, pady=20, sticky="we")


        # Maximum depth of trees
        self.labels.append(ctk.CTkLabel(self, text="Maximum depth"))
        self.labels[-1].grid(row=2, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(Spinbox(self))
        self.entries[-1].set(None) # Default value
        self.entries[-1].grid(row=2, column=1, padx=20, pady=20, sticky="we")
    
    def get(self):
        dic = {}
        for i in range(len(self.entries)):
            try:
                dic[self.labels[i].cget("text")] = self.entries[i].get()
            except Exception as e:
                print(f"Error getting value for {self.labels[i].cget('text')}: {e}")
        return dic