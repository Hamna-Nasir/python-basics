# Input Variables and Type Conversion
name = str(input("Enter your name : "))
age = int(input("Enter your age : "))
cgpa = float(input("Enter your CGPA : "))
print("My name is", name, "and my age is", age+5 , "and my CGPA is", cgpa)


#Arithematic operators 
a = 20
b = 6
c = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**2)

#Comparision operators 
print(age >= 18)
print(a == b)
print(a != c)
print(a <= b)
print(a > b)

#Logical operators
print(age >= 18 and age <= 30)
print(age >= 18 or age <= 30)

#assignment operators
a += 5
print(a)