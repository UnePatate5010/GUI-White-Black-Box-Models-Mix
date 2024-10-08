import sys
import customtkinter as ctk
from widgets.scrollFrame import ScrollFrame
from widgets.datasets.datasetFrame import DatasetFrame
from widgets.runFrame import RunFrame
from widgets.outputFrames.graphFrame import GraphFrame
from widgets.outputFrames.statsFrame import StatsFrame
from widgets.outputFrames.schemaFrame import SchemaFrame
from constants import *
from widgets.widgetExceptions import *

ctk.deactivate_automatic_dpi_awareness()

class GUI(ctk.CTk):
    """The GUI class is the main window of the application. It is charged to instantiate and display all
    input and outpout frames.
    """

    def __init__(self):
        """Constructor method
        """
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
        self.grader = ScrollFrame(self, "Grader", MODEL_FRAMES.keys())
        self.grader.grid(row=4, rowspan=3, column=1, padx=10, pady=10, sticky="ewns")

        # Base classifier frame
        self.base = ScrollFrame(self, "Base Classifier", MODEL_FRAMES.keys())
        self.base.grid(row=4, rowspan=3, column=2, padx=10, pady=10, sticky="ewns")

        # Deferral classifier frame
        self.deferral = ScrollFrame(self, "Deferral Classifier", MODEL_FRAMES.keys())
        self.deferral.grid(row=4, rowspan=3, column=3, padx=10, pady=10, sticky="ewns")

        # Resampling methods
        self.resampling = ScrollFrame(self, "Resampling method", RESAMPLING_FRAMES.keys(), scroll_display_name="Select a resampling method")
        self.resampling.grid(row=4, rowspan=2, column=4, padx=10, pady=10, sticky="ewns")

        # Run button
        self.run = RunFrame(self)
        self.run.grid(row=6, column=4, padx=10, pady=10, sticky="news")

        # ========== Output frames ========== #

        # Graph frame
        self.graph = GraphFrame(self)
        self.graph.grid(row=0, rowspan=4, column=0, columnspan=3, padx=10, pady=10, sticky="news")

        # Schema frame
        self.schema = SchemaFrame(self)
        self.schema.grid(row=0, rowspan=3, column=3, columnspan=2, padx=10, pady=10, sticky="news")

        # Stats frame
        self.stats = StatsFrame(self)
        self.stats.grid(row=3, column=3, columnspan=2, padx=10, pady=10, sticky="news")


    def freeze(self):
        """'Freeze' all frames by disabling all buttons/entries/spinboxes/menus of the interface.
        """
        self.dataset.freeze()
        self.grader.freeze()
        self.base.freeze()
        self.deferral.freeze()
        self.resampling.freeze()
        self.run.freeze()

    def unfreeze(self):
        """'Unfreeze' all frames by enabling back every possible input.
        """
        self.dataset.unfreeze()
        self.grader.unfreeze()
        self.base.unfreeze()
        self.deferral.unfreeze()
        self.resampling.unfreeze()
        self.run.unfreeze()

    def get(self):
        """Returns a list of value inputed by the user in the different frames.
    
        :raises UnselectedItemError: raises an error if a field was not properly filled.
        :return: A List of values inputed by the user in each frame.
        :rtype: List
        """
        error = []
        L = []
        try:
            L.append(self.dataset.get())
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
             L.append(self.grader.get())
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
             L.append(self.base.get())
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
             L.append(self.deferral.get())
        except UnselectedItemError as e:
            error.append(e.missing)
        try:
             L.append(self.resampling.get())
        except UnselectedItemError as e:
            error.append(e.missing)
        if len(error):
            raise UnselectedItemError("Missing items", error)
        return L

if __name__ == "__main__":
    if len(sys.argv) == 2:
        color = sys.argv[1]
        try:
            ctk.set_appearance_mode(color)
        except:
            print("Color should be either \"dark\" or \"light\".")
    elif len(sys.argv) > 2:
        print("Too many arguments. There should be only one that is either \"dark\" or \"light\". Arguments ignored")

    window = GUI()
    window.protocol("WM_DELETE_WINDOW", window.quit) # Prevent some errors related to matplotlib plots not closing correctly
    window.mainloop()