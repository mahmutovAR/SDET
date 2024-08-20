class SubmitError(Exception):
    """Exception raises if the data entered into the form fields
    has not been submitted."""
    def __init__(self):
        self.error = 'The form has not been submitted'

    def __str__(self):
        return {self.error}
