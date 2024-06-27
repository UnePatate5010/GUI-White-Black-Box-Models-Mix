class UnselectedItemError(Exception):
    def __init__(self, message, missingElement):
        super().__init__(message)
        self.missing = missingElement