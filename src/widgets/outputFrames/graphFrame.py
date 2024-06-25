import customtkinter as ctk

class GraphFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside


        self.canvas = ctk.CTkCanvas(self)
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky="ewns")
