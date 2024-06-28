import customtkinter as ctk

class StatsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Statistics", fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ewn")

        # ========== Stats ========== #

        self.labels = {}
        self.values = {}

        # Accuracy
        self.labels["accuracy"] = ctk.CTkLabel(self, text="Accuracy of the whole model")
        self.labels["accuracy"].grid(row=1, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy"] = ctk.CTkLabel(self, text="")
        self.values["accuracy"].grid(row=1, column=1, padx=10, pady=10, sticky="ewns")

        # Number of elements declared as hard
        self.labels["nb_hard"] = ctk.CTkLabel(self, text="Number of hard elements")
        self.labels["nb_hard"].grid(row=2, column=0, padx=10, pady=10, sticky="ewns")
        self.values["nb_hard"] = ctk.CTkLabel(self, text="")
        self.values["nb_hard"].grid(row=2, column=1, padx=10, pady=10, sticky="ewns")

        # Accuracy of the base classifier alone
        self.labels["accuracy_base"] = ctk.CTkLabel(self, text="Accuracy of the base classifier")
        self.labels["accuracy_base"].grid(row=3, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_base"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_base"].grid(row=3, column=1, padx=10, pady=10, sticky="ewns")

        # Accuracy of the deferral classifier alone
        self.labels["accuracy_deferral"] = ctk.CTkLabel(self, text="Accuracy of the deferral classifier")
        self.labels["accuracy_deferral"].grid(row=4, column=0, padx=10, pady=10, sticky="ewns")
        self.values["accuracy_deferral"] = ctk.CTkLabel(self, text="")
        self.values["accuracy_deferral"].grid(row=4, column=1, padx=10, pady=10, sticky="ewns")

    def set(self, **kwargs):
        """
        Method used to set fields of the the frame
        """
        for key, value in kwargs.items():
            self.values[key].configure(text=value)
