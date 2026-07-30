age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible to vote.")

is_student = True
if is_student != True:
    print("You are not a student.")
else:
    print("You are a student.")


marks = int(input("Enter your marks : "))
if marks >= 90:
    print("You got A grade.")
elif marks >= 80:
    print("You got B grade.")
elif marks >= 70:
    print("You got C grade.")
else:
    print("You got D grade.")


if age >= 18 and is_student == True:
    print("You are eligible for the youth program.")


lage = 22

if lage >= 18:

    license = input("Do you have a license? (yes/no): ")

    if license == "yes":
        print("You can drive.")

    else:
        print("Get a license first.")

else:
    print("Too young to drive.")
