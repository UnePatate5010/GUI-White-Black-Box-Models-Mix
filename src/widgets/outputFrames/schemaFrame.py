import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.tree import plot_tree, DecisionTreeClassifier


class SchemaFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="White box model frame", fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, padx=10, pady=10, sticky="ewn")

        self.canvas = None

    def draw(self, base):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        fig1, ax1 = plt.subplots(figsize=(5, 5), dpi=100)

        if isinstance(base, DecisionTreeClassifier):
            plot_tree(base, ax=ax1, rounded=True, impurity=False, label="root", filled=True)
        
        self.canvas = FigureCanvasTkAgg(fig1, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="ewsn")

