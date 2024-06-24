"""
The ClassifierFrane is a customtkinter frame that encompass all input fields related
to classifiers. Two of those should be instantiated, one for the base clasifier, one
for the deferral classifier.
"""


import customtkinter as ctk




class ClassifierFrame(ctk.CTkFrame):
    def __init__(self, master, name="classifier"):
        """
        Initialisation method

        :param master: the master frame/window of this frame
        :param name: displayed name at the top of the frame, default to "classifier"
        :type name: str
        """
        super().__init__(master)

        