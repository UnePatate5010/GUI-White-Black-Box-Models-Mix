"""
Base Class for models frames. It brings several attributes and methods used in the different frames -> refactoring
"""

class Model():
    def __init__(self):
        """Constructor method
        """
        self.labels = [] # List of labels (for entries)
        self.entries = [] # List of entry fields

    def get(self):
        """
        Method used to retrieve information inputed by the user

        :returns: dictionnary where keys are labels of input fields and values are correpsonding inputed values
        """
        dic = {}
        for i in range(len(self.entries)):
            # Deal with scrollable menu for true or false
            if self.entries[i].get() == "True":
                value = True
            elif self.entries[i].get() == "False":
                value = False
            else:
                value = self.entries[i].get()
            dic.update({self.labels[i].cget("text"): value})
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