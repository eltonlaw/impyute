""" impyute.util.errors """
class BadInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
