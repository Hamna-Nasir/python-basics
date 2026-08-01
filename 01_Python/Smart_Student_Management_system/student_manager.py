# student_manager.py
from data import students 


def add_student(student_id, name, age, department, marks, Grade):

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "marks": marks,
        "Grade": Grade,
    }

    students.append(student)

    print(f"{name} added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, "
              f"Department: {student['department']}, Marks: {student['marks']}, Grade: {student['Grade']}")

def search_student(student_id):
    for student in students:
        if student['id'] == student_id:
            print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, "
                  f"Department: {student['department']}, Marks: {student['marks']}, Grade: {student['Grade']}")
            return
    print(f"Student with ID {student_id} not found.")

def update_student(student_id, name=None, age=None, department=None, marks=None, Grade=None):
    for student in students:
        if student['id'] == student_id:
            if name is not None:
                student['name'] = name
            if age is not None:
                student['age'] = age
            if department is not None:
                student['department'] = department
            if marks is not None:
                student['marks'] = marks
            if Grade is not None:
                student['Grade'] = Grade
            print(f"Student with ID {student_id} updated successfully.")
            return
    print(f"Student with ID {student_id} not found.")

def delete_student(student_id):
    for i, student in enumerate(students):
        if student['id'] == student_id:
            del students[i]
            print(f"Student with ID {student_id} deleted successfully.")
            return
    print(f"Student with ID {student_id} not found.")

def show_statistics():
    if not students:
        print("No students found.")
        return
    total_students = len(students)
    average_marks = sum(student['marks'] for student in students) / total_students
    print(f"Total Students: {total_students}")
    print(f"Average Marks: {average_marks:.2f}")
