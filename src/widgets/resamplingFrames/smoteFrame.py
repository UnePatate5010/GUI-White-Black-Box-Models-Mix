import customtkinter as ctk
from widgets.modelFrames.model import Model
from widgets.CTkSpinbox.CtkSpinbox import Spinbox

class SMOTEFrame(ctk.CTkFrame, Model):

    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        Model.__init__(self)

        self.grid_columnconfigure((1), weight=1)

        # k neighbors entry: spinbox menu
        self.labels.append(ctk.CTkLabel(self, text="Criterion"))
        self.labels[-1].grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(Spinbox(self))
        self.entries[-1].set(5) # Default value
        self.entries[-1].grid(row=0, column=1, padx=20, pady=20, sticky="we")