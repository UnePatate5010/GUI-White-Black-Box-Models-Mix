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


    def draw(self, X, y, X_val, y_val, model, grader):
        """This method plots a graph to display result of the experiments. It is called by the RunFrame (run button).

        :param X: The dataset
        :type X: list
        :param y: Labels of the dataset
        :type y: list
        :param X_val: Validation set
        :type X_val: list
        :param y_val: Labels of the dataset
        :type y_val: list
        :param model: Trained model (the fused model from the base/deferral classifer and the grader)
        :type model: class
        :param grader: Trained grader
        :type grader: class
        """
        plt.close("all")

        self.fig = [] # Attribute to store different figures
        self.fig_index = 0

        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.fig.append(Figure(figsize = (10, 5), dpi = 100, facecolor="white"))
        plot = self.fig[-1].add_subplot(111)

        true_min_x = min(X[:, 0].min(), X_val[:, 0].min())
        true_max_x = max(X[:, 0].max(), X_val[:, 0].max())
        true_min_y = min(X[:, 1].min(), X_val[:, 1].min())
        true_max_y = max(X[:, 1].max(), X_val[:, 1].max())
        step_x = (true_max_x - true_min_x) / 500
        step_y = (true_max_y - true_min_y) / 500

        xx, yy = np.meshgrid(np.arange(true_min_x - step_x, true_max_x + step_x, step_x),
                     np.arange(true_min_y - step_y, true_max_y + step_y, step_y))
        
        # List of unique labels
        y_u = np.unique(y)

        # Plot regions for the second set of labels using `grader`
        Z2 = grader.predict(np.c_[xx.ravel(), yy.ravel()])
        Z2 = Z2.reshape(xx.shape)
        area = plot.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu_r)

        # Plot decision boundary for the first set of labels using `model`
        Z1 = model.predict(np.c_[xx.ravel(), yy.ravel()])
        Z1 = Z1.reshape(xx.shape)
        curve = plot.contour(xx, yy, Z1, levels=len(y_u), linewidths=1, colors='black')

        # Plot points of each class
        for i in y_u:
            plot.scatter(X[:, 0][y == i], X[:, 1][y == i], edgecolor='k', marker='o', label=str(i))

        # Legend (little trick to legend the decision boundary and hard/easy area)
        contour_legend = Line2D([0], [0], color='black', lw=1, label='Decision Boundary')
        handles, labels = plot.get_legend_handles_labels()
        handles.append(contour_legend)
        labels.append('Decision Boundary')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu_r(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot.legend(handles=handles, labels=labels)
        plot.title.set_text("Graph of the dataset with the 'hard' region and the decision boundary of the model (Training set)")



        # Second plot with decision boundaries of base and deferral classifiers
        self.fig.append(Figure(figsize = (10, 5), dpi = 100, facecolor="white"))
        plot2 = self.fig[-1].add_subplot(111)

        area = plot2.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu_r)


        # Plot decision boundary for the first set of labels using `base`
        Z3 = model.predict_base(np.c_[xx.ravel(), yy.ravel()])
        Z3 = Z3.reshape(xx.shape)
        curve1 = plot2.contour(xx, yy, Z3, levels=len(y_u), linewidths=4, colors='green')

        # Plot decision boundary for the first set of labels using `deferral`
        Z4 = model.predict_deferral(np.c_[xx.ravel(), yy.ravel()])
        Z4 = Z4.reshape(xx.shape)
        curve2 = plot2.contour(xx, yy, Z4, levels=len(y_u), linewidths=2, colors='violet')
        
        # Plot points of each class
        for i in y_u:
            plot2.scatter(X[:, 0][y == i], X[:, 1][y == i], edgecolor='k', marker='o', label=str(i))
        
        contour_legend1 = Line2D([0], [0], color='green', lw=4, label='Decision Boundary Base')
        contour_legend2 = Line2D([0], [0], color='violet', lw=2, label='Decision Boundary Deferral')
        handles, labels = plot2.get_legend_handles_labels()
        handles.append(contour_legend1)
        handles.append(contour_legend2)
        labels.append('Decision Boundary Base')
        labels.append('Decision Boundary Deferral')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu_r(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot2.legend(handles=handles, labels=labels)
        plot2.title.set_text("Graph of the dataset with the decision boundaries of the base and deferral classifiers (Training set)")


        # Idem as first figure but with validation set
        self.fig.append(Figure(figsize = (10, 5), dpi = 100, facecolor="white"))
        plot3 = self.fig[-1].add_subplot(111)

        area = plot3.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu_r)
        curve = plot3.contour(xx, yy, Z1, levels=len(y_u), linewidths=1, colors='black')

        for i in y_u:
            plot3.scatter(X_val[:, 0][y_val == i], X_val[:, 1][y_val == i], edgecolor='k', marker='o', label=str(i))

        # Legend (little trick to legend the decision boundary and hard/easy area)
        contour_legend = Line2D([0], [0], color='black', lw=1, label='Decision Boundary')
        handles, labels = plot.get_legend_handles_labels()
        handles.append(contour_legend)
        labels.append('Decision Boundary')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu_r(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot3.legend(handles=handles, labels=labels)
        plot3.title.set_text("Graph of the dataset with the 'hard' region and the decision boundary of the model (Validation set)")

        # Idem as second figure but with validation set
        self.fig.append(Figure(figsize = (10, 5), dpi = 100, facecolor="white"))
        plot4 = self.fig[-1].add_subplot(111)

        area = plot4.contourf(xx, yy, Z2, alpha=0.8, cmap=plt.cm.RdYlBu_r)
        curve1 = plot4.contour(xx, yy, Z3, levels=len(y_u), linewidths=4, colors='green')
        curve2 = plot4.contour(xx, yy, Z4, levels=len(y_u), linewidths=2, colors='violet')

        for i in y_u:
            plot4.scatter(X_val[:, 0][y_val == i], X_val[:, 1][y_val == i], edgecolor='k', marker='o', label=str(i))
        
        contour_legend1 = Line2D([0], [0], color='green', lw=4, label='Decision Boundary Base')
        contour_legend2 = Line2D([0], [0], color='violet', lw=1, label='Decision Boundary Deferral')
        handles, labels = plot2.get_legend_handles_labels()
        handles.append(contour_legend1)
        handles.append(contour_legend2)
        labels.append('Decision Boundary Base')
        labels.append('Decision Boundary Deferral')
        handles.append(Line2D([0], [0], color='white', markerfacecolor=plt.cm.RdYlBu_r(0.9), markersize=10, marker='s'))
        labels.append('Hard region')
        plot4.legend(handles=handles, labels=labels)
        plot4.title.set_text("Graph of the dataset with the decision boundaries of the base and deferral classifiers (Validation set)")

        # Display first figure
        self.canvas = FigureCanvasTkAgg(self.fig[0], master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ewsn")


    def clean(self):
        if self.canvas != None:
            self.canvas.get_tk_widget().grid_forget()