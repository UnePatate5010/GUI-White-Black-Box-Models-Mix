"""This file provides the DatasetFrame, a frame used to select a dataset.
"""
import customtkinter as ctk
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from CTkToolTip import CTkToolTip
from widgets.widgetExceptions import *
import os
from datasets.loadDataset import loadDataset
from constants import DIM_REDUCTION


class DatasetFrame(ctk.CTkFrame):
    """Frame used to select a dataset for the experiment.
    
    :param master: The master frame/window of this frame
    :type master: class
    """

    def __init__(self, master):
        """
        Constructor method
        """

        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure(5, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Dataset", fg_color="#727272", corner_radius=10)
        self.name.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ewn")

        # Values of the scrollable menu
        self.scrollValues = get_relative_paths("./datasets/")

        # Scrollable menu
        self.optionmenu = ctk.CTkOptionMenu(self, width=250, values=["Select a dataset"], fg_color="#a51f6a", button_color="#701448", button_hover_color="#4f203a")
        self.optionmenu.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.ctkscroll = CTkScrollableDropdown(self.optionmenu, values=self.scrollValues, command=self.on_dropdown_select_dataset)

        self.test_label = None

        # Scrollable menu
        self.dimRedValues = DIM_REDUCTION.keys()
        self.dimRedMenu = ctk.CTkOptionMenu(self, width=250, values=["Select a dimensionality reduction method"], fg_color="#a51f6a", button_color="#701448", button_hover_color="#4f203a")
        self.dimRedMenu.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.dimRedCtkscroll = CTkScrollableDropdown(self.dimRedMenu, values=self.dimRedValues, command=self.on_dropdown_select_reduction)

        self.current_reduction = None # Name of the frame currently displayed
        self.frames = {} # Dictionnary associating frame name to frame class

        

    def on_dropdown_select_dataset(self, frame):
        """Method called when an item is selected in the scrollable menu. Changes the displayed dataset.

        :param frame: Selected element in the scrollable menu to display fields
        :type frame: str
        """
        self.optionmenu.set(frame)
        self.optionmenu.configure(fg_color="#1f6aa5", button_color="#144870", button_hover_color="#203a4f")

        if not self.test_label:
            # Percentage of data for the test set
            self.test_label = ctk.CTkLabel(self, text="Percentage of the test set", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
            self.test_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            CTkToolTip(self.test_label, "The percentage of the dataset that will be used as a test set")
            self.test_spinbox = Spinbox(self, minimum_value=1, maximum_value=99, type=float, none_enable=False)
            self.test_spinbox.set(20) # Default value
            self.test_spinbox.grid(row=2, column=1, padx=10, pady=10, sticky="we")

            self.random_label = ctk.CTkLabel(self, text="Random split of the dataset", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
            CTkToolTip(self.random_label, "If True, the dataset is randomly split between the training and test sets. If False, the last 'X'% of the dataset will be the test set and the rest the training set (where 'X' is the value chosen in the previous field)")
            self.random_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            self.random_menu = ctk.CTkOptionMenu(self, width=250, values=["True"])
            self.random_menu.grid(row=3, column=1, padx=10, pady=10, sticky="we")
            self.random_scroll = CTkScrollableDropdown(self.random_menu, values=["True", "False"])


    
    def on_dropdown_select_reduction(self, frame):
        """
        Modify the displayed value on the scrollable menu and update displayed fields (for the dimensionality reduction technique menu)

        :param frame: Selected element in the scrollable menu to display fields
        :type frame: str
        """
        self.dimRedMenu.set(frame)  
        self.update_fields(frame)
        self.dimRedMenu.configure(fg_color="#1f6aa5", button_color="#144870", button_hover_color="#203a4f")

    def update_fields(self, frame):
        """
        Update displayed fields depending on the provided frame name

        :param frame: Selected element in the scrollable menu to display fields
        :type frame: str
        """
        # Remove current displayed frame if existing
        if self.current_reduction != None and self.current_reduction != "None":
            self.frames[self.current_reduction].grid_remove()

        # Instantiate the frame if not already existing (and stored in self.frames)
        if frame != "None":
            if frame not in self.frames:
                self.frames[frame] =  DIM_REDUCTION[frame](self)


            self.current_reduction = frame
            self.frames[frame].grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        else:
            self.current_reduction = None

    def get(self):
        """
        Method called to retrieve input data from the frame itself.

        :return: The selected element in the scrollable menu, the percentage of test set, a boolean corresponding to if the split is randomized or not
          and the instanciated dimensionality reduction technique
        :rtype: str, float, boolean, <object> or None
        """
        if self.optionmenu.get() == "Select a dataset":
            raise UnselectedItemError("Missing item", self.name.cget("text"))
        if self.current_reduction == None:
            ret = None
        else:
            ret = self.frames[self.current_reduction].get()
        if self.random_menu.get() == "True":
            rand_split = True
        else:
            rand_split = False
        return loadDataset(self.optionmenu.get()), self.test_spinbox.get()  / 100, rand_split, ret
    
    def freeze(self):
        """
        Freeze all fields (disable)
        """
        self.optionmenu.configure(state='disabled')

    def unfreeze(self):
        """
        Unfreeze all fields (enable)
        """
        self.optionmenu.configure(state='normal')


def get_relative_paths(directory):
    relative_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), directory)
            relative_paths.append(directory + relative_path)
    return relative_paths
