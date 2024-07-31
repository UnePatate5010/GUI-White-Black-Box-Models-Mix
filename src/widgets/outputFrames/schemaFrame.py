"""This file contains a Frame used to plot schema of white box models (base classifier)
"""
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.tree import plot_tree, DecisionTreeClassifier


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
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="White box model schema", fg_color="#727272", corner_radius=10)
        self.name.grid(row=0, column=0, padx=10, pady=10, sticky="ewn")

        self.canvas = None

    def draw(self, base):
        """This method plots a schema of the base classifier (if supported). It is called by the RunFrame (run button).

        :param base: The trained base classifier
        :type base: class
        """
        # Destroy the canvas if already existing
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        fig1, ax1 = plt.subplots(figsize=(5, 5), dpi=100)

        # Plot a schema if the base classifier is a supported model
        if isinstance(base, DecisionTreeClassifier):
            plot_tree(base, ax=ax1, rounded=True, impurity=False, label="root", filled=True)
        
        # Display the plot in the canvas
        self.canvas = FigureCanvasTkAgg(fig1, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10, sticky="ewsn")

