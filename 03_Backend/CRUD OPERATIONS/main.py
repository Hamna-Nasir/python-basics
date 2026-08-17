from fastapi import FastAPI, HTTPException
from model import Student

app = FastAPI()

students = []


@app.post("/students")
def add_student(student: Student):

    for s in students:
        if s.student_id == student.student_id:
            raise HTTPException(status_code=400, detail="Student ID already exists.")

    students.append(student)

    return {"message": "Student added successfully!", "student": student}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student.student_id == student_id:
            return student

    raise HTTPException(status_code=404, detail="Student not found.")


@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.student_id == student_id:
            students[index] = updated_student

            return {
                "message": "Student updated successfully!",
                "student": updated_student,
            }

    raise HTTPException(status_code=404, detail="Student not found.")


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student.student_id == student_id:
            students.remove(student)

            return {"message": "Student deleted successfully!"}

    raise HTTPException(status_code=404, detail="Student not found.")


