import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from datasets.dimReduction.umap import umap


class UMAPFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):

    def __init__(self, master):
        """Constructor method
        """
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((1, 0), weight=1)

        # Number of neighbors
        self.labels.append(ctk.CTkLabel(self, text="Number of neighbors", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "he size of local neighborhood (in terms of number of neighboring sample points) used for manifold approximation.")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=True))
        self.entries[-1].set(15) # Default value
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Minimum distance
        self.labels.append(ctk.CTkLabel(self, text="Minimum distance", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=1, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "The effective minimum distance between embedded points. Smaller values will result in a more clustered/clumped embedding where nearby points on the manifold are drawn closer together, while larger values will result on a more even dispersal of points.")
        self.entries.append(Spinbox(self, minimum_value=0, type=float, none_enable=False))
        self.entries[-1].set(1) # Default value
        self.entries[-1].grid(row=1, column=1, padx=10, pady=10, sticky="we")

        # Metric
        self.labels.append(ctk.CTkLabel(self, text="Metric", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=2, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "The metric to use to compute distances in high dimensional space.")
        self.scrollValues = ["euclidean", "manhattan", "chebyshev", "canberra"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["euclidean"]))
        self.entries[-1].grid(row=2, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)



    def get(self):
        return umap(*EmbeddedScrollFrame.get(self))