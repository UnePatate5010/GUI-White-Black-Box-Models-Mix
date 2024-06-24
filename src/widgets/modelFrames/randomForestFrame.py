import customtkinter as ctk

class RandomForestFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.labels = []
        self.entries = []

        self.labels.append(ctk.CTkLabel(self, text="Trees"))
        self.labels[0].grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(ctk.CTkEntry(self, height=10, width=200))
        self.entries[0].grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.labels.append(ctk.CTkLabel(self, text="Depth"))
        self.labels[1].grid(row=1, column=0, padx=20, pady=20, sticky="w")
        self.entries.append(ctk.CTkEntry(self, height=10, width=200))
        self.entries[1].grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Disable entry field and change its color
        # self.entries[0].configure(state="disabled", fg_color="green")
    
    def get(self):
        dic = {}
        for i in range(len(self.entries)):
            dic.update({self.labels[i].cget("text"): self.entries[i].get()})
        return dic