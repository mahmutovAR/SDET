class SubmitError(Exception):
    """Exception raises if the data entered into the form fields
    has not been submitted."""
    def __str__(self):
        return 'The form has not been submitted'
