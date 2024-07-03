"""
This files contains cutsom exceptions. 
"""

class UnselectedItemError(Exception):
    """Exception raised when the user tries to run the experiment but has not selected all fields.

    :param message: Error message
    :type message: str
    :param missingElement: Field that has not been selected
    :type missingElement: str or list (of str)
    """
    def __init__(self, message, missingElement):
        super().__init__(message)
        self.missing = missingElement