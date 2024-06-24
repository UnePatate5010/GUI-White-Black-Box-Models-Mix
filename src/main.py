import customtkinter as ctk
from widgets.classifier_widget import ClassifierFrame


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()  
        self._state_before_windows_set_titlebar_color = 'zoomed'
        self.title("Test window")

        self.base = ClassifierFrame(self, "For classifier")
        self.base.grid(row=0, column=0, padx=10, pady=10, sticky="ewns")


window = GUI()
window.mainloop()