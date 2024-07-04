"""The GraphFrame class provided by this file is charged to display the graph that shows the dataset, decisoin boudaries...
"""
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.lines import Line2D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphFrame(ctk.CTkFrame):
    """Class providing a space and a method to plot a graph of the dataset and results.

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
        self.name = ctk.CTkLabel(self, text="Graph", fg_color="#333333", corner_radius=10)
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
            self.canvas = FigureCanvasTkAgg(self.fig[self.fig_index], master = self)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")

    def right(self):
        if self.fig != []:
            if self.fig_index != len(self.fig) - 1:
                self.fig_index += 1
            else:
                self.fig_index = 0
            self.canvas = FigureCanvasTkAgg(self.fig[self.fig_index], master = self)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")


    def draw(self, X, y, model, grader):
        """This method plots a graph to display result of the experiments. It is called by the RunFrame (run button).

        :param X: The dataset
        :type X: list
        :param y: Labels of the dataset
        :type y: list
        :param model: Trained model (the fused model from the base/deferral classifer and the grader)
        :type model: class
        :param grader: Trained grader
        :type grader: class
        """
        self.fig = [] # Attribute to stroe different figures
        self.fig_index = 0

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.fig.append(Figure(figsize = (10, 5), dpi = 100, facecolor="grey"))
        plot = self.fig[-1].add_subplot(111)

        xx, yy = np.meshgrid(np.arange(X[:, 0].min() -0.05, X[:, 0].max() + 0.05, 0.01),
                     np.arange(X[:, 1].min() - 0.05, X[:, 1].max() + 0.05, 0.01))
        
        # Plot regions for the second set of labels using `grader`
        Z2 = grader.predict(np.c_[xx.ravel(), yy.ravel()])
        Z2 = Z2.reshape(xx.shape)
        area = plot.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu_r)

        # Plot points of each class
        y_u = np.unique(y)
        for i in y_u:
            plot.scatter(X[:, 0][y == i], X[:, 1][y == i], edgecolor='k', marker='o', label=str(i))

        # Plot decision boundary for the first set of labels using `model`
        Z1 = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z1 = Z1.reshape(xx.shape)
        curve = plot.contour(xx, yy, Z1, levels=[0.5], linewidths=2, colors='black')

        # Legend (little trick to legend the decision boundary and hard/easy area)
        contour_legend = Line2D([0], [0], color='black', lw=2, label='Decision Boundary')
        handles, labels = plot.get_legend_handles_labels()
        handles.append(contour_legend)
        labels.append('Decision Boundary')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu_r(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot.legend(handles=handles, labels=labels)



        # Second plot with decision boundaries of base and deferral classifiers
        self.fig.append(Figure(figsize = (10, 5), dpi = 100, facecolor="grey"))
        plot2 = self.fig[-1].add_subplot(111)

        area = plot2.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu_r)

        # Plot points of each class
        for i in y_u:
            plot2.scatter(X[:, 0][y == i], X[:, 1][y == i], edgecolor='k', marker='o', label=str(i))

        # Plot decision boundary for the first set of labels using `base`
        Z2 = model.predict_base(np.c_[xx.ravel(), yy.ravel()])
        Z2 = Z2.reshape(xx.shape)
        curve1 = plot2.contour(xx, yy, Z2, levels=[0.5], linewidths=4, colors='forestgreen')

        # Plot decision boundary for the first set of labels using `deferral`
        Z3 = model.predict_deferral(np.c_[xx.ravel(), yy.ravel()])
        Z3 = Z3.reshape(xx.shape)
        curve2 = plot2.contour(xx, yy, Z3, levels=[0.5], linewidths=2, colors='gold')
        
        contour_legend1 = Line2D([0], [0], color='green', lw=2, label='Decision Boundary Base')
        contour_legend2 = Line2D([0], [0], color='cyan', lw=2, label='Decision Boundary Deferral')
        handles, labels = plot2.get_legend_handles_labels()
        handles.append(contour_legend1)
        handles.append(contour_legend2)
        labels.append('Decision Boundary Base')
        labels.append('Decision Boundary Deferral')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu_r(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot2.legend(handles=handles, labels=labels)


        self.canvas = FigureCanvasTkAgg(self.fig[0], master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")