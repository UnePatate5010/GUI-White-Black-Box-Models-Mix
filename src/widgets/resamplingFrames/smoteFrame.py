"""
This file provide a frame to input hyperparameters of the SMOTE algorithm
"""
import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.modelFrames.model import Model
from widgets.CTkSpinbox.CtkSpinbox import Spinbox

class SMOTEFrame(ctk.CTkScrollableFrame, Model):

    def __init__(self, master):
        ctk.CTkScrollableFrame.__init__(self, master)
        Model.__init__(self)

        self.grid_columnconfigure((1), weight=1)

        # k neighbors entry: spinbox menu
        self.labels.append(ctk.CTkLabel(self, text="K-neighbors"))
        self.labels[-1].grid(row=0, column=0, padx=20, pady=20, sticky="w")
        CTkToolTip(self.labels[-1], "The number of nearest neighbors used to define the neighborhood of samples to use to generate the synthetic samples")
        self.entries.append(Spinbox(self, minimum_value=1))
        self.entries[-1].set(5) # Default value
        self.entries[-1].grid(row=0, column=1, padx=20, pady=20, sticky="we")