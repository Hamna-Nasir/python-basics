from fastapi import FastAPI, HTTPException
from models import Student
import repository

app = FastAPI()


@app.get("/students")
def students():

    return repository.get_students()





@app.post("/students")
def add(student: Student):

    repository.add_student(student)

    return {"message": "Student added successfully."}


@app.put("/students/{student_id}")
def update(student_id: int, student: Student):

    repository.update_student(student_id, student)

    return {"message": "Student updated."}


@app.delete("/students/{student_id}")
def delete(student_id: int):

    repository.delete_student(student_id)

    return {"message": "Student deleted."}


