"""
Base Class for models frames. It brings several attributes and methods used in the different frames -> refactoring
"""

class Model():
    def __init__(self):
        self.labels = [] # List of labels (for entries)
        self.entries = [] # List of entry fields

    def get(self):
        """
        Method used to retrieve information inputed by the user

        :returns: dictionnary where keys are labels of input fields and values are correpsonding inputed values
        """
        dic = {}
        for i in range(len(self.entries)):
            dic.update({self.labels[i].cget("text"): self.entries[i].get()})
        return dic

    def freeze(self):
        """
        Freeze all fields (disable)
        """
        for i in range(len(self.entries)):
            self.entries[i].configure(state='disabled')

    def unfreeze(self):
        """
        Unfreeze all fields (enable)
        """
        for i in range(len(self.entries)):
            self.entries[i].configure(state='normal')