class StudentRepository:

    def __init__(self, connection):

        self.connection = connection
        self.cursor = connection.cursor()

    def get_all_students(self):

        self.cursor.execute("SELECT * FROM studenttable")

        return self.cursor.fetchall()

    def add_student(self, name, age, department, cgpa):

        try:

            self.cursor.execute(
                """
                INSERT INTO studenttable(name,age,department,cgpa)
                VALUES (%s,%s,%s,%s)
                """,
                (name, age, department, cgpa),
            )

            self.connection.commit()

            print("Student Added Successfully")

        except Exception as e:

            self.connection.rollback()

            print(e)
