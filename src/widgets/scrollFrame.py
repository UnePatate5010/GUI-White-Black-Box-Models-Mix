"""
The ScrollFrame is a generic frame that has a scrollable menu and display new fields depending on
selected values.
"""

import customtkinter as ctk
from constants import ALL
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.widgetExceptions import *

class ScrollFrame(ctk.CTkFrame):
    """
    This class represents a frame with a scollable menu. The said menu is constitued of provided elements.
    The frame display input fields depending on the element selected in the scrollable menu.
    
    :param master: The master frame/window of this frame
    :type master: class
    :param name: Displayed name at the top of the frame, default to "Scrollable Frame"
    :type name: str, optional
    :param models: List of models names, used for display and frames loading, default to []
    :type models: list
    :param scroll_display_name: Name to display on the scrollable menu before anything has been selected, default to "Select a classifier"
    :type scroll_display_name: str
    """
        
    def __init__(self, master, name="Scrollable Frame", models=[], scroll_display_name = "Select a classifier"):
        """
        Constructor method
        """

        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text=name, fg_color="#333333", corner_radius=10)
        self.name.grid(row=0, column=0, padx=10, pady=10, sticky="ewn")

        # Values of the scrollable menu
        self.scrollValues = models

        # Scrollable menu
        self.optionmenu = ctk.CTkOptionMenu(self, width=250, values=[scroll_display_name], fg_color="#a51f6a", button_color="#701448", button_hover_color="#4f203a")
        self.optionmenu.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.ctkscroll = CTkScrollableDropdown(self.optionmenu, values=self.scrollValues, command=self.on_dropdown_select)

        # Set up frames
        self.current_frame = None # Name of the frame currently displayed
        self.frames = {} # Dictionnary associating frame name to frame class
    
    def on_dropdown_select(self, frame):
        """
        Modify the displayed value on the scrollable menu and update displayed fields

        :param frame: Selected element in the scrollable menu to display fields
        :type frame: str
        """
        self.optionmenu.set(frame)  
        self.update_fields(frame)
        self.optionmenu.configure(fg_color="#1f6aa5", button_color="#144870", button_hover_color="#203a4f")


    def update_fields(self, frame):
        """
        Update displayed fields depending on the provided frame name

        :param frame: Selected element in the scrollable menu to display fields
        :type frame: str
        """
        # Remove current displayed frame if existing
        if self.current_frame != None:
            self.frames[self.current_frame].grid_remove()

        # Instantiate the frame if not already existing (and stored in self.frames)
        if frame not in self.frames:
            self.frames[frame] =  ALL[frame](self)


        self.current_frame = frame
        self.frames[frame].grid(row=2, column=0, padx=10, pady=10, sticky="ewns")


    def get(self):
        """
        Method called to retrieve input data from the frame itself and inner frames.

        :return: The selected element in the scrollable menu and a dictionnary from the corresponding inner frame
        :rtype: str, dict
        """
        if self.current_frame == None:
            raise UnselectedItemError("An element was not selected", self.name.cget("text"))
        return self.current_frame, self.frames[self.current_frame].get()
    
    def freeze(self):
        """
        Freeze all fields (disable)
        """
        self.optionmenu.configure(state='disabled')
        if self.current_frame != None:
            self.frames[self.current_frame].freeze()

    def unfreeze(self):
        """
        Unfreeze all fields (enable)
        """
        self.optionmenu.configure(state='normal')
        if self.current_frame != None:
            self.frames[self.current_frame].unfreeze()