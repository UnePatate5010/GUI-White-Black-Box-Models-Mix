import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from models.fuzzy import fuzzyClassifier

class FuzzyFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):
    """
    Frame containing all entry fields for Decision Tree Clasifier.

    :param master: the master frame/window of this frame
    :type master: class
    """

    def __init__(self, master):
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((0, 1), weight=1)

        # nrules
        self.labels.append(ctk.CTkLabel(self, text="nrules", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(1) # Default value
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # tolerance
        self.labels.append(ctk.CTkLabel(self, text="tolerance", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entries.append(Spinbox(self, minimum_value=0, none_enable=False))
        self.entries[-1].set(0) # Default value
        self.entries[-1].grid(row=1, column=1, padx=10, pady=10, sticky="we")

        # n_gen
        self.labels.append(ctk.CTkLabel(self, text="n_gen", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(30) # Default value
        self.entries[-1].grid(row=2, column=1, padx=10, pady=10, sticky="we")

        # pop_size
        self.labels.append(ctk.CTkLabel(self, text="pop_size", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(20) # Default value
        self.entries[-1].grid(row=3, column=1, padx=10, pady=10, sticky="we")

    def get(self):
        return fuzzyClassifier(*EmbeddedScrollFrame.get(self))