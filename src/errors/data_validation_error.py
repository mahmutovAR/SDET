class EnteredDataValidationError(Exception):
    """Exception raises if the data entered into the form fields
    does not match the data presented in the pop-up window."""
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return {self.error}
