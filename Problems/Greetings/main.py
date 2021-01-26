class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def great(self):
        return "Hello, I am {}!".format(self.name)


print(Person(input()).great())