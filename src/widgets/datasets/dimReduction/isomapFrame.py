import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from datasets.dimReduction.isomap import isomap


class IsomapFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):

    def __init__(self, master):
        """Constructor method
        """
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((1, 0), weight=1)

        # Number of neighbors
        self.labels.append(ctk.CTkLabel(self, text="Number of neighbors", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Number of neighbors to consider for each point. If n_neighbors is an int, then radius must be None.")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=True))
        self.entries[-1].set(10) # Default value
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Radius
        self.labels.append(ctk.CTkLabel(self, text="Radius", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=1, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Limiting distance of neighbors to return. If radius is a float, then n_neighbors must be set to None.")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=True))
        self.entries[-1].set(None) # Default value
        self.entries[-1].grid(row=1, column=1, padx=10, pady=10, sticky="we")

        # Eigen solver
        self.labels.append(ctk.CTkLabel(self, text="Eigen solver", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=2, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "'auto' : Attempt to choose the most efficient solver for the given problem.\n'arpack' : Use Arnoldi decomposition to find the eigenvalues and eigenvectors.\n'dense' : Use a direct solver (i.e. LAPACK) for the eigenvalue decomposition.")
        self.scrollValues = ["auto", "arpack", "dense"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["auto"]))
        self.entries[-1].grid(row=2, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Number of iterations
        self.labels.append(ctk.CTkLabel(self, text="Number of iterations", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=3, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Maximum number of iterations for the optimization. Should be at least 250.")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(1000) # Default value
        self.entries[-1].grid(row=3, column=1, padx=10, pady=10, sticky="we")

        # Path method
        self.labels.append(ctk.CTkLabel(self, text="Method", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=4, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Method to use in finding shortest path.\n'auto' : attempt to choose the best algorithm automatically.\n'FW' : Floyd-Warshall algorithm.\n'D' : Dijkstra’s algorithm.")
        self.scrollValues = ["auto", "FW", "D"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["auto"]))
        self.entries[-1].grid(row=4, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Neighbors algorithm
        self.labels.append(ctk.CTkLabel(self, text="Neighbors algorithm", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=5, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Algorithm to use for nearest neighbors search, passed to neighbors.NearestNeighbors instance.")
        self.scrollValues = ["auto", "brute", "kd_tree", "ball_tree"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["auto"]))
        self.entries[-1].grid(row=5, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)


    def get(self):
        return isomap(*EmbeddedScrollFrame.get(self))