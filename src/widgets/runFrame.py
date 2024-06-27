import customtkinter as ctk
from widgets.widgetExceptions import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from translation import translateAndInstantiate
from experiment.run import run


class RunFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.run_button = ctk.CTkButton(self, text="RUN", command=self.button_callback, fg_color="#6aa51f")
        self.run_button.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    
    def button_callback(self):
        # Freeze all fields
        # self.master.freeze()

        # Get methods and hyperparameters
        try:
            input = self.master.get()
            # print(input)
        except UnselectedItemError as e:
            print(f"Missing an element. Please select a {e.missing}")
            self.master.unfreeze()
            return

        # Format them correctly (convert dicts to reflect real arguments names)
        (X, y), grader, base, deferral, resampling = translateAndInstantiate(input)

        # Call the main function
        model, grader = run(X, y, grader, base, deferral, resampling)

        # Update output frames with results
        self.master.graph.draw(X, y, model, grader)

        # Unfreeze all fields
        # self.master.unfreeze()


    def freeze(self):
        self.run_button.configure(state="disabled")

    def unfreeze(self):
        self.run_button.configure(state="normal")
