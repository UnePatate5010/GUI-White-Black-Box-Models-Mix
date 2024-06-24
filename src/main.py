import customtkinter as ctk
from widgets.scrollFrame import ScrollFrame
from constants import Models


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()  
        self._state_before_windows_set_titlebar_color = 'zoomed'
        self.title("Test window")

        # Grid specification
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Base classifier frame
        self.base = ScrollFrame(self, "Base Classifier", Models.CLASSIFIERS.value)
        self.base.grid(row=3, rowspan=3, column=1, padx=10, pady=10, sticky="ewns")


window = GUI()
window.mainloop()