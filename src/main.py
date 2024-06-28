import customtkinter as ctk
from widgets.scrollFrame import ScrollFrame
from widgets.dataset.datasetFrame import DatasetFrame
from widgets.runFrame import RunFrame
from widgets.outputFrames.graphFrame import GraphFrame
from widgets.outputFrames.statsFrame import StatsFrame
from constants import ScrollLists
from widgets.widgetExceptions import *


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()  
        self._state_before_windows_set_titlebar_color = "zoomed" # Maximiwe the window
        self.title("GUI")
        
        # This part is for Ubuntu because for some reason previous lines don't work (Works fine on Windows)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        
        # Grid specification
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        # ========== Input frames ========== #
        
        # Dataset Frame
        self.dataset = DatasetFrame(self)
        self.dataset.grid(row=4, rowspan=3, column=0, padx=10, pady=10, sticky="ewns")

        # Grader frame
        self.grader = ScrollFrame(self, "Grader", ScrollLists.GRADERS.value)
        self.grader.grid(row=4, rowspan=3, column=1, padx=10, pady=10, sticky="ewns")

        # Base classifier frame
        self.base = ScrollFrame(self, "Base Classifier", ScrollLists.CLASSIFIERS.value)
        self.base.grid(row=4, rowspan=3, column=2, padx=10, pady=10, sticky="ewns")

        # Deferral classifier frame
        self.deferral = ScrollFrame(self, "Deferral Classifier", ScrollLists.CLASSIFIERS.value)
        self.deferral.grid(row=4, rowspan=3, column=3, padx=10, pady=10, sticky="ewns")

        # Resampling methods
        self.resampling = ScrollFrame(self, "Resampling method", ScrollLists.RESAMPLING.value)
        self.resampling.grid(row=4, rowspan=2, column=4, padx=10, pady=10, sticky="ewns")

        # Run button
        self.run = RunFrame(self)
        self.run.grid(row=6, column=4, padx=10, pady=10, sticky="news")

        # ========== Output frames ========== #

        # Graph frame
        self.graph = GraphFrame(self)
        self.graph.grid(row=0, rowspan=4, column=0, columnspan=3, padx=10, pady=10, sticky="news")

        # Schema frame PLACEHOLDER
        self.schema = GraphFrame(self)
        self.schema.grid(row=0, rowspan=3, column=3, columnspan=2, padx=10, pady=10, sticky="news")

        # Stats frame
        self.stats = StatsFrame(self)
        self.stats.grid(row=3, column=3, columnspan=2, padx=10, pady=10, sticky="news")


    def freeze(self):
        self.dataset.freeze()
        self.grader.freeze()
        self.base.freeze()
        self.deferral.freeze()
        self.resampling.freeze()
        self.run.freeze()

    def unfreeze(self):
        self.dataset.unfreeze()
        self.grader.unfreeze()
        self.base.unfreeze()
        self.deferral.unfreeze()
        self.resampling.unfreeze()
        self.run.unfreeze()

    def get(self):
        """
        :rtype: {str: (str:{})}
        """
        error = []
        dic = {}
        try:
            dic["dataset"] = self.dataset.get()
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
            dic["grader"] = self.grader.get()
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
            dic["base"] = self.base.get()
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
            dic["deferral"] = self.deferral.get()
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
            dic["resampling"] = self.resampling.get()
        except UnselectedItemError as e:
            error.append(e.missing)
        if len(error):
            raise UnselectedItemError("Missing items", error)
        return dic

window = GUI()
window.mainloop()