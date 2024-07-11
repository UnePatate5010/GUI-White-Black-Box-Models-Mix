"""
This frame correspond to the run button. It is charged to run an experiment with the selected parameter when the button is pressed. 
It also provides computed data and models to output frames and draws/plots/shows results.
"""
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from widgets.widgetExceptions import *
from experiment.run import run
from datasets.loadDataset import loadDataset


class RunFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.run_button = ctk.CTkButton(self, text="RUN", command=self.button_callback, fg_color="#6aa51f", hover_color="#426713")
        self.run_button.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    
    def button_callback(self):
        # Freeze all fields
        # self.master.freeze()

        # Get methods and hyperparameters
        try:
            input = self.master.get()
            # print(input)
        except UnselectedItemError as e:
            string = ""
            for m in e.missing:
                string += "\n- " + m
            CTkMessagebox(title="Error", message="Some parameters have not been selected. Please select:" + string, icon="cancel")
            self.master.unfreeze()
            return

        # Format them correctly (convert dicts to reflect real arguments names)
        dataset, grader, base, deferral, resampling = input
        # Load dataset
        X, y = loadDataset(dataset)
        # Call the main function
        model, grader, base, deferral, stats = run(X, y, grader, base, deferral, resampling)

        # Update output frames with results
        self.master.graph.draw(X, y, model, grader)
        self.master.stats.set(accuracy = stats[0], 
                              nb_hard = str(stats[1]) + " out of " + str(len(X)) + " elements", 
                              accuracy_base = stats[2], 
                              accuracy_deferral = stats[3])
        self.master.schema.draw(base)

        # Unfreeze all fields
        # self.master.unfreeze()


    def freeze(self):
        """
        Freeze all fields (disable)
        """
        self.run_button.configure(state="disabled")

    def unfreeze(self):
        """
        Unfreeze all fields (enable)
        """
        self.run_button.configure(state="normal")
