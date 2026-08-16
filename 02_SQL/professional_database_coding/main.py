from connection import Database
from student_repository import StudentRepository

db = Database()

connection = db.get_connection()

repo = StudentRepository(connection)
newstudent = repo.add_student('Akbar' , 22 ,'IT' ,3.6)
print(newstudent)

students = repo.get_all_students()


for student in students:
    print(student)
    


connection.close()
