"""
This frame is displayed when Support Vector Machine is selected, providing fields to input/select
hyperparameters.
"""

import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from models.svm import svm

class SvmFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):
    """
    Frame containing all entry fields for SVM.

    :param master: the master frame/window of this frame
    :type master: class
    """

    def __init__(self, master):
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((0, 1), weight=1)

        # Regularization parameter
        self.labels.append(ctk.CTkLabel(self, text="Regularization parameter", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Regularization parameter.")
        self.entries.append(Spinbox(self, minimum_value=0, none_enable=False))
        self.entries[-1].set(1) # Default value
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Kernel
        self.labels.append(ctk.CTkLabel(self, text="Kernel", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=1, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Specifies the kernel type to be used in the algorithm.")
        self.scrollValues = ["linear", "poly", "rbf", "sigmoid"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["rbf"]))
        self.entries[-1].grid(row=1, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Degree
        self.labels.append(ctk.CTkLabel(self, text="Degree", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=2, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Degree of the polynomial kernel function (\"poly\"). Must be non-negative. Ignored by all other kernels.")
        self.entries.append(Spinbox(self, minimum_value=0, none_enable=False))
        self.entries[-1].set(3) # Default value
        self.entries[-1].grid(row=2, column=1, padx=10, pady=10, sticky="we")

        # Kernel coefficient
        self.labels.append(ctk.CTkLabel(self, text="Kernel coefficient", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=3, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Kernel coefficient for \"rbf\", \"poly\" and \"sigmoid\".")
        self.scrollValues = ["scale", "auto"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["scale"]))
        self.entries[-1].grid(row=3, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Maximum iteration
        self.labels.append(ctk.CTkLabel(self, text="Maximum iteration", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=4, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Hard limit on iterations within solver, or -1 for no limit.")
        self.entries.append(Spinbox(self, minimum_value=-1, none_enable=False))
        self.entries[-1].set(-1) # Default value
        self.entries[-1].grid(row=4, column=1, padx=10, pady=10, sticky="we")

    def get(self):
        return svm(*EmbeddedScrollFrame.get(self))