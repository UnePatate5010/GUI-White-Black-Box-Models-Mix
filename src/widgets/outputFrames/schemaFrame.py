"""This file contains a Frame used to plot schema of white box models (base classifier)
"""
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.tree import plot_tree, DecisionTreeClassifier
from matplotlib.figure import Figure 
from models.fuzzy import fuzzyClassifier


class SchemaFrame(ctk.CTkFrame):
    """Class providing a space and a method to plot a the schema.

    :param master: the master frame/window of this frame
    :type master: class
    """
        
    def __init__(self, master):
        """Constructor method
        """
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="White box model schema", fg_color="#727272", corner_radius=10)
        self.name.grid(row=0, column=1, padx=10, pady=10, sticky="ewn")

        self.left_button = ctk.CTkButton(self, text="←", command=self.left)
        self.left_button.grid(row=0, column=0, padx=10, pady=10, sticky="news")

        self.left_button = ctk.CTkButton(self, text="→", command=self.right)
        self.left_button.grid(row=0, column=2, padx=10, pady=10, sticky="news")

        self.canvas = None
        self.fig = []
        self.fig_index = 0

    def left(self):
        if self.fig != []:
            if self.fig_index:
                self.fig_index -= 1
            else:
                self.fig_index = len(self.fig) - 1
            self.canvas = FigureCanvasTkAgg(self.fig[self.fig_index][0], master = self)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")

    def right(self):
        if self.fig != []:
            if self.fig_index != len(self.fig) - 1:
                self.fig_index += 1
            else:
                self.fig_index = 0
            self.canvas = FigureCanvasTkAgg(self.fig[self.fig_index][0], master = self)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")

    def draw(self, base):
        """This method plots a schema of the base classifier (if supported). It is called by the RunFrame (run button).

        :param base: The trained base classifier
        :type base: class
        """
        
        plt.close("all")
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.fig = [] # Attribute to store different figures
        self.fig_index = 0

        # Destroy the canvas if already existing
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        # Decision Tree
        if isinstance(base, DecisionTreeClassifier):
            self.fig.append(plt.subplots(figsize=(5, 5), dpi=100))
            f, ax = self.fig[-1]
            plot_tree(base, ax=ax, rounded=True, impurity=False, label="root", filled=True)

        # fuzzy classifier
        if isinstance(base, fuzzyClassifier):
            self.fig = base.plot_fuzzy()

        
        # Display the plot in the canvas
        if self.fig != []:
            self.canvas = FigureCanvasTkAgg(self.fig[0][0], master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")

