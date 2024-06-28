import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Graph", fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, padx=10, pady=10, sticky="ewn")


    def draw(self, X, y, model, grader):
        global canvas
        if canvas:
            canvas.get_tk_widget().destroy()
        fig = Figure(figsize = (5, 5), dpi = 100) 
        plot = fig.add_subplot(111)

        xx, yy = np.meshgrid(np.arange(X[:, 0].min() -0.01, X[:, 0].max() + 0.01, 0.01),
                     np.arange(X[:, 1].min() - 0.01, X[:, 1].max() + 0.01, 0.01))
        
        # Plot decision boundary for the first set of labels using `model`
        Z1 = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z1 = Z1.reshape(xx.shape)
        plot.contour(xx, yy, Z1, levels=[0.5], linewidths=2, colors='purple')
        plot.legend("Decision boundary")

        # Plot regions for the second set of labels using `grader`
        Z2 = grader.predict(np.c_[xx.ravel(), yy.ravel()])
        Z2 = Z2.reshape(xx.shape)
        plot.contourf(xx, yy, Z2, alpha=0.3, cmap="winter")
        
        plot.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', marker='o', cmap="bwr")

        canvas = FigureCanvasTkAgg(fig, master = self)
        canvas.draw()
        canvas.get_tk_widget().grid(sticky="ewsn")


canvas = None