class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class student(person):

    def __init__(self, name,age, marks):
        super().__init__(name, age)
        self.marks = marks


class teacher(person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

student = student("Hamna", 21 , 90)
teacher = teacher("Hammad", 30, "Math")
print(f"Student Name: {student.name}, Age: {student.age} ,Marks: {student.marks}")
print(f"Teacher Name: {teacher.name}, Age: {teacher.age}, Subject: {teacher.subject}")

