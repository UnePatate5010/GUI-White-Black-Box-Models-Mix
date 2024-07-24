import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from datasets.dimReduction.pca import pca


class PCAFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):

    def __init__(self, master):
        """Constructor method
        """
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((1, 0), weight=1)

        # Whiten
        self.labels.append(ctk.CTkLabel(self, text="Whiten", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "When True (False by default) the components_ vectors are multiplied by the square root of n_samples and then divided by the singular values to ensure uncorrelated outputs with unit component-wise variances.")
        self.scrollValues = ["True", "False"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["False"]))
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # SVD solver
        self.labels.append(ctk.CTkLabel(self, text="SVD solver", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=1, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "'auto': Chose one of the solver depending on the amount of features.\n 'full': Run exact full SVD calling the standard LAPACK solver via scipy.linalg.svd and select the components by postprocessing.\n'arpack': Run SVD truncated to n_components calling ARPACK solver via scipy.sparse.linalg.svds. It requires strictly 0 < n_components < min(X.shape).\n 'randomized': Run randomized SVD by the method of Halko et al.")
        self.scrollValues = ["auto", "full", "arpack", "randomiwed"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["pca"]))
        self.entries[-1].grid(row=1, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)



    def get(self):
        return pca(*EmbeddedScrollFrame.get(self))