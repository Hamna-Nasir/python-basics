import data
import student_manager
from helper import generate_line
from grade import calculate_grade

while True:
    print(generate_line())
    print("Welcome to the Smart Student Management System")
    print(generate_line())

    print("\nMenu:")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Statistics")
    print("7. Exit")

    print(f"\n{generate_line()}")

    try:
        choice = int(input("Enter your choice (1-7): "))
        if choice == 1:
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            marks = int(input("Enter Marks: "))

            Grade = calculate_grade(marks)

            student_manager.add_student(
                student_id,
                name,
                age,
                department,
                marks,
                Grade
            )
        elif choice == 2:
            student_manager.view_students() 
        elif choice == 3:
            student_id = int(input("Enter student ID to search: "))
            student_manager.search_student(student_id)
        elif choice == 4:
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name (leave blank to keep unchanged): ")
            age = input("Enter new age (leave blank to keep unchanged): ")
            department = input("Enter new department (leave blank to keep unchanged): ")
            marks = input("Enter new marks (leave blank to keep unchanged): ")
            student_manager.update_student(student_id, name or None, age or None, department or None, marks or None, Grade or None)
        elif choice == 5:
            student_id = int(input("Enter student ID to delete: "))
            student_manager.delete_student(student_id)  
        elif choice == 6:
            student_manager.show_statistics()
        elif choice == 7:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.") 
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
