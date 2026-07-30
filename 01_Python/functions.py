# functions
def add(a, b):
    return a + b

print(add(2,5))

name = input("Enter your name: ")
def greet(name):
    print("Hello, " + name + "!")
greet(name)

def welcome():
    print("Welcome to the program!")
welcome()
welcome()
welcome()

def greetings(namee):
    print(f"Hello, {namee}! Welcome to the program.")
    
greetings("Hamna")
greetings("Hammad")
greetings("Hafsa")

def student(name , university):
    print(f"{name} : {university}")
    
student("Hamna", "SSUET")
student("Hadiya", "NED")
student("Areeba", "NED")
student("Sundus", "JUW")

def profile(name, age, city):
    print(name)
    print(age)
    print(city)
    
profile("Hamna", 20, "Karachi")


# local vs Global variables
global_var = "I am a global variable"
def my_function():
    local_var = "I am a local variable"
    print(local_var)
    print(global_var)
    
my_function()
#print(local_var)  # This will raise an error because local_var is not accessible outside the function
print(global_var)  # This will work because global_var is accessible everywhere