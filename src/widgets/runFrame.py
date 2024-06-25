import customtkinter as ctk


class RunFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.run_button = ctk.CTkButton(self, text="RUN", command=self.button_callback)
        self.run_button.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    
    def button_callback(self):
        # print(self.master.base.get()) # Example use
        pass