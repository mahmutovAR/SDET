class EnvVarError(Exception):
    """Error class, is raised if required settings are not set."""
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return f'Error! Environment variable does not exist or is invalid: {self.error}'
