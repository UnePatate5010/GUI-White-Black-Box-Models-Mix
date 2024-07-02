import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.lines import Line2D
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

        self.canvas = None


    def draw(self, X, y, model, grader):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        fig = Figure(figsize = (10, 5), dpi = 100, facecolor="grey") 
        plot = fig.add_subplot(111)

        xx, yy = np.meshgrid(np.arange(X[:, 0].min() -0.05, X[:, 0].max() + 0.05, 0.01),
                     np.arange(X[:, 1].min() - 0.05, X[:, 1].max() + 0.05, 0.01))
        
        # Plot decision boundary for the first set of labels using `model`
        Z1 = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z1 = Z1.reshape(xx.shape)
        curve = plot.contour(xx, yy, Z1, levels=[0.5], linewidths=2, colors='black')
        
        # Plot regions for the second set of labels using `grader`
        Z2 = grader.predict(np.c_[xx.ravel(), yy.ravel()])
        Z2 = Z2.reshape(xx.shape)
        area = plot.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu)
        # fig.colorbar(area)
        
        # Plot points of each class
        y_u = np.unique(y)
        for i in y_u:
            plot.scatter(X[:, 0][y == i], X[:, 1][y == i], edgecolor='k', marker='o', label=str(i))

        # Legend (little trick to legend the decision boundary and hard/easy area)
        contour_legend = Line2D([0], [0], color='black', lw=2, label='Decision Boundary')
        handles, labels = plot.get_legend_handles_labels()
        handles.append(contour_legend)
        labels.append('Decision Boundary')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot.legend(handles=handles, labels=labels)


        self.canvas = FigureCanvasTkAgg(fig, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(sticky="ewsn")