class EnteredDataValidationError(Exception):
    """Exception raises if the data entered into the form fields
    does not match the data presented in the pop-up window."""
    def __init__(self, error_field):
        self.error_field = error_field

    def __str__(self):
        return f'The "{self.error_field}" field value does not match the entered data'
