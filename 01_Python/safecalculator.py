# safeCalculator
try:
    A = int(input("Enter A :"))
    B = int(input("Enter B :"))
    print( A / B )
    
except ValueError:
    print("Enter Numbers only!")
    
except ZeroDivisionError:
    print("can't divide number by zero!")
    

# Student Marks

marks = int(input("Enter your marks!")) 
if marks < 0:
    raise ValueError("marks can't be less than 0!")
if marks > 100:
    raise ValueError("marks can't be greater than 100!")
if marks >= 80:
    print(f"you scored {marks} : A+ Grade!")
if marks < 80 and marks >=70:
    print(f"you scored {marks} : A Grade!")
if marks < 70 and marks >=60:
    print(f"you scored {marks} : B Grade!")
if marks < 60 and marks >=50:
    print(f"you scored {marks} : C Grade!")
if marks < 50:
    print("you failed!")
