class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    # use appropriate decorator
    @classmethod
    def from_string(cls, string):
        return cls(*string.split("-"))
