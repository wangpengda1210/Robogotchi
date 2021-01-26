class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2

    def is_right(self):
        return self.a ** 2 + self.b ** 2 == self.c ** 2

    def area(self):
        if not self.is_right():
            return "Not right"
        else:
            return self.a * self.b / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
print(RightTriangle(input_c, input_a, input_b).area())
