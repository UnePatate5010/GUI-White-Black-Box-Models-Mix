import customtkinter as ctk
from CTkToolTip import CTkToolTip
from widgets.embeddedScrollFrame import EmbeddedScrollFrame
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from datasets.dimReduction.tsne import tsne


class TSNEFrame(ctk.CTkScrollableFrame, EmbeddedScrollFrame):

    def __init__(self, master):
        """Constructor method
        """
        ctk.CTkScrollableFrame.__init__(self, master)
        EmbeddedScrollFrame.__init__(self)

        self.grid_columnconfigure((1, 0), weight=1)

        # Perplexity
        self.labels.append(ctk.CTkLabel(self, text="Perplexity", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=0, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "The perplexity is related to the number of nearest neighbors that is used in other manifold learning algorithms. Larger datasets usually require a larger perplexity. Consider selecting a value between 5 and 50.")
        self.entries.append(Spinbox(self, minimum_value=5, none_enable=False))
        self.entries[-1].set(30) # Default value
        self.entries[-1].grid(row=0, column=1, padx=10, pady=10, sticky="we")

        # Number of iterations
        self.labels.append(ctk.CTkLabel(self, text="Number of iterations", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=1, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Maximum number of iterations for the optimization. Should be at least 250.")
        self.entries.append(Spinbox(self, minimum_value=1, none_enable=False))
        self.entries[-1].set(1000) # Default value
        self.entries[-1].grid(row=1, column=1, padx=10, pady=10, sticky="we")

        # Maximun number of iterations without progress
        self.labels.append(ctk.CTkLabel(self, text="Maximum number of iterations without progress", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=2, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Maximum number of iterations without progress before we abort the optimization, used after 250 initial iterations with early exaggeration.")
        self.entries.append(Spinbox(self, minimum_value=50, none_enable=False))
        self.entries[-1].set(300) # Default value
        self.entries[-1].grid(row=2, column=1, padx=10, pady=10, sticky="we")

        # Initialization of embedding
        self.labels.append(ctk.CTkLabel(self, text="Initialization of embedding", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=3, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "Initialization of embedding. PCA initialization cannot be used with precomputed distances and is usually more globally stable than random initialization.")
        self.scrollValues = ["random", "pca"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["pca"]))
        self.entries[-1].grid(row=3, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)

        # Method
        self.labels.append(ctk.CTkLabel(self, text="Method", wraplength=master.winfo_width()//2 - 20, justify="left", padx=10))
        self.labels[-1].grid(row=4, column=0, padx=10, pady=10, sticky="w")
        CTkToolTip(self.labels[-1], "By default the gradient calculation algorithm uses Barnes-Hut approximation running in O(NlogN) time. method='exact' will run on the slower, but exact, algorithm in O(N^2) time.")
        self.scrollValues = ["barnes_hut", "exact"]
        self.entries.append(ctk.CTkOptionMenu(self, values=["barnes_hut"]))
        self.entries[-1].grid(row=4, column=1, padx=10, pady=10, sticky="we")
        CTkScrollableDropdown(self.entries[-1], values=self.scrollValues)


    def get(self):
        return tsne(*EmbeddedScrollFrame.get(self))