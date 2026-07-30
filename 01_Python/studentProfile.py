def student_profile(name, age, university):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"University: {university}")
    
student_profile("Hamna", 21, "SSUET")


# Grade calculator
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"  

print(calculate_grade(98))


# bmi calculator
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

calculated_bmi = calculate_bmi(70, 1.75)
print(f"Your BMI is: {calculated_bmi:.2f}")