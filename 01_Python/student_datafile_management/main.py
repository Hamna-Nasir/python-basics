import csv

with open(r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\student_datafile_management\students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Marks"])
    writer.writerow(["Hamna", 92])
    writer.writerow(["Ali", 85])
    writer.writerow(["Sara", 78])
    writer.writerow(["Ahmed", 95])
    writer.writerow(["Ayesha", 88])
with open(
    r"C:\\Users\a\OneDrive\Documents\AI Product Engineering\AI_Product_Engineer\01_Python\student_datafile_management\students.csv",
    "r",
) as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
