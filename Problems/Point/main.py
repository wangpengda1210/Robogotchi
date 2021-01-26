class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, another):
        return ((self.x - another.x) ** 2 + (self.y - another.y) ** 2) ** 0.5
