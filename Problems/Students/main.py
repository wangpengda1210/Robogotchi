class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = self.name[0:1] + self.last_name + str(self.birth_year)


print(Student(input(), input(), int(input())).student_id)
