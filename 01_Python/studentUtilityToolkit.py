name = input("Enter your name: ")
age = int(input("Enter your age: "))
university = input("Enter your university: ")
field_of_study = input("Enter your field of study: ")
section = input("Enter your section: ")
cgpa = float(input("Enter your CGPA: "))

operator = input("Enter option you wanna perform: \n1. Display Student Information\n2. Check CGPA Status\n3. Check Age Status\n4. Check Section Status\n5. Check Field of Study Status")

def display_student_info(name, age, university, field_of_study, section, cgpa):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"University: {university}")
    print(f"Field of Study: {field_of_study}")
    print(f"Section: {section}")
    print(f"CGPA: {cgpa}")

def check_cgpa_status(cgpa):
    if cgpa >= 3.5:
        return "Excellent"
    elif cgpa >= 3.0:
        return "Good"
    elif cgpa >= 2.5:
        return "Average"
    else:
        return "Poor"
    
def check_age_status(age): 
    if age < 18:
        return "Minor"
    elif age >= 18 and age < 25:
        return "Young Adult"
    else:
        return "Adult"
    
def check_section_status(section):
    if section.lower() == "a":
        return "Section A"
    elif section.lower() == "b":
        return "Section B"
    else:
        return "Unknown Section"
    
def check_field_of_study_status(field_of_study):
    if field_of_study.lower() == "computer science":
        return "Computer Science"
    elif field_of_study.lower() == "information technology":
        return "Information Technology"
    else:
        return "Other Field of Study"

if operator == "1":
    print(display_student_info(name, age, university, field_of_study, section, cgpa))
if operator == "2":
    print(check_cgpa_status(cgpa))
if operator == "3":
    print(check_age_status(age))
if operator == "4":
    print(check_section_status(section))
if operator == "5":
    print(check_field_of_study_status(field_of_study))
