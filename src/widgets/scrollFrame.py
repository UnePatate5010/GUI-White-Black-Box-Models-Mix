"""
The ClassifierFrane is a customtkinter frame that encompass all input fields related
to classifiers. Two of those should be instantiated, one for the base clasifier, one
for the deferral classifier.
"""

import customtkinter as ctk
from constants import Models, MODEL_FRAMES
from CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown




class ScrollFrame(ctk.CTkFrame):
    def __init__(self, master, name="Scrollable Frame", models=[]):
        """
        Initialisation method

        :param master: the master frame/window of this frame
        :param name: displayed name at the top of the frame, default to "Scrollable Frame"
        :type name: str
        :param models: list of models names (strings), used for display and frames loading
        :type models: [str]
        """
        super().__init__(master)

        # Display frame name
        ctk.CTkLabel(self, text=name).grid(row=0, column=0, padx=10, pady=10, sticky="ewn")

        # Values of the scrollable menu
        self.scrollValues = Models.CLASSIFIERS.value

        # Scrollable menu
        self.optionmenu = ctk.CTkOptionMenu(self, width=300, values=["Select a classifier"])
        self.optionmenu.grid(row=1, column=0, padx=10, pady=10, sticky="ewn")
        self.ctkscroll = CTkScrollableDropdown(self.optionmenu, values=self.scrollValues, command=self.on_dropdown_select)

        # Set up frames
        self.current_frame = None
        self.frames = {}
        for i in self.scrollValues:
            self.frames[i] = MODEL_FRAMES[i](self)
    
    def on_dropdown_select(self, selected_value):
        """
        Modify the displayed value on the scrollable menu and update displayed fields
        """
        self.optionmenu.set(selected_value)  
        self.update_fields(selected_value)


    def update_fields(self, selected_value):
        if self.current_frame != None:
            self.frames[self.current_frame].grid_remove()
        self.current_frame = selected_value
        self.frames[selected_value].grid(row=2, column=0, padx=10, pady=10, sticky="ews")