"""
Custom spinbox widget used to input numbers.
"""

import customtkinter as ctk
from typing import Union, Callable

class Spinbox(ctk.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = ctk.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(100, "100")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[int, None]:
        val = self.entry.get()
        if val == None:
            return None
        try:
            return int(val)
        except ValueError:
            return None

    def set(self, value):
        self.entry.delete(0, "end")
        if value == None:
            self.entry.insert(0, "None")
        else:
            self.entry.insert(0, str(int(value)))


    def configure(self, **kwargs):
        if "state" in kwargs:
            self.state = kwargs.pop("state")
            if self.state == "disabled":
                self.disable()
            elif self.state == "normal":
                self.enable()
        
        super().configure(kwargs)

    def disable(self):
        self.entry.configure(state='disabled')
        self.add_button.configure(state='disabled')
        self.subtract_button.configure(state='disabled')
    
    def enable(self):
        self.entry.configure(state='normal')
        self.add_button.configure(state='normal')
        self.subtract_button.configure(state='normal')