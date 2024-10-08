"""
This frame correspond to the run button. It is charged to run an experiment with the selected parameter when the button is pressed. 
It also provides computed data and models to output frames and draws/plots/shows results.
"""
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from widgets.widgetExceptions import *
from experiment.run import run


class RunFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.run_button = ctk.CTkButton(self, text="RUN", command=self.button_callback, fg_color="#6aa51f", hover_color="#426713")
        self.run_button.grid(row=0, column=1, columnspan=2, padx=2, pady=2, sticky="news")

        self.run_button = ctk.CTkButton(self, text="Theme", command=self.button_theme)
        self.run_button.grid(row=0, column=0, padx=2, pady=2, sticky="news")

    def button_theme(self):
        current = ctk.get_appearance_mode()
        if current == "Dark":
            ctk.set_appearance_mode("light")
        else:
            ctk.set_appearance_mode("dark")
    
    def button_callback(self):
        # Freeze all fields
        # self.master.freeze()
       
        self.master.graph.clean()

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

        # Retrieve the different outputs
        ((X, y), percentage, rand_split, dim_red_method), grader, base, deferral, resampling = input

        # Reduce dimension if needed
        n_features = len(X[0])
        if dim_red_method != None and n_features > 2:
            X = dim_red_method.fit_transform(X)

        # Call the main function
        model, grader, base, deferral, stats, (X, y), (X_test, y_test), (X_grad, y_grad), (X_grad_n, y_grad_n) = run(X, y, grader, base, deferral, resampling, percentage, rand_split)

        # Update output frames with results
        self.master.graph.clean()
        if len(X[0]) <= 2: # Draw only if 2D
            self.master.graph.draw(X, y, X_test, y_test, model, grader, X_grad, y_grad, X_grad_n, y_grad_n)
        self.master.stats.set(accuracy_test = round(stats[0], 3), 
                              nb_hard_test = str(stats[1]) + " out of " + str(len(X_test)) + " elements (" + str(round(stats[1]/len(X_test) * 100, 3)) + "%)", 
                              accuracy_base_test = round(stats[2], 3), 
                              accuracy_deferral_test = round(stats[3], 3),
                              accuracy_train = round(stats[4], 3), 
                              nb_hard_train = str(round(stats[5], 3)) + " out of " + str(len(X)) + " elements (" + str(round(stats[5]/len(X) * 100, 3)) + "%)", 
                              accuracy_base_train = round(stats[6], 3), 
                              accuracy_deferral_train = round(stats[7], 3),
                              n_features = n_features)
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
