# student_manager.py
from db import get_all_students, get_student_by_id, insert_student, update_student as db_update_student, delete_student as db_delete_student


def add_student(student_id, name, age, department, marks, Grade):
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "marks": marks,
        "Grade": Grade,
    }
    insert_student(student)
    print(f"{name} added successfully.")


def view_students():
    students = get_all_students()
    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} \nName: {student['name']} \nAge: {student['age']}"
            f"\nDepartment: {student['department']} \nMarks: {student['marks']} \nGrade: {student['grade']}\n"
        )


def search_student(student_id):
    student = get_student_by_id(student_id)
    if student:
        print(
            f"ID: {student['id']} \nName: {student['name']} \nAge: {student['age']} "
            f"\nDepartment: {student['department']} \nMarks: {student['marks']} \nGrade: {student['grade']}"
        )
        return

    print(f"Student with ID {student_id} not found.")


def update_student(student_id, name=None, age=None, department=None, marks=None, Grade=None):
    grade_value = Grade if Grade is not None else None
    success = db_update_student(student_id, name=name, age=age, department=department, marks=marks, grade=grade_value)
    if success:
        print(f"Student with ID {student_id} updated successfully.")
    else:
        print(f"Student with ID {student_id} not found.")


def delete_student(student_id):
    success = db_delete_student(student_id)
    if success:
        print(f"Student with ID {student_id} deleted successfully.")
    else:
        print(f"Student with ID {student_id} not found.")


def show_statistics():
    students = get_all_students()
    if not students:
        print("No students found.")
        return

    total_students = len(students)
    average_marks = sum(student['marks'] for student in students) / total_students
    highest_marks = max(student['marks'] for student in students)
    lowest_marks = min(student['marks'] for student in students)
    
    print(f"Total Students: {total_students}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
