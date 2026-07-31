# age = int(input("Enter your age :"))
# print(age)  # this can cause error in case of wrong datatype input


# using try-except
try:
    age = int(input("Enter your age :"))
    print(age)  
except:
    print("Invalid input! Please enter a number.")

# ValueError
try:
    num = int(input("Enter Your Name :"))
    print(num)
except ValueError:
    print("Enter valid Numeric value !")


# Error Types
'''
ValueError
ZeroDivisionError
IndexError
KeyError
TypeError
'''
# Multi Exceptions
try:
    A = int(input("Enter A:"))
    B = int(input("Enter B:"))
    print( A / B)
except ValueError:
    print("Numbers only!")

except ZeroDivisionError:
    print("Cannot divide by zero.")
    
else:  # execute ths block incase of no error
    print("Everything is perfect !")
    
finally: # must exceute this block in everycase
    print("Closing File!")
    
    
# raising own exceptions 
num = -5
if num < 0:
    raise ValueError("Number can't be negative !")
