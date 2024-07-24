"""
This file provide a frame to input hyperparameters of the SMOTE algorithm
"""
import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from resamplingMethods.smote import smote

class SMOTEFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):
    """
    Frame containing all entry fields for the SMOTE resampling method.

    :param master: the master frame/window of this frame
    :type master: class
    """

    def __init__(self, master):
        """Constructor method
        """
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((0, 1), weight=1)

        # k neighbors entry: spinbox menu
        self.labels.append(ctk.CTkLabel(self, text="K-neighbors", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "The number of nearest neighbors used to define the neighborhood of samples to use to generate the synthetic samples")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(5) # Default value
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")

    def get(self):
        return smote(*EmbeddedScrollFrame.get(self))