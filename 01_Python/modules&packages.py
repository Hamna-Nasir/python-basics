'''
import calculator
print(calculator.add(10, 5))  
print(calculator.subtract(10, 5)) 
'''
from calculator import add, subtract , multiply , divide
import math as m
import random as r
from datetime import date as d
from datetime import datetime
import requests
import greetings

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

print(m.sqrt(16))

print(r.randint(1, 10))

today = d.today()
print("Current date:", today)
current_time = datetime.now().strftime("%H:%M:%S")
print("Current time:", current_time)

print(greetings.greet("Hamna"))
print(greetings.morning("Hamna"))
print(greetings.evening("Hamna"))
print(greetings.night("Hamna"))

print(f"generating random 6 digit password : {r.randint(100000, 999999)}")
