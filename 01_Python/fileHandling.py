'''
file = open("C:\\Users\\a\\OneDrive\\Documents\\AI Product Engineering\\AI_Product_Engineer\\01_Python\\data.txt", "r")
content = file.read()
print(content)
file.close()
'''

'''
with open("C:\\Users\\a\\OneDrive\\Documents\\AI Product Engineering\\AI_Product_Engineer\\01_Python\\data.txt","r") as file:
    content = file.read()
    print(content)

with open(
    "C:\\Users\\a\\OneDrive\\Documents\\AI Product Engineering\\AI_Product_Engineer\\01_Python\\data.txt",
    "a",
) as file:
    new = file.write("\nLearning Python")
    print(new)

with open(
    "C:\\Users\\a\\OneDrive\\Documents\\AI Product Engineering\\AI_Product_Engineer\\01_Python\\data.txt",
    "r",
) as file:
    for line in file:
        print(line)
'''

import csv
import json

print("Reading file using try and except block")
try:
    with open("bdc.txt", "r") as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist.")


with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\data.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

with open(
    r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\data.csv",
    "w",
    newline="",
) as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Hamna", 92])
    writer.writerow(["Ali", 85])


student = {"name": "Hamna", "age": 21}

with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\students.json", "w") as file:
    json.dump(student, file, indent=4)
with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\students.json", "r") as file:
    student = json.load(file)

print(student)
