class Stack:

    def __init__(self):
        self.values = []

    def push(self, el):
        self.values.append(el)

    def pop(self):
        to_pop = self.peek()
        self.values.pop()
        return to_pop

    def peek(self):
        return self.values[len(self.values) - 1]

    def is_empty(self):
        return len(self.values) == 0
