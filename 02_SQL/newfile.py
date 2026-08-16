import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        database="newdb",
        user="postgres",
        password="hamnanasir",
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employes;")
    employees = cursor.fetchall()

    for employee in employees:
        print(employee)

except Exception as e:
    print("Database Error:", e)

finally:
    if "cursor" in locals():
        cursor.close()

    if "connection" in locals():
        connection.close()
