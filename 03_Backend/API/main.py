from fastapi import FastAPI

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
        {"id":101,"name":"Hamna"},
        {"id":102,"name":"Ali"}
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