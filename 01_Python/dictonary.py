# dictionary
student = {
    "name" : "Hamna",
    "age" : 21 , 
    "cgpa" : 3.85
}

print(student)
print(student.get("age"))

student["city"] = "Karachi"
print(student)

student["cgpa"] = 4.0
print(student)

student.pop("city")
print(student)

print(student.items())

for key in student:
    print(key)

for value in student.values():
    print(value)

for key , value in student.items():
    print(key , ":" , value)


# Nested dictionary
students = {
    "student1": {"name": "Hamna", "cgpa": 3.9},
    "student2": {"name": "Ali", "cgpa": 3.6},
}

print(students["student2"]["name"])

student = {"name": "Hamna", "age": 21, "university": "SSUET", "cgpa": 3.9}
for key , value in student.items():
    print(f"{key} : {value}")

# phoneBook
phoneBook = {}
for i in range(5):
    name = input("Enter name :")
    numb = int(input("Enter phone number :"))
    phoneBook[name] = numb
print(phoneBook.get("hamna")) 


