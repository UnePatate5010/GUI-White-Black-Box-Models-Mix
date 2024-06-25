import customtkinter as ctk

class GraphFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.canvas = ctk.CTkCanvas(self)
        self.canvas.grid(row=0, column=0, padx=10, pady=10, sticky="ewns")
