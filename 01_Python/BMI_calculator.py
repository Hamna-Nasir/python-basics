# BMI Calculator 
name = input("Enter your name : ")
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in m : "))

bmi = weight / (height ** 2)
print (name , "Your BMI is : ", bmi)