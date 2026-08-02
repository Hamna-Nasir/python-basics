from notes import *
print("Welcome to the Notes Taking System!")
print("\nMenu:")
print("1. Add a note")
print("2. View notes")
print("3. Exit")

while True:
    choice = input("\nEnter your choice (1-3): ")

    if choice == '1':
        add_note()
    elif choice == '2':
        print("\nYour Notes:")
        view_notes()
    elif choice == '3':
        exit_program()
        break
    else:
        print("Invalid choice. Please try again.")