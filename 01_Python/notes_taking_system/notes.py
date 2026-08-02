    
with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\notes_taking_system\notes.txt", "r") as file:
    content = file.read()
    print(content)
def add_note():
    note = input("Enter your note: ")
    with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\notes_taking_system\notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully!")
    
def view_notes():
    with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\notes_taking_system\notes.txt", "r") as file:
        content = file.read()
        print("Your notes:")
        print(content)

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()