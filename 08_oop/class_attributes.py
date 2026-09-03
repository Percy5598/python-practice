class Student:
    # Class attribute is shared by all instances of the class
    university = "LUT University"

    def __init__(self, name, score):
        self.name = name
        self.score = score

student1 = Student("Prashant", 90)
student2 = Student("Anna", 85)

print(student1.university)
print(student2.university)