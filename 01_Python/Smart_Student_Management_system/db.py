import os

import psycopg2
from psycopg2.extras import RealDictCursor


def get_connection(dbname=None):
    return psycopg2.connect(
        host=os.getenv("PG_HOST", "localhost"),
        port=os.getenv("PG_PORT", "5432"),
        dbname=dbname or os.getenv("PG_DATABASE", "student_management"),
        user=os.getenv("PG_USER", "postgres"),
        password=os.getenv("PG_PASSWORD", "postgres"),
    )


def init_db():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS student (
                        id INT PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        age INT NOT NULL,
                        department VARCHAR(50),
                        marks INT,
                        grade VARCHAR(3)
                    );
                    """
                )
        return True
    except Exception as exc:
        print("Warning: PostgreSQL initialization failed:", exc)
        return False


def insert_student(student):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO student (id, name, age, department, marks, grade) VALUES (%s, %s, %s, %s, %s, %s)",
                (
                    student["id"],
                    student["name"],
                    student["age"],
                    student["department"],
                    student["marks"],
                    student["Grade"],
                ),
            )
        conn.commit()


def get_all_students():
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT id, name, age, department, marks, grade FROM student ORDER BY id")
            return cursor.fetchall()


def get_student_by_id(student_id):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(
                "SELECT id, name, age, department, marks, grade FROM student WHERE id = %s",
                (student_id,),
            )
            return cursor.fetchone()


def update_student(student_id, name=None, age=None, department=None, marks=None, grade=None):
    updates = []
    values = []
    if name is not None:
        updates.append("name = %s")
        values.append(name)
    if age is not None:
        updates.append("age = %s")
        values.append(age)
    if department is not None:
        updates.append("department = %s")
        values.append(department)
    if marks is not None:
        updates.append("marks = %s")
        values.append(marks)
    if grade is not None:
        updates.append("grade = %s")
        values.append(grade)

    if not updates:
        return False

    values.append(student_id)
    query = f"UPDATE student SET {', '.join(updates)} WHERE id = %s"

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, tuple(values))
        conn.commit()
        return cursor.rowcount > 0


def delete_student(student_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM student WHERE id = %s", (student_id,))
            deleted = cursor.rowcount > 0
        conn.commit()
        return deleted
