"""In this file, the StatsFrame class represents a frame in which different statistics of the 
experiment can be displayed."""

import customtkinter as ctk

class StatsFrame(ctk.CTkScrollableFrame):
    """Class providing a space and a method to display statistics

    :param master: the master frame/window of this frame
    :type master: class
    """
        
    def __init__(self, master):
        """Constructor method
        """

        super().__init__(master)

        # self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Statistics", fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ewn")

        # ========== Stats ========== #

        self.labels = {}
        self.values = {}

        # test set
        # Accuracy
        self.labels["accuracy_test"] = ctk.CTkLabel(self, text="Accuracy of the whole model (test set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["accuracy_test"].grid(row=1, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_test"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_test"].grid(row=1, column=1, padx=10, pady=10, sticky="ewns")

        # Number of elements declared as hard
        self.labels["nb_hard_test"] = ctk.CTkLabel(self, text="Number of hard elements (test set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["nb_hard_test"].grid(row=2, column=0, padx=10, pady=10, sticky="ewns")
        self.values["nb_hard_test"] = ctk.CTkLabel(self, text="")
        self.values["nb_hard_test"].grid(row=2, column=1, padx=10, pady=10, sticky="ewns")

        # Accuracy of the base classifier alone
        self.labels["accuracy_base_test"] = ctk.CTkLabel(self, text="Accuracy of the base classifier (test set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["accuracy_base_test"].grid(row=3, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_base_test"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_base_test"].grid(row=3, column=1, padx=10, pady=10, sticky="ewns")

        # Accuracy of the deferral classifier alone
        self.labels["accuracy_deferral_test"] = ctk.CTkLabel(self, text="Accuracy of the deferral classifier (test set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["accuracy_deferral_test"].grid(row=4, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_deferral_test"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_deferral_test"].grid(row=4, column=1, padx=10, pady=10, sticky="ewns")
        
        # Training set
        # Accuracy
        self.labels["accuracy_train"] = ctk.CTkLabel(self, text="Accuracy of the whole model (training set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["accuracy_train"].grid(row=5, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_train"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_train"].grid(row=5, column=1, padx=10, pady=10, sticky="ewns")

        # Number of elements declared as hard
        self.labels["nb_hard_train"] = ctk.CTkLabel(self, text="Number of hard elements (training set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["nb_hard_train"].grid(row=6, column=0, padx=10, pady=10, sticky="ewns")
        self.values["nb_hard_train"] = ctk.CTkLabel(self, text="")
        self.values["nb_hard_train"].grid(row=6, column=1, padx=10, pady=10, sticky="ewns")

        # Accuracy of the base classifier alone
        self.labels["accuracy_base_train"] = ctk.CTkLabel(self, text="Accuracy of the base classifier (training set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["accuracy_base_train"].grid(row=7, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_base_train"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_base_train"].grid(row=7, column=1, padx=10, pady=10, sticky="ewns")

        # Accuracy of the deferral classifier alone
        self.labels["accuracy_deferral_train"] = ctk.CTkLabel(self, text="Accuracy of the deferral classifier (training set)", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["accuracy_deferral_train"].grid(row=8, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_deferral_train"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_deferral_train"].grid(row=8, column=1, padx=10, pady=10, sticky="ewns")

        # Number of features
        self.labels["n_features"] = ctk.CTkLabel(self, text="Number of features in the base dataset", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
        self.labels["n_features"].grid(row=9, column=0, padx=10, pady=10, sticky="ewns")
        self.values["n_features"] = ctk.CTkLabel(self, text="")
        self.values["n_features"].grid(row=9, column=1, padx=10, pady=10, sticky="ewns")

    def set(self, **kwargs):
        """
        Method used to set fields of the the frame

        :param kwargs: Dictionnary of associating a statistic to a value
        :kwargs; dict
        """
        for key, value in kwargs.items():
            self.values[key].configure(text=value)
