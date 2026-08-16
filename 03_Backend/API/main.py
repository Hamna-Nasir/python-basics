from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to my first FastAPI application!"
    }

@app.get("/about")
def about():
    return {
        "developer": "Hamna",
        "goal": "Become an AI Software Engineer"
    }

@app.get("/students")
def students():
    return [
        {"id":101,"name":"Hamna","department":"Computer Science"},
        {"id":102,"name":"Ali","department":"IT"}
    ]

@app.get("/skills")
def skills():
    return[
        "Python",
        "SQL",
        "PostgreSQL"
]

@app.get("/dream")
def dream():
    return{
            "career":"AI Software Engineer"
    }


@app.get("/courses")
def courses():
    return [
            {"id":1,"name":"Python"},
            {"id":2,"name":"Java"},
            {"id":3,"name":"C++"},
            {"id":4,"name":"JS"},
            {"id":5,"name":"PHP"},
        ]

@app.get("/students/{student_id}/courses/{course_id}")
def get_course(student_id: int, course_id: int):
    return {
        "student_id": student_id,
        "course_id": course_id
    }


@app.get("/students")
def get_students(department: str):
    return {"department": department}


@app.get("/search")
def search(name: Optional[str] = None):
    return {"name": name}


@app.get("/students/{student_id}")
def student(student_id: int, details: bool = False):

    return {"student_id": student_id, "details": details}
