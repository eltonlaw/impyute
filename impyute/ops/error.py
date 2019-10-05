""" Impyute specific error messages """

class BadInputError(Exception):
    "Error thrown when input args don't match spec"
    pass

class BadOutputError(Exception):
    "Error thrown when outputs don't match spec"
    pass
