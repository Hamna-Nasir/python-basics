class Student:

    def __init__(self):
        self.name = "Hamna"
        self._cgpa = 0  # Protected attribute
        self.__password = "mysecret"  # Private attribute

    def set_cgpa(self, cgpa):

        if 0 <= cgpa <= 4:

            self._cgpa = cgpa

        else:

            print("Invalid CGPA")

    def get_cgpa(self):
        return self._cgpa

    def get_password(self):
        return self.__password

student = Student()
print(f"Student Name: {student.name}")
student.set_cgpa(3.8)
print(student.get_cgpa())
print(student.get_password())
