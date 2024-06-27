import customtkinter as ctk
from widgets.CTkScrollableDropdown.CTkScrollableDropdown.ctk_scrollable_dropdown import CTkScrollableDropdown
from widgets.widgetExceptions import *
from constants import ScrollLists

class DatasetFrame(ctk.CTkFrame):
    """
    Frame used to select a dataset for the experiment.
    """

    def __init__(self, master):
        """
        Constructor method
        """

        super().__init__(master)

        self.grid_propagate(False) # Prevent the frame from changing size depending on widgets inside
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # Display frame name
        self.name = ctk.CTkLabel(self, text="Dataset")
        self.name.grid(row=0, column=0, padx=10, pady=10, sticky="ewn")

        # Values of the scrollable menu
        self.scrollValues = ScrollLists.DATASETS.value

        # Scrollable menu
        self.optionmenu = ctk.CTkOptionMenu(self, width=250, values=["Select a dataset"], fg_color="#a51f6a", button_color="#701448", button_hover_color="#4f203a")
        self.optionmenu.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.ctkscroll = CTkScrollableDropdown(self.optionmenu, values=self.scrollValues, command=self.on_dropdown_select)

    def on_dropdown_select(self, frame):
        self.optionmenu.set(frame)
        self.optionmenu.configure(fg_color="#1f6aa5", button_color="#144870", button_hover_color="#203a4f")

    def get(self):
        if self.optionmenu.get() == "Select a dataset":
            raise UnselectedItemError("Missing item", self.name.cget("text"))
        return self.optionmenu.get()
    
    def freeze(self):
        self.optionmenu.configure(state='disabled')

    def unfreeze(self):
        self.optionmenu.configure(state='normal')