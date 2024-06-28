import customtkinter as ctk

class StatsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Statistics", fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ewn")

        # ========== Stats ========== #

        # Accuracy
        self.name = ctk.CTkLabel(self, text="Accuracy")
        self.name.grid(row=1, column=0, padx=10, pady=10, sticky="ewn")
        self.name = ctk.CTkLabel(self, text="")
        self.name.grid(row=1, column=1, padx=10, pady=10, sticky="ewn")

