from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import status
from typing import Optional
app = FastAPI()

class Student(BaseModel):
    student_id: int
    name: str
    age: int
    department: str
    cgpa: float


@app.post("/students")
def create_student(student: Student):

    return {"message": "Student created successfully!", "student": student}


@app.post("/students", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):

    return student


students = []
@app.post("/students")
def add_student(student: Student):

    students.append(student)

    return student


@app.get("/students")
def get_students():

    return students
