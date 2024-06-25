import customtkinter as ctk
from widgets.scrollFrame import ScrollFrame
from widgets.runFrame import RunFrame
from widgets.outputFrames.graphFrame import GraphFrame
from constants import Models


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()  
        self._state_before_windows_set_titlebar_color = "zoomed"
        self.title("GUI")
        
        # This part is for Ubuntu because for some reason previous lines don't work (Works fine on Windows)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        
        # Grid specification
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        
        # Dataset Frame
        self.dataset = ScrollFrame(self, "Placeholder", [])
        self.dataset.grid(row=4, rowspan=3, column=0, padx=10, pady=10, sticky="ewns")

        # Grader frame
        self.grader = ScrollFrame(self, "Grader", Models.GRADERS.value)
        self.grader.grid(row=4, rowspan=3, column=1, padx=10, pady=10, sticky="ewns")

        # Base classifier frame
        self.base = ScrollFrame(self, "Base Classifier", Models.CLASSIFIERS.value)
        self.base.grid(row=4, rowspan=3, column=2, padx=10, pady=10, sticky="ewns")

        # Deferral classifier frame
        self.deferral = ScrollFrame(self, "Base Classifier", Models.CLASSIFIERS.value)
        self.deferral.grid(row=4, rowspan=3, column=3, padx=10, pady=10, sticky="ewns")

        # Run button
        self.run = RunFrame(self)
        self.run.grid(row=6, column=4, padx=10, pady=10, sticky="news")

        # Graph frame
        self.graph = GraphFrame(self)
        self.graph.grid(row=0, rowspan=4, column=0, columnspan=3, padx=10, pady=10, sticky="news")

window = GUI()
window.mainloop()