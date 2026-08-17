from database import get_connection


def get_students():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return students


def add_student(student):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            student.student_id,
            student.name,
            student.age,
            student.department,
            student.cgpa,
        ),
    )

    connection.commit()

    cursor.close()
    connection.close()


def add_student(student):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students
        VALUES (%s,%s,%s,%s,%s)
        """,
        (
            student.student_id,
            student.name,
            student.age,
            student.department,
            student.cgpa,
        ),
    )

    connection.commit()

    cursor.close()
    connection.close()


def update_student(student_id, student):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE students
        SET
            name=%s,
            age=%s,
            department=%s,
            cgpa=%s
        WHERE student_id=%s
        """,
        (student.name, student.age, student.department, student.cgpa, student_id),
    )

    connection.commit()

    cursor.close()
    connection.close()


def delete_student(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))

    connection.commit()

    cursor.close()
    connection.close()


