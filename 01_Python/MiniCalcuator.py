num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b   
def multiply(a, b):
    return a * b 
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
if operation == '+':
    result = add(num1, num2)
    print(f"The result of {num1} + {num2} is: {result}")   
elif operation == '-':
    result = subtract(num1, num2)
    print(f"The result of {num1} - {num2} is: {result}")   
elif operation == '*':
    result = multiply(num1, num2)
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == '/':
    result = divide(num1, num2)
    print(f"The result of {num1} / {num2} is: {result}")