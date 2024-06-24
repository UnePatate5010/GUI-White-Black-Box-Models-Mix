import customtkinter as ctk

class DecisionTreeFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        ctk.CTkLabel(self, text="Depth").pack()
        self.entry = ctk.CTkEntry(self, height=10, width=200)
        self.entry.pack()
    
    def get(self):
        return self.entry.get()