"""This file provides the DatasetFrame, a frame used to select a dataset.
"""
import customtkinter as ctk
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.CTkSpinbox.CtkSpinbox import Spinbox
from CTkToolTip import CTkToolTip
from widgets.widgetExceptions import *
import os
from datasets.loadDataset import loadDataset


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
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure((1, 2), weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Dataset", fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ewn")

        # Values of the scrollable menu
        self.scrollValues = get_relative_paths("./datasets/")

        # Scrollable menu
        self.optionmenu = ctk.CTkOptionMenu(self, width=250, values=["Select a dataset"], fg_color="#a51f6a", button_color="#701448", button_hover_color="#4f203a")
        self.optionmenu.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.ctkscroll = CTkScrollableDropdown(self.optionmenu, values=self.scrollValues, command=self.on_dropdown_select)

        self.validation_label = None
        

    def on_dropdown_select(self, frame):
        """Method called when an item is selected in the scrollable menu. Changes the displayed dataset.
        """
        self.optionmenu.set(frame)
        self.optionmenu.configure(fg_color="#1f6aa5", button_color="#144870", button_hover_color="#203a4f")

        if not self.validation_label:
            # Percentage of data for the validation set
            self.validation_label = ctk.CTkLabel(self, text="Percentage of the validation set", wraplength=self.winfo_width()//2 - 20, justify="left", padx=10)
            self.validation_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            CTkToolTip(self.validation_label, "The percentage of the dataset that will be used as a validation set")
            self.validation_spinbox = Spinbox(self, minimum_value=1, none_enable=False)
            self.validation_spinbox.set(20) # Default value
            self.validation_spinbox.grid(row=2, column=1, padx=10, pady=10, sticky="we")

    def get(self):
        """
        Method called to retrieve input data from the frame itself.

        :return: The selected element in the scrollable menu
        :rtype: str
        """
        if self.optionmenu.get() == "Select a dataset":
            raise UnselectedItemError("Missing item", self.name.cget("text"))
        return loadDataset(self.optionmenu.get()), self.validation_spinbox.get() / 100
    
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
