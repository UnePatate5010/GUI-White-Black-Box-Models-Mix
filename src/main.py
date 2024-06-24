import customtkinter as ctk
from widgets.scrollFrame import ScrollFrame
from constants import Models


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()  
        self._state_before_windows_set_titlebar_color = "zoomed"
        self.title("GUI")
        
        # This part is for Ubuntu because for some reason previous lines don't work
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        
        # Grid specification
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

        # Grader frame
        self.base = ScrollFrame(self, "Grader", Models.CLASSIFIERS.value)
        self.base.grid(row=3, rowspan=3, column=1, padx=10, pady=10, sticky="ewns")

        # Base classifier frame
        self.base = ScrollFrame(self, "Base Classifier", Models.CLASSIFIERS.value)
        self.base.grid(row=3, rowspan=3, column=2, padx=10, pady=10, sticky="ewns")

        # Deferral classifier frame
        self.base = ScrollFrame(self, "Base Classifier", Models.CLASSIFIERS.value)
        self.base.grid(row=3, rowspan=3, column=3, padx=10, pady=10, sticky="ewns")

window = GUI()
window.mainloop()